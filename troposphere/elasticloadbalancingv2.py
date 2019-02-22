# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, If, Tags
from .validators import (
    elb_name, exactly_one, network_port,
    tg_healthcheck_port, integer,
    one_of
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


class AuthenticateCognitoConfig(AWSProperty):
    props = {
        "AuthenticationRequestExtraParams": (dict, False),
        "OnUnauthenticatedRequest": (basestring, False),
        "Scope": (basestring, False),
        "SessionCookieName": (basestring, False),
        "SessionTimeout": (integer, True),
        "UserPoolArn": (basestring, True),
        "UserPoolClientId": (basestring, True),
        "UserPoolDomain": (basestring, True)
    }


class AuthenticateOidcConfig(AWSProperty):
    props = {
        "AuthenticationRequestExtraParams": (dict, False),
        "AuthorizationEndpoint": (basestring, True),
        "ClientId": (basestring, True),
        "ClientSecret": (basestring, True),
        "Issuer": (basestring, True),
        "OnUnauthenticatedRequest": (basestring, False),
        "Scope": (basestring, False),
        "SessionCookieName": (basestring, False),
        "SessionTimeout": (integer, False),
        "TokenEndpoint": (basestring, True),
        "UserInfoEndpoint": (basestring, True)
    }


class RedirectConfig(AWSProperty):
    # https://docs.aws.amazon.com/
    # AWSCloudFormation/latest/UserGuide/
    # aws-properties-elasticloadbalancingv2-listener-redirectconfig.html
    props = {
        'Host': (basestring, False),
        'Path': (basestring, False),
        'Port': (basestring, False),
        'Protocol': (basestring, False),
        'Query': (basestring, False),
        'StatusCode': (basestring, True),
    }

    def validate(self):
        one_of(self.__class__.__name__,
               self.properties,
               'StatusCode',
               ['HTTP_301', 'HTTP_302'])


class FixedResponseConfig(AWSProperty):
    props = {
        'ContentType': (basestring, False),
        'MessageBody': (basestring, False),
        'StatusCode': (basestring, False),
    }

    def validate(self):
        one_of(self.__class__.__name__,
               self.properties,
               'ContentType',
               ['text/plain', 'text/css', 'text/html',
                'application/javascript', 'application/json'])


class Action(AWSProperty):
    props = {
        "AuthenticateCognitoConfig": (AuthenticateCognitoConfig, False),
        "AuthenticateOidcConfig": (AuthenticateOidcConfig, False),
        "FixedResponseConfig": (FixedResponseConfig, False),
        "Order": (integer, False),
        "RedirectConfig": (RedirectConfig, False),
        "TargetGroupArn": (basestring, False),
        "Type": (basestring, True)
    }

    def validate(self):
        one_of(self.__class__.__name__,
               self.properties,
               'Type',
               ['forward', 'redirect', 'fixed-response'])

        def requires(action_type, prop):
            if self.properties.get('Type') == action_type and \
                    prop not in self.properties:
                raise ValueError(
                    'Type "%s" requires definition of "%s"' % (
                        action_type, prop
                    )
                )

            if prop in self.properties and \
                    self.properties.get('Type') != action_type:
                raise ValueError(
                    'Definition of "%s" allowed only with '
                    'type "%s", was: "%s"' % (
                        prop, action_type, self.properties.get('Type')
                    )
                )

        requires('forward', 'TargetGroupArn')
        requires('redirect', 'RedirectConfig')
        requires('fixed-response', 'FixedResponseConfig')


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
