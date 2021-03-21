# Copyright (c) 2012-2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSProperty, AWSObject, Tags
from .compat import policytypes
from .validators import boolean, integer, integer_range, positive_integer

VALID_VOLUME_TYPES = ('standard', 'gp2', 'io1')
VALID_TLS_SECURITY_POLICIES = (
    'Policy-Min-TLS-1-0-2019-07',
    'Policy-Min-TLS-1-2-2019-07'
    )


def validate_volume_type(volume_type):
    """Validate VolumeType for ElasticsearchDomain"""
    if volume_type not in VALID_VOLUME_TYPES:
        raise ValueError("Elasticsearch Domain VolumeType must be one of: %s" %
                         ", ".join(VALID_VOLUME_TYPES))
    return volume_type


def validate_tls_security_policy(tls_security_policy):
    """Validate TLS Security Policy for ElasticsearchDomain"""
    if tls_security_policy not in VALID_TLS_SECURITY_POLICIES:
        raise ValueError("Minimum TLS Security Policy must be one of: %s" %
                         ", ".join(VALID_TLS_SECURITY_POLICIES))
    return tls_security_policy


class CognitoOptions(AWSProperty):
    props = {
        'Enabled': (boolean, False),
        'IdentityPoolId': (str, False),
        'RoleArn': (str, False),
        'UserPoolId': (str, False),
    }


class DomainEndpointOptions(AWSProperty):
    props = {
        'CustomEndpoint': (str, False),
        'CustomEndpointCertificateArn': (str, False),
        'CustomEndpointEnabled': (boolean, False),  # Conditional
        'EnforceHTTPS': (boolean, False),
        'TLSSecurityPolicy': (validate_tls_security_policy, False),
    }


class EBSOptions(AWSProperty):
    props = {
        'EBSEnabled': (boolean, False),
        'Iops': (positive_integer, False),
        'VolumeSize': (integer, False),
        'VolumeType': (validate_volume_type, False)
    }

    def validate(self):
        volume_type = self.properties.get('VolumeType')
        iops = self.properties.get('Iops')
        if volume_type == 'io1' and not iops:
            raise ValueError("Must specify Iops if VolumeType is 'io1'.")


class ZoneAwarenessConfig(AWSProperty):
    props = {
        'AvailabilityZoneCount': (integer, False),
    }


class ElasticsearchClusterConfig(AWSProperty):
    props = {
        'DedicatedMasterCount': (integer, False),
        'DedicatedMasterEnabled': (boolean, False),
        'DedicatedMasterType': (str, False),
        'InstanceCount': (integer, False),
        'InstanceType': (str, False),
        'WarmCount': (integer, False),
        'WarmEnabled': (boolean, False),
        'WarmType': (str, False),
        'ZoneAwarenessConfig': (ZoneAwarenessConfig, False),
        'ZoneAwarenessEnabled': (boolean, False)
    }


class EncryptionAtRestOptions(AWSProperty):
    props = {
        'Enabled': (boolean, False),
        'KmsKeyId': (str, False),
    }


class NodeToNodeEncryptionOptions(AWSProperty):
    props = {
        'Enabled': (boolean, False),
    }


class SnapshotOptions(AWSProperty):
    props = {
        'AutomatedSnapshotStartHour': (integer_range(0, 23), False)
    }


class VPCOptions(AWSProperty):
    props = {
        'SecurityGroupIds': ([str], False),
        'SubnetIds': ([str], False)
    }


class MasterUserOptions(AWSProperty):
    props = {
        'MasterUserARN': (str, False),
        'MasterUserName': (str, False),
        'MasterUserPassword': (str, False),
    }


class AdvancedSecurityOptionsInput(AWSProperty):
    props = {
        'Enabled': (boolean, False),
        'InternalUserDatabaseEnabled': (boolean, False),
        'MasterUserOptions': (MasterUserOptions, False),
    }


class Domain(AWSObject):
    resource_type = "AWS::Elasticsearch::Domain"

    props = {
        'AccessPolicies': (policytypes, False),
        'AdvancedOptions': (dict, False),
        'AdvancedSecurityOptions': (AdvancedSecurityOptionsInput, False),
        'CognitoOptions': (CognitoOptions, False),
        'DomainName': (str, False),
        'DomainEndpointOptions': (DomainEndpointOptions, False),
        'EBSOptions': (EBSOptions, False),
        'ElasticsearchClusterConfig': (ElasticsearchClusterConfig, False),
        'ElasticsearchVersion': (str, False),
        'EncryptionAtRestOptions': (EncryptionAtRestOptions, False),
        'LogPublishingOptions': (dict, False),
        'NodeToNodeEncryptionOptions': (NodeToNodeEncryptionOptions, False),
        'SnapshotOptions': (SnapshotOptions, False),
        'Tags': ((Tags, list), False),
        'VPCOptions': (VPCOptions, False),
    }


# Backward compatibility
ElasticsearchDomain = Domain
