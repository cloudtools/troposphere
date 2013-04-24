# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


import json
import re
import types

from . import validators

__version__ = "0.2.7"

# constants for DeletionPolicy
Delete = 'Delete'
Retain = 'Retain'
Snapshot = 'Snapshot'

valid_names = re.compile(r'^[a-zA-Z0-9]+$')


class AWSObject(object):
    def __init__(self, name, type=None, dictname=None, props={}, **kwargs):
        self.name = name
        self.type = type
        self.props = props
        # Cache the keys for validity checks
        self.propnames = props.keys()
        self.attributes = ['DependsOn', 'DeletionPolicy',
                           'Metadata', 'UpdatePolicy']

        # unset/None is also legal
        if name and not valid_names.match(name):
            raise ValueError('Name not alphanumeric')

        # Create the list of properties set on this object by the user
        self.properties = {}
        if dictname:
            self.resource = {
                dictname: self.properties,
            }
        else:
            self.resource = self.properties
        if self.type:
            self.resource['Type'] = self.type
        self.__initialized = True

        # Now that it is initialized, populate it with the kwargs
        for k, v in kwargs.items():
            # Special case Resource Attributes
            if k in self.attributes:
                self.resource[k] = v
            else:
                self.__setattr__(k, v)

    def __getattr__(self, name):
        try:
            return self.properties.__getitem__(name)
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if '_AWSObject__initialized' not in self.__dict__:
            return dict.__setattr__(self, name, value)
        elif name in self.propnames:
            # Check the type of the object and compare against what we were
            # expecting.
            expected_type = self.props[name][0]

            # If it's a function, call it...
            if isinstance(expected_type, types.FunctionType):
                value = expected_type(value)
                return self.properties.__setitem__(name, value)

            # If it's a list of types, check against those types...
            elif isinstance(expected_type, list):
                # If we're expecting a list, then make sure it is a list
                if not isinstance(value, list):
                    self._raise_type(name, value, expected_type)

                # Iterate over the list and make sure it matches our
                # type checks
                for v in value:
                    if not isinstance(v, tuple(expected_type)):
                        self._raise_type(name, v, expected_type)
                # Validated so assign it
                return self.properties.__setitem__(name, value)

            # Single type so check the type of the object and compare against
            # what we were expecting. Special case AWS helper functions.
            elif isinstance(value, expected_type) or \
                    isinstance(value, AWSHelperFn):
                return self.properties.__setitem__(name, value)
            else:
                self._raise_type(name, value, expected_type)

        raise AttributeError("%s object does not support attribute %s" %
                            (self.type, name))

    def _raise_type(self, name, value, expected_type):
        raise TypeError('%s is %s, expected %s' %
                        (name, type(value), expected_type))

    def validate(self):
        pass

    def JSONrepr(self):
        for k, v in self.props.items():
            if v[1] and k not in self.properties:
                raise ValueError("Resource %s required in type %s" %
                                 (k, self.type))
        self.validate()
        # If no other properties are set, only return the Type.
        # Mainly used to not have an empty "Properties".
        if self.properties:
            return self.resource
        else:
            return {'Type': self.type}


class AWSProperty(AWSObject):
    """
    Used for CloudFormation Resource Property objects
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/
    aws-product-property-reference.html
    """

    def __init__(self, **kwargs):
        sup = super(AWSProperty, self)
        sup.__init__(None, props=self.props, **kwargs)


def validate_pausetime(pausetime):
    if not pausetime.startswith('PT'):
        raise ValueError('PauseTime should look like PT#H#M#S')
    return pausetime


class UpdatePolicy(AWSObject):
    props = {
        'MaxBatchSize': (basestring, False),
        'MinInstancesInService': (basestring, False),
        'PauseTime': (validate_pausetime, False),
    }

    valid_update_policies = (
        'AutoScalingRollingUpdate',
    )

    def __init__(self, name, **kwargs):
        sup = super(UpdatePolicy, self)
        sup.__init__(None, None, name, self.props, **kwargs)

        if name not in self.valid_update_policies:
            raise ValueError('UpdatePolicy name must be one of %r' % (
                self.valid_update_policies,))


class AWSHelperFn(object):
    def getdata(self, data):
        if isinstance(data, AWSObject):
            return data.name
        else:
            return data


class Base64(AWSHelperFn):
    def __init__(self, data):
        self.data = {'Fn::Base64': data}

    def JSONrepr(self):
        return self.data


class FindInMap(AWSHelperFn):
    def __init__(self, map, key, value):
        self.data = {'Fn::FindInMap': [self.getdata(map), key, value]}

    def JSONrepr(self):
        return self.data


class GetAtt(AWSHelperFn):
    def __init__(self, logicalName, attrName):
        self.data = {'Fn::GetAtt': [self.getdata(logicalName), attrName]}

    def JSONrepr(self):
        return self.data


class GetAZs(AWSHelperFn):
    def __init__(self, region):
        self.data = {'Fn::GetAZs': region}

    def JSONrepr(self):
        return self.data


class Join(AWSHelperFn):
    def __init__(self, delimiter, values):
        self.data = {'Fn::Join': [delimiter, values]}

    def JSONrepr(self):
        return self.data


class Name(AWSHelperFn):
    def __init__(self, data):
        self.data = self.getdata(data)

    def JSONrepr(self):
        return self.data


class Select(AWSHelperFn):
    def __init__(self, indx, objects):
        self.data = {'Fn::Select': [indx, objects]}

    def JSONrepr(self):
        return self.data


class Ref(AWSHelperFn):
    def __init__(self, data):
        self.data = {'Ref': self.getdata(data)}

    def JSONrepr(self):
        return self.data


class awsencode(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'JSONrepr'):
            return obj.JSONrepr()
        return json.JSONEncoder.default(self, obj)


class Tags(object):
    def __init__(self, **kwargs):
        self.tags = []
        for k, v in kwargs.iteritems():
            self.tags.append({
                'Key': k,
                'Value': v,
            })

    def JSONrepr(self):
        return self.tags


class Template(object):
    props = {
        'AWSTemplateFormatVersion': (basestring, False),
        'Description': (basestring, False),
        'Parameters': (dict, False),
        'Mappings': (dict, False),
        'Resources': (dict, False),
        'Outputs': (dict, False),
    }

    def __init__(self):
        self.description = None
        self.mappings = {}
        self.outputs = {}
        self.parameters = {}
        self.resources = {}
        self.version = None

    def add_description(self, description):
        self.description = description

    def add_output(self, output):
        if isinstance(output, list):
            for o in output:
                self.outputs[o.name] = o
        else:
            self.outputs[output.name] = output
        return output

    def add_mapping(self, name, mapping):
        self.mappings[name] = mapping

    def add_parameter(self, parameter):
        if isinstance(parameter, list):
            for p in parameter:
                self.parameters[p.name] = p
        else:
            self.parameters[parameter.name] = parameter
        return parameter

    def add_resource(self, resource):
        if isinstance(resource, list):
            for r in resource:
                self.resources[r.name] = r
        else:
            self.resources[resource.name] = resource
        return resource

    def add_version(self, version=None):
        if version:
            self.version = version
        else:
            self.version = "2010-09-09"

    def to_json(self, indent=4, sort_keys=True):
        t = {}
        if self.description:
            t['Description'] = self.description
        if self.mappings:
            t['Mappings'] = self.mappings
        if self.outputs:
            t['Outputs'] = self.outputs
        if self.parameters:
            t['Parameters'] = self.parameters
        if self.version:
            t['AWSTemplateFormatVersion'] = self.version
        t['Resources'] = self.resources

        return json.dumps(t, cls=awsencode, indent=indent, sort_keys=sort_keys)

    def JSONrepr(self):
        return [self.parameters, self.mappings, self.resources]


class Output(AWSObject):
    props = {
        'Description': (basestring, False),
        'Value': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        sup = super(Output, self)
        sup.__init__(name, None, props=self.props, **kwargs)


class Parameter(AWSObject):
    props = {
        'Type': (basestring, True),
        'Default': (basestring, False),
        'NoEcho': (bool, False),
        'AllowedValues': (list, False),
        'AllowedPattern': (basestring, False),
        'MaxLength': (validators.positive_integer, False),
        'MinLength': (validators.positive_integer, False),
        'MaxValue': (validators.integer, False),
        'MinValue': (validators.integer, False),
        'Description': (basestring, False),
        'ConstraintDescription': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = None
        sup = super(Parameter, self)
        sup.__init__(name, props=self.props, **kwargs)
