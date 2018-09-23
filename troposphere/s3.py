# Copyright (c) 2013, Bob Van Zant <bob@veznat.com>
# All rights reserved.
#
# See LICENSE file for full license.
import warnings

from . import AWSHelperFn, AWSObject, AWSProperty, Tags
from .validators import boolean, positive_integer, s3_bucket_name
from .validators import s3_transfer_acceleration_status

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


class AccelerateConfiguration(AWSProperty):
    props = {
        'AccelerationStatus': (s3_transfer_acceleration_status, True),
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


class AbortIncompleteMultipartUpload(AWSProperty):
    props = {
        'DaysAfterInitiation': (positive_integer, True),
    }


class NoncurrentVersionTransition(AWSProperty):
    props = {
        'StorageClass': (basestring, True),
        'TransitionInDays': (positive_integer, True),
    }


class TagFilter(AWSProperty):
    props = {
        'Key': (basestring, True),
        'Value': (basestring, True),
    }


class LifecycleRule(AWSProperty):
    props = {
        'AbortIncompleteMultipartUpload':
            (AbortIncompleteMultipartUpload, False),
        'ExpirationDate': (basestring, False),
        'ExpirationInDays': (positive_integer, False),
        'Id': (basestring, False),
        'NoncurrentVersionExpirationInDays': (positive_integer, False),
        'NoncurrentVersionTransition': (NoncurrentVersionTransition, False),
        'NoncurrentVersionTransitions': ([NoncurrentVersionTransition], False),
        'Prefix': (basestring, False),
        'Status': (basestring, True),
        'TagFilters': ([TagFilter], False),
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


class MetricsConfiguration(AWSProperty):
    props = {
        'Id': (basestring, True),
        'Prefix': (basestring, False),
        'TagFilters': ([TagFilter], False),
    }


class NotificationConfiguration(AWSProperty):
    props = {
        'LambdaConfigurations': ([LambdaConfigurations], False),
        'QueueConfigurations': ([QueueConfigurations], False),
        'TopicConfigurations': ([TopicConfigurations], False),
    }


class AccessControlTranslation(AWSProperty):
    props = {
        'Owner': (basestring, True),
    }


class EncryptionConfiguration(AWSProperty):
    props = {
        'ReplicaKmsKeyID': (basestring, True),
    }


class ReplicationConfigurationRulesDestination(AWSProperty):
    props = {
        'AccessControlTranslation': (AccessControlTranslation, False),
        'Account': (basestring, False),
        'Bucket': (basestring, True),
        'EncryptionConfiguration': (EncryptionConfiguration, False),
        'StorageClass': (basestring, False),
    }


class SseKmsEncryptedObjects(AWSProperty):
    props = {
        'Status': (basestring, True),
    }


class SourceSelectionCriteria(AWSProperty):
    props = {
        'SseKmsEncryptedObjects': (SseKmsEncryptedObjects, True),
    }


class ReplicationConfigurationRules(AWSProperty):
    props = {
        'Destination': (ReplicationConfigurationRulesDestination, True),
        'Id': (basestring, False),
        'Prefix': (basestring, True),
        'SourceSelectionCriteria': (SourceSelectionCriteria, False),
        'Status': (basestring, True)
    }


class ReplicationConfiguration(AWSProperty):
    props = {
        'Role': (basestring, True),
        'Rules': ([ReplicationConfigurationRules], True)
    }


class Destination(AWSProperty):
    props = {
        'BucketAccountId': (basestring, False),
        'BucketArn': (basestring, True),
        'Format': (basestring, True),
        'Prefix': (basestring, False),
    }


class DataExport(AWSProperty):
    props = {
        'Destination': (Destination, True),
        'OutputSchemaVersion': (basestring, True),
    }


class StorageClassAnalysis(AWSProperty):
    props = {
        'DataExport': (DataExport, False),
    }


class AnalyticsConfiguration(AWSProperty):
    props = {
        'Id': (basestring, True),
        'Prefix': (basestring, False),
        'StorageClassAnalysis': (StorageClassAnalysis, True),
        'TagFilters': ([TagFilter], False),
    }


class ServerSideEncryptionByDefault(AWSProperty):
    props = {
        'KMSMasterKeyID': (basestring, False),
        'SSEAlgorithm': (basestring, True),
    }


class ServerSideEncryptionRule(AWSProperty):
    props = {
        'ServerSideEncryptionByDefault':
            (ServerSideEncryptionByDefault, False),
    }


class BucketEncryption(AWSProperty):
    props = {
        'ServerSideEncryptionConfiguration':
            ([ServerSideEncryptionRule], True),
    }


class InventoryConfiguration(AWSProperty):
    props = {
        'Destination': (Destination, True),
        'Enabled': (boolean, True),
        'Id': (basestring, True),
        'IncludedObjectVersions': (basestring, True),
        'OptionalFields': ([basestring], True),
        'Prefix': (basestring, False),
        'ScheduleFrequency': (basestring, True),
    }


class Bucket(AWSObject):
    resource_type = "AWS::S3::Bucket"

    props = {
        'AccessControl': (basestring, False),
        'AccelerateConfiguration': (AccelerateConfiguration, False),
        'AnalyticsConfigurations': ([AnalyticsConfiguration], False),
        'BucketEncryption': (BucketEncryption, False),
        'BucketName': (s3_bucket_name, False),
        'CorsConfiguration': (CorsConfiguration, False),
        'InventoryConfigurations': ([InventoryConfiguration], False),
        'LifecycleConfiguration': (LifecycleConfiguration, False),
        'LoggingConfiguration': (LoggingConfiguration, False),
        'MetricsConfigurations': ([MetricsConfiguration], False),
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

    def validate(self):
        access_control = self.properties.get('AccessControl')
        if access_control is not None and \
                not isinstance(access_control, AWSHelperFn):
            if access_control not in self.access_control_types:
                raise ValueError('AccessControl must be one of "%s"' % (
                    ', '.join(self.access_control_types)))


class BucketPolicy(AWSObject):
    resource_type = "AWS::S3::BucketPolicy"

    props = {
        'Bucket': (basestring, True),
        'PolicyDocument': (policytypes, True),
    }
