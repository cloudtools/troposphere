# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import elb_name, integer_range, network_port, tags_or_list


def validate_int_to_str(x):
    """
    Backward compatibility - field was int and now str.
    Property: HealthCheck.Interval
    Property: HealthCheck.Timeout
    """

    if isinstance(x, int):
        return str(x)
    if isinstance(x, str):
        return str(int(x))

    raise TypeError(f"Value {x} of type {type(x)} must be either int or str")


def validate_elb_name(x):
    """
    Property: LoadBalancer.LoadBalancerName
    """
    return elb_name(x)


def validate_network_port(x):
    """
    Property: Listener.InstancePort
    Property: Listener.LoadBalancerPort
    """
    return network_port(x)


def validate_tags_or_list(x):
    """
    Property: LoadBalancer.Tags
    """
    return tags_or_list(x)


def validate_threshold(port):
    """
    Property: HealthCheck.HealthyThreshold
    Property: HealthCheck.UnhealthyThreshold
    """
    return integer_range(2, 10)(port)
