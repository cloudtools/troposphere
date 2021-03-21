# Copyright (c) 2013, Bob Van Zant <bob@veznat.com>
# All rights reserved.
#
# See LICENSE file for full license.
import warnings

from . import AWSHelperFn, AWSObject, AWSProperty, Tags
from .compat import policytypes
from .validators import boolean, double, integer, positive_integer
from .validators import s3_bucket_name, s3_transfer_acceleration_status

Private = "Private"
PublicRead = "PublicRead"
PublicReadWrite = "PublicReadWrite"
AuthenticatedRead = "AuthenticatedRead"
BucketOwnerRead = "BucketOwnerRead"
BucketOwnerFullControl = "BucketOwnerFullControl"
LogDeliveryWrite = "LogDeliveryWrite"


class PublicAccessBlockConfiguration(AWSProperty):
    props = {
        'BlockPublicAcls': (boolean, False),
        'BlockPublicPolicy': (boolean, False),
        'IgnorePublicAcls': (boolean, False),
        'RestrictPublicBuckets': (boolean, False),
    }


class VpcConfiguration(AWSProperty):
    props = {
        'VpcId': (str, False),
    }


class AccessPoint(AWSObject):
    resource_type = "AWS::S3::AccessPoint"

    props = {
        'Bucket': (str, True),
        'CreationDate': (str, False),
        'Name': (str, False),
        'NetworkOrigin': (str, False),
        'Policy': (dict, False),
        'PolicyStatus': (dict, False),
        'PublicAccessBlockConfiguration':
            (PublicAccessBlockConfiguration, False),
        'VpcConfiguration': (VpcConfiguration, False),
    }


class CorsRules(AWSProperty):
    props = {
        'AllowedHeaders': ([str], False),
        'AllowedMethods': ([str], True),
        'AllowedOrigins': ([str], True),
        'ExposedHeaders': ([str], False),
        'Id': (str, False),
        'MaxAge': (positive_integer, False),
    }


class CorsConfiguration(AWSProperty):
    props = {
        'CorsRules': ([CorsRules], True),
    }


class VersioningConfiguration(AWSProperty):
    props = {
        'Status': (str, False),
    }


class AccelerateConfiguration(AWSProperty):
    props = {
        'AccelerationStatus': (s3_transfer_acceleration_status, True),
    }


class RedirectAllRequestsTo(AWSProperty):
    props = {
        'HostName': (str, True),
        'Protocol': (str, False),
    }


class RedirectRule(AWSProperty):
    props = {
        'HostName': (str, False),
        'HttpRedirectCode': (str, False),
        'Protocol': (str, False),
        'ReplaceKeyPrefixWith': (str, False),
        'ReplaceKeyWith': (str, False),
    }


class RoutingRuleCondition(AWSProperty):
    props = {
        'HttpErrorCodeReturnedEquals': (str, False),
        'KeyPrefixEquals': (str, False),
    }


class RoutingRule(AWSProperty):
    props = {
        'RedirectRule': (RedirectRule, True),
        'RoutingRuleCondition': (RoutingRuleCondition, False),
    }


class WebsiteConfiguration(AWSProperty):
    props = {
        'IndexDocument': (str, False),
        'ErrorDocument': (str, False),
        'RedirectAllRequestsTo': (RedirectAllRequestsTo, False),
        'RoutingRules': ([RoutingRule], False),
    }


class LifecycleRuleTransition(AWSProperty):
    props = {
        'StorageClass': (str, True),
        'TransitionDate': (str, False),
        'TransitionInDays': (positive_integer, False),
    }


class AbortIncompleteMultipartUpload(AWSProperty):
    props = {
        'DaysAfterInitiation': (positive_integer, True),
    }


class NoncurrentVersionTransition(AWSProperty):
    props = {
        'StorageClass': (str, True),
        'TransitionInDays': (positive_integer, True),
    }


class TagFilter(AWSProperty):
    props = {
        'Key': (str, True),
        'Value': (str, True),
    }


class LifecycleRule(AWSProperty):
    props = {
        'AbortIncompleteMultipartUpload':
            (AbortIncompleteMultipartUpload, False),
        'ExpirationDate': (str, False),
        'ExpirationInDays': (positive_integer, False),
        'Id': (str, False),
        'NoncurrentVersionExpirationInDays': (positive_integer, False),
        'NoncurrentVersionTransition': (NoncurrentVersionTransition, False),
        'NoncurrentVersionTransitions': ([NoncurrentVersionTransition], False),
        'Prefix': (str, False),
        'Status': (str, True),
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
        'LogFilePrefix': (str, False),
    }


class Rules(AWSProperty):
    props = {
        'Name': (str, True),
        'Value': (str, True)
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
        'Event': (str, True),
        'Filter': (Filter, False),
        'Function': (str, True),
    }


class QueueConfigurations(AWSProperty):
    props = {
        'Event': (str, True),
        'Filter': (Filter, False),
        'Queue': (str, True),
    }


class TopicConfigurations(AWSProperty):
    props = {
        'Event': (str, True),
        'Filter': (Filter, False),
        'Topic': (str, True),
    }


class MetricsConfiguration(AWSProperty):
    props = {
        'Id': (str, True),
        'Prefix': (str, False),
        'TagFilters': ([TagFilter], False),
    }


class NotificationConfiguration(AWSProperty):
    props = {
        'LambdaConfigurations': ([LambdaConfigurations], False),
        'QueueConfigurations': ([QueueConfigurations], False),
        'TopicConfigurations': ([TopicConfigurations], False),
    }


class OwnershipControlsRule(AWSProperty):
    props = {
        'ObjectOwnership': (str, False),
    }


class OwnershipControls(AWSProperty):
    props = {
        'Rules': ([OwnershipControlsRule], True),
    }


class DeleteMarkerReplication(AWSProperty):
    props = {
        'Status': (str, False),
    }


class AccessControlTranslation(AWSProperty):
    props = {
        'Owner': (str, True),
    }


class EncryptionConfiguration(AWSProperty):
    props = {
        'ReplicaKmsKeyID': (str, True),
    }


class ReplicationTimeValue(AWSProperty):
    props = {
        'Minutes': (integer, True),
    }


class Metrics(AWSProperty):
    props = {
        'EventThreshold': (ReplicationTimeValue, False),
        'Status': (str, True),
    }


class ReplicationTime(AWSProperty):
    props = {
        'Status': (str, True),
        'Time': (ReplicationTimeValue, True),
    }


class ReplicationConfigurationRulesDestination(AWSProperty):
    props = {
        'AccessControlTranslation': (AccessControlTranslation, False),
        'Account': (str, False),
        'Bucket': (str, True),
        'EncryptionConfiguration': (EncryptionConfiguration, False),
        'Metrics': (Metrics, False),
        'ReplicationTime': (ReplicationTime, False),
        'StorageClass': (str, False),
    }


class ReplicationRuleAndOperator(AWSProperty):
    props = {
        'Prefix': (str, False),
        'TagFilters': ([TagFilter], False),
    }


class ReplicationRuleFilter(AWSProperty):
    props = {
        'And': (ReplicationRuleAndOperator, False),
        'Prefix': (str, False),
        'TagFilter': (TagFilter, False),
    }


class ReplicaModifications(AWSProperty):
    props = {
        'Status': (str, True),
    }


class SseKmsEncryptedObjects(AWSProperty):
    props = {
        'Status': (str, True),
    }


class SourceSelectionCriteria(AWSProperty):
    props = {
        'ReplicaModifications': (ReplicaModifications, False),
        'SseKmsEncryptedObjects': (SseKmsEncryptedObjects, False),
    }


class ReplicationConfigurationRules(AWSProperty):
    props = {
        'DeleteMarkerReplication': (DeleteMarkerReplication, False),
        'Destination': (ReplicationConfigurationRulesDestination, True),
        'Filter': (ReplicationRuleFilter, False),
        'Id': (str, False),
        'Prefix': (str, True),
        'Priority': (integer, False),
        'SourceSelectionCriteria': (SourceSelectionCriteria, False),
        'Status': (str, True)
    }


class ReplicationConfiguration(AWSProperty):
    props = {
        'Role': (str, True),
        'Rules': ([ReplicationConfigurationRules], True)
    }


class Destination(AWSProperty):
    props = {
        'BucketAccountId': (str, False),
        'BucketArn': (str, True),
        'Format': (str, True),
        'Prefix': (str, False),
    }


class DataExport(AWSProperty):
    props = {
        'Destination': (Destination, True),
        'OutputSchemaVersion': (str, True),
    }


class StorageClassAnalysis(AWSProperty):
    props = {
        'DataExport': (DataExport, False),
    }


class AnalyticsConfiguration(AWSProperty):
    props = {
        'Id': (str, True),
        'Prefix': (str, False),
        'StorageClassAnalysis': (StorageClassAnalysis, True),
        'TagFilters': ([TagFilter], False),
    }


class ServerSideEncryptionByDefault(AWSProperty):
    props = {
        'KMSMasterKeyID': (str, False),
        'SSEAlgorithm': (str, True),
    }


class ServerSideEncryptionRule(AWSProperty):
    props = {
        'BucketKeyEnabled': (boolean, False),
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
        'Id': (str, True),
        'IncludedObjectVersions': (str, True),
        'OptionalFields': ([str], True),
        'Prefix': (str, False),
        'ScheduleFrequency': (str, True),
    }


class DefaultRetention(AWSProperty):
    props = {
        'Days': (integer, False),
        'Mode': (str, False),
        'Years': (integer, False),
    }


class ObjectLockRule(AWSProperty):
    props = {
        'DefaultRetention': (DefaultRetention, False),
    }


class ObjectLockConfiguration(AWSProperty):
    props = {
        'ObjectLockEnabled': (str, False),
        'Rule': (ObjectLockRule, False),
    }


class Bucket(AWSObject):
    resource_type = "AWS::S3::Bucket"

    props = {
        'AccelerateConfiguration': (AccelerateConfiguration, False),
        'AccessControl': (str, False),
        'AnalyticsConfigurations': ([AnalyticsConfiguration], False),
        'BucketEncryption': (BucketEncryption, False),
        'BucketName': (s3_bucket_name, False),
        'CorsConfiguration': (CorsConfiguration, False),
        'InventoryConfigurations': ([InventoryConfiguration], False),
        'LifecycleConfiguration': (LifecycleConfiguration, False),
        'LoggingConfiguration': (LoggingConfiguration, False),
        'MetricsConfigurations': ([MetricsConfiguration], False),
        'NotificationConfiguration': (NotificationConfiguration, False),
        'ObjectLockConfiguration': (ObjectLockConfiguration, False),
        'ObjectLockEnabled': (boolean, False),
        'OwnershipControls': (OwnershipControls, False),
        'PublicAccessBlockConfiguration': (PublicAccessBlockConfiguration,
                                           False),
        'ReplicationConfiguration': (ReplicationConfiguration, False),
        'Tags': (Tags, False),
        'VersioningConfiguration': (VersioningConfiguration, False),
        'WebsiteConfiguration': (WebsiteConfiguration, False),
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
        'Bucket': (str, True),
        'PolicyDocument': (policytypes, True),
    }


class ActivityMetrics(AWSProperty):
    props = {
        'IsEnabled': (boolean, False),
    }


class SelectionCriteria(AWSProperty):
    props = {
        'Delimiter': (str, False),
        'MaxDepth': (integer, False),
        'MinStorageBytesPercentage': (double, False),
    }


class PrefixLevelStorageMetrics(AWSProperty):
    props = {
        'IsEnabled': (boolean, False),
        'SelectionCriteria': (SelectionCriteria, False),
    }


class PrefixLevel(AWSProperty):
    props = {
        'StorageMetrics': (PrefixLevelStorageMetrics, True),
    }


class BucketLevel(AWSProperty):
    props = {
        'ActivityMetrics': (ActivityMetrics, False),
        'PrefixLevel': (PrefixLevel, False),
    }


class AccountLevel(AWSProperty):
    props = {
        'ActivityMetrics': (ActivityMetrics, False),
        'BucketLevel': (BucketLevel, True),
    }


class AwsOrg(AWSProperty):
    props = {
        'Arn': (str, True),
    }


class BucketsAndRegions(AWSProperty):
    props = {
        'Buckets': ([str], False),
        'Regions': ([str], False),
    }


class StorageLensConfiguration(AWSProperty):
    props = {
        'AccountLevel': (AccountLevel, True),
        'AwsOrg': (AwsOrg, False),
        'DataExport': (DataExport, False),
        'Exclude': (BucketsAndRegions, False),
        'Id': (str, True),
        'Include': (BucketsAndRegions, False),
        'IsEnabled': (boolean, True),
        'StorageLensArn': (str, False),
    }


class StorageLens(AWSObject):
    resource_type = "AWS::S3::StorageLens"

    props = {
        'StorageLensConfiguration': (StorageLensConfiguration, True),
        'Tags': (Tags, False),
    }
