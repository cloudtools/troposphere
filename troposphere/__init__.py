# Copyright (c) 2011-2012, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


import json


class AWSObject(object):
    def __init__(self, type=None, name=None, props={}, **kwargs):
        self.name = name
        self.type = type
        self.props = props
        self.names = props.keys()
        # Create the list of properties set on this object by the user
        self.properties = {}
        if name:
            self.resource = {
                    name: self.properties,
            }
        else:
            self.resource = self.properties
        if self.type:
            self.resource['Type'] = self.type
        self.__initialized = True
        # Now that it is initialized, populate it with the kwargs
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __getattr__(self, name):
        try:
            return self.properties.__getitem__(name)
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if '_AWSObject__initialized' not in self.__dict__:
            return dict.__setattr__(self, name, value)
        elif name in self.names:
            # Check the type of the object and compare against what
            # we were expecting. Special case AWS helper functions.
            if isinstance(value, self.props[name][0]) or \
                isinstance(value, AWSHelperFn):
                return self.properties.__setitem__(name, value)
            else:
                raise ValueError
        raise AttributeError

    def JSONrepr(self):
        for k, v in self.props.items():
            if v[1] and k not in self.properties:
                print "Resource %s required in type %s" % (k, self.type)
        return self.resource


class AWSHelperFn(object):
    pass


class Base64(AWSHelperFn):
    def __init__(self, data):
        self.data = {'Fn::Base64': data}

    def JSONrepr(self):
        return self.data


class FindInMap(AWSHelperFn):
    def __init__(self, map, key, value):
        self.data = {'Fn::FindInMap': [map, key, value]}

    def JSONrepr(self):
        return self.data


class GetAtt(AWSHelperFn):
    def __init__(self, logicalName, attrName):
        self.data = {'Fn::GetAtt': [logicalName, attrName]}

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


class Select(AWSHelperFn):
    def __init__(self, indx, objects):
        self.data = {'Fn::Select': [indx, objects]}

    def JSONrepr(self):
        return self.data


class Ref(AWSHelperFn):
    def __init__(self, data):
        self.data = {'Ref': data}

    def JSONrepr(self):
        return self.data


class awsencode(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'JSONrepr'):
            return obj.JSONrepr()
        return json.JSONEncoder.default(self, obj)


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
        self.mappings = {}
        self.outputs = {}
        self.parameters = {}
        self.resources = {}

    def to_json(self, indent=4, sort_keys=True):
        t = {}
        if self.outputs:
            t['Outputs'] = self.outputs
        if self.parameters:
            t['Parameters'] = self.parameters
        if self.mappings:
            t['Mappings'] = self.mappings
        t['Resources'] = self.resources

        return json.dumps(t, cls=awsencode, indent=indent, sort_keys=sort_keys)

    def JSONrepr(self):
        return [self.parameters, self.mappings, self.resources]


class Output(AWSObject):
    props = {
        'Description': (basestring, False),
        'Value': (basestring, True),
    }

    def __init__(self, **kwargs):
        self.type = None
        sup = super(Output, self)
        sup.__init__(props=self.props, **kwargs)


class Parameter(AWSObject):
    props = {
        'Type': (basestring, True),
        'Default': (basestring, False),
        'NoEcho': (bool, False),
        'AllowedValues': (list, False),
        'AllowedPattern': (basestring, False),
        'MaxLength': (basestring, False),
        'MinLength': (basestring, False),
        'MaxValue': (basestring, False),
        'MinValue': (basestring, False),
        'Description': (basestring, False),
        'ConstraintDescription': (basestring, False),
    }

    def __init__(self, **kwargs):
        self.type = None
        sup = super(Parameter, self)
        sup.__init__(props=self.props, **kwargs)
