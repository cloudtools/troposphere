# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty

class LogSetup(AWSProperty):
    props = {
        'Enable': (bool, False),
        'Types': ([basestring], False)
        }

    def validate(self):
        types = set(self.properties.get('Types'))
        conditionals = ['api', 'audit', 'authenticator', 'controllerManager',
                        'scheduler']
        if not (types.issubset(conditionals)):
            raise ValueError(
                '%s must be one of: %s' % (', '.join(types),
                                           ', '.join(conditionals)))


class Logging(AWSProperty):
    props = {
        'ClusterLogging': ([LogSetup], False)
    }


class ResourcesVpcConfig(AWSProperty):
    props = {
        'SecurityGroupIds': ([basestring], False),
        'SubnetIds': ([basestring], True),
    }


class Cluster(AWSObject):
    resource_type = "AWS::EKS::Cluster"

    props = {
        'Name': (basestring, False),
        'Logging': (Logging, False),
        'ResourcesVpcConfig': (ResourcesVpcConfig, True),
        'RoleArn': (basestring, True),
        'Version': (basestring, False),
    }
