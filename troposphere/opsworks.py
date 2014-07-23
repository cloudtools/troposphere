# Copyright (c) 2014, Yuta Okamoto <okapies@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Ref
from .validators import boolean, integer


class Source(AWSProperty):
    props = {
        'Password': (basestring, False),
        'Revision': (basestring, False),
        'SshKey': (basestring, False),
        'Type': (basestring, False),
        'Url': (basestring, False),
        'Username': (basestring, False),
    }


class SslConfiguration(AWSProperty):
    props = {
        'Certificate': (basestring, True),
        'Chain': (basestring, False),
        'PrivateKey': (basestring, True),
    }


class Recipes(AWSProperty):
    props = {
        'Configure': ([basestring], False),
        'Deploy': ([basestring], False),
        'Setup': ([basestring], False),
        'Shutdown': ([basestring], False),
        'Undeploy': ([basestring], False),
    }


class VolumeConfiguration(AWSProperty):
    props = {
        'MountPoint': (basestring, True),
        'NumberOfDisks': (integer, True),
        'RaidLevel': (integer, False),
        'Size': (integer, True),
    }


class StackConfigurationManager(AWSProperty):
    props = {
        'Name': (basestring, False),
        'Version': (basestring, False),
    }


class App(AWSObject):
    type = "AWS::OpsWorks::App"

    props = {
        'AppSource': (Source, False),
        'Attributes': (dict, False),
        'Description': (basestring, False),
        'Domains': ([basestring], False),
        'EnableSsl': (boolean, False),
        'Name': (basestring, True),
        'Shortname': (basestring, False),
        'SslConfiguration': (SslConfiguration, False),
        'StackId': (basestring, True),
        'Type': (basestring, True),
    }


class ElasticLoadBalancerAttachment(AWSObject):
    type = "AWS::OpsWorks::ElasticLoadBalancerAttachment"

    props = {
        'ElasticLoadBalancerName': (basestring, True),
        'LayerId': (basestring, True),
    }


class Instance(AWSObject):
    type = "AWS::OpsWorks::Instance"

    props = {
        'AmiId': (basestring, False),
        'Architecture': (basestring, False),
        'AvailabilityZone': (basestring, False),
        'InstallUpdatesOnBoot': (boolean, False),
        'InstanceType': (basestring, True),
        'LayerIds': ([basestring, Ref], True),
        'Os': (basestring, False),
        'RootDeviceType': (basestring, False),
        'SshKeyName': (basestring, False),
        'StackId': (basestring, True),
        'SubnetId': (basestring, False),
    }


class Layer(AWSObject):
    type = "AWS::OpsWorks::Layer"

    props = {
        'Attributes': (dict, False),
        'AutoAssignElasticIps': (boolean, True),
        'AutoAssignPublicIps': (boolean, True),
        'CustomInstanceProfileArn': (basestring, False),
        'CustomRecipes': (Recipes, False),
        'CustomSecurityGroupIds': ([basestring, Ref], False),
        'EnableAutoHealing': (boolean, True),
        'InstallUpdatesOnBoot': (boolean, False),
        'Name': (basestring, True),
        'Packages': ([basestring], False),
        'Shortname': (basestring, True),
        'StackId': (basestring, True),
        'Type': (basestring, True),
        'VolumeConfigurations': ([VolumeConfiguration], False),
    }


class Stack(AWSObject):
    type = "AWS::OpsWorks::Stack"

    props = {
        'Attributes': (dict, False),
        'ConfigurationManager': (StackConfigurationManager, False),
        'CustomCookbooksSource': (Source, False),
        'CustomJson': (dict, False),
        'DefaultAvailabilityZone': (basestring, False),
        'DefaultInstanceProfileArn': (basestring, True),
        'DefaultOs': (basestring, False),
        'DefaultRootDeviceType': (basestring, False),
        'DefaultSshKeyName': (basestring, False),
        'DefaultSubnetId': (basestring, False),
        'HostnameTheme': (basestring, False),
        'Name': (basestring, True),
        'ServiceRoleArn': (basestring, True),
        'UseCustomCookbooks': (boolean, False),
        'VpcId': (basestring, False),
    }
