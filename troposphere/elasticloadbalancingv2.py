# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, If, Tags
from .validators import (
    elb_name, exactly_one, network_port,
    tg_healthcheck_port, integer,
    one_of, boolean
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
        "SessionTimeout": (integer, False),
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
        'StatusCode': (basestring, True),
    }

    def validate(self):
        one_of(self.__class__.__name__,
               self.properties,
               'ContentType',
               [None, 'text/plain', 'text/css', 'text/html',
                'application/javascript', 'application/json'])


class TargetGroupTuple(AWSProperty):
    props = {
        'TargetGroupArn': (str, True),
        'Weight': (integer, False),
    }


class TargetGroupStickinessConfig(AWSProperty):
    props = {
        'DurationSeconds': (integer, False),
        'Enabled': (boolean, False),
    }


class ForwardConfig(AWSProperty):
    props = {
        'TargetGroups': ([TargetGroupTuple], False),
        'TargetGroupStickinessConfig': (TargetGroupStickinessConfig, False),
    }


class Action(AWSProperty):
    props = {
        "AuthenticateCognitoConfig": (AuthenticateCognitoConfig, False),
        "AuthenticateOidcConfig": (AuthenticateOidcConfig, False),
        "FixedResponseConfig": (FixedResponseConfig, False),
        "Order": (integer, False),
        "RedirectConfig": (RedirectConfig, False),
        "TargetGroupArn": (basestring, False),
        "ForwardConfig": (ForwardConfig, False),
        "Type": (basestring, True)
    }

    @staticmethod
    def any_property(require_prop, properties):
        return any(p in require_prop for p in properties)

    def validate(self):
        one_of(self.__class__.__name__,
               self.properties,
               'Type',
               ['forward', 'redirect', 'fixed-response',
                'authenticate-cognito', 'authenticate-oidc'])

        def requires(action_type, prop):
            properties = [definition for definition in
                          self.properties.keys()]
            if self.properties.get('Type') == action_type and \
               not self.any_property(prop, properties):
                raise ValueError(
                    'Type "%s" requires definition of "%s"' % (
                        action_type, prop
                    )
                )
            if self.any_property(prop, properties) and self.properties.get(
                    'Type') != action_type:
                raise ValueError(
                    'Definition of "%s" allowed only with '
                    'type "%s", was: "%s"' % (
                        prop, action_type, self.properties.get('Type')
                    )
                )

        requires('forward', ['TargetGroupArn', 'ForwardConfig'])
        requires('redirect', ['RedirectConfig'])
        requires('fixed-response', ['FixedResponseConfig'])


class HostHeaderConfig(AWSProperty):
    props = {
        'Values': ([basestring], False),
    }


class HttpHeaderConfig(AWSProperty):
    props = {
        'HttpHeaderName': (basestring, False),
        'Values': ([basestring], False),
    }


class HttpRequestMethodConfig(AWSProperty):
    props = {
        'Values': ([basestring], False),
    }


class PathPatternConfig(AWSProperty):
    props = {
        'Values': ([basestring], False),
    }


class QueryStringKeyValue(AWSProperty):
    props = {
        'Key': (basestring, False),
        'Value': (basestring, False),
    }


class QueryStringConfig(AWSProperty):
    props = {
        'Values': ([QueryStringKeyValue], False),
    }


class SourceIpConfig(AWSProperty):
    props = {
        'Values': ([basestring], False),
    }


class Condition(AWSProperty):
    props = {
        'Field': (basestring, False),
        'HostHeaderConfig': (HostHeaderConfig, False),
        'HttpHeaderConfig': (HttpHeaderConfig, False),
        'HttpRequestMethodConfig': (HttpRequestMethodConfig, False),
        'PathPatternConfig': (PathPatternConfig, False),
        'QueryStringConfig': (QueryStringConfig, False),
        'SourceIpConfig': (SourceIpConfig, False),
        'Values': ([basestring], False),
    }


class Matcher(AWSProperty):
    props = {
        'HttpCode': (basestring, True)
    }


class SubnetMapping(AWSProperty):
    props = {
        'AllocationId': (basestring, False),
        'PrivateIPv4Address': (basestring, False),
        'SubnetId': (basestring, True),
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
        'AlpnPolicy': ([basestring], False),
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
TARGET_TYPE_LAMBDA = 'lambda'


def validate_target_type(target_type):
    valid_types = [TARGET_TYPE_INSTANCE, TARGET_TYPE_IP, TARGET_TYPE_LAMBDA]
    if target_type not in valid_types:
        raise ValueError(
            'TargetGroup.TargetType must be one of: "%s"' %
            ', '.join(valid_types)
        )
    return target_type


class TargetGroup(AWSObject):
    resource_type = "AWS::ElasticLoadBalancingV2::TargetGroup"

    props = {
        'HealthCheckEnabled': (boolean, False),
        'HealthCheckIntervalSeconds': (integer, False),
        'HealthCheckPath': (basestring, False),
        'HealthCheckPort': (tg_healthcheck_port, False),
        'HealthCheckProtocol': (basestring, False),
        'HealthCheckTimeoutSeconds': (integer, False),
        'HealthyThresholdCount': (integer, False),
        'Matcher': (Matcher, False),
        'Name': (basestring, False),
        'Port': (network_port, False),
        'Protocol': (basestring, False),
        'Tags': ((Tags, list), False),
        'TargetGroupAttributes': ([TargetGroupAttribute], False),
        'Targets': ([TargetDescription], False),
        'TargetType': (validate_target_type, False),
        'UnhealthyThresholdCount': (integer, False),
        'VpcId': (basestring, False),
    }

    def validate(self):
        def check_properties(action_types, props_to_check, required):

            for this_type in action_types:

                self_props = self.properties
                if self_props.get('TargetType') == this_type:

                    invalid_props = []
                    for prop in props_to_check:

                        if (prop not in self_props and required is True) or \
                              (prop in self_props and required is False):
                            invalid_props.append(prop)

                    if len(invalid_props) > 0:
                        # Make error message more readable in the default case
                        type_msg = ('Omitting TargetType' if this_type is None
                                    else 'TargetType of "%s"' % this_type)

                        raise ValueError(
                            '%s in "%s" %s definitions of %s' % (
                                type_msg,
                                self.__class__.__name__,
                                "requires" if required is True
                                else "must not contain",
                                str(invalid_props).strip('[]')
                            ))

        # None defaults to instance as per the AWS docs
        check_properties([
            None,
            TARGET_TYPE_INSTANCE,
            TARGET_TYPE_IP
        ],
            [
                'Port',
                'Protocol',
                'VpcId'
            ],
            True)
        check_properties([
            TARGET_TYPE_LAMBDA
        ],
            [
                'Port',
                'Protocol',
                'VpcId'
            ],
            False)


class LoadBalancer(AWSObject):
    resource_type = "AWS::ElasticLoadBalancingV2::LoadBalancer"

    props = {
        'IpAddressType': (basestring, False),
        'LoadBalancerAttributes': ([LoadBalancerAttributes], False),
        'Name': (elb_name, False),
        'Scheme': (basestring, False),
        'SecurityGroups': ([basestring], False),
        'SubnetMappings': ([SubnetMapping], False),
        'Subnets': ([basestring], False),
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
