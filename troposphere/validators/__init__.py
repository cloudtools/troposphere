# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import json
from re import compile


def boolean(x):
    if x in [True, 1, "1", "true", "True"]:
        return True
    if x in [False, 0, "0", "false", "False"]:
        return False
    raise ValueError


def integer(x):
    try:
        int(x)
    except (ValueError, TypeError):
        raise ValueError("%r is not a valid integer" % x)
    else:
        return x


def positive_integer(x):
    p = integer(x)
    if int(p) < 0:
        raise ValueError("%r is not a positive integer" % x)
    return x


def integer_range(minimum_val, maximum_val):
    def integer_range_checker(x):
        i = int(x)
        if i < minimum_val or i > maximum_val:
            raise ValueError(
                "Integer must be between %d and %d" % (minimum_val, maximum_val)
            )
        return x

    return integer_range_checker


def integer_list_item(allowed_values):
    def integer_list_item_checker(x):
        i = int(x)
        if i in allowed_values:
            return x
        raise ValueError(
            "Integer must be one of following: %s"
            % ", ".join(str(j) for j in allowed_values)
        )

    return integer_list_item_checker


def double(x):
    try:
        float(x)
    except (ValueError, TypeError):
        raise ValueError("%r is not a valid double" % x)
    else:
        return x


def tags_or_list(x):
    """backward compatibility"""
    from .. import AWSHelperFn, Tags

    if isinstance(x, (AWSHelperFn, Tags, list)):
        return x

    raise ValueError(f"Value {x} of type {type(x)} must be either Tags or list")


def ignore(x):
    """Method to indicate bypassing property validation"""
    return x


def defer(x):
    """Method to indicate defering property validation"""
    return x


def network_port(x):
    from .. import AWSHelperFn

    # Network ports can be Ref items
    if isinstance(x, AWSHelperFn):
        return x

    i = integer(x)
    if int(i) < -1 or int(i) > 65535:
        raise ValueError("network port %r must been between 0 and 65535" % i)
    return x


def s3_bucket_name(b):
    # consecutive periods not allowed

    if ".." in b:
        raise ValueError("%s is not a valid s3 bucket name" % b)

    # IP addresses not allowed

    ip_re = compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if ip_re.match(b):
        raise ValueError("%s is not a valid s3 bucket name" % b)

    s3_bucket_name_re = compile(r"^[a-z\d][a-z\d\.-]{1,61}[a-z\d]$")
    if s3_bucket_name_re.match(b):
        return b
    else:
        raise ValueError("%s is not a valid s3 bucket name" % b)


def elb_name(b):
    elb_name_re = compile(
        r"^[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,30}[a-zA-Z0-9]{1})?$"
    )  # noqa
    if elb_name_re.match(b):
        return b
    else:
        raise ValueError("%s is not a valid elb name" % b)


def encoding(encoding):
    valid_encodings = ["plain", "base64"]
    if encoding not in valid_encodings:
        raise ValueError("Encoding needs to be one of %r" % valid_encodings)
    return encoding


def one_of(class_name, properties, property, conditionals):
    from .. import AWSHelperFn

    if isinstance(properties.get(property), AWSHelperFn) or issubclass(
        type(properties.get(property)), AWSHelperFn
    ):
        return
    if properties.get(property) not in conditionals:
        raise ValueError(
            # Ensure we handle None as a valid value
            '%s.%s must be one of: "%s"'
            % (
                class_name,
                property,
                ", ".join(condition for condition in conditionals if condition),
            ),
            "or a CFN Intrinsic function / troposphere.AWSHelperFn",
        )


def mutually_exclusive(class_name, properties, conditionals):
    from .. import NoValue

    found_list = []
    for c in conditionals:
        if c in properties and not properties[c] == NoValue:
            found_list.append(c)
    seen = set(found_list)
    specified_count = len(seen)
    if specified_count > 1:
        raise ValueError(
            ("%s: only one of the following" " can be specified: %s")
            % (class_name, ", ".join(conditionals))
        )
    return specified_count


def exactly_one(class_name, properties, conditionals):
    specified_count = mutually_exclusive(class_name, properties, conditionals)
    if specified_count != 1:
        raise ValueError(
            ("%s: one of the following" " must be specified: %s")
            % (class_name, ", ".join(conditionals))
        )
    return specified_count


def check_required(class_name, properties, conditionals):
    for c in conditionals:
        if c not in properties:
            raise ValueError("Resource %s required in %s" % (c, class_name))


def json_checker(prop):
    from .. import AWSHelperFn

    if isinstance(prop, str):
        # Verify it is a valid json string
        json.loads(prop)
        return prop
    elif isinstance(prop, dict):
        # Convert the dict to a basestring
        return json.dumps(prop)
    elif isinstance(prop, AWSHelperFn):
        return prop
    else:
        raise TypeError("json object must be a str or dict")


def waf_action_type(action):
    valid_actions = ["ALLOW", "BLOCK", "COUNT"]
    if action not in valid_actions:
        raise ValueError('Type must be one of: "%s"' % (", ".join(valid_actions)))
    return action
