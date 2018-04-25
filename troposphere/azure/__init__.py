import json
import re
import cfn_flip as cfn_flip

from troposphere import  encode_to_dict, AWSObject, AWSProperty, Parameter, validators

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
        'description': (str, False),
        'variables': (str, False),
        'parameters': (dict, False),
        'resources': (dict, False),
        'outputs': (dict, False),
    }

    def __init__(self, Description=None, ContentVersion="1.0.0.0"):
        self.contentVersion = ContentVersion
        self.description = Description
        self.variables = []
        self.parameters = {}
        self.resources = []
        self.outputs = {}

    def add_description(self, description):
        self.description = description

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
                item = next(
                    iter(filter(lambda x: hasattr(x, 'title') and hasattr(v, 'title') and x.title == v.title, lst)),
                    None)
                if item:
                    self.handle_duplicate_key(v.title)
                else:
                    lst.append(v)
        else:
            item = next(iter(
                filter(lambda x: hasattr(x, 'title') and hasattr(values, 'title') and x.title == values.title, lst)),
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
        if self.description:
            t['description'] = self.description

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

    def __init__(self, title, template=None, validation=True, **kwargs):
        AWSObject.__init__(self, title, template, validation, **kwargs)

        if 'Type' in self.resource:
            self.resource['type'] = self.resource['Type']
            del self.resource['Type']

        if hasattr(self, 'location') and self.location and 'location' not in self.resource:
            self.resource['location'] = "[resourceGroup().location]"

        if title:
            self.resource['name'] = self.title

        if hasattr(self, 'apiVersion'):
            self.resource['apiVersion'] = self.apiVersion

        # move root props from properties to resources dict to be in root of object when serialized
        super(ARMObject, self)._validate_props()
        for rootProp in list(filter(lambda x: issubclass(type(x[1]), ARMRootProperty), self.properties.items())):
            k, v = rootProp
            self.resource[k] = v
            del self.properties[k]
            del self.props[k]

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

    def validate_title(self):
        if not valid_names_azure.match(self.title):
            raise ValueError('Name "%s" is not valid' % self.title)

    # fluent api
    def with_depends_on(self, dependsOn):
        if 'dependsOn' not in self.resource:
            self.resource['dependsOn'] = []
        if isinstance(dependsOn, list):
            for d in dependsOn:
                self._add_dependency(d)
        else:
            self._add_dependency(dependsOn)
        return self

    def _add_dependency(self, dependency):
        if isinstance(dependency, ARMObject):
            self.resource['dependsOn'].append(dependency.Ref())
        elif isinstance(dependency, str):
            self.resource['dependsOn'].append(dependency)
        else:
            raise ValueError('Unsupported type')


class ARMProperty(AWSProperty):
    pass


class ARMRootProperty(ARMProperty):
    pass


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
