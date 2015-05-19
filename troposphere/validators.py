# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


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


def s3_bucket_name(b):
    from re import compile
    s3_bucket_name_re = compile(r'^[a-z\d][a-z\d\.-]{1,61}[a-z\d]$')
    if s3_bucket_name_re.match(b):
        return b
    else:
        raise ValueError("%s is not a valid s3 bucket name" % b)


def encoding(encoding):
    valid_encodings = ['plain', 'base64']
    if encoding not in valid_encodings:
        raise ValueError('Encoding needs to be one of %r' % valid_encodings)
    return encoding
