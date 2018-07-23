import argparse
import json

import sys


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
# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
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


map_type3 = {
    'Boolean': 'bool',
    'Double': 'float',
    'Integer': 'int',
    'Json': 'dict',
    'Long': 'int',
    'String': 'str',
    'Timestamp': 'str',
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


def get_type3(value):
    if 'PrimitiveType' in value:
        return map_type3.get(value['PrimitiveType'], value['PrimitiveType'])
    if value['Type'] == 'List':
        if 'ItemType' in value:
            return "[%s]" % value['ItemType']
        else:
            return "[%s]" % map_type3.get(value['PrimitiveItemType'])
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
        if key == 'Tags':
            value_type = "Tags"
        else:
            value_type = get_type(value)

        # Wrap long names for pycodestyle
        if len(key) + len(value_type) < 55:
            print "        '%s': (%s, %s)," % (
                key, value_type, get_required(value))
        else:
            print "        '%s':\n            (%s, %s)," % (
                key, value_type, get_required(value))
    print '    }'


def output_class_stub(class_name, properties, resource_name=None):
    print
    print
    if resource_name:
        print 'class %s(AWSObject):' % class_name
        print '    resource_type: str'
        print
        sys.stdout.write('    def __init__(self, title')
    else:
        print 'class %s(AWSProperty):' % class_name
        print
        sys.stdout.write('    def __init__(self')

    for key, value in sorted(properties.iteritems()):
        if key == 'Tags':
            value_type = "Tags"
        else:
            value_type = get_type3(value)

        if value_type.startswith("["):  # Means that args are a list
            sys.stdout.write(', %s:List%s=...' % (key, value_type))
        else:
            sys.stdout.write(', %s:%s=...' % (key, value_type))

    print ') -> None: ...'
    print

    for key, value in sorted(properties.iteritems()):
        if key == 'Tags':
            value_type = "Tags"
        else:
            value_type = get_type3(value)

        if value_type.startswith("["):  # Means that args are a list
            print '    %s: List%s' % (key, value_type)
        else:
            print '    %s: %s' % (key, value_type)


def process_file(filename, stub=False):
    f = open(filename)
    j = json.load(f)

    if 'PropertyTypes' in j:
        for property_name, property_dict in j['PropertyTypes'].items():
            if property_name == "Tag":
                print "from troposphere import Tags"
                print
                continue
            class_name = property_name.split('.')[1]
            properties = property_dict['Properties']
            if stub:
                output_class_stub(class_name, properties)
            else:
                output_class(class_name, properties)

    for resource_name, resource_dict in j['ResourceType'].items():
        class_name = resource_name.split(':')[4]
        properties = resource_dict['Properties']
        if stub:
            output_class_stub(class_name, properties, resource_name)
        else:
            output_class(class_name, properties, resource_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--stub', action='store_true', default=False)
    parser.add_argument('filename', nargs='+')
    args = parser.parse_args()

    if args.stub:
        print copyright_header,
        for f in args.filename:
            process_file(f, stub=True)
    else:
        print copyright_header,
        for f in args.filename:
            process_file(f)
