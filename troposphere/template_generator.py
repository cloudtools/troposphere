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
    Template, Ref,
    Output, Parameter,  # AWSDeclarations
    AWSObject,  # covers resources
    AWSHelperFn, GenericHelperFn)  # covers ref, fn::, etc
from troposphere.cloudformation import AWSCustomObject
from troposphere.policies import UpdatePolicy, CreationPolicy

# these are all the modules we want to cover.
from troposphere import (
    autoscaling, awslambda, cloudformation, cloudfront, cloudtrail, cloudwatch,
    codedeploy, codepipeline, config, datapipeline, directoryservice,
    dynamodb2, ec2, ecr, ecs, efs, elasticache, elasticsearch,
    elasticbeanstalk, elasticloadbalancing, emr, iam, kinesis, kms, logs,
    opsworks, policies, rds, redshift, route53, s3, sdb, sns, sqs, ssm, waf,
    workspaces, apigateway)
from troposphere.openstack import heat, neutron, nova


class TemplateGenerator(Template):
    SUPPORTED_MODULES = [
        # aws
        autoscaling, awslambda, cloudformation, cloudfront, cloudtrail,
        cloudwatch, codedeploy, codepipeline, config, datapipeline,
        directoryservice, dynamodb2, ec2, ecr, ecs, efs, elasticache,
        elasticsearch, elasticbeanstalk, elasticloadbalancing, emr, iam,
        kinesis, kms, logs, opsworks, policies, rds, redshift, route53, s3,
        sdb, sns, sqs, ssm, waf, workspaces, troposphere, apigateway,
        # openstack
        heat, neutron, nova
    ]

    _inspect_members = set()
    _inspect_resources = {}
    _inspect_functions = {}

    def __init__(self, cf_template):
        """
        Instantiates a new Troposphere Template based on an existing
        Cloudformation Template.
        """
        super(TemplateGenerator, self).__init__()
        self._reference_map = {}
        if 'AWSTemplateFormatVersion' in cf_template:
            self.add_version(cf_template['AWSTemplateFormatVersion'])
        if 'Description' in cf_template:
            self.add_description(cf_template['Description'])
        if 'Metadata' in cf_template:
            self.add_metadata(cf_template['Metadata'])
        for k, v in cf_template.get('Parameters', {}).iteritems():
            self.add_parameter(self._create_instance(Parameter, v, k))
        for k, v in cf_template.get('Mappings', {}).iteritems():
            self.add_mapping(k, self._convert_definition(v))
        for k, v in cf_template.get('Conditions', {}).iteritems():
            self.add_condition(k, self._convert_definition(v, k))
        for k, v in cf_template.get('Resources', {}).iteritems():
            self.add_resource(self._convert_definition(v, k))
        for k, v in cf_template.get('Outputs', {}).iteritems():
            self.add_output(self._create_instance(Output, v, k))

    @property
    def inspect_members(self):
        """
        Returns the list of all troposphere inspect_members we are able to
        construct
        """
        if not self._inspect_members:
            #  -- monkey patch begin --
            # until https://github.com/cloudtools/troposphere/pull/463
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
            TemplateGenerator._inspect_members = set(members)  # remove dupes
        return self._inspect_members

    @property
    def inspect_resources(self):
        """ Returns a map of `ResourceType: ResourceClass` """
        if not self._inspect_resources:
            TemplateGenerator._inspect_resources = {
                m.resource_type: m
                for m in self.inspect_members
                if issubclass(m, (AWSObject, AWSCustomObject)) and
                hasattr(m, 'resource_type')}
        return self._inspect_resources

    @property
    def functions(self):
        """ Returns a map of `FunctionName: FunctionClass` """
        if not self._inspect_functions:
            TemplateGenerator._inspect_functions = {
                m.__name__: m for m in self.inspect_members
                if issubclass(m, AWSHelperFn)}
        return self._inspect_functions

    def _generate_custom_type(self, resource_type):
        """ Generates a custom type with a custom resource type """
        if not resource_type.startswith("Custom::"):
            raise TypeError("Custom types must start with Custom::")
        custom_type = type(
            str(resource_type.replace("::", "")),
            (self.inspect_resources['AWS::CloudFormation::CustomResource'],),
            {'resource_type': resource_type})
        self.inspect_members.add(custom_type)
        self.inspect_resources[resource_type] = custom_type
        return custom_type

    def _convert_definition(self, definition, ref=None):
        """
        Converts any object to its troposphere equivalent, if applicable.
        This function will recurse into obj's lists and mappings to create
        additional objects as necessary.
        """
        if isinstance(definition, Mapping):
            if 'Type' in definition:  # this is an AWS Resource
                expected_type = None
                try:
                    expected_type = self.inspect_resources[definition['Type']]
                except KeyError:
                    # if the user uses the custom way to name custom resources,
                    # we'll dynamically create a new subclass for this use and
                    # pass that instead of the typical CustomObject resource
                    try:
                        expected_type = self._generate_custom_type(
                            definition['Type'])
                    except TypeError:
                        assert not expected_type

                if expected_type:
                    args = definition.get('Properties', {}).copy()
                    if 'Condition' in definition:
                        args.update({'Condition': definition['Condition']})
                    if 'UpdatePolicy' in definition:
                        # there's only 1 kind of UpdatePolicy; use it
                        args.update({'UpdatePolicy': self._create_instance(
                            UpdatePolicy, definition['UpdatePolicy'])})
                    if 'CreationPolicy' in definition:
                        # there's only 1 kind of CreationPolicy; use it
                        args.update({'CreationPolicy': self._create_instance(
                            CreationPolicy, definition['CreationPolicy'])})
                    if 'DeletionPolicy' in definition:
                        # DeletionPolicity is very basic
                        args.update(
                            {'DeletionPolicy': self._convert_definition(
                                definition['DeletionPolicy'])})
                    if 'Metadata' in definition:
                        # there are various kind of metadata; pass it as-is
                        args.update(
                            {'Metadata': self._convert_definition(
                                definition['Metadata'])})
                    if 'DependsOn' in definition:
                        args.update(
                            {'DependsOn': self._convert_definition(
                                definition['DependsOn'])})
                    return self._create_instance(expected_type, args, ref)

            if len(definition) == 1:  # This might be a function?
                function_type = self._get_function_type(definition.keys()[0])
                if function_type:
                    return self._create_instance(
                        function_type, definition.values()[0])

            # return as dict
            return {k: self._convert_definition(v)
                    for k, v in definition.iteritems()}

        elif (isinstance(definition, Sequence) and
                not isinstance(definition, basestring)):
            return [self._convert_definition(v) for v in definition]

        # anything else is returned as-is
        return definition

    def _create_instance(self, cls, args, ref=None):
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

        if isinstance(cls, Sequence) or cls not in self.inspect_members:
            # this object doesn't map to any known object. could be a string
            # or int, or a Ref... or a list of types such as
            # [basestring, FindInMap, Ref] or maybe a
            # validator such as `integer` or `port_range`
            return self._convert_definition(args)

        elif issubclass(cls, AWSHelperFn):
            # special handling for functions, we want to handle it before
            # entering the other conditions.
            if isinstance(args, Sequence) and not isinstance(args, basestring):
                return cls(*self._convert_definition(args))
            else:
                if issubclass(cls, autoscaling.Metadata):
                    # special handling for this class type
                    assert isinstance(args, Mapping)
                    init_config = self._create_instance(
                        cloudformation.InitConfig,
                        args['AWS::CloudFormation::Init']['config'])
                    init = self._create_instance(
                        cloudformation.Init, {'config': init_config})
                    auth = None
                    if 'AWS::CloudFormation::Authentication' in args:
                        auth_blocks = {}
                        for k in args['AWS::CloudFormation::Authentication']:
                            auth_blocks[k] = self._create_instance(
                                cloudformation.AuthenticationBlock,
                                args['AWS::CloudFormation::Authentication'][k],
                                k)
                        auth = self._create_instance(
                            cloudformation.Authentication, auth_blocks)

                    return cls(init, auth)

                # watch out for double-refs...
                args = self._convert_definition(args)
                if isinstance(args, Ref) and issubclass(cls, Ref):
                    # skip the cls, we can't have a ref in a ref!
                    return args

                args = self._convert_definition(args)
                try:
                    return cls(args)
                except TypeError as ex:
                    if '__init__() takes exactly' not in ex.message:
                        raise
                    # special AWSHelperFn typically take lowercased parameters,
                    # but templates use uppercase. for this reason we cannot
                    # map to most of them, so we fallback with a generic one.
                    # this might not work for all types if they do extra
                    # processing in their init routine.
                    return GenericHelperFn(args)

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
                        expected_type in self.inspect_members):
                    kwargs[prop_name] = self._create_instance(
                        expected_type, args[prop_name], prop_name)
                else:
                    kwargs[prop_name] = self._convert_definition(
                        args[prop_name], prop_name)

            args = self._convert_definition(kwargs)
            if isinstance(args, Ref):
                # sometimes, we can substitute a whole definition for a ref
                return args
            assert isinstance(args, Mapping)
            return self._add_reference(ref, cls(title=ref, **args))

        if ref:
            return self._add_reference(
                ref, cls(self._convert_definition(args)))

        return cls(self._convert_definition(args))

    def _add_reference(self, ref, obj):
        self._reference_map[ref] = obj
        return obj

    def _get_function_type(self, function_name):
        """
        Returns the function object that matches the provided name.
        Only Fn:: and Ref functions are supported here
        """
        if (function_name.startswith("Fn::") and
                function_name[4:] in self.functions):
            return self.functions[function_name[4:]]
        return self.functions['Ref'] if function_name == "Ref" else None
