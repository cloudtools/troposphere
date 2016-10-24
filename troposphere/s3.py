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
        'Transitions': ([LifecycleRuleTransition], False)
    }

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


class LifecycleConfiguration(AWSProperty):
    props = {
        'Rules': ([LifecycleRule], True),
    }


class LoggingConfiguration(AWSProperty):
    props = {
        'DestinationBucketName': (s3_bucket_name, False),
        'LogFilePrefix': (basestring, False),
    }


class Rules(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Value': (basestring, True)
    }


class S3Key(AWSProperty):
    props = {
        'Rules': ([Rules], True)
    }


class Filter(AWSProperty):
    props = {
        'S3Key': (S3Key, True)
    }


class LambdaConfigurations(AWSProperty):
    props = {
        'Event': (basestring, True),
        'Filter': (Filter, False),
        'Function': (basestring, True),
    }


class QueueConfigurations(AWSProperty):
    props = {
        'Event': (basestring, True),
        'Filter': (Filter, False),
        'Queue': (basestring, True),
    }


class TopicConfigurations(AWSProperty):
    props = {
        'Event': (basestring, True),
        'Filter': (Filter, False),
        'Topic': (basestring, True),
    }


class NotificationConfiguration(AWSProperty):
    props = {
        'LambdaConfigurations': ([LambdaConfigurations], False),
        'QueueConfigurations': ([QueueConfigurations], False),
        'TopicConfigurations': ([TopicConfigurations], False),
    }


class ReplicationConfigurationRulesDestination(AWSProperty):
    props = {
        'Bucket': (basestring, True),
        'StorageClass': (basestring, False)
    }


class ReplicationConfigurationRules(AWSProperty):
    props = {
        'Destination': (ReplicationConfigurationRulesDestination, True),
        'Id': (basestring, False),
        'Prefix': (basestring, True),
        'Status': (basestring, True)
    }


class ReplicationConfiguration(AWSProperty):
    props = {
        'Role': (basestring, True),
        'Rules': ([ReplicationConfigurationRules], True)
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
        'ReplicationConfiguration': (ReplicationConfiguration, False),
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

    def __init__(self, name=None, **kwargs):

        # note: 'name' is the resource title, not the bucket name

        if not name and 'title' in kwargs:
            name = kwargs.pop('title')
        if not name:
            raise TypeError("You must provide a title for the bucket resource")
        super(Bucket, self).__init__(name, **kwargs)

        if 'AccessControl' in kwargs and \
                isinstance(kwargs['AccessControl'], basestring):
            if kwargs['AccessControl'] not in self.access_control_types:
                raise ValueError('AccessControl must be one of "%s"' % (
                    ', '.join(self.access_control_types)))


class BucketPolicy(AWSObject):
    resource_type = "AWS::S3::BucketPolicy"

    props = {
        'Bucket': (basestring, True),
        'PolicyDocument': (policytypes, True),
    }
