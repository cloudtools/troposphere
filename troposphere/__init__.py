# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
import collections.abc
import json
import re
import sys
import types
from typing import Any, Callable, Dict, List, Tuple, Type, Union

import cfn_flip  # type: ignore

from . import validators

__version__ = "4.0.0-beta.0"

# constants for DeletionPolicy and UpdateReplacePolicy
Delete = "Delete"
Retain = "Retain"
Snapshot = "Snapshot"

# Pseudo Parameters
AWS_ACCOUNT_ID = "AWS::AccountId"
AWS_NOTIFICATION_ARNS = "AWS::NotificationARNs"
AWS_NO_VALUE = "AWS::NoValue"
AWS_PARTITION = "AWS::Partition"
AWS_REGION = "AWS::Region"
AWS_STACK_ID = "AWS::StackId"
AWS_STACK_NAME = "AWS::StackName"
AWS_URL_SUFFIX = "AWS::URLSuffix"

# Template Limits
MAX_MAPPINGS = 200
MAX_OUTPUTS = 200
MAX_PARAMETERS = 200
MAX_RESOURCES = 500
PARAMETER_TITLE_MAX = 255


valid_names = re.compile(r"^[a-zA-Z0-9]+$")


def is_aws_object_subclass(cls):
    is_aws_object = False
    try:
        is_aws_object = issubclass(cls, BaseAWSObject)
    # prop_type isn't a class
    except TypeError:
        pass
    return is_aws_object


def encode_to_dict(obj):
    if hasattr(obj, "to_dict"):
        # Calling encode_to_dict to ensure object is
        # nomalized to a base dictionary all the way down.
        return encode_to_dict(obj.to_dict())
    elif isinstance(obj, (list, tuple)):
        new_lst = []
        for o in obj:
            new_lst.append(encode_to_dict(o))
        return new_lst
    elif isinstance(obj, dict):
        props = {}
        for name, prop in obj.items():
            props[name] = encode_to_dict(prop)

        return props
    # This is useful when dealing with external libs using
    # this format. Specifically awacs.
    elif hasattr(obj, "JSONrepr"):
        return encode_to_dict(obj.JSONrepr())
    return obj


def depends_on_helper(obj):
    """Handles using .title if the given object is a troposphere resource.

    If the given object is a troposphere resource, use the `.title` attribute
    of that resource. If it's a string, just use the string. This should allow
    more pythonic use of DependsOn.
    """
    if isinstance(obj, AWSObject):
        return obj.title
    elif isinstance(obj, list):
        return list(map(depends_on_helper, obj))
    return obj


class BaseAWSObject:
    def __init__(self, title, template=None, validation=True, **kwargs):
        self.title = title
        self.template = template
        self.do_validation = validation
        # Cache the keys for validity checks
        self.propnames = set(self.props.keys())
        self.attributes = [
            "Condition",
            "CreationPolicy",
            "DeletionPolicy",
            "DependsOn",
            "Metadata",
            "UpdatePolicy",
            "UpdateReplacePolicy",
        ]

        # try to validate the title if its there
        if self.title:
            self.validate_title()

        # Create the list of properties set on this object by the user
        self.properties = {}
        dictname = getattr(self, "dictname", None)
        if dictname:
            self.resource = {
                dictname: self.properties,
            }
        else:
            self.resource = self.properties
        if hasattr(self, "resource_type") and self.resource_type is not None:
            self.resource["Type"] = self.resource_type
        self.__initialized = True

        # Check for properties defined in the class
        for k, (_, required) in self.props.items():
            v = getattr(type(self), k, None)
            if v is not None and k not in kwargs:
                self.__setattr__(k, v)

        # Now that it is initialized, populate it with the kwargs
        for k, v in kwargs.items():
            self.__setattr__(k, v)

        self.add_to_template()

    def add_to_template(self):
        # Bound it to template if we know it
        if self.template is not None:
            self.template.add_resource(self)

    def __getattr__(self, name):
        # If pickle loads this object, then __getattr__ will cause
        # an infinite loop when pickle invokes this object to look for
        # __setstate__ before attributes is "loaded" into this object.
        # Therefore, short circuit the rest of this call if attributes
        # is not loaded yet.
        if "attributes" not in self.__dict__:
            raise AttributeError(name)
        try:
            if name in self.attributes:
                return self.resource[name]
            else:
                return self.properties.__getitem__(name)
        except KeyError:
            # Fall back to the name attribute in the object rather than
            # in the properties dict. This is for non-OpenStack backwards
            # compatibility since OpenStack objects use a "name" property.
            if name == "name":
                return self.__getattribute__("title")
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if (
            name in self.__dict__.keys()
            or "_BaseAWSObject__initialized" not in self.__dict__
        ):
            return dict.__setattr__(self, name, value)
        elif name in self.attributes:
            if name == "DependsOn":
                self.resource[name] = depends_on_helper(value)
            else:
                self.resource[name] = value
            return None
        elif name in self.propnames:
            # Check the type of the object and compare against what we were
            # expecting.
            expected_type = self.props[name][0]

            # If the value is a AWSHelperFn we can't do much validation
            # we'll have to leave that to Amazon.  Maybe there's another way
            # to deal with this that we'll come up with eventually
            if isinstance(value, AWSHelperFn):
                return self.properties.__setitem__(name, value)

            # If it's a function, call it...
            elif isinstance(expected_type, types.FunctionType):
                try:
                    value = expected_type(value)
                except Exception:
                    sys.stderr.write(
                        "%s: %s.%s function validator '%s' threw "
                        "exception:\n"
                        % (self.__class__, self.title, name, expected_type.__name__)
                    )
                    raise
                return self.properties.__setitem__(name, value)

            # If it's a list of types, check against those types...
            elif isinstance(expected_type, list):
                # If we're expecting a list, then make sure it is a list
                if not isinstance(value, list):
                    self._raise_type(name, value, expected_type)

                # Special case a list of a single validation function
                if len(expected_type) == 1 and isinstance(
                    expected_type[0], types.FunctionType
                ):
                    new_value = list(map(expected_type[0], value))
                    return self.properties.__setitem__(name, new_value)

                # Iterate over the list and make sure it matches our
                # type checks (as above accept AWSHelperFn because
                # we can't do the validation ourselves)
                for v in value:
                    if not isinstance(v, tuple(expected_type)) and not isinstance(
                        v, AWSHelperFn
                    ):
                        self._raise_type(name, v, expected_type)
                # Validated so assign it
                return self.properties.__setitem__(name, value)

            # Final validity check, compare the type of value against
            # expected_type which should now be either a single type or
            # a tuple of types.
            elif isinstance(value, expected_type):
                return self.properties.__setitem__(name, value)
            else:
                self._raise_type(name, value, expected_type)

        type_name = getattr(self, "resource_type", self.__class__.__name__)

        if type_name == "AWS::CloudFormation::CustomResource" or type_name.startswith(
            "Custom::"
        ):
            # Add custom resource arguments to the dict without any further
            # validation. The properties of a CustomResource is not known.
            return self.properties.__setitem__(name, value)

        raise AttributeError(
            "%s object does not support attribute %s" % (type_name, name)
        )

    def _raise_type(self, name, value, expected_type):
        raise TypeError(
            "%s: %s.%s is %s, expected %s"
            % (self.__class__, self.title, name, type(value), expected_type)
        )

    def validate_title(self):
        if not valid_names.match(self.title):
            raise ValueError('Name "%s" not alphanumeric' % self.title)

    def validate(self):
        pass

    def no_validation(self):
        self.do_validation = False
        return self

    def to_dict(self):
        if self.do_validation:
            self._validate_props()
            self.validate()

        if self.properties:
            return encode_to_dict(self.resource)
        elif hasattr(self, "resource_type"):
            d = {}
            for k, v in self.resource.items():
                if k != "Properties":
                    d[k] = v
            return d
        else:
            return {}

    @classmethod
    def _from_dict(cls, title=None, **kwargs):
        props = {}
        for prop_name, value in kwargs.items():
            try:
                prop_attrs = cls.props[prop_name]
            except KeyError:
                raise AttributeError(
                    "Object type %s does not have a "
                    "%s property." % (cls.__name__, prop_name)
                )
            prop_type = prop_attrs[0]
            value = kwargs[prop_name]
            is_aws_object = is_aws_object_subclass(prop_type)
            if is_aws_object:
                if not isinstance(value, collections.abc.Mapping):
                    raise ValueError(
                        "Property definition for %s must be "
                        "a Mapping type" % prop_name
                    )
                value = prop_type._from_dict(**value)

            if isinstance(prop_type, list):
                if not isinstance(value, list):
                    raise TypeError("Attribute %s must be a " "list." % prop_name)
                new_value = []
                for v in value:
                    new_v = v
                    if is_aws_object_subclass(prop_type[0]):
                        if not isinstance(v, collections.abc.Mapping):
                            raise ValueError(
                                "Property definition for %s must be "
                                "a list of Mapping types" % prop_name
                            )
                        new_v = prop_type[0]._from_dict(**v)
                    new_value.append(new_v)
                value = new_value
            props[prop_name] = value
        if title:
            return cls(title, **props)
        return cls(**props)

    @classmethod
    def from_dict(cls, title, d):
        return cls._from_dict(title, **d)

    def _validate_props(self):
        for k, (_, required) in self.props.items():
            if required and k not in self.properties:
                rtype = getattr(self, "resource_type", "<unknown type>")
                title = getattr(self, "title")
                msg = "Resource %s required in type %s" % (k, rtype)
                if title:
                    msg += " (title: %s)" % title
                raise ValueError(msg)


class AWSObject(BaseAWSObject):
    dictname = "Properties"

    def ref(self):
        return Ref(self)

    Ref = ref

    def get_att(self, value):
        return GetAtt(self, value)

    GetAtt = get_att


class AWSDeclaration(BaseAWSObject):
    """
    Used for CloudFormation Resource Property objects
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/
    aws-product-property-reference.html
    """

    def __init__(self, title, **kwargs):
        super().__init__(title, **kwargs)

    def ref(self):
        return Ref(self)

    Ref = ref


class AWSProperty(BaseAWSObject):
    """
    Used for CloudFormation Resource Property objects
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/
    aws-product-property-reference.html
    """

    dictname = None

    def __init__(self, title=None, **kwargs):
        super().__init__(title, **kwargs)


class AWSAttribute(BaseAWSObject):
    dictname = None

    """
    Used for CloudFormation Resource Attribute objects
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/
    aws-product-attribute-reference.html
    """

    def __init__(self, title=None, **kwargs):
        super().__init__(title, **kwargs)


def validate_delimiter(delimiter):
    if not isinstance(delimiter, str):
        raise ValueError("Delimiter must be a String, %s provided" % type(delimiter))


def validate_pausetime(pausetime):
    if not pausetime.startswith("PT"):
        raise ValueError("PauseTime should look like PT#H#M#S")
    return pausetime


class AWSHelperFn:
    def getdata(self, data):
        if isinstance(data, BaseAWSObject):
            return data.title
        else:
            return data

    def to_dict(self):
        return encode_to_dict(self.data)


class GenericHelperFn(AWSHelperFn):
    """Used as a fallback for the template generator"""

    def __init__(self, data):
        self.data = self.getdata(data)

    def to_dict(self):
        return encode_to_dict(self.data)


class Base64(AWSHelperFn):
    def __init__(self, data):
        self.data = {"Fn::Base64": data}


class FindInMap(AWSHelperFn):
    def __init__(self, mapname, toplevelkey, secondlevelkey):
        self.data = {
            "Fn::FindInMap": [self.getdata(mapname), toplevelkey, secondlevelkey]
        }


class GetAtt(AWSHelperFn):
    def __init__(self, logicalName, attrName):  # noqa: N803
        self.data = {"Fn::GetAtt": [self.getdata(logicalName), attrName]}


class Cidr(AWSHelperFn):
    def __init__(self, ipblock, count, sizemask=None):
        if sizemask:
            self.data = {"Fn::Cidr": [ipblock, count, sizemask]}
        else:
            self.data = {"Fn::Cidr": [ipblock, count]}


class GetAZs(AWSHelperFn):
    def __init__(self, region=""):
        self.data = {"Fn::GetAZs": region}


class If(AWSHelperFn):
    def __init__(self, cond, true, false):
        self.data = {"Fn::If": [self.getdata(cond), true, false]}


class Equals(AWSHelperFn):
    def __init__(self, value_one, value_two):
        self.data = {"Fn::Equals": [value_one, value_two]}


class And(AWSHelperFn):
    def __init__(self, cond_one, cond_two, *conds):
        self.data = {"Fn::And": [cond_one, cond_two] + list(conds)}


class Or(AWSHelperFn):
    def __init__(self, cond_one, cond_two, *conds):
        self.data = {"Fn::Or": [cond_one, cond_two] + list(conds)}


class Not(AWSHelperFn):
    def __init__(self, cond):
        self.data = {"Fn::Not": [self.getdata(cond)]}


class Join(AWSHelperFn):
    def __init__(self, delimiter, values):
        validate_delimiter(delimiter)
        self.data = {"Fn::Join": [delimiter, values]}


class Split(AWSHelperFn):
    def __init__(self, delimiter, values):
        validate_delimiter(delimiter)
        self.data = {"Fn::Split": [delimiter, values]}


class Sub(AWSHelperFn):
    def __init__(self, input_str, dict_values=None, **values):
        # merge dict
        if dict_values:
            values.update(dict_values)
        self.data = {"Fn::Sub": [input_str, values] if values else input_str}


class Name(AWSHelperFn):
    def __init__(self, data):
        self.data = self.getdata(data)


class Select(AWSHelperFn):
    def __init__(self, indx, objects):
        self.data = {"Fn::Select": [indx, objects]}


class Ref(AWSHelperFn):
    def __init__(self, data):
        self.data = {"Ref": self.getdata(data)}

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.data == other.data
        return list(self.data.values())[0] == other

    def __hash__(self):
        return hash(list(self.data.values())[0])


# The type of the props dict
PropsDictType = Dict[
    str,
    Tuple[
        Union[
            str, AWSProperty, AWSHelperFn, Callable, Dict, List[Any], Tuple[Type, ...]
        ],
        bool,
    ],
]

# Pseudo Parameter Ref's
AccountId = Ref(AWS_ACCOUNT_ID)
NotificationARNs = Ref(AWS_NOTIFICATION_ARNS)
NoValue = Ref(AWS_NO_VALUE)
Partition = Ref(AWS_PARTITION)
Region = Ref(AWS_REGION)
StackId = Ref(AWS_STACK_ID)
StackName = Ref(AWS_STACK_NAME)
URLSuffix = Ref(AWS_URL_SUFFIX)


class Condition(AWSHelperFn):
    def __init__(self, data):
        self.data = {"Condition": self.getdata(data)}


class ImportValue(AWSHelperFn):
    def __init__(self, data):
        self.data = {"Fn::ImportValue": data}


class Tag(AWSHelperFn):
    def __init__(self, k, v):
        self.data = {
            "Key": k,
            "Value": v,
        }


class Tags(AWSHelperFn):
    def __init__(self, *args, **kwargs):
        self.tags = []
        if not args:
            # Assume kwargs variant
            tag_dict = kwargs
        else:
            tag_dict = {}
            for arg in args:
                # Validate argument passed in is an AWSHelperFn or...
                if isinstance(arg, AWSHelperFn):
                    self.tags.append(arg)
                # Validate argument passed in is a dict
                elif isinstance(arg, dict):
                    tag_dict.update(arg)
                else:
                    raise TypeError(
                        "Tags needs to be either kwargs, dict, or AWSHelperFn"
                    )

        def add_tag(tag_list, k, v):
            tag_list.append(
                {
                    "Key": k,
                    "Value": v,
                }
            )

        # Detect and handle non-string Tag items which do not sort in Python3
        if all(isinstance(k, str) for k in tag_dict):
            for k, v in sorted(tag_dict.items()):
                add_tag(self.tags, k, v)
        else:
            for k, v in tag_dict.items():
                add_tag(self.tags, k, v)

    # allow concatenation of the Tags object via '+' operator
    def __add__(self, newtags):
        newtags.tags = self.tags + newtags.tags
        return newtags

    def to_dict(self):
        return [encode_to_dict(tag) for tag in self.tags]

    @classmethod
    def from_dict(cls, title=None, **kwargs):
        return cls(**kwargs)


class Template:
    from troposphere.serverless import Globals

    props = {
        "AWSTemplateFormatVersion": (str, False),
        "Transform": (str, False),
        "Description": (str, False),
        "Parameters": (dict, False),
        "Mappings": (dict, False),
        "Resources": (dict, False),
        "Globals": (Globals, False),
        "Outputs": (dict, False),
        "Rules": (dict, False),
    }

    def __init__(self, Description=None, Metadata=None):  # noqa: N803
        self.description = Description
        self.metadata = {} if Metadata is None else Metadata
        self.conditions = {}
        self.mappings = {}
        self.outputs = {}
        self.parameters = {}
        self.resources = {}
        self.rules = {}
        self.globals = None
        self.version = None
        self.transform = None

    def set_description(self, description):
        self.description = description

    def set_metadata(self, metadata):
        self.metadata = metadata

    def add_condition(self, name, condition):
        self.conditions[name] = condition
        return name

    def handle_duplicate_key(self, key):
        raise ValueError('duplicate key "%s" detected' % key)

    def _update(self, d, values):
        if isinstance(values, list):
            for v in values:
                if v.title in d:
                    self.handle_duplicate_key(v.title)
                d[v.title] = v
        else:
            if values.title in d:
                self.handle_duplicate_key(values.title)
            d[values.title] = values
        return values

    def add_output(self, output):
        if len(self.outputs) >= MAX_OUTPUTS:
            raise ValueError("Maximum outputs %d reached" % MAX_OUTPUTS)
        return self._update(self.outputs, output)

    def add_mapping(self, name, mapping):
        if len(self.mappings) >= MAX_MAPPINGS:
            raise ValueError("Maximum mappings %d reached" % MAX_MAPPINGS)
        if name not in self.mappings:
            self.mappings[name] = {}
        self.mappings[name].update(mapping)

    def add_parameter(self, parameter):
        if len(self.parameters) >= MAX_PARAMETERS:
            raise ValueError("Maximum parameters %d reached" % MAX_PARAMETERS)
        return self._update(self.parameters, parameter)

    def get_or_add_parameter(self, parameter):
        if parameter.title in self.parameters:
            return self.parameters[parameter.title]
        else:
            self.add_parameter(parameter)
        return parameter

    def add_resource(self, resource):
        if len(self.resources) >= MAX_RESOURCES:
            raise ValueError("Maximum number of resources %d reached" % MAX_RESOURCES)
        return self._update(self.resources, resource)

    def add_rule(self, name, rule):
        """
        Add a Rule to the template to enforce extra constraints on the
        parameters. As of June 2019 rules are undocumented in CloudFormation
        but have the same syntax and behaviour as in ServiceCatalog:
        https://docs.aws.amazon.com/servicecatalog/latest/adminguide/reference-template_constraint_rules.html

        :param rule: a dict with 'Assertions' (mandatory) and 'RuleCondition'
                     (optional) keys
        """
        # TODO: check maximum number of Rules, and enforce limit.
        if name in self.rules:
            self.handle_duplicate_key(name)
        self.rules[name] = rule

    def set_version(self, version=None):
        if version:
            self.version = version
        else:
            self.version = "2010-09-09"

    def set_transform(self, transform):
        from troposphere.serverless import SERVERLESS_TRANSFORM

        if self.globals and transform != SERVERLESS_TRANSFORM:
            raise ValueError(
                "Cannot set transform to non-Serverless while using Globals"
            )
        self.transform = transform

    def set_globals(self, globals: Globals):
        from troposphere.serverless import SERVERLESS_TRANSFORM

        if self.transform != SERVERLESS_TRANSFORM:
            raise ValueError(
                f"Cannot set Globals for non-Serverless template (set transform to '{SERVERLESS_TRANSFORM}' first)"
            )
        self.globals = globals

    def to_dict(self):
        t = {}
        if self.description:
            t["Description"] = self.description
        if self.metadata:
            t["Metadata"] = self.metadata
        if self.conditions:
            t["Conditions"] = self.conditions
        if self.mappings:
            t["Mappings"] = self.mappings
        if self.outputs:
            t["Outputs"] = self.outputs
        if self.parameters:
            t["Parameters"] = self.parameters
        if self.version:
            t["AWSTemplateFormatVersion"] = self.version
        if self.transform:
            t["Transform"] = self.transform
        if self.rules:
            t["Rules"] = self.rules
        if self.globals:
            t["Globals"] = self.globals
        t["Resources"] = self.resources

        return encode_to_dict(t)

    def set_parameter_label(self, parameter, label):
        """
        Sets the Label used in the User Interface for the given parameter.
        :type parameter: str or Parameter
        :type label: str
        """
        labels = self.metadata.setdefault(
            "AWS::CloudFormation::Interface", {}
        ).setdefault("ParameterLabels", {})

        if isinstance(parameter, BaseAWSObject):
            parameter = parameter.title

        labels[parameter] = {"default": label}

    def add_parameter_to_group(self, parameter, group_name):
        """
        Add a parameter under a group (created if needed).
        :type parameter: str or Parameter
        :type group_name: str
        """
        groups = self.metadata.setdefault(
            "AWS::CloudFormation::Interface", {}
        ).setdefault("ParameterGroups", [])

        if isinstance(parameter, BaseAWSObject):
            parameter = parameter.title

        # Check if group_name already exists
        existing_group = None
        for group in groups:
            if group["Label"]["default"] == group_name:
                existing_group = group
                break

        if existing_group is None:
            existing_group = {
                "Label": {"default": group_name},
                "Parameters": [],
            }
            groups.append(existing_group)

        existing_group["Parameters"].append(parameter)

        return group_name

    def to_json(self, indent=4, sort_keys=True, separators=(",", ": ")):
        return json.dumps(
            self.to_dict(), indent=indent, sort_keys=sort_keys, separators=separators
        )

    def to_yaml(self, clean_up=False, long_form=False, sort_keys=True):
        return cfn_flip.to_yaml(
            self.to_json(sort_keys=sort_keys), clean_up=clean_up, long_form=long_form
        )

    def __eq__(self, other):
        if isinstance(other, Template):
            return self.to_json() == other.to_json()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.to_json())


class Export(AWSHelperFn):
    def __init__(self, name):
        self.data = {
            "Name": name,
        }


class Output(AWSDeclaration):
    props = {
        "Description": (str, False),
        "Export": (Export, False),
        "Value": (str, True),
    }

    def add_to_template(self):
        # Bound it to template if we know it
        if self.template is not None:
            self.template.add_output(self)


class Parameter(AWSDeclaration):
    STRING_PROPERTIES = ["AllowedPattern", "MaxLength", "MinLength"]
    NUMBER_PROPERTIES = ["MaxValue", "MinValue"]
    props = {
        "Type": (str, True),
        "Default": ((str, int, float), False),
        "NoEcho": (bool, False),
        "AllowedValues": (list, False),
        "AllowedPattern": (str, False),
        "MaxLength": (validators.positive_integer, False),
        "MinLength": (validators.positive_integer, False),
        "MaxValue": (validators.integer, False),
        "MinValue": (validators.integer, False),
        "Description": (str, False),
        "ConstraintDescription": (str, False),
    }

    def add_to_template(self):
        # Bound it to template if we know it
        if self.template is not None:
            self.template.add_parameter(self)

    def validate_title(self):
        if len(self.title) > PARAMETER_TITLE_MAX:
            raise ValueError(
                "Parameter title can be no longer than "
                "%d characters" % PARAMETER_TITLE_MAX
            )
        super().validate_title()

    def validate(self):
        def check_type(t, v):
            try:
                t(v)
                return True
            except ValueError:
                return False

        # Validate the Default parameter value
        default = self.properties.get("Default")
        if default:
            error_str = (
                "Parameter default type mismatch: expecting "
                "type %s got %s with value %r"
            )
            # Get the Type specified and see whether the default type
            # matches (in the case of a String Type) or can be coerced
            # into one of the number formats.
            param_type = self.properties.get("Type")
            if param_type == "String" and not isinstance(default, str):
                raise ValueError(error_str % ("String", type(default), default))
            elif param_type == "Number":
                allowed = [float, int]
                # See if the default value can be coerced into one
                # of the correct types
                if not any(check_type(x, default) for x in allowed):
                    raise ValueError(error_str % (param_type, type(default), default))
            elif param_type == "List<Number>":
                if not isinstance(default, str):
                    raise ValueError(error_str % (param_type, type(default), default))
                allowed = [float, int]
                dlist = default.split(",")
                for d in dlist:
                    # Verify the split array are all numbers
                    if not any(check_type(x, d) for x in allowed):
                        raise ValueError(error_str % (param_type, type(d), dlist))

        if self.properties["Type"] != "String":
            for p in self.STRING_PROPERTIES:
                if p in self.properties:
                    raise ValueError(
                        "%s can only be used with parameters of " "the String type." % p
                    )
        if self.properties["Type"] != "Number":
            for p in self.NUMBER_PROPERTIES:
                if p in self.properties:
                    raise ValueError(
                        "%s can only be used with parameters of " "the Number type." % p
                    )
