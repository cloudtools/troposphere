# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import integer
from .validators.route53resolver import validate_ruletype


class FirewallDomainList(AWSObject):
    """
    `FirewallDomainList <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html>`__
    """

    resource_type = "AWS::Route53Resolver::FirewallDomainList"

    props: PropsDictType = {
        "DomainFileUrl": (str, False),
        "Domains": ([str], False),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class FirewallRule(AWSProperty):
    """
    `FirewallRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html>`__
    """

    props: PropsDictType = {
        "Action": (str, True),
        "BlockOverrideDnsType": (str, False),
        "BlockOverrideDomain": (str, False),
        "BlockOverrideTtl": (integer, False),
        "BlockResponse": (str, False),
        "ConfidenceThreshold": (str, False),
        "DnsThreatProtection": (str, False),
        "FirewallDomainListId": (str, False),
        "FirewallDomainRedirectionAction": (str, False),
        "FirewallThreatProtectionId": (str, False),
        "Priority": (integer, True),
        "Qtype": (str, False),
    }


class FirewallRuleGroup(AWSObject):
    """
    `FirewallRuleGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html>`__
    """

    resource_type = "AWS::Route53Resolver::FirewallRuleGroup"

    props: PropsDictType = {
        "FirewallRules": ([FirewallRule], False),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class FirewallRuleGroupAssociation(AWSObject):
    """
    `FirewallRuleGroupAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html>`__
    """

    resource_type = "AWS::Route53Resolver::FirewallRuleGroupAssociation"

    props: PropsDictType = {
        "FirewallRuleGroupId": (str, True),
        "MutationProtection": (str, False),
        "Name": (str, False),
        "Priority": (integer, True),
        "Tags": (Tags, False),
        "VpcId": (str, True),
    }


class OutpostResolver(AWSObject):
    """
    `OutpostResolver <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-outpostresolver.html>`__
    """

    resource_type = "AWS::Route53Resolver::OutpostResolver"

    props: PropsDictType = {
        "InstanceCount": (integer, False),
        "Name": (str, True),
        "OutpostArn": (str, True),
        "PreferredInstanceType": (str, True),
        "Tags": (Tags, False),
    }


class ResolverConfig(AWSObject):
    """
    `ResolverConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html>`__
    """

    resource_type = "AWS::Route53Resolver::ResolverConfig"

    props: PropsDictType = {
        "AutodefinedReverseFlag": (str, True),
        "ResourceId": (str, True),
    }


class ResolverDNSSECConfig(AWSObject):
    """
    `ResolverDNSSECConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html>`__
    """

    resource_type = "AWS::Route53Resolver::ResolverDNSSECConfig"

    props: PropsDictType = {
        "ResourceId": (str, False),
    }


class IpAddressRequest(AWSProperty):
    """
    `IpAddressRequest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html>`__
    """

    props: PropsDictType = {
        "Ip": (str, False),
        "Ipv6": (str, False),
        "SubnetId": (str, True),
    }


class ResolverEndpoint(AWSObject):
    """
    `ResolverEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html>`__
    """

    resource_type = "AWS::Route53Resolver::ResolverEndpoint"

    props: PropsDictType = {
        "Direction": (str, True),
        "IpAddresses": ([IpAddressRequest], True),
        "Name": (str, False),
        "OutpostArn": (str, False),
        "PreferredInstanceType": (str, False),
        "Protocols": ([str], False),
        "ResolverEndpointType": (str, False),
        "SecurityGroupIds": ([str], True),
        "Tags": (Tags, False),
    }


class ResolverQueryLoggingConfig(AWSObject):
    """
    `ResolverQueryLoggingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html>`__
    """

    resource_type = "AWS::Route53Resolver::ResolverQueryLoggingConfig"

    props: PropsDictType = {
        "DestinationArn": (str, False),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class ResolverQueryLoggingConfigAssociation(AWSObject):
    """
    `ResolverQueryLoggingConfigAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html>`__
    """

    resource_type = "AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation"

    props: PropsDictType = {
        "ResolverQueryLogConfigId": (str, False),
        "ResourceId": (str, False),
    }


class TargetAddress(AWSProperty):
    """
    `TargetAddress <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html>`__
    """

    props: PropsDictType = {
        "Ip": (str, False),
        "Ipv6": (str, False),
        "Port": (str, False),
        "Protocol": (str, False),
        "ServerNameIndication": (str, False),
    }


class ResolverRule(AWSObject):
    """
    `ResolverRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html>`__
    """

    resource_type = "AWS::Route53Resolver::ResolverRule"

    props: PropsDictType = {
        "DelegationRecord": (str, False),
        "DomainName": (str, False),
        "Name": (str, False),
        "ResolverEndpointId": (str, False),
        "RuleType": (validate_ruletype, True),
        "Tags": (Tags, False),
        "TargetIps": ([TargetAddress], False),
    }


class ResolverRuleAssociation(AWSObject):
    """
    `ResolverRuleAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html>`__
    """

    resource_type = "AWS::Route53Resolver::ResolverRuleAssociation"

    props: PropsDictType = {
        "Name": (str, False),
        "ResolverRuleId": (str, True),
        "VPCId": (str, True),
    }
