# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from .. import If
from ..type_defs.compat import Final
from . import elb_name, exactly_one, network_port, one_of, tags_or_list


def tg_healthcheck_port(x):
    """
    Property: TargetGroup.HealthCheckPort
    """
    if isinstance(x, str) and x == "traffic-port":
        return x
    return network_port(x)


def validate_elb_name(x):
    """
    Property: LoadBalancer.Name
    """
    return elb_name(x)


def validate_network_port(x):
    """
    Property: TargetDescription.Port
    Property: Listener.Port
    Property: TargetGroup.Port
    """
    return network_port(x)


def validate_tags_or_list(x):
    """
    Property: LoadBalancer.Tags
    Property: TargetGroup.Tags
    """
    return tags_or_list(x)


def validate_redirect_config(self):
    """
    Class: RedirectConfig
    """
    one_of(
        self.__class__.__name__,
        self.properties,
        "StatusCode",
        ["HTTP_301", "HTTP_302"],
    )


def validate_fixed_response_config(self):
    """
    Class: FixedResponseConfig
    """
    one_of(
        self.__class__.__name__,
        self.properties,
        "ContentType",
        [
            None,
            "text/plain",
            "text/css",
            "text/html",
            "application/javascript",
            "application/json",
        ],
    )


def validate_action(self):
    """
    Class: Action
    """
    one_of(
        self.__class__.__name__,
        self.properties,
        "Type",
        [
            "forward",
            "redirect",
            "fixed-response",
            "authenticate-cognito",
            "authenticate-oidc",
        ],
    )

    def any_property(require_prop, properties):
        return any(p in require_prop for p in properties)

    def requires(action_type, prop):
        properties = [definition for definition in self.properties.keys()]
        if self.properties.get("Type") == action_type and not any_property(
            prop, properties
        ):
            raise ValueError(
                'Type "%s" requires definition of "%s"' % (action_type, prop)
            )
        if (
            any_property(prop, properties)
            and self.properties.get("Type") != action_type
        ):
            raise ValueError(
                'Definition of "%s" allowed only with '
                'type "%s", was: "%s"'
                % (prop, action_type, self.properties.get("Type"))
            )

    requires("forward", ["TargetGroupArn", "ForwardConfig"])
    requires("redirect", ["RedirectConfig"])
    requires("fixed-response", ["FixedResponseConfig"])


TARGET_TYPE_ALB: Final = "alb"
TARGET_TYPE_INSTANCE: Final = "instance"
TARGET_TYPE_IP: Final = "ip"
TARGET_TYPE_LAMBDA: Final = "lambda"


def validate_target_type(target_type):
    """
    Property: TargetGroup.TargetType
    """
    valid_types = [
        TARGET_TYPE_ALB,
        TARGET_TYPE_INSTANCE,
        TARGET_TYPE_IP,
        TARGET_TYPE_LAMBDA,
    ]
    if target_type not in valid_types:
        raise ValueError(
            'TargetGroup.TargetType must be one of: "%s"' % ", ".join(valid_types)
        )
    return target_type


def validate_target_group(self):
    """
    Class: TargetGroup
    """

    def check_properties(action_types, props_to_check, required):
        for this_type in action_types:
            self_props = self.properties
            if self_props.get("TargetType") == this_type:
                invalid_props = []
                for prop in props_to_check:
                    if (prop not in self_props and required is True) or (
                        prop in self_props and required is False
                    ):
                        invalid_props.append(prop)

                if len(invalid_props) > 0:
                    # Make error message more readable in the default case
                    type_msg = (
                        "Omitting TargetType"
                        if this_type is None
                        else 'TargetType of "%s"' % this_type
                    )

                    raise ValueError(
                        '%s in "%s" %s definitions of %s'
                        % (
                            type_msg,
                            self.__class__.__name__,
                            "requires" if required is True else "must not contain",
                            str(invalid_props).strip("[]"),
                        )
                    )

    # None defaults to instance as per the AWS docs
    check_properties(
        [None, TARGET_TYPE_INSTANCE, TARGET_TYPE_IP],
        ["Port", "Protocol", "VpcId"],
        True,
    )
    check_properties([TARGET_TYPE_LAMBDA], ["Port", "Protocol", "VpcId"], False)


def validate_loadbalancer(self):
    """
    Class: LoadBalancer
    """
    conds = [
        "SubnetMappings",
        "Subnets",
    ]

    def check_if(names, props):
        validated = []
        for name in names:
            validated.append(name in props and isinstance(props[name], If))
        return all(validated)

    if check_if(conds, self.properties):
        return

    exactly_one(self.__class__.__name__, self.properties, conds)
