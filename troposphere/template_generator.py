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

import inspect
from collections import Sequence, Mapping

import troposphere
from troposphere import (
    Template,
    Output, Parameter,  # AWSDeclarations
    AWSObject,  # covers resources
    AWSHelperFn)  # covers ref, fn::, etc
from troposphere.cloudformation import AWSCustomObject

# these are all the modules we want to cover.
from troposphere import (
    autoscaling, awslambda, cloudformation, cloudfront, cloudtrail, cloudwatch,
    codedeploy, codepipeline, config, datapipeline, directoryservice,
    dynamodb2, ec2, ecr, ecs, efs, elasticache, elasticbeanstalk,
    elasticloadbalancing, iam, kinesis, kms, logs, opsworks, policies, rds,
    redshift, route53, s3, sdb, sns, sqs, ssm, waf, workspaces)


class TemplateGenerator(Template):
    SUPPORTED_MODULES = [
        autoscaling, awslambda, cloudformation, cloudfront, cloudtrail,
        cloudwatch, codedeploy, codepipeline, config, datapipeline,
        directoryservice, dynamodb2, ec2, ecr, ecs, efs, elasticache,
        elasticbeanstalk, elasticloadbalancing, iam, kinesis, kms, logs,
        opsworks, policies, rds, redshift, route53, s3, sdb, sns, sqs, ssm, waf,
        workspaces, troposphere]

    _members = set()
    _resources = {}
    _functions = {}

    def __init__(self, cf_template):
        """
        Instantiates a new Troposphere Template based on an existing
        Cloudformation Template.
        """
        super(TemplateGenerator, self).__init__()
        if 'AWSTemplateFormatVersion' in cf_template:
            self.add_version(cf_template['AWSTemplateFormatVersion'])
        if 'Description' in cf_template:
            self.add_description(cf_template['Description'])
        if 'Metadata' in cf_template:
            self.add_metadata(cf_template['Metadata'])
        for k, v in cf_template.get('Parameters', {}).iteritems():
            self.add_parameter(self._create_instance(Parameter, v, k))
        for k, v in cf_template.get('Mappings', {}).iteritems():
            self.add_mapping(k, **self._convert_definition(v))
        for k, v in cf_template.get('Resources', {}).iteritems():
            self.add_resource(self._convert_definition(v, k))
        for k, v in cf_template.get('Outputs', {}).iteritems():
            self.add_output(self._create_instance(Output, v, k))

    @property
    def members(self):
        """
        Returns the list of all troposphere members we are able to
        construct
        """
        if not self._members:
            #  -- monkey patch begin --
            # until https://github.com/cloudtools/troposphere/pull/463 is merged
            from troposphere.ec2 import NetworkAclEntry, SecurityGroupIngress
            from troposphere.validators import boolean, network_port
            NetworkAclEntry.props['Egress'] = (boolean, False)
            SecurityGroupIngress.props['FromPort'] = (network_port, False)
            SecurityGroupIngress.props['ToPort'] = (network_port, False)
            #  -- monkey patch end --

            def members_predicate(m):
                return inspect.isclass(m) and not inspect.isbuiltin(m)

            members = []
            for module in self.SUPPORTED_MODULES:
                members.extend((m[1] for m in inspect.getmembers(
                    module, members_predicate)))
            TemplateGenerator._members = set(members)  # eliminate dupes
        return self._members

    @property
    def resources(self):
        """ Returns a map of `ResourceType: ResourceClass` """
        if not self._resources:
            TemplateGenerator._resources = {
                m.resource_type: m
                for m in self.members
                if issubclass(m, (AWSObject, AWSCustomObject)) and
                hasattr(m, 'resource_type')}
        return self._resources

    @property
    def functions(self):
        """ Returns a map of `FunctionName: FunctionClass` """
        if not self._functions:
            TemplateGenerator._functions = {
                m.__name__: m for m in self.members
                if issubclass(m, AWSHelperFn)}
        return self._functions

    def _generate_custom_type(self, resource_type):
        """ Generates a custom type with a custom resource type """
        if not resource_type.startswith("Custom::"):
            raise TypeError("Custom types must start with Custom::")
        custom_type = type(
            str(resource_type.replace("::", "")),
            (self.resources['AWS::CloudFormation::CustomResource'],),
            {'resource_type': resource_type})
        self.members.add(custom_type)
        self.resources[resource_type] = custom_type
        return custom_type

    def _convert_definition(self, definition, title=None):
        """
        Converts any object to its troposphere equivalent, if applicable.
        This function will recurse into obj's lists and mappings to create
        additional objects as necessary.
        """
        if isinstance(definition, Mapping):
            if 'Type' in definition:  # this is an AWS Resource
                expected_type = None
                try:
                    expected_type = self.resources[definition['Type']]
                except KeyError:
                    # if the user uses the custom way to name custom resources,
                    # we'll dynamically create a new subclass for this use and
                    # pass that instead of the typical CustomObject resource
                    try:
                        expected_type = self._generate_custom_type(
                            definition['Type'])
                    except TypeError:
                        assert expected_type is None

                if expected_type:
                    return self._create_instance(
                        expected_type, definition.get('Properties'), title)

            if len(definition) == 1:  # This might be a function?
                function_type = self._get_function_type(definition.keys()[0])
                if function_type:
                    return self._create_instance(
                        function_type, definition.values()[0], title)

            # return as dict
            return {k: self._convert_definition(v, k)
                    for k, v in definition.iteritems()}

        elif (not isinstance(definition, basestring) and
                isinstance(definition, Sequence)):
            return [self._convert_definition(v, title=title)
                    for v in definition]

        # anything else is returned as-is
        return definition

    def _create_instance(self, cls, args, title=None):
        """
        Returns an instance of `to_build` with `data` passed as arguments.

        Recursively inspects `data` to create nested objects and functions as
        necessary.

        `to_build` will only be considered only if it's an object we track
         (i.e.: troposphere objects).

        If `to_build` has a `props` attribute, nested properties will be
         instanciated as troposphere Property objects as necessary.

        If `to_build` is a list and contains a single troposphere type, the
         returned value will be a list of instances of that type.
        """
        if isinstance(cls, Sequence):
            if len(cls) == 1:
                # a list of 1 type means we must provide a list of such objects
                if (isinstance(args, basestring) or
                        not isinstance(args, Sequence)):
                    args = [args]
                return [self._create_instance(cls[0], v) for v in args]

        if isinstance(cls, Sequence) or cls not in self.members:
            # this object is not from troposphere; could be a string or int,
            # or a Ref... or a list of types such as
            # [basestring, FindInMap, Ref] or maybe a
            # validator such as `integer` or `port_range`
            return self._convert_definition(args, title=title)

        elif issubclass(cls, AWSHelperFn):
            # special handling for functions, we want to handle it before
            # entering the other conditions.
            if isinstance(args, Sequence) and not isinstance(args, basestring):
                return cls(*self._convert_definition(args))
            else:
                return cls(self._convert_definition(args))

        elif isinstance(args, Mapping):
            # we try to build as many troposphere objects as we can by
            # inspecting its type validation metadata
            kwargs = {}
            kwargs.update(args)
            for prop_name in getattr(cls, 'props', []):
                if prop_name not in args:
                    continue  # the user did not specify this value; skip it
                expected_type = cls.props[prop_name][0]

                if (isinstance(expected_type, Sequence) or
                        expected_type in self.members):
                    kwargs[prop_name] = self._create_instance(
                        expected_type, args[prop_name], prop_name)
                else:
                    kwargs[prop_name] = self._convert_definition(
                        args[prop_name], title=prop_name)

            return cls(title=title, **self._convert_definition(kwargs))

        # fallback when no match
        return cls(self._convert_definition(args), title=title)

    def _get_function_type(self, function_name):
        """
        Returns the function object that matches the provided name.
        Only Fn:: and Ref functions are supported here
        """
        if (function_name.startswith("Fn::") and
                function_name[4:] in self.functions):
            return self.functions[function_name[4:]]
        return self.functions['Ref'] if function_name == "Ref" else None
