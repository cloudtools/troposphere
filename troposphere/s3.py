# Copyright (c) 2013, Bob Van Zant <bob@veznat.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import positive_integer, s3_bucket_name
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


Private = "Private"
PublicRead = "PublicRead"
PublicReadWrite = "PublicReadWrite"
AuthenticatedRead = "AuthenticatedRead"
BucketOwnerRead = "BucketOwnerRead"
BucketOwnerFullControl = "BucketOwnerFullControl"
LogDeliveryWrite = "LogDeliveryWrite"


class CorsRules(AWSProperty):
    props = {
        'AllowedHeaders': ([basestring], False),
        'AllowedMethods': ([basestring], True),
        'AllowedOrigins': ([basestring], True),
        'ExposedHeaders': ([basestring], False),
        'Id': (basestring, False),
        'MaxAge': (positive_integer, False),
    }


class CorsConfiguration(AWSProperty):
    props = {
        'CorsRules': ([CorsRules], True),
    }


class VersioningConfiguration(AWSProperty):
    props = {
        'Status': (basestring, False),
    }


class RedirectAllRequestsTo(AWSProperty):
    props = {
        'HostName': (basestring, True),
        'Protocol': (basestring, False),
    }


class RedirectRule(AWSProperty):
    props = {
        'HostName': (basestring, False),
        'HttpRedirectCode': (basestring, False),
        'Protocol': (basestring, False),
        'ReplaceKeyPrefixWith': (basestring, False),
        'ReplaceKeyWith': (basestring, False),
    }


class RoutingRuleCondition(AWSProperty):
    props = {
        'HttpErrorCodeReturnedEquals': (basestring, False),
        'KeyPrefixEquals': (basestring, False),
    }


class RoutingRule(AWSProperty):
    props = {
        'RedirectRule': (RedirectRule, True),
        'RoutingRuleCondition': (RoutingRuleCondition, False),
    }


class WebsiteConfiguration(AWSProperty):
    props = {
        'IndexDocument': (basestring, False),
        'ErrorDocument': (basestring, False),
        'RedirectAllRequestsTo': (RedirectAllRequestsTo, False),
        'RoutingRules': ([RoutingRule], False),
    }


class LifecycleRuleTransition(AWSProperty):
    props = {
        'StorageClass': (basestring, True),
        'TransitionDate': (basestring, False),
        'TransitionInDays': (positive_integer, False),
    }


class NoncurrentVersionTransition(AWSProperty):
    props = {
        'StorageClass': (basestring, True),
        'TransitionInDays': (positive_integer, True),
    }


class LifecycleRule(AWSProperty):
    props = {
        'ExpirationDate': (basestring, False),
        'ExpirationInDays': (positive_integer, False),
        'Id': (basestring, False),
        'NoncurrentVersionExpirationInDays': (positive_integer, False),
        'NoncurrentVersionTransition': (NoncurrentVersionTransition, False),
        'Prefix': (basestring, False),
        'Status': (basestring, True),
        'Transition': (LifecycleRuleTransition, False),
    }


class LifecycleConfiguration(AWSProperty):
    props = {
        'Rules': ([LifecycleRule], True),
    }


class LoggingConfiguration(AWSProperty):
    props = {
        'DestinationBucketName': (s3_bucket_name, False),
        'LogFilePrefix': (basestring, False),
    }


class TopicConfiguration(AWSProperty):
    props = {
        'Event': (basestring, True),
        'Topic': (basestring, True),
    }


class NotificationConfiguration(AWSProperty):
    props = {
        'TopicConfigurations': ([TopicConfiguration], True),
    }


class Bucket(AWSObject):
    resource_type = "AWS::S3::Bucket"

    props = {
        'AccessControl': (basestring, False),
        'BucketName': (s3_bucket_name, False),
        'CorsConfiguration': (CorsConfiguration, False),
        'LifecycleConfiguration': (LifecycleConfiguration, False),
        'LoggingConfiguration': (LoggingConfiguration, False),
        'NotificationConfiguration': (NotificationConfiguration, False),
        'Tags': (Tags, False),
        'WebsiteConfiguration': (WebsiteConfiguration, False),
        'VersioningConfiguration': (VersioningConfiguration, False)
    }

    access_control_types = [
        Private,
        PublicRead,
        PublicReadWrite,
        AuthenticatedRead,
        BucketOwnerRead,
        BucketOwnerFullControl,
        LogDeliveryWrite,
    ]

    def __init__(self, name, **kwargs):
        super(Bucket, self).__init__(name, **kwargs)

        if 'AccessControl' in kwargs:
            if kwargs['AccessControl'] not in self.access_control_types:
                raise ValueError('AccessControl must be one of "%s"' % (
                    ', '.join(self.access_control_types)))


class BucketPolicy(AWSObject):
    resource_type = "AWS::S3::BucketPolicy"

    props = {
        'Bucket': (basestring, True),
        'PolicyDocument': (policytypes, True),
    }
