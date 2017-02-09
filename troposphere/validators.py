# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
from re import compile


def boolean(x):
    if x in [True, 1, '1', 'true', 'True']:
        return "true"
    if x in [False, 0, '0', 'false', 'False']:
        return "false"
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
            raise ValueError('Integer must be between %d and %d' % (
                minimum_val, maximum_val))
        return x

    return integer_range_checker


def network_port(x):
    from . import AWSHelperFn

    # Network ports can be Ref items
    if isinstance(x, AWSHelperFn):
        return x

    i = integer(x)
    if int(i) < -1 or int(i) > 65535:
        raise ValueError("network port %r must been between 0 and 65535" % i)
    return x


def tg_healthcheck_port(x):
    if isinstance(x, str) and x == "traffic-port":
        return x
    return network_port(x)


def s3_bucket_name(b):

    # consecutive periods not allowed

    if '..' in b:
        raise ValueError("%s is not a valid s3 bucket name" % b)

    # IP addresses not allowed

    ip_re = compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    if ip_re.match(b):
        raise ValueError("%s is not a valid s3 bucket name" % b)

    s3_bucket_name_re = compile(r'^[a-z\d][a-z\d\.-]{1,61}[a-z\d]$')
    if s3_bucket_name_re.match(b):
        return b
    else:
        raise ValueError("%s is not a valid s3 bucket name" % b)


def elb_name(b):
    elb_name_re = compile(r'^[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,30}[a-zA-Z0-9]{1})?$')  # noqa
    if elb_name_re.match(b):
        return b
    else:
        raise ValueError("%s is not a valid elb name" % b)


def encoding(encoding):
    valid_encodings = ['plain', 'base64']
    if encoding not in valid_encodings:
        raise ValueError('Encoding needs to be one of %r' % valid_encodings)
    return encoding


def status(status):
    valid_statuses = ['Active', 'Inactive']
    if status not in valid_statuses:
        raise ValueError('Status needs to be one of %r' % valid_statuses)
    return status


def iam_names(b):
    iam_name_re = compile(r'^[a-zA-Z0-9_\.\+\=\@\-\,]+$')
    if iam_name_re.match(b):
        return b
    else:
        raise ValueError("%s is not a valid iam name" % b)


def iam_user_name(user_name):
    if not user_name:
        raise ValueError(
            "AWS::IAM::User property 'UserName' may not be empty")

    if len(user_name) > 64:
        raise ValueError(
            "AWS::IAM::User property 'UserName' may not exceed 64 characters")

    iam_user_name_re = compile(r'^[\w+=,.@-]+$')
    if iam_user_name_re.match(user_name):
        return user_name
    else:
        raise ValueError(
            "%s is not a valid value for AWS::IAM::User property 'UserName'",
            user_name)


def iam_path(path):
    if len(path) > 512:
        raise ValueError('IAM path %s may not exceed 512 characters', path)

    iam_path_re = compile(r'^\/.*\/$|^\/$')
    if not iam_path_re.match(path):
        raise ValueError("%s is not a valid iam path name" % path)
    return path


def iam_role_name(role_name):
    if len(role_name) > 64:
        raise ValueError('IAM Role Name may not exceed 64 characters')
    iam_names(role_name)
    return role_name


def iam_group_name(group_name):
    if len(group_name) > 128:
        raise ValueError('IAM Role Name may not exceed 128 characters')
    iam_names(group_name)
    return group_name


def mutually_exclusive(class_name, properties, conditionals):
    found_list = []
    for c in conditionals:
        if c in properties:
            found_list.append(c)
    seen = set(found_list)
    specified_count = len(seen)
    if specified_count > 1:
        raise ValueError(('%s: only one of the following'
                          ' can be specified: %s') % (
                          class_name, ', '.join(conditionals)))
    return specified_count


def exactly_one(class_name, properties, conditionals):
    specified_count = mutually_exclusive(class_name, properties, conditionals)
    if specified_count != 1:
        raise ValueError(('%s: one of the following'
                          ' must be specified: %s') % (
                          class_name, ', '.join(conditionals)))
    return specified_count
