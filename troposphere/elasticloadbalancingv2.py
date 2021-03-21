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
        'Key': (str, False),
        'Value': (str, False)
    }


class Certificate(AWSProperty):
    props = {
        'CertificateArn': (str, False)
    }


class AuthenticateCognitoConfig(AWSProperty):
    props = {
        "AuthenticationRequestExtraParams": (dict, False),
        "OnUnauthenticatedRequest": (str, False),
        "Scope": (str, False),
        "SessionCookieName": (str, False),
        "SessionTimeout": (integer, False),
        "UserPoolArn": (str, True),
        "UserPoolClientId": (str, True),
        "UserPoolDomain": (str, True)
    }


class AuthenticateOidcConfig(AWSProperty):
    props = {
        "AuthenticationRequestExtraParams": (dict, False),
        "AuthorizationEndpoint": (str, True),
        "ClientId": (str, True),
        "ClientSecret": (str, True),
        "Issuer": (str, True),
        "OnUnauthenticatedRequest": (str, False),
        "Scope": (str, False),
        "SessionCookieName": (str, False),
        "SessionTimeout": (integer, False),
        "TokenEndpoint": (str, True),
        "UserInfoEndpoint": (str, True)
    }


class RedirectConfig(AWSProperty):
    # https://docs.aws.amazon.com/
    # AWSCloudFormation/latest/UserGuide/
    # aws-properties-elasticloadbalancingv2-listener-redirectconfig.html
    props = {
        'Host': (str, False),
        'Path': (str, False),
        'Port': (str, False),
        'Protocol': (str, False),
        'Query': (str, False),
        'StatusCode': (str, True),
    }

    def validate(self):
        one_of(self.__class__.__name__,
               self.properties,
               'StatusCode',
               ['HTTP_301', 'HTTP_302'])


class FixedResponseConfig(AWSProperty):
    props = {
        'ContentType': (str, False),
        'MessageBody': (str, False),
        'StatusCode': (str, True),
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
        "TargetGroupArn": (str, False),
        "ForwardConfig": (ForwardConfig, False),
        "Type": (str, True)
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
                          list(self.properties.keys())]
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
        'Values': ([str], False),
    }


class HttpHeaderConfig(AWSProperty):
    props = {
        'HttpHeaderName': (str, False),
        'Values': ([str], False),
    }


class HttpRequestMethodConfig(AWSProperty):
    props = {
        'Values': ([str], False),
    }


class PathPatternConfig(AWSProperty):
    props = {
        'Values': ([str], False),
    }


class QueryStringKeyValue(AWSProperty):
    props = {
        'Key': (str, False),
        'Value': (str, False),
    }


class QueryStringConfig(AWSProperty):
    props = {
        'Values': ([QueryStringKeyValue], False),
    }


class SourceIpConfig(AWSProperty):
    props = {
        'Values': ([str], False),
    }


class Condition(AWSProperty):
    props = {
        'Field': (str, False),
        'HostHeaderConfig': (HostHeaderConfig, False),
        'HttpHeaderConfig': (HttpHeaderConfig, False),
        'HttpRequestMethodConfig': (HttpRequestMethodConfig, False),
        'PathPatternConfig': (PathPatternConfig, False),
        'QueryStringConfig': (QueryStringConfig, False),
        'SourceIpConfig': (SourceIpConfig, False),
        'Values': ([str], False),
    }


class Matcher(AWSProperty):
    props = {
        'HttpCode': (str, True)
    }


class SubnetMapping(AWSProperty):
    props = {
        'AllocationId': (str, False),
        'PrivateIPv4Address': (str, False),
        'SubnetId': (str, True),
    }


class TargetGroupAttribute(AWSProperty):
    props = {
        'Key': (str, False),
        'Value': (str, False)
    }


class TargetDescription(AWSProperty):
    props = {
        'AvailabilityZone': (str, False),
        'Id': (str, True),
        'Port': (network_port, False)
    }


class Listener(AWSObject):
    resource_type = "AWS::ElasticLoadBalancingV2::Listener"

    props = {
        'AlpnPolicy': ([str], False),
        'Certificates': ([Certificate], False),
        'DefaultActions': ([Action], True),
        'LoadBalancerArn': (str, True),
        'Port': (network_port, True),
        'Protocol': (str, True),
        'SslPolicy': (str, False)
    }


class ListenerCertificate(AWSObject):
    resource_type = "AWS::ElasticLoadBalancingV2::ListenerCertificate"

    props = {
        'Certificates': ([Certificate], True),
        'ListenerArn': (str, True),
    }


class ListenerRule(AWSObject):
    resource_type = "AWS::ElasticLoadBalancingV2::ListenerRule"

    props = {
        'Actions': ([Action], True),
        'Conditions': ([Condition], True),
        'ListenerArn': (str, True),
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
        'HealthCheckPath': (str, False),
        'HealthCheckPort': (tg_healthcheck_port, False),
        'HealthCheckProtocol': (str, False),
        'HealthCheckTimeoutSeconds': (integer, False),
        'HealthyThresholdCount': (integer, False),
        'Matcher': (Matcher, False),
        'Name': (str, False),
        'Port': (network_port, False),
        'Protocol': (str, False),
        'Tags': ((Tags, list), False),
        'TargetGroupAttributes': ([TargetGroupAttribute], False),
        'Targets': ([TargetDescription], False),
        'TargetType': (validate_target_type, False),
        'UnhealthyThresholdCount': (integer, False),
        'VpcId': (str, False),
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
        'IpAddressType': (str, False),
        'LoadBalancerAttributes': ([LoadBalancerAttributes], False),
        'Name': (elb_name, False),
        'Scheme': (str, False),
        'SecurityGroups': ([str], False),
        'SubnetMappings': ([SubnetMapping], False),
        'Subnets': ([str], False),
        'Tags': ((Tags, list), False),
        'Type': (str, False),
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
