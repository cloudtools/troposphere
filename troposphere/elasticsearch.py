# Copyright (c) 2012-2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSProperty, AWSObject
from .validators import boolean, integer, integer_range

try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


class Tag(AWSHelperFn):
    def __init__(self, key, value):
        self.data = {'Key': key, 'Value': value}

    def JSONrepr(self):
        return self.data


def validate_volume_type(volume_type):
    volume_types = ('standard', 'io1', 'gp2')
    if volume_type not in volume_types:
        raise ValueError("VolumeType (given: %s) must be one of: %s" % (
            volume_type, ', '.join(volume_types)))
    return volume_type


class EBSOptions(AWSProperty):
    props = {
        'EBSEnabled': (boolean, False),
        'Iops': (integer, False),
        'VolumeSize': (integer, False),
        'VolumeType': (validate_volume_type, False)
    }

    def validate(self):
        volume_type = self.properties.get('VolumeType')
        iops = self.properties.get('Iops')
        if volume_type == 'io1' and not iops:
            raise ValueError("Must specify Iops if VolumeType is 'io1'.")
        if volume_type != 'io1' and iops:
            raise ValueError("Cannot specify Iops if VolumeType is not 'io1'.")


class ElasticsearchClusterConfig(AWSProperty):
    props = {
        'DedicatedMasterCount': (integer, False),
        'DedicatedMasterEnabled': (boolean, False),
        'DedicatedMasterType': (basestring, False),
        'InstanceCount': (integer, False),
        'InstanceType': (basestring, False),
        'ZoneAwarenessEnabled': (boolean, False)
    }


class SnapshotOptions(AWSProperty):
    props = {
        'AutomatedSnapshotStartHour': (integer_range(0, 23), False)
    }


class ElasticsearchDomain(AWSObject):
    resource_type = "AWS::Elasticsearch::Domain"

    props = {
        'AccessPolicies': (policytypes, False),
        'AdvancedOptions': (dict, False),
        'DomainName': (basestring, True),
        'EBSOptions': (EBSOptions, False),
        'ElasticsearchClusterConfig': (ElasticsearchClusterConfig, False),
        'SnapshotOptions': (SnapshotOptions, False),
        'Tags': (list, False)
    }
