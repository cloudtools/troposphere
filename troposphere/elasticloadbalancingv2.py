# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, If, Tags
from .validators import (
    elb_name, exactly_one, network_port,
    tg_healthcheck_port, integer
)


class LoadBalancerAttributes(AWSProperty):
    props = {
        'Key': (basestring, False),
        'Value': (basestring, False)
    }


class Certificate(AWSProperty):
    props = {
        'CertificateArn': (basestring, False)
    }


class Action(AWSProperty):
    props = {
        'TargetGroupArn': (basestring, True),
        'Type': (basestring, True)
    }


class Condition(AWSProperty):
    props = {
        'Field': (basestring, True),
        'Values': ([basestring], True)
    }


class Matcher(AWSProperty):
    props = {
        'HttpCode': (basestring, False)
    }


class SubnetMapping(AWSProperty):
    props = {
        'AllocationId': (basestring, True),
        'SubnetId': (basestring, True)
    }


class TargetGroupAttribute(AWSProperty):
    props = {
        'Key': (basestring, False),
        'Value': (basestring, False)
    }


class TargetDescription(AWSProperty):
    props = {
        'AvailabilityZone': (basestring, False),
        'Id': (basestring, True),
        'Port': (network_port, False)
    }


class Listener(AWSObject):
    resource_type = "AWS::ElasticLoadBalancingV2::Listener"

    props = {
        'Certificates': ([Certificate], False),
        'DefaultActions': ([Action], True),
        'LoadBalancerArn': (basestring, True),
        'Port': (network_port, True),
        'Protocol': (basestring, True),
        'SslPolicy': (basestring, False)
    }


class ListenerCertificate(AWSObject):
    resource_type = "AWS::ElasticLoadBalancingV2::ListenerCertificate"

    props = {
        'Certificates': ([Certificate], True),
        'ListenerArn': (basestring, True),
    }


class ListenerRule(AWSObject):
    resource_type = "AWS::ElasticLoadBalancingV2::ListenerRule"

    props = {
        'Actions': ([Action], True),
        'Conditions': ([Condition], True),
        'ListenerArn': (basestring, True),
        'Priority': (integer, True)
    }


TARGET_TYPE_INSTANCE = 'instance'
TARGET_TYPE_IP = 'ip'


class TargetGroup(AWSObject):
    resource_type = "AWS::ElasticLoadBalancingV2::TargetGroup"

    props = {
        'HealthCheckIntervalSeconds': (integer, False),
        'HealthCheckPath': (basestring, False),
        'HealthCheckPort': (tg_healthcheck_port, False),
        'HealthCheckProtocol': (basestring, False),
        'HealthCheckTimeoutSeconds': (integer, False),
        'HealthyThresholdCount': (integer, False),
        'Matcher': (Matcher, False),
        'Name': (basestring, False),
        'Port': (network_port, True),
        'Protocol': (basestring, True),
        'Tags': ((Tags, list), False),
        'TargetGroupAttributes': ([TargetGroupAttribute], False),
        'Targets': ([TargetDescription], False),
        'TargetType': (basestring, False),
        'UnhealthyThresholdCount': (integer, False),
        'VpcId': (basestring, True),
    }


class LoadBalancer(AWSObject):
    resource_type = "AWS::ElasticLoadBalancingV2::LoadBalancer"

    props = {
        'LoadBalancerAttributes': ([LoadBalancerAttributes], False),
        'Name': (elb_name, False),
        'Scheme': (basestring, False),
        'IpAddressType': (basestring, False),
        'SecurityGroups': (list, False),
        'SubnetMappings': ([SubnetMapping], False),
        'Subnets': (list, False),
        'Tags': ((Tags, list), False),
        'Type': (basestring, False),
    }

    def validate(self):
        conds = [
            'SubnetMappings',
            'Subnets',
        ]

        def check_if(names, props):
            validated = []
            for name in names:
                validated.append(name in props and isinstance(props[name], If))
            return all(validated)

        if check_if(conds, self.properties):
            return

        exactly_one(self.__class__.__name__, self.properties, conds)
