# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import integer, positive_integer, network_port, boolean


VALID_RULETYPES = ('SYSTEM', 'FORWARD')


def validate_ruletype(ruletype):
    """Validate RuleType for ResolverRule."""

    if ruletype not in VALID_RULETYPES:
        raise ValueError("Rule type must be one of: %s" %
                         ", ".join(VALID_RULETYPES))
    return ruletype


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
        'MultiValueAnswer': (boolean, False),
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


class AlarmIdentifier(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Region': (basestring, True),
    }


class HealthCheckConfiguration(AWSProperty):
    props = {
        'AlarmIdentifier': (AlarmIdentifier, False),
        'ChildHealthChecks': ([basestring], False),
        'EnableSNI': (boolean, False),
        'FailureThreshold': (positive_integer, False),
        'FullyQualifiedDomainName': (basestring, False),
        'HealthThreshold': (positive_integer, False),
        'InsufficientDataHealthStatus': (basestring, False),
        'Inverted': (boolean, False),
        'IPAddress': (basestring, False),
        'MeasureLatency': (boolean, False),
        'Port': (network_port, False),
        'Regions': ([basestring], False),
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


class QueryLoggingConfig(AWSProperty):
    props = {
        'CloudWatchLogsLogGroupArn': (basestring, True),
    }


class HostedZone(AWSObject):
    resource_type = "AWS::Route53::HostedZone"

    props = {
        'HostedZoneConfig': (HostedZoneConfiguration, False),
        'HostedZoneTags': (Tags, False),
        'Name': (basestring, True),
        'QueryLoggingConfig': (QueryLoggingConfig, False),
        'VPCs': ([HostedZoneVPCs], False),
    }


class IpAddressRequest(AWSProperty):
    props = {
        'Ip': (basestring, False),
        'SubnetId': (basestring, True),
    }


class ResolverEndpoint(AWSObject):
    resource_type = "AWS::Route53Resolver::ResolverEndpoint"

    props = {
        'Direction': (basestring, True),
        'IpAddresses': ([IpAddressRequest], True),
        'Name': (basestring, False),
        'SecurityGroupIds': ([basestring], True),
        'Tags': (Tags, False),
    }


class ResolverQueryLoggingConfig(AWSObject):
    resource_type = "AWS::Route53Resolver::ResolverQueryLoggingConfig"

    props = {
        'DestinationArn': (basestring, False),
        'Name': (basestring, False),
    }


class ResolverQueryLoggingConfigAssociation(AWSObject):
    resource_type = \
        "AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation"

    props = {
        'ResolverQueryLogConfigId': (basestring, False),
        'ResourceId': (basestring, False),
    }


class TargetAddress(AWSProperty):
    props = {
        'Ip': (basestring, True),
        'Port': (basestring, True),
    }


class ResolverRule(AWSObject):
    resource_type = "AWS::Route53Resolver::ResolverRule"

    props = {
        'DomainName': (basestring, True),
        'Name': (basestring, False),
        'ResolverEndpointId': (basestring, False),
        'RuleType': (validate_ruletype, True),
        'Tags': (Tags, False),
        'TargetIps': ([TargetAddress], False),
    }


class ResolverRuleAssociation(AWSObject):
    resource_type = "AWS::Route53Resolver::ResolverRuleAssociation"

    props = {
        'Name': (basestring, False),
        'ResolverRuleId': (basestring, True),
        'VPCId': (basestring, True),
    }
