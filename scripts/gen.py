import argparse
import json


# Python code generator to create new troposphere classes from the
# AWS resource specification.
#
# Todo:
# - Currently only handles the single files (not the all-in-one)
#   (Note: but will deal with things like spec/GuardDuty*)
# - Handle adding in validators
# - Verify propery dependency/ordering in the file
# - Needs better error checking
# - Need to figure out the correct Timestamp type

copyright_header = """\
# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, integer
"""


def get_required(value):
    return value['Required']


map_type = {
    'Boolean': 'boolean',
    'Double': 'float',
    'Integer': 'integer',
    'Json': 'dict',
    'Long': 'integer',
    'String': 'basestring',
    'Timestamp': 'basestring',
}


def get_type(value):
    if 'PrimitiveType' in value:
        return map_type.get(value['PrimitiveType'], value['PrimitiveType'])
    if value['Type'] == 'List':
        if 'ItemType' in value:
            return "[%s]" % value['ItemType']
        else:
            return "[%s]" % map_type.get(value['PrimitiveItemType'])
    elif value['Type'] == 'Map':
        return 'dict'
    else:
        # Non-primitive (Property) name
        return value['Type']

    import pprint
    pprint.pprint(value)
    raise ValueError("get_type")


def output_class(class_name, properties, resource_name=None):
    print
    print
    if resource_name:
        print 'class %s(AWSObject):' % class_name
        print '    resource_type = "%s"' % resource_name
        print
    else:
        print 'class %s(AWSProperty):' % class_name

    # Output the props dict
    print '    props = {'
    for key, value in sorted(properties.iteritems()):
        value_type = get_type(value)

        # Wrap long names for pycodestyle
        if len(key) + len(value_type) < 55:
            print "        '%s': (%s, %s)," % (
                key, value_type, get_required(value))
        else:
            print "        '%s':\n            (%s, %s)," % (
                key, value_type, get_required(value))
    print '    }'


def process_file(filename):
    f = open(filename)
    j = json.load(f)

    if 'PropertyTypes' in j:
        for property_name, property_dict in j['PropertyTypes'].items():
            class_name = property_name.split('.')[1]
            properties = property_dict['Properties']
            output_class(class_name, properties)

    for resource_name, resource_dict in j['ResourceType'].items():
        class_name = resource_name.split(':')[4]
        properties = resource_dict['Properties']
        output_class(class_name, properties, resource_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='+')
    args = parser.parse_args()

    print copyright_header,
    for f in args.filename:
        process_file(f)
