# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def boolean(x):
    if isinstance(x, bool):
        return x
    if x in [1, '1', 'true', 'True']:
        return True
    if x in [0, '0', 'false', 'False']:
        return False
    raise ValueError


def integer(x):
    if isinstance(x, int):
        return x
    if isinstance(x, basestring):
        return int(x)


def positive_integer(x):
    x = integer(x)
    if x < 0:
        raise ValueError
    return x


def integer_range(minimum_val, maximum_val):
    def integer_range_checker(x):
        x = integer(x)
        if x < minimum_val or x > maximum_val:
            raise ValueError('Integer must be between %d and %d' % (
                minimum_val, maximum_val))
        return x

    return integer_range_checker


def network_port(x):
    from . import AWSHelperFn

    # Network ports can be Ref items
    if isinstance(x, AWSHelperFn):
        return x

    x = integer(x)
    if x < -1 or x > 65535:
        raise ValueError
    return x
