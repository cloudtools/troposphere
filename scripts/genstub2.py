import argparse
import json


# Python 3 code generator to create new troposphere class stubs from the
# AWS resource specification. Stubs are required to allow IDEs to autocomplete
# dynamically generated classes.


copyright_header = """\
# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

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
        print '    resource_type = None # Type: basestring'
        print
    else:
        print 'class %s(AWSProperty):' % class_name

    for key, value in sorted(properties.iteritems()):
        if key == 'Tags':
            value_type = "Tags"
        else:
            value_type = get_type(value)

        if value_type.startswith("["):  # Means that args are a list
            print '    %s = None # Type: List%s' % (key, value_type)
        else:
            print '    %s = None # Type: %s' % (key, value_type)


def process_file(filename):
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
