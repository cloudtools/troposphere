#!/usr/bin/env python


import argparse
import json
import pprint


class object_registry(object):
    """Keep track of objects being created as Parameters or Resources
    in order to map back to due to use in intrinsic functions like
    Ref() and GetAtt().
    """
    def __init__(self):
        self.objects = {}

    def add(self, o):
        new_name = o.replace('-', '_')
        self.objects[o] = new_name
        return new_name

    def lookup(self, o):
        if o in self.objects:
            return self.objects[o]
        else:
            return output_value(o)

objects = object_registry()

object_functions = {
    "Table":        [ "ProvisionedThroughput", "PrimaryKey", "Element" ],
    "LoadBalancer": [ "HealthCheck", "ConnectionDrainingPolicy", "AccessLoggingPolicy" ],
    "Queue":        [ "RedrivePolicy" ],
    "Bucket":       [ "WebsiteConfiguration" ],
    "User":         [ "LoginProfile" ],
    "Topic":        [ "Subscription" ],
    "Instance":     [ "NetworkInterfaceProperty", "PrivateIpAddressSpecification" ],
    "RecordSet":    [ "RecordSetType" ],
    "Policy":       [ "PolicyType" ],
}

def additional_imports(o):
    if object_functions.has_key(o):
        return ", ".join([o] + object_functions[o])
    else:
        return o

def do_header(d):
    """Output a stock header for the new Python script and also try to
    figure out the Resource imports needed by the template.
    """
    print 'from troposphere import Base64, Select, FindInMap, GetAtt, GetAZs, Join, Output, If, And, Not, Or, Equals, Condition'
    print 'from troposphere import Parameter, Ref, Tags, Template'
    print 'from troposphere.cloudformation import Init'
    print 'from troposphere.cloudfront import Distribution, DistributionConfig'
    print 'from troposphere.cloudfront import Origin, DefaultCacheBehavior'
    print 'from troposphere.ec2 import PortRange'

    # Loop over the resources to find imports
    if 'Resources' in d:
        seen = []
        resources = d['Resources']
        for k, v in resources.items():
            (mod, tropo_object) = generate_troposphere_object(v['Type'])
            if tropo_object not in seen:
                seen.append(tropo_object)
                print 'from troposphere.%s import %s' % (mod, additional_imports(tropo_object))
    print
    print
    print "t = Template()"
    print


def do_awstemplateformatversion(d):
    """Output the template version"""
    print 't.add_version("%s")' % (d['AWSTemplateFormatVersion'], )
    print


def do_description(d):
    """Output the template Description"""
    print 't.add_description("""\\\n%s""")' % (d['Description'], )


def do_parameters(d):
    """Output the template Parameters"""
    params = d['Parameters']
    for k, v in params.items():
        object_name = objects.add(k)
        print '%s = t.add_parameter(Parameter(' % (object_name,)
        print '    "%s",' % (k, )
        for pk, pv in v.items():
            print '    %s=%s,' % (pk, output_value(pv))
        print "))"
        print


def do_conditions(d):
    """Output the template Conditions"""
    conditions = d['Conditions']
    for k, v in conditions.items():
        print 't.add_condition("%s",' % (k,)
        print '    %s' % output_value(v)
        print ")"
        print

def do_mappings(d):
    """Output the template Mappings"""
    mappings = d['Mappings']
    for k, v in mappings.items():
        print 't.add_mapping("%s",' % (k,)
        pprint.pprint(v)
        print ")"
        print


def map_module(mod):
    """Map module names as needed"""
    if mod == "lambda":
        return "awslambda"
    return mod


def generate_troposphere_object(typename):
    """Try to determine the troposphere object to create from the Type
    specification from the Resource being converted.
    """
    t = typename.split(':')
    if len(t) == 5:
        return (map_module(t[2].lower()), t[4])
    else:
        return ('', typename)


def output_dict(d):
    out = []
    for k,v in d.items():
        out.append("%s=%s" % (k.replace('\\', '\\\\'), output_value(v)))
    return ", ".join(out)

known_functions = {
    "DistributionConfig":       1,
    "DefaultCacheBehavior":     1,
    "ProvisionedThroughput":    1,
    "NetworkInterfaces":        1,
    "WebsiteConfiguration":     1,
    "RedrivePolicy":            1,
    "Subscription":             1,
    "KeySchema":                1,
    "HashKeyElement":           1,
    "HealthCheck":              1,
    "LoginProfile":             1,
    "ConnectionDrainingPolicy": 1,
    "AccessLoggingPolicy":      1,
    "AWS::CloudFormation::Init":1,
    "PrivateIpAddresses"       :1,
    "ContainerDefinitions"     :1,
}

function_quirks = {
    "KeySchema":          "PrimaryKey",
    "HashKeyElement":     { "Element": ["AttributeName", "AttributeType"] },
    "NetworkInterfaces":  [ "NetworkInterfaceProperty" ],
    "Subscription":       [ "Subscription" ],
    "LoginProfile":       { "LoginProfile": ["Password"] },
    "AWS::CloudFormation::Init": {"Init": []},
    "PrivateIpAddresses" : ["PrivateIpAddressSpecification"],
    "ContainerDefinitions": ["ContainerDefinition"],
}

def do_output_function(k, f, v):
    print '    %s=%s(' % (k, f)
    for pk, pv in v.items():
        if known_functions.has_key(pk):
            do_resources_content(pk, pv, "")
        else:
            print "        %s=%s," % (pk, output_value(pv))
    print '    ),'

def do_output_quirk_list(k, f, v):
    print '    %s=[' % (k)
    for e in v:
        print '    %s(' % (f)
        for pk, pv in e.items():
            if known_functions.has_key(pk):
                do_resources_content(pk, pv)
            else:
                print "        %s=%s," % (pk, output_value(pv))
        print '    ),'
    print '    ],'

def do_output_quirk_mapping(k, v):
    m = function_quirks[k]
    for pk in m.keys():
        print '    %s=%s(' % (k, pk)
        for e in m[pk]:
            print "        %s," % (output_value(v[e]))
        print '    ),'

def do_output_quirk_metadata(k, v):
    m = function_quirks[k]
    for pk in m.keys():
        print '    Metadata=%s(' % (pk)
        print "        %s," % (output_value(v))
        print '    ),'

def do_resources_content(k, v, p=""):
    if function_quirks.has_key(k):
        x = function_quirks[k];
        if(isinstance(x, dict)):
            if(p == "Metadata"):
                do_output_quirk_metadata(k, v)
            else:
                do_output_quirk_mapping(k, v)
        elif(isinstance(x, list)):
           do_output_quirk_list(k, x[0], v)
        else:
           do_output_function(k, x, v)
    else:
        do_output_function(k, k, v)

top_level_aliases = {
    "RecordSet": "RecordSetType",
    "Policy":    "PolicyType",
}

def do_resources(d):
    """Output the template Resources"""
    resources = d['Resources']
    for k, v in resources.items():
        object_name = objects.add(k)
        (_, tropo_object) = generate_troposphere_object(v['Type'])
        if(top_level_aliases.has_key(tropo_object)):
            tropo_object = top_level_aliases[tropo_object]
        print '%s = t.add_resource(%s(' % (object_name, tropo_object)
        print '    "%s",' % (k, )
        for p in filter(lambda x: v.has_key(x), ['Metadata', 'Properties']):
            for pk, pv in v[p].items():
                if pk == "Tags":
                    print '    Tags=Tags('
                    for d in pv:
                        print "        %s=%s," % (
                            d['Key'], output_value(d['Value']))
                    print '    ),'
                elif pk == 'PortRange':
                    print "    %s=%s(%s)," % (pk, pk, output_dict(pv))
                elif known_functions.has_key(pk):
                    do_resources_content(pk, pv, p)
                elif isinstance(pv, basestring):
                    print '    %s="%s",' % (pk, pv)
                else:
                    print '    %s=%s,' % (pk, output_value(pv))
        if v.has_key("DependsOn"):
            print '    %s=%s,' % ("DependsOn", output_value(v['DependsOn']))
        if v.has_key("Condition"):
            print '    %s=%s,' % ("Condition", output_value(v['Condition']))
        print "))"
        print


def handle_no_objects(name, values):
    """Handle intrinsic functions which do not have a named resource"""
    return name + "(" + ", ".join(map(output_value, values)) + ")"

def handle_one_object(name, values):
    """Handle intrinsic functions which have a single named resource"""
    ret = name + "("
    for i, param in enumerate(values):
        if i > 0:
            ret += ", "
        # First parameter might be an object name or pseudo parameter
        if i == 0:
            ret += objects.lookup(param)
        else:
            ret += output_value(param)
    return ret + ")"


function_map = {
    'Fn::Base64': ("Base64", handle_no_objects),
    'Fn::And': ("And", handle_no_objects),
    'Fn::Or': ("Or", handle_no_objects),
    'Fn::Not': ("Not", handle_no_objects),
    'Fn::If': ("If", handle_one_object),
    'Fn::Equals': ("Equals", handle_no_objects),
    'Fn::FindInMap': ("FindInMap", handle_no_objects),
    'Fn::GetAtt': ("GetAtt", handle_one_object),
    'Fn::GetAZs': ("GetAZs", handle_no_objects),
    'Fn::Join': ("Join", handle_no_objects),
    'Fn::Select': ("Select", handle_one_object),
    'Ref': ("Ref", handle_one_object),
    'Condition': ("Condition", handle_one_object),
}


def output_value(v):
    """Output a value which may be a string or a set of function calls."""
    if isinstance(v, basestring):
        return '"%s"' % (v.replace('\\', '\\\\').replace('\n', '\\n').replace("\"", "\\\""))
    elif isinstance(v, bool):
        return '%s' % (str(v))
    elif isinstance(v, int):
        return '%d' % (v)
    elif isinstance(v, list):
        return "[" + ", ".join(map(output_value, v)) + "]"

    out = []
    # Should only be one of these...
    for fk, fv in v.items():
        if fk in function_map:
            (shortname, handler) = function_map[fk]
            if not isinstance(fv, list):
                fv = [fv]
            return handler(shortname, fv)
        else:
            out.append( '"' + fk + '": ' + output_value(fv))
    return "{ " + ", ".join(out) + " }"


def do_outputs(d):
    """Output the template Outputs"""
    outputs = d['Outputs']
    for k, v in outputs.items():
        print '%s = t.add_output(Output(' % (k,)
        print '    "%s",' % (k, )
        for pk, pv in v.items():
            if isinstance(pv, basestring):
                print '    %s="%s",' % (pk, pv)
            else:
                print '    %s=%s,' % (pk, output_value(pv))
        print "))"
        print


def do_trailer(d):
    """Output a trailer section for the new Python script."""
    print 'print(t.to_json())'


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="template to convert")
    args = parser.parse_args()

    d = json.load(open(args.filename))

    do_header(d)

    sections = [
        'AWSTemplateFormatVersion',
        'Description',
        'Parameters',
        'Conditions',
        'Mappings',
        'Resources',
        'Outputs',
    ]

    for s in sections:
        if s in d.keys():
            globals()["do_" + s.lower()](d)

    do_trailer(d)
