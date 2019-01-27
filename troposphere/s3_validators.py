# Copyright (c) 2013, Bob Van Zant <bob@veznat.com>
# All rights reserved.
#
# See LICENSE file for full license.

import warnings
from troposphere import AWSHelperFn


class RuleMixin(object):
    def validate(self):
        if 'Transition' in self.properties:
            if 'Transitions' not in self.properties:
                # aws moved from a single transition to a list of them
                # and deprecated 'Transition', so let's just move it to
                # the new property and not annoy the user.
                self.properties['Transitions'] = [
                    self.properties.pop('Transition')]
            else:
                raise ValueError(
                    'Cannot specify both "Transition" and "Transitions" '
                    'properties on S3 Bucket Lifecycle Rule. Please use '
                    '"Transitions" since the former has been deprecated.')

        if 'NoncurrentVersionTransition' in self.properties:
            if 'NoncurrentVersionTransitions' not in self.properties:
                warnings.warn(
                    'NoncurrentVersionTransition has been deprecated in '
                    'favour of NoncurrentVersionTransitions.'
                )
                # Translate the old transition format to the new format
                self.properties['NoncurrentVersionTransitions'] = [
                    self.properties.pop('NoncurrentVersionTransition')]
            else:
                raise ValueError(
                    'Cannot specify both "NoncurrentVersionTransition" and '
                    '"NoncurrentVersionTransitions" properties on S3 Bucket '
                    'Lifecycle Rule. Please use '
                    '"NoncurrentVersionTransitions" since the former has been '
                    'deprecated.')

        if 'ExpirationInDays' in self.properties and 'ExpirationDate' in \
                self.properties:
            raise ValueError(
                'Cannot specify both "ExpirationDate" and "ExpirationInDays"'
            )


class BucketMixin(object):
    access_control_types = [
        "Private",
        "PublicRead",
        "PublicReadWrite",
        "AuthenticatedRead",
        "BucketOwnerRead",
        "BucketOwnerFullControl",
        "LogDeliveryWrite",
    ]

    def validate(self):
        access_control = self.properties.get('AccessControl')
        if access_control is not None and \
                not isinstance(access_control, AWSHelperFn):
            if access_control not in self.access_control_types:
                raise ValueError('AccessControl must be one of "%s"' % (
                    ', '.join(self.access_control_types)))


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


def s3_transfer_acceleration_status(value):
    valid_status = ['Enabled', 'Suspended']
    if value not in valid_status:
        raise ValueError(
            'AccelerationStatus must be one of: "%s"' % (
                ', '.join(valid_status)
            )
        )
    return value
