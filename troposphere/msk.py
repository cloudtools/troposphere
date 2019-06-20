# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import AWSObject
from . import AWSProperty
from .validators import boolean
from .validators import integer


class EBSStorageInfo(AWSProperty):
    props = {
        'VolumeSize': (integer, False),
    }


class StorageInfo(AWSProperty):
    props = {
        'EBSStorageInfo': (EBSStorageInfo, False),
    }


class BrokerNodeGroupInfo(AWSProperty):
    props = {
        'BrokerAZDistribution': (basestring, False),
        'ClientSubnets': ([basestring], True),
        'InstanceType': (basestring, True),
        'SecurityGroups': ([basestring], False),
        'StorageInfo': (StorageInfo, False),
    }


class Tls(AWSProperty):
    props = {
        'CertificateAuthorityArnList': ([basestring], False),
    }


class ClientAuthentication(AWSProperty):
    props = {
        'Tls': (Tls, False),
    }


class ConfigurationInfo(AWSProperty):
    props = {
        'Arn': (basestring, True),
        'Revision': (integer, True),
    }


class EncryptionAtRest(AWSProperty):
    props = {
        'DataVolumeKMSKeyId': (basestring, True),
    }


class EncryptionInTransit(AWSProperty):
    props = {
        'ClientBroker': (basestring, False),
        'InCluster': (boolean, False),
    }


class EncryptionInfo(AWSProperty):
    props = {
        'EncryptionAtRest': (EncryptionAtRest, False),
        'EncryptionInTransit': (EncryptionInTransit, False),
    }


class Cluster(AWSObject):
    resource_type = "AWS::MSK::Cluster"

    props = {
        'BrokerNodeGroupInfo': (BrokerNodeGroupInfo, True),
        'ClientAuthentication': (ClientAuthentication, False),
        'ClusterName': (basestring, True),
        'ConfigurationInfo': (ConfigurationInfo, False),
        'EncryptionInfo': (EncryptionInfo, False),
        'EnhancedMonitoring': (basestring, False),
        'KafkaVersion': (basestring, True),
        'NumberOfBrokerNodes': (integer, True),
        'Tags': (dict, False),
    }
