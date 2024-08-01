# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import json_checker, positive_integer, tags_or_list


def dict_or_string(x):
    """
    Property: Model.Schema
    """

    if isinstance(x, (dict, str)):
        return x
    raise TypeError(f"Value {x} of type {type(x)} must be either dict or str")


def validate_tags_or_list(x):
    """
    Property: StageDescription.Tags
    Property: Stage.Tags
    """
    return tags_or_list(x)


def validate_timeout_in_millis(x):
    """
    Property: Integration.TimeoutInMillis
    """
    int(x)
    if x < 50:
        raise ValueError(f"TimeoutInMillis of {x} must be greater than 50")
    return x


def validate_authorizer_ttl(ttl_value):
    """Validate authorizer ttl timeout
    :param ttl_value: The TTL timeout in seconds
    :return: The provided TTL value if valid
    Property: Authorizer.AuthorizerResultTtlInSeconds
    """
    ttl_value = int(positive_integer(ttl_value))
    if ttl_value > 3600:
        raise ValueError("The AuthorizerResultTtlInSeconds should be <= 3600")
    return ttl_value


def validate_gateway_response_type(response_type):
    """Validate response type
    :param response_type: The GatewayResponse response type
    :return: The provided value if valid
    Property: GatewayResponse.ResponseType
    """
    valid_response_types = [
        "ACCESS_DENIED",
        "API_CONFIGURATION_ERROR",
        "AUTHORIZER_FAILURE",
        "AUTHORIZER_CONFIGURATION_ERROR",
        "BAD_REQUEST_PARAMETERS",
        "BAD_REQUEST_BODY",
        "DEFAULT_4XX",
        "DEFAULT_5XX",
        "EXPIRED_TOKEN",
        "INVALID_SIGNATURE",
        "INTEGRATION_FAILURE",
        "INTEGRATION_TIMEOUT",
        "INVALID_API_KEY",
        "MISSING_AUTHENTICATION_TOKEN",
        "QUOTA_EXCEEDED",
        "REQUEST_TOO_LARGE",
        "RESOURCE_NOT_FOUND",
        "THROTTLED",
        "UNAUTHORIZED",
        "UNSUPPORTED_MEDIA_TYPE",
    ]
    if response_type not in valid_response_types:
        raise ValueError("{} is not a valid ResponseType".format(response_type))
    return response_type


def validate_model(self):
    """
    Class: Model
    """
    name = "Schema"
    if name in self.properties:
        schema = self.properties.get(name)
        self.properties[name] = json_checker(schema)
