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


class DNSSEC(AWSObject):
    resource_type = "AWS::Route53::DNSSEC"

    props = {
        'HostedZoneId': (str, True),
    }


class KeySigningKey(AWSObject):
    resource_type = "AWS::Route53::KeySigningKey"

    props = {
        'HostedZoneId': (str, True),
        'KeyManagementServiceArn': (str, True),
        'Name': (str, True),
        'Status': (str, True),
    }


class AliasTarget(AWSProperty):
    props = {
        'HostedZoneId': (str, True),
        'DNSName': (str, True),
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
        'ContinentCode': (str, False),
        'CountryCode': (str, False),
        'SubdivisionCode': (str, False),
    }


class BaseRecordSet(object):
    props = {
        'AliasTarget': (AliasTarget, False),
        'Comment': (str, False),
        'Failover': (str, False),
        'GeoLocation': (GeoLocation, False),
        'HealthCheckId': (str, False),
        'HostedZoneId': (str, False),
        'HostedZoneName': (str, False),
        'MultiValueAnswer': (boolean, False),
        'Name': (str, True),
        'Region': (str, False),
        'ResourceRecords': (list, False),
        'SetIdentifier': (str, False),
        'TTL': (integer, False),
        'Type': (str, True),
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
        'HostedZoneId': (str, False),
        'HostedZoneName': (str, False),
        'RecordSets': (list, False),
        'Comment': (str, False),
    }


class AlarmIdentifier(AWSProperty):
    props = {
        'Name': (str, True),
        'Region': (str, True),
    }


class HealthCheckConfiguration(AWSProperty):
    props = {
        'AlarmIdentifier': (AlarmIdentifier, False),
        'ChildHealthChecks': ([str], False),
        'EnableSNI': (boolean, False),
        'FailureThreshold': (positive_integer, False),
        'FullyQualifiedDomainName': (str, False),
        'HealthThreshold': (positive_integer, False),
        'InsufficientDataHealthStatus': (str, False),
        'Inverted': (boolean, False),
        'IPAddress': (str, False),
        'MeasureLatency': (boolean, False),
        'Port': (network_port, False),
        'Regions': ([str], False),
        'RequestInterval': (positive_integer, False),
        'ResourcePath': (str, False),
        'SearchString': (str, False),
        'Type': (str, True),
    }


class HealthCheck(AWSObject):
    resource_type = "AWS::Route53::HealthCheck"

    props = {
        'HealthCheckConfig': (HealthCheckConfiguration, True),
        'HealthCheckTags': (Tags, False),
    }


class HostedZoneConfiguration(AWSProperty):
    props = {
        'Comment': (str, False),
    }


class HostedZoneVPCs(AWSProperty):
    props = {
        'VPCId': (str, True),
        'VPCRegion': (str, True),
    }


class QueryLoggingConfig(AWSProperty):
    props = {
        'CloudWatchLogsLogGroupArn': (str, True),
    }


class HostedZone(AWSObject):
    resource_type = "AWS::Route53::HostedZone"

    props = {
        'HostedZoneConfig': (HostedZoneConfiguration, False),
        'HostedZoneTags': (Tags, False),
        'Name': (str, True),
        'QueryLoggingConfig': (QueryLoggingConfig, False),
        'VPCs': ([HostedZoneVPCs], False),
    }


class ResolverDNSSECConfig(AWSObject):
    resource_type = "AWS::Route53Resolver::ResolverDNSSECConfig"

    props = {
        'ResourceId': (str, False),
    }


class IpAddressRequest(AWSProperty):
    props = {
        'Ip': (str, False),
        'SubnetId': (str, True),
    }


class ResolverEndpoint(AWSObject):
    resource_type = "AWS::Route53Resolver::ResolverEndpoint"

    props = {
        'Direction': (str, True),
        'IpAddresses': ([IpAddressRequest], True),
        'Name': (str, False),
        'SecurityGroupIds': ([str], True),
        'Tags': (Tags, False),
    }


class ResolverQueryLoggingConfig(AWSObject):
    resource_type = "AWS::Route53Resolver::ResolverQueryLoggingConfig"

    props = {
        'DestinationArn': (str, False),
        'Name': (str, False),
    }


class ResolverQueryLoggingConfigAssociation(AWSObject):
    resource_type = \
        "AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation"

    props = {
        'ResolverQueryLogConfigId': (str, False),
        'ResourceId': (str, False),
    }


class TargetAddress(AWSProperty):
    props = {
        'Ip': (str, True),
        'Port': (str, True),
    }


class ResolverRule(AWSObject):
    resource_type = "AWS::Route53Resolver::ResolverRule"

    props = {
        'DomainName': (str, True),
        'Name': (str, False),
        'ResolverEndpointId': (str, False),
        'RuleType': (validate_ruletype, True),
        'Tags': (Tags, False),
        'TargetIps': ([TargetAddress], False),
    }


class ResolverRuleAssociation(AWSObject):
    resource_type = "AWS::Route53Resolver::ResolverRuleAssociation"

    props = {
        'Name': (str, False),
        'ResolverRuleId': (str, True),
        'VPCId': (str, True),
    }
