"""
This module makes it possible to instantiate a new Troposphere Template object
from an existing CloudFormation Template.

Usage:
    from troposphere.template_generator import TemplateGenerator
    import json

    with open("myCloudFormationTemplate.json") as f:
        json_template = json.load(f)

    template = TemplateGenerator(json_template)
    template.to_json()
"""

import importlib
import inspect
import os
import pkgutil
from collections.abc import Mapping, Sequence

from troposphere import AWSObject  # covers resources
from troposphere import GenericHelperFn  # covers ref, fn::, etc
from troposphere import Parameter  # AWSDeclarations
from troposphere import (
    AWSHelperFn,
    Export,
    Output,
    Ref,
    Tags,
    Template,
    autoscaling,
    cloudformation,
)
from troposphere.policies import CreationPolicy, UpdatePolicy


class TemplateGenerator(Template):
    DEPRECATED_MODULES = ["troposphere.dynamodb2"]
    EXCLUDE_MODULES = DEPRECATED_MODULES + [
        "troposphere.openstack.heat",
        "troposphere.openstack.neutron",
        "troposphere.openstack.nova",
    ]

    _inspect_members = set()  # type: ignore
    _inspect_resources = {}  # type: ignore
    _custom_members = set()  # type: ignore
    _inspect_functions = {}  # type: ignore

    def __init__(self, cf_template, **kwargs):
        """
        Instantiates a new Troposphere Template based on an existing
        Cloudformation Template.
        """
        super().__init__()
        if "CustomMembers" in kwargs:
            self._custom_members = set(kwargs["CustomMembers"])

        self._reference_map = {}
        if "AWSTemplateFormatVersion" in cf_template:
            self.set_version(cf_template["AWSTemplateFormatVersion"])
        if "Transform" in cf_template:
            self.set_transform(cf_template["Transform"])
        if "Description" in cf_template:
            self.set_description(cf_template["Description"])
        if "Metadata" in cf_template:
            self.set_metadata(cf_template["Metadata"])
        for k, v in cf_template.get("Parameters", {}).items():
            self.add_parameter(self._create_instance(Parameter, v, k))
        for k, v in cf_template.get("Mappings", {}).items():
            self.add_mapping(k, self._convert_definition(v))
        for k, v in cf_template.get("Conditions", {}).items():
            self.add_condition(k, self._convert_definition(v, k))
        for k, v in cf_template.get("Resources", {}).items():
            self.add_resource(
                self._convert_definition(v, k, self._get_resource_type_cls(k, v))
            )
        for k, v in cf_template.get("Outputs", {}).items():
            self.add_output(self._create_instance(Output, v, k))

    @property
    def inspect_members(self):
        """
        Returns the list of all troposphere members we are able to
        construct
        """
        if not self._inspect_members:
            TemplateGenerator._inspect_members = self._import_all_troposphere_modules()
        return self._inspect_members

    @property
    def inspect_resources(self):
        """Returns a map of `ResourceType: ResourceClass`"""
        if not self._inspect_resources:
            d = {}
            for m in self.inspect_members:
                if issubclass(
                    m, (AWSObject, cloudformation.AWSCustomObject)
                ) and hasattr(m, "resource_type"):
                    d[m.resource_type] = m

            TemplateGenerator._inspect_resources = d

        return self._inspect_resources

    @property
    def inspect_functions(self):
        """Returns a map of `FunctionName: FunctionClass`"""
        if not self._inspect_functions:
            d = {}
            for m in self.inspect_members:
                if issubclass(m, AWSHelperFn):
                    d[m.__name__] = m

            TemplateGenerator._inspect_functions = d

        return self._inspect_functions

    def _get_resource_type_cls(self, name, resource):
        """Attempts to return troposphere class that represents Type of
        provided resource. Attempts to find the troposphere class who's
        `resource_type` field is the same as the provided resources `Type`
        field.

        :param resource: Resource to find troposphere class for
        :return: None: If no class found for provided resource
                 type: Type of provided resource
        :raise ResourceTypeNotDefined:
                  Provided resource does not have a `Type` field
        """
        # If provided resource does not have `Type` field
        if "Type" not in resource:
            raise ResourceTypeNotDefined(name)

        # Attempt to find troposphere resource with:
        #   `resource_type` == resource['Type']
        try:
            return self.inspect_resources[resource["Type"]]
        except KeyError:
            # is there a custom mapping?
            for custom_member in self._custom_members:
                if custom_member.resource_type == resource["Type"]:
                    return custom_member
            # If no resource with `resource_type` == resource['Type'] found
            return None

    def _convert_definition(self, definition, ref=None, cls=None):
        """
        Converts any object to its troposphere equivalent, if applicable.
        This function will recurse into lists and mappings to create
        additional objects as necessary.

        :param {*} definition: Object to convert
        :param str ref: Name of key in parent dict that the provided definition
                        is from, can be None
        :param type cls: Troposphere class which represents provided definition
        """
        if isinstance(definition, Mapping):
            if "Type" in definition:  # this is an AWS Resource
                expected_type = None
                if cls is not None:
                    expected_type = cls
                else:
                    # if the user uses the custom way to name custom resources,
                    # we'll dynamically create a new subclass for this use and
                    # pass that instead of the typical CustomObject resource
                    try:
                        expected_type = self._generate_custom_type(definition["Type"])
                    except TypeError:
                        # If definition['Type'] turns out not to be a custom
                        # type (aka doesn't start with "Custom::")
                        if ref is not None:
                            raise ResourceTypeNotFound(ref, definition["Type"])
                        else:
                            # Make sure expected_type is nothing (as
                            # it always should be)
                            assert not expected_type

                if expected_type:
                    args = self._normalize_properties(definition)
                    return self._create_instance(expected_type, args, ref)

            if len(definition) == 1:  # This might be a function?
                function_type = self._get_function_type(list(definition.keys())[0])
                if function_type:
                    return self._create_instance(
                        function_type, list(definition.values())[0]
                    )

            # nothing special here - return as dict
            d = {}
            for k, v in definition.items():
                d[k] = self._convert_definition(v)
            return d

        elif isinstance(definition, Sequence) and not isinstance(definition, str):
            return [self._convert_definition(v) for v in definition]

        # anything else is returned as-is
        return definition

    def _create_instance(self, cls, args, ref=None):
        """
        Returns an instance of `cls` with `args` passed as arguments.

        Recursively inspects `args` to create nested objects and functions as
        necessary.

        `cls` will only be considered only if it's an object we track
         (i.e.: troposphere objects).

        If `cls` has a `props` attribute, nested properties will be
         instanciated as troposphere Property objects as necessary.

        If `cls` is a list and contains a single troposphere type, the
         returned value will be a list of instances of that type.
        """
        if isinstance(cls, Sequence):
            if len(cls) == 1:
                # a list of 1 type means we must provide a list of such objects
                if isinstance(args, str) or not isinstance(args, Sequence):
                    args = [args]
                return [self._create_instance(cls[0], v) for v in args]

        if isinstance(cls, Sequence) or cls not in self.inspect_members.union(
            self._custom_members
        ):
            # this object doesn't map to any known object. could be a string
            # or int, or a Ref... or a list of types such as
            # [basestring, FindInMap, Ref] or maybe a
            # validator such as `integer` or `port_range`
            return self._convert_definition(args)

        elif issubclass(cls, AWSHelperFn):
            # special handling for functions, we want to handle it before
            # entering the other conditions.
            try:
                if issubclass(cls, Tags):
                    arg_dict = {}
                    for d in args:
                        arg_dict[d["Key"]] = d["Value"]
                    return cls(arg_dict)

                if isinstance(args, Sequence) and not isinstance(args, str):
                    return cls(*self._convert_definition(args))

                if issubclass(cls, autoscaling.Metadata):
                    return self._generate_autoscaling_metadata(cls, args)

                if issubclass(cls, Export):
                    return cls(args["Name"])

                args = self._convert_definition(args)
                if isinstance(args, Ref) and issubclass(cls, Ref):
                    # watch out for double-refs...
                    # this can happen if an object's .props has 'Ref'
                    # as the expected type (which is wrong and should be
                    # changed to basestring!)
                    return args

                return cls(args)

            except TypeError as ex:
                if "__init__() takes exactly" not in ex.message:
                    raise
                # special AWSHelperFn typically take lowercased parameters,
                # but templates use uppercase. for this reason we cannot
                # map to most of them, so we fallback with a generic one.
                # this might not work for all types if they do extra
                # processing in their init routine
                return GenericHelperFn(args)

        elif isinstance(args, Mapping):
            # we try to build as many troposphere objects as we can by
            # inspecting its type validation metadata
            kwargs = {}
            kwargs.update(args)
            for prop_name in getattr(cls, "props", []):
                if prop_name not in kwargs:
                    continue  # the user did not specify this value; skip it
                expected_type = cls.props[prop_name][0]

                if (
                    isinstance(expected_type, Sequence)
                    or expected_type in self.inspect_members
                ):
                    kwargs[prop_name] = self._create_instance(
                        expected_type, kwargs[prop_name], prop_name
                    )
                elif expected_type == bool:
                    if kwargs[prop_name] in ("True", "true", "1"):
                        kwargs[prop_name] = True
                    elif kwargs[prop_name] in ("False", "false", "0"):
                        kwargs[prop_name] = False
                    else:
                        kwargs[prop_name] = self._convert_definition(
                            kwargs[prop_name], prop_name
                        )
                else:
                    kwargs[prop_name] = self._convert_definition(
                        kwargs[prop_name], prop_name
                    )

            args = self._convert_definition(kwargs)
            if isinstance(args, Ref):
                # use the returned ref instead of creating a new object
                return args
            if isinstance(args, AWSHelperFn):
                return self._convert_definition(kwargs)
            assert isinstance(args, Mapping)
            return cls(title=ref, **args)

        return cls(self._convert_definition(args))

    def _normalize_properties(self, definition):
        """
        Inspects the definition and returns a copy of it that is updated
        with any special property such as Condition, UpdatePolicy and the
        like.
        """
        args = definition.get("Properties", {}).copy()
        if "Condition" in definition:
            args.update({"Condition": definition["Condition"]})
        if "UpdatePolicy" in definition:
            # there's only 1 kind of UpdatePolicy; use it
            args.update(
                {
                    "UpdatePolicy": self._create_instance(
                        UpdatePolicy, definition["UpdatePolicy"]
                    )
                }
            )
        if "CreationPolicy" in definition:
            # there's only 1 kind of CreationPolicy; use it
            args.update(
                {
                    "CreationPolicy": self._create_instance(
                        CreationPolicy, definition["CreationPolicy"]
                    )
                }
            )
        if "DeletionPolicy" in definition:
            # DeletionPolicity is very basic
            args.update(
                {
                    "DeletionPolicy": self._convert_definition(
                        definition["DeletionPolicy"]
                    )
                }
            )
        if "Metadata" in definition:
            # there are various kind of metadata; pass it as-is
            args.update({"Metadata": self._convert_definition(definition["Metadata"])})
        if "DependsOn" in definition:
            args.update(
                {"DependsOn": self._convert_definition(definition["DependsOn"])}
            )
        return args

    def _generate_custom_type(self, resource_type):
        """
        Dynamically allocates a new CustomResource class definition using the
        specified Custom::SomeCustomName resource type. This special resource
        type is equivalent to the AWS::CloudFormation::CustomResource.
        """
        if not resource_type.startswith("Custom::"):
            raise TypeError("Custom types must start with Custom::")
        custom_type = type(
            str(resource_type.replace("::", "")),
            (self.inspect_resources["AWS::CloudFormation::CustomResource"],),
            {"resource_type": resource_type},
        )
        self.inspect_members.add(custom_type)
        self.inspect_resources[resource_type] = custom_type
        return custom_type

    def _generate_autoscaling_metadata(self, cls, args):
        """Provides special handling for the autoscaling.Metadata object"""
        assert isinstance(args, Mapping)
        init_config = self._create_instance(
            cloudformation.InitConfig, args["AWS::CloudFormation::Init"]["config"]
        )
        init = self._create_instance(cloudformation.Init, {"config": init_config})
        auth = None
        if "AWS::CloudFormation::Authentication" in args:
            auth_blocks = {}
            for k in args["AWS::CloudFormation::Authentication"]:
                auth_blocks[k] = self._create_instance(
                    cloudformation.AuthenticationBlock,
                    args["AWS::CloudFormation::Authentication"][k],
                    k,
                )
            auth = self._create_instance(cloudformation.Authentication, auth_blocks)

        return cls(init, auth)

    def _get_function_type(self, function_name):
        """
        Returns the function object that matches the provided name.
        Only Fn:: and Ref functions are supported here so that other
        functions specific to troposphere are skipped.
        """
        if (
            function_name.startswith("Fn::")
            and function_name[4:] in self.inspect_functions
        ):
            return self.inspect_functions[function_name[4:]]
        return self.inspect_functions["Ref"] if function_name == "Ref" else None

    def _import_all_troposphere_modules(self):
        """Imports all troposphere modules and returns them"""
        dirname = os.path.join(os.path.dirname(__file__))
        module_names = [
            pkg_name
            for importer, pkg_name, is_pkg in pkgutil.walk_packages(
                [dirname], prefix="troposphere."
            )
            if not is_pkg and pkg_name not in self.EXCLUDE_MODULES
        ]
        module_names.append("troposphere")

        modules = []
        for name in module_names:
            modules.append(importlib.import_module(name))

        def members_predicate(m):
            return inspect.isclass(m) and not inspect.isbuiltin(m)

        members = []
        for module in modules:
            members.extend(
                (m[1] for m in inspect.getmembers(module, members_predicate))
            )

        return set(members)


class ResourceTypeNotFound(Exception):
    def __init__(self, resource, resource_type):
        Exception.__init__(
            self, "ResourceType not found for " + resource_type + " - " + resource
        )
        self.resource_type = resource_type
        self.resource = resource


class ResourceTypeNotDefined(Exception):
    def __init__(self, resource):
        Exception.__init__(self, "ResourceType not defined for " + resource)
        self.resource = resource
