# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from ..compat import validate_policytype
from . import integer_range, tags_or_list


def policytypes(policy):
    """
    Property: Domain.AccessPolicies
    """
    return validate_policytype(policy)


def validate_automated_snapshot_start_hour(port):
    """
    Property: SnapshotOptions.AutomatedSnapshotStartHour
    """
    return integer_range(0, 23)(port)


def validate_tags_or_list(x):
    """
    Property: Domain.Tags
    """
    return tags_or_list(x)


def validate_volume_type(volume_type):
    """
    Validate VolumeType for ElasticsearchDomain
    Property: EBSOptions.VolumeType
    """

    VALID_VOLUME_TYPES = ("standard", "gp2", "gp3", "io1")

    if volume_type not in VALID_VOLUME_TYPES:
        raise ValueError(
            "Elasticsearch Domain VolumeType must be one of: %s"
            % ", ".join(VALID_VOLUME_TYPES)
        )
    return volume_type


def validate_tls_security_policy(tls_security_policy):
    """
    Validate TLS Security Policy for ElasticsearchDomain
    Property: DomainEndpointOptions.TLSSecurityPolicy
    """

    VALID_TLS_SECURITY_POLICIES = (
        "Policy-Min-TLS-1-0-2019-07",
        "Policy-Min-TLS-1-2-2019-07",
    )

    if tls_security_policy not in VALID_TLS_SECURITY_POLICIES:
        raise ValueError(
            "Minimum TLS Security Policy must be one of: %s"
            % ", ".join(VALID_TLS_SECURITY_POLICIES)
        )
    return tls_security_policy


def validate_ebs_options(self):
    """
    Class: EBSOptions
    """

    volume_type = self.properties.get("VolumeType")
    iops = self.properties.get("Iops")
    if volume_type == "io1" and not iops:
        raise ValueError("Must specify Iops if VolumeType is 'io1'.")
