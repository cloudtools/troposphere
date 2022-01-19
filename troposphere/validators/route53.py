# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from .. import AWSProperty
from . import boolean, network_port, positive_integer


class AlarmIdentifier(AWSProperty):
    """
    Export:
    """

    props = {
        "Name": (str, True),
        "Region": (str, True),
    }


class HealthCheckConfiguration(AWSProperty):
    """
    Export:
    """

    props = {
        "AlarmIdentifier": (AlarmIdentifier, False),
        "ChildHealthChecks": ([str], False),
        "EnableSNI": (boolean, False),
        "FailureThreshold": (positive_integer, False),
        "FullyQualifiedDomainName": (str, False),
        "HealthThreshold": (positive_integer, False),
        "InsufficientDataHealthStatus": (str, False),
        "Inverted": (boolean, False),
        "IPAddress": (str, False),
        "MeasureLatency": (boolean, False),
        "Port": (network_port, False),
        "Regions": ([str], False),
        "RequestInterval": (positive_integer, False),
        "ResourcePath": (str, False),
        "SearchString": (str, False),
        "Type": (str, True),
    }


class AliasTarget(AWSProperty):
    """
    Export:
    """

    props = {
        "HostedZoneId": (str, True),
        "DNSName": (str, True),
        "EvaluateTargetHealth": (boolean, False),
    }

    def __init__(
        self, hostedzoneid=None, dnsname=None, evaluatetargethealth=None, **kwargs
    ):
        # provided for backward compatibility
        if hostedzoneid is not None:
            kwargs["HostedZoneId"] = hostedzoneid
        if dnsname is not None:
            kwargs["DNSName"] = dnsname
        if evaluatetargethealth is not None:
            kwargs["EvaluateTargetHealth"] = evaluatetargethealth
        super().__init__(**kwargs)
