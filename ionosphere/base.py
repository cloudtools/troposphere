import json
import re

import cfn_flip as cfn_flip

from ionosphere import encode_to_dict, AWSObject, AWSProperty, Parameter, validators, AWSHelperFn

# Template Limits
MAX_VARIABLES = 256
MAX_OUTPUTS = 64
MAX_PARAMETERS = 256
MAX_RESOURCES = 800
PARAMETER_TITLE_MAX = 255

valid_names_azure = re.compile(r'^[a-zA-Z0-9_-]+$')


class ARMTemplate(object):
    props = {
        '$schema': (str, False),
        'contentVersion': (str, False),
        'variables': (str, False),
        'parameters': (dict, False),
        'resources': (dict, True),
        'outputs': (dict, False),
    }

    def __init__(self, contentVersion="1.0.0.0"):
        self.contentVersion = contentVersion
        self.variables = []
        self.parameters = {}
        self.resources = []
        self.outputs = {}

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

    def _update_list(self, lst, values):
        if isinstance(values, list):
            for v in values:
                item = next(iter(filter(lambda x: hasattr(x, 'title') and hasattr(v, 'title') and x.title == v.title,
                                        lst)), None)
                if item:
                    self.handle_duplicate_key(v.title)
                else:
                    lst.append(v)
        else:
            item = next(
                iter(filter(lambda x: hasattr(x, 'title') and hasattr(values, 'title') and x.title == values.title, lst)),
                None)
            if item:
                self.handle_duplicate_key(values.title)
            else:
                lst.append(values)
        return values

    def add_output(self, output):
        if len(self.outputs) >= MAX_OUTPUTS:
            raise ValueError('Maximum outputs %d reached' % MAX_OUTPUTS)
        return self._update(self.outputs, output)

    def add_parameter(self, parameter):
        if len(self.parameters) >= MAX_PARAMETERS:
            raise ValueError('Maximum parameters %d reached' % MAX_PARAMETERS)
        return self._update(self.parameters, parameter)

    def add_variable(self, variable):
        if len(self.variables) >= MAX_VARIABLES:
            raise ValueError('Maximum variables %d reached' % MAX_VARIABLES)
        return self._update_list(self.variables, variable)

    def add_resource(self, resource):
        if len(self.resources) >= MAX_RESOURCES:
            raise ValueError('Maximum number of resources %d reached'
                             % MAX_RESOURCES)
        return self._update_list(self.resources, resource)

    def add_content_version(self, version=None):
        if version:
            self.contentVersion = version
        else:
            self.contentVersion = "1.0.0.0"

    def to_dict(self):
        t = {}

        if self.outputs:
            t['outputs'] = self.outputs
        if self.parameters:
            t['parameters'] = self.parameters
        if self.contentVersion:
            t['contentVersion'] = self.contentVersion

        t['resources'] = self.resources
        t['$schema'] = "http://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json"

        return encode_to_dict(t)

    def to_json(self, indent=4, sort_keys=True, separators=(',', ': ')):
        return json.dumps(self.to_dict(), indent=indent,
                          sort_keys=sort_keys, separators=separators)

    def to_yaml(self, long_form=False):
        return cfn_flip.to_yaml(self.to_json(), long_form)


class ARMObject(AWSObject):
    dictname = 'properties'
    root_props = None

    def __init__(self, title, template=None, validation=True, **kwargs):
        AWSObject.__init__(self, title, template, validation, **kwargs)

        if hasattr(self, 'location') and self.location and 'location' not in self.resource:
            self.resource['location'] = "[resourceGroup().location]"

        if title:
            self.resource['name'] = self.title

        if hasattr(self, 'apiVersion'):
            self.resource['apiVersion'] = self.apiVersion

        # move root props from properties to resources dict to be in root of object when serialized
        # super(ARMObject, self)._validate_props()
        # for rootProp in list(filter(lambda x: issubclass(type(x[1]), ARMRootProperty), self.properties.items())):
        #     k, v = rootProp
        #     self.resource[k] = v
        #     del self.properties[k]
        #     del self.props[k]

    def to_dict(self):
        if 'name' in self.resource:
            self.resource['name'] = self.title
        if 'tags' in self.properties:
            self.resource['tags'] = self.properties['tags']
            del self.properties['tags']
        if 'dependsOn' in self.properties:
            self.resource['dependsOn'] = self.properties['dependsOn']
            del self.properties['dependsOn']
        return AWSObject.to_dict(self)

    def ref(self):
        return "[resourceId('{0}/','{1}')]".format(self.resource['type'], self.title)

    Ref = ref

    def get_att(self, value):
        raise NotImplementedError()

    # todo - add stuff relevant for azure like refs to properties shortcuts similar to what we have in in the AWSObject

    def validate_title(self):
        if not valid_names_azure.match(self.title):
            raise ValueError('Name "%s" is not valid' % self.title)

    # fluent api
    def with_depends_on(self, depends_on):
        if 'dependsOn' not in self.resource:
            self.resource['dependsOn'] = []
        self.resource['dependsOn'].extend(self._add_dependencies(depends_on))
        return self

    def _add_dependencies(self, value):
        if isinstance(value, list):
            result = []
            for d in value:
                result.append(self._add_dependency(d))
            return result
        else:
            return [self._add_dependency(value)]

    def _add_dependency(self, dependency):
        if isinstance(dependency, ARMObject):
            return dependency.Ref()
        elif isinstance(dependency, str):
            return dependency
        else:
            raise ValueError('Unsupported type')

    def _move_prop_to_root(self, key):
        if key in self.properties:
            self.resource[key] = self.properties[key]
            del self.properties[key]


class ARMProperty(AWSProperty):
    # Used to specify properties that should be on the root object in Azure
    root_props = None

    def validate_title(self):
        if not valid_names_azure.match(self.title):
            raise ValueError('Name "%s" is not valid' % self.title)


# class ARMRootProperty(ARMProperty):
#     pass


class ARMParameter(Parameter):
    STRING_PROPERTIES = ['maxLength', 'minLength']
    NUMBER_PROPERTIES = ['maxValue', 'minValue']
    SUPPORTED_TYPES = ['string', 'secureString', 'int', 'bool', 'object', 'secureObject', 'array']

    props = {
        'type': (str, True),
        'defaultValue': ((str, int, float), False),
        'allowedValues': (list, False),
        'maxLength': (validators.positive_integer, False),
        'minLength': (validators.positive_integer, False),
        'maxValue': (validators.integer, False),
        'minValue': (validators.integer, False),
        'description': (str, False)
    }

    root_props = None

    def to_dict(self):
        if 'description' in self.properties:
            description = self.properties['description']
            self.properties['metadata'] = {'description': description}
            del self.properties['description']

        return Parameter.to_dict(self)

    def ref(self):
        return "[parameters('{}')]".format(self.title)

    Ref = ref

    def validate(self):
        def check_type(t, v):
            try:
                t(v)
                return True
            except ValueError:
                return False

        # Validate allowed types
        if self.properties['type'] not in self.SUPPORTED_TYPES:
            raise ValueError("{} is not a supported parameter type. Supported types: {}".format(
                self.properties['type'], self.SUPPORTED_TYPES))

        # Validate the Default parameter value
        default = self.properties.get('defaultValue')
        if default:
            error_str = ("Parameter default type mismatch: expecting "
                         "type %s got %s with value %r")
            # Get the Type specified and see whether the default type
            # matches (in the case of a String Type) or can be coerced
            # into one of the number formats.
            param_type = self.properties.get('type')
            if (param_type == 'string' or param_type == 'secureString') and not isinstance(default, str):
                raise ValueError(error_str %
                                 ('string', type(default), default))
            elif param_type == 'int' and not isinstance(default, int):
                raise ValueError(error_str %
                                 (param_type, type(default), default))
            elif param_type == 'bool' and not isinstance(default, bool):
                raise ValueError(error_str %
                                 (param_type, type(default), default))
            elif param_type == 'array':
                if not isinstance(default, str):
                    raise ValueError(error_str %
                                     (param_type, type(default), default))
                allowed = [str, int]
                dlist = default.split(",")
                for d in dlist:
                    # Verify the split array are all in allowed
                    if not any([check_type(x, d) for x in allowed]):
                        raise ValueError(error_str %
                                         (param_type, type(d), dlist))

        if self.properties['type'] != 'string':
            for p in self.STRING_PROPERTIES:
                if p in self.properties:
                    raise ValueError("%s can only be used with parameters of "
                                     "the String type." % p)
        if self.properties['type'] != 'int':
            for p in self.NUMBER_PROPERTIES:
                if p in self.properties:
                    raise ValueError("%s can only be used with parameters of "
                                     "the Number type." % p)


class SubResource(ARMProperty):
    props = {
        'id': (str, True),
    }


class SubResourceRef(AWSHelperFn):
    def __init__(self, root_resource, sub_resource, root, child):
        sub_resource_ref = self._build_sub_resource_ref(root_resource, sub_resource)
        root_name = self._get_title(root)
        child_name = self._get_title(child)
        self.data = {'id': "[resourceId('{0}', '{1}', '{2}')]".format(sub_resource_ref, root_name, child_name)}

    def _build_sub_resource_ref(self, root_resource, sub_resource):
        root_resource_type = self._get_resource_type(root_resource)
        sub_resource_type = self._get_resource_type(sub_resource)
        return "{0}/{1}".format(root_resource_type, sub_resource_type)

    def _get_resource_type(self, r):
        return r if isinstance(r, str) else r.resource_type

    def _get_title(self, obj):
        if isinstance(obj, str):
            return obj
        return obj.title
