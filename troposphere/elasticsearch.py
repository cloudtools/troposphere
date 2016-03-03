# Copyright (c) 2013, David Irvine <irvined@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, Ref, GetAtt, Tags, AWSProperty
from .validators import boolean, integer


class ElasticSearchEBSOption(AWSProperty):
    props = {
        "EBSEnabled": (boolean, False),
        "Iops": (integer, False),
        "VolumeSize": (integer, False),
        "VolumeType": (basestring, False),
    }


class ElasticSearchClusterConfig(AWSProperty):
    props = {
        "DedicatedMasterCount": (integer, False),
        "DedicatedMasterEnabled": (boolean, False),
        "DedicatedMasterType": (basestring, False),
        "InstanceCount": (integer, False),
        "InstanceType": (basestring, False),
        "ZoneAwarenessEnabled": (boolean, False)
    }


class ElasticSearchSnapshotOption(AWSProperty):
    props = {
        "AutomatedSnapshotStartHour": (integer, False)
    }


class ElasticSearchDomain(AWSObject):
    resource_type = "AWS::Elasticsearch::Domain"

    props = {
        'AccessPolicies': (dict, False),
        'AdvancedOptions': (dict, False),
        'DomainName': (basestring, True),
        'EBSOptions': (ElasticSearchClusterConfig, False),
        'ElasticsearchClusterConfig': (ElasticSearchClusterConfig, False),
        'SnapshotOptions': (ElasticSearchSnapshotOption, False),
        'Tags': (Tags, False),
    }

