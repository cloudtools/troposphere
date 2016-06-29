# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import integer, positive_integer, network_port, boolean


class AliasTarget(AWSProperty):
    props = {
        'HostedZoneId': (basestring, True),
        'DNSName': (basestring, True),
        'EvaluateTargetHealth': (boolean, False)
    }

    def __init__(self,
                 hostedzoneid=None,
                 dnsname=None,
                 evaluatetargethealth=None,
                 **kwargs):
        # provided for backward compatibility
        if hostedzoneid is not None:
            kwargs['HostedZoneId'] = hostedzoneid
        if dnsname is not None:
            kwargs['DNSName'] = dnsname
        if evaluatetargethealth is not None:
            kwargs['EvaluateTargetHealth'] = evaluatetargethealth
        super(AliasTarget, self).__init__(**kwargs)


class GeoLocation(AWSProperty):
    props = {
        'ContinentCode': (basestring, False),
        'CountryCode': (basestring, False),
        'SubdivisionCode': (basestring, False),
    }


class BaseRecordSet(object):
    props = {
        'AliasTarget': (AliasTarget, False),
        'Comment': (basestring, False),
        'Failover': (basestring, False),
        'GeoLocation': (GeoLocation, False),
        'HealthCheckId': (basestring, False),
        'HostedZoneId': (basestring, False),
        'HostedZoneName': (basestring, False),
        'Name': (basestring, True),
        'Region': (basestring, False),
        'ResourceRecords': (list, False),
        'SetIdentifier': (basestring, False),
        'TTL': (integer, False),
        'Type': (basestring, True),
        'Weight': (integer, False),
    }


class RecordSetType(AWSObject, BaseRecordSet):
    # This is a top-level resource
    resource_type = "AWS::Route53::RecordSet"


class RecordSet(AWSProperty, BaseRecordSet):
    # This is for use in a list with RecordSetGroup (below)
    pass


class RecordSetGroup(AWSObject):
    resource_type = "AWS::Route53::RecordSetGroup"

    props = {
        'HostedZoneId': (basestring, False),
        'HostedZoneName': (basestring, False),
        'RecordSets': (list, False),
        'Comment': (basestring, False),
    }


class HealthCheckConfiguration(AWSProperty):
    props = {
        'FailureThreshold': (positive_integer, False),
        'FullyQualifiedDomainName': (basestring, False),
        'IPAddress': (basestring, False),
        'Port': (network_port, False),
        'RequestInterval': (positive_integer, False),
        'ResourcePath': (basestring, False),
        'SearchString': (basestring, False),
        'Type': (basestring, True),
    }


class HealthCheck(AWSObject):
    resource_type = "AWS::Route53::HealthCheck"

    props = {
        'HealthCheckConfig': (HealthCheckConfiguration, True),
        'HealthCheckTags': (Tags, False),
    }


class HostedZoneConfiguration(AWSProperty):
    props = {
        'Comment': (basestring, False),
    }


class HostedZoneVPCs(AWSProperty):
    props = {
        'VPCId': (basestring, True),
        'VPCRegion': (basestring, True),
    }


class HostedZone(AWSObject):
    resource_type = "AWS::Route53::HostedZone"

    props = {
        'HostedZoneConfig': (HostedZoneConfiguration, False),
        'HostedZoneTags': (Tags, False),
        'Name': (basestring, True),
        'VPCs': ([HostedZoneVPCs], False),
    }
