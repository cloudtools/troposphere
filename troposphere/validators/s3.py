# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


import warnings

from ..compat import validate_policytype
from . import s3_bucket_name

Private = "Private"
PublicRead = "PublicRead"
PublicReadWrite = "PublicReadWrite"
AuthenticatedRead = "AuthenticatedRead"
BucketOwnerRead = "BucketOwnerRead"
BucketOwnerFullControl = "BucketOwnerFullControl"
LogDeliveryWrite = "LogDeliveryWrite"


def policytypes(policy):
    """
    Property: AccessPoint.Policy
    Property: BucketPolicy.PolicyDocument
    Property: MultiRegionAccessPointPolicy.Policy
    """
    return validate_policytype(policy)


def validate_s3_bucket_name(b):
    """
    Property: Bucket.BucketName
    Property: LoggingConfiguration.DestinationBucketName
    """
    return s3_bucket_name(b)


def s3_transfer_acceleration_status(value):
    """
    Property: AccelerateConfiguration.AccelerationStatus
    """
    valid_status = ["Enabled", "Suspended"]
    if value not in valid_status:
        raise ValueError(
            'AccelerationStatus must be one of: "%s"' % (", ".join(valid_status))
        )
    return value


def validate_bucket(self):
    """
    Class: Bucket
    """

    from .. import AWSHelperFn

    access_control_types = [
        Private,
        PublicRead,
        PublicReadWrite,
        AuthenticatedRead,
        BucketOwnerRead,
        BucketOwnerFullControl,
        LogDeliveryWrite,
    ]

    access_control = self.properties.get("AccessControl")
    if access_control is not None and not isinstance(access_control, AWSHelperFn):
        if access_control not in access_control_types:
            access_types = ", ".join(access_control_types)
            raise ValueError(f"AccessControl must be one of {access_types}")


def validate_lifecycle_rule(self):
    """
    Class: LifecycleRule
    """
    if "Transition" in self.properties:
        if "Transitions" not in self.properties:
            # aws moved from a single transition to a list of them
            # and deprecated 'Transition', so let's just move it to
            # the new property and not annoy the user.
            self.properties["Transitions"] = [self.properties.pop("Transition")]
        else:
            raise ValueError(
                'Cannot specify both "Transition" and "Transitions" '
                "properties on S3 Bucket Lifecycle Rule. Please use "
                '"Transitions" since the former has been deprecated.'
            )

    if "NoncurrentVersionTransition" in self.properties:
        if "NoncurrentVersionTransitions" not in self.properties:
            warnings.warn(
                "NoncurrentVersionTransition has been deprecated in "
                "favour of NoncurrentVersionTransitions."
            )
            # Translate the old transition format to the new format
            self.properties["NoncurrentVersionTransitions"] = [
                self.properties.pop("NoncurrentVersionTransition")
            ]
        else:
            raise ValueError(
                'Cannot specify both "NoncurrentVersionTransition" and '
                '"NoncurrentVersionTransitions" properties on S3 Bucket '
                "Lifecycle Rule. Please use "
                '"NoncurrentVersionTransitions" since the former has been '
                "deprecated."
            )

    if "ExpirationInDays" in self.properties and "ExpirationDate" in self.properties:
        raise ValueError('Cannot specify both "ExpirationDate" and "ExpirationInDays"')
