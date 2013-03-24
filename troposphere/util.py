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


def network_port(x):
    x = integer(x)
    if x < -1 or x > 65535:
        raise ValueError
    return x
