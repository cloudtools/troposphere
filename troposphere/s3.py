# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.s3 import AuthenticatedRead  # noqa: F401
from .validators.s3 import BucketOwnerFullControl  # noqa: F401
from .validators.s3 import BucketOwnerRead  # noqa: F401
from .validators.s3 import LogDeliveryWrite  # noqa: F401
from .validators.s3 import Private  # noqa: F401
from .validators.s3 import PublicRead  # noqa: F401
from .validators.s3 import PublicReadWrite  # noqa: F401
from .validators.s3 import (
    policytypes,
    s3_transfer_acceleration_status,
    validate_bucket,
    validate_lifecycle_rule,
    validate_s3_bucket_name,
)


class AccessGrantsLocationConfiguration(AWSProperty):
    """
    `AccessGrantsLocationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accessgrant-accessgrantslocationconfiguration.html>`__
    """

    props: PropsDictType = {
        "S3SubPrefix": (str, True),
    }


class Grantee(AWSProperty):
    """
    `Grantee <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accessgrant-grantee.html>`__
    """

    props: PropsDictType = {
        "GranteeIdentifier": (str, True),
        "GranteeType": (str, True),
    }


class AccessGrant(AWSObject):
    """
    `AccessGrant <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accessgrant.html>`__
    """

    resource_type = "AWS::S3::AccessGrant"

    props: PropsDictType = {
        "AccessGrantsLocationConfiguration": (AccessGrantsLocationConfiguration, False),
        "AccessGrantsLocationId": (str, True),
        "ApplicationArn": (str, False),
        "Grantee": (Grantee, True),
        "Permission": (str, True),
        "S3PrefixType": (str, False),
        "Tags": (Tags, False),
    }


class AccessGrantsInstance(AWSObject):
    """
    `AccessGrantsInstance <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accessgrantsinstance.html>`__
    """

    resource_type = "AWS::S3::AccessGrantsInstance"

    props: PropsDictType = {
        "IdentityCenterArn": (str, False),
        "Tags": (Tags, False),
    }


class AccessGrantsLocation(AWSObject):
    """
    `AccessGrantsLocation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accessgrantslocation.html>`__
    """

    resource_type = "AWS::S3::AccessGrantsLocation"

    props: PropsDictType = {
        "IamRoleArn": (str, False),
        "LocationScope": (str, False),
        "Tags": (Tags, False),
    }


class PublicAccessBlockConfiguration(AWSProperty):
    """
    `PublicAccessBlockConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-publicaccessblockconfiguration.html>`__
    """

    props: PropsDictType = {
        "BlockPublicAcls": (boolean, False),
        "BlockPublicPolicy": (boolean, False),
        "IgnorePublicAcls": (boolean, False),
        "RestrictPublicBuckets": (boolean, False),
    }


class VpcConfiguration(AWSProperty):
    """
    `VpcConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accesspoint-vpcconfiguration.html>`__
    """

    props: PropsDictType = {
        "VpcId": (str, False),
    }


class AccessPoint(AWSObject):
    """
    `AccessPoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accesspoint.html>`__
    """

    resource_type = "AWS::S3::AccessPoint"

    props: PropsDictType = {
        "Bucket": (str, True),
        "BucketAccountId": (str, False),
        "Name": (str, False),
        "Policy": (policytypes, False),
        "PublicAccessBlockConfiguration": (PublicAccessBlockConfiguration, False),
        "VpcConfiguration": (VpcConfiguration, False),
    }


class AccelerateConfiguration(AWSProperty):
    """
    `AccelerateConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-accelerateconfiguration.html>`__
    """

    props: PropsDictType = {
        "AccelerationStatus": (s3_transfer_acceleration_status, True),
    }


class Destination(AWSProperty):
    """
    `Destination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-destination.html>`__
    """

    props: PropsDictType = {
        "BucketAccountId": (str, False),
        "BucketArn": (str, True),
        "Format": (str, True),
        "Prefix": (str, False),
    }


class DataExport(AWSProperty):
    """
    `DataExport <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-dataexport.html>`__
    """

    props: PropsDictType = {
        "Destination": (Destination, True),
        "OutputSchemaVersion": (str, True),
    }


class StorageClassAnalysis(AWSProperty):
    """
    `StorageClassAnalysis <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-storageclassanalysis.html>`__
    """

    props: PropsDictType = {
        "DataExport": (DataExport, False),
    }


class TagFilter(AWSProperty):
    """
    `TagFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-tagfilter.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, True),
    }


class AnalyticsConfiguration(AWSProperty):
    """
    `AnalyticsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-analyticsconfiguration.html>`__
    """

    props: PropsDictType = {
        "Id": (str, True),
        "Prefix": (str, False),
        "StorageClassAnalysis": (StorageClassAnalysis, True),
        "TagFilters": ([TagFilter], False),
    }


class ServerSideEncryptionByDefault(AWSProperty):
    """
    `ServerSideEncryptionByDefault <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionbydefault.html>`__
    """

    props: PropsDictType = {
        "KMSMasterKeyID": (str, False),
        "SSEAlgorithm": (str, True),
    }


class ServerSideEncryptionRule(AWSProperty):
    """
    `ServerSideEncryptionRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionrule.html>`__
    """

    props: PropsDictType = {
        "BucketKeyEnabled": (boolean, False),
        "ServerSideEncryptionByDefault": (ServerSideEncryptionByDefault, False),
    }


class BucketEncryption(AWSProperty):
    """
    `BucketEncryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-bucketencryption.html>`__
    """

    props: PropsDictType = {
        "ServerSideEncryptionConfiguration": ([ServerSideEncryptionRule], True),
    }


class CorsRules(AWSProperty):
    """
    `CorsRules <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors-corsrule.html>`__
    """

    props: PropsDictType = {
        "AllowedHeaders": ([str], False),
        "AllowedMethods": ([str], True),
        "AllowedOrigins": ([str], True),
        "ExposedHeaders": ([str], False),
        "Id": (str, False),
        "MaxAge": (integer, False),
    }


class CorsConfiguration(AWSProperty):
    """
    `CorsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors.html>`__
    """

    props: PropsDictType = {
        "CorsRules": ([CorsRules], True),
    }


class Tiering(AWSProperty):
    """
    `Tiering <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-tiering.html>`__
    """

    props: PropsDictType = {
        "AccessTier": (str, True),
        "Days": (integer, True),
    }


class IntelligentTieringConfiguration(AWSProperty):
    """
    `IntelligentTieringConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-intelligenttieringconfiguration.html>`__
    """

    props: PropsDictType = {
        "Id": (str, True),
        "Prefix": (str, False),
        "Status": (str, True),
        "TagFilters": ([TagFilter], False),
        "Tierings": ([Tiering], True),
    }


class InventoryConfiguration(AWSProperty):
    """
    `InventoryConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html>`__
    """

    props: PropsDictType = {
        "Destination": (Destination, True),
        "Enabled": (boolean, True),
        "Id": (str, True),
        "IncludedObjectVersions": (str, True),
        "OptionalFields": ([str], False),
        "Prefix": (str, False),
        "ScheduleFrequency": (str, True),
    }


class AbortIncompleteMultipartUpload(AWSProperty):
    """
    `AbortIncompleteMultipartUpload <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-abortincompletemultipartupload.html>`__
    """

    props: PropsDictType = {
        "DaysAfterInitiation": (integer, True),
    }


class LifecycleRuleTransition(AWSProperty):
    """
    `LifecycleRuleTransition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-transition.html>`__
    """

    props: PropsDictType = {
        "StorageClass": (str, True),
        "TransitionDate": (str, False),
        "TransitionInDays": (integer, False),
    }


class NoncurrentVersionExpiration(AWSProperty):
    """
    `NoncurrentVersionExpiration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-noncurrentversionexpiration.html>`__
    """

    props: PropsDictType = {
        "NewerNoncurrentVersions": (integer, False),
        "NoncurrentDays": (integer, True),
    }


class NoncurrentVersionTransition(AWSProperty):
    """
    `NoncurrentVersionTransition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-noncurrentversiontransition.html>`__
    """

    props: PropsDictType = {
        "NewerNoncurrentVersions": (integer, False),
        "StorageClass": (str, True),
        "TransitionInDays": (integer, True),
    }


class LifecycleRule(AWSProperty):
    """
    `LifecycleRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html>`__
    """

    props: PropsDictType = {
        "AbortIncompleteMultipartUpload": (AbortIncompleteMultipartUpload, False),
        "ExpirationDate": (str, False),
        "ExpirationInDays": (integer, False),
        "ExpiredObjectDeleteMarker": (boolean, False),
        "Id": (str, False),
        "NoncurrentVersionExpiration": (NoncurrentVersionExpiration, False),
        "NoncurrentVersionExpirationInDays": (integer, False),
        "NoncurrentVersionTransition": (NoncurrentVersionTransition, False),
        "NoncurrentVersionTransitions": ([NoncurrentVersionTransition], False),
        "ObjectSizeGreaterThan": (integer, False),
        "ObjectSizeLessThan": (integer, False),
        "Prefix": (str, False),
        "Status": (str, True),
        "TagFilters": ([TagFilter], False),
        "Transition": (LifecycleRuleTransition, False),
        "Transitions": ([LifecycleRuleTransition], False),
    }

    def validate(self):
        validate_lifecycle_rule(self)


class LifecycleConfiguration(AWSProperty):
    """
    `LifecycleConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig.html>`__
    """

    props: PropsDictType = {
        "Rules": ([LifecycleRule], True),
    }


class LoggingConfiguration(AWSProperty):
    """
    `LoggingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-loggingconfig.html>`__
    """

    props: PropsDictType = {
        "DestinationBucketName": (validate_s3_bucket_name, False),
        "LogFilePrefix": (str, False),
    }


class MetricsConfiguration(AWSProperty):
    """
    `MetricsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-metricsconfiguration.html>`__
    """

    props: PropsDictType = {
        "AccessPointArn": (str, False),
        "Id": (str, True),
        "Prefix": (str, False),
        "TagFilters": ([TagFilter], False),
    }


class EventBridgeConfiguration(AWSProperty):
    """
    `EventBridgeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-eventbridgeconfig.html>`__
    """

    props: PropsDictType = {
        "EventBridgeEnabled": (boolean, False),
    }


class Rules(AWSProperty):
    """
    `Rules <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfiguration-config-filter-s3key-rules.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Value": (str, True),
    }


class S3Key(AWSProperty):
    """
    `S3Key <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfiguration-config-filter-s3key.html>`__
    """

    props: PropsDictType = {
        "Rules": ([Rules], True),
    }


class Filter(AWSProperty):
    """
    `Filter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfiguration-config-filter.html>`__
    """

    props: PropsDictType = {
        "S3Key": (S3Key, True),
    }


class LambdaConfigurations(AWSProperty):
    """
    `LambdaConfigurations <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-lambdaconfig.html>`__
    """

    props: PropsDictType = {
        "Event": (str, True),
        "Filter": (Filter, False),
        "Function": (str, True),
    }


class QueueConfigurations(AWSProperty):
    """
    `QueueConfigurations <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-queueconfig.html>`__
    """

    props: PropsDictType = {
        "Event": (str, True),
        "Filter": (Filter, False),
        "Queue": (str, True),
    }


class TopicConfigurations(AWSProperty):
    """
    `TopicConfigurations <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-topicconfig.html>`__
    """

    props: PropsDictType = {
        "Event": (str, True),
        "Filter": (Filter, False),
        "Topic": (str, True),
    }


class NotificationConfiguration(AWSProperty):
    """
    `NotificationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig.html>`__
    """

    props: PropsDictType = {
        "EventBridgeConfiguration": (EventBridgeConfiguration, False),
        "LambdaConfigurations": ([LambdaConfigurations], False),
        "QueueConfigurations": ([QueueConfigurations], False),
        "TopicConfigurations": ([TopicConfigurations], False),
    }


class DefaultRetention(AWSProperty):
    """
    `DefaultRetention <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-defaultretention.html>`__
    """

    props: PropsDictType = {
        "Days": (integer, False),
        "Mode": (str, False),
        "Years": (integer, False),
    }


class ObjectLockRule(AWSProperty):
    """
    `ObjectLockRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-objectlockrule.html>`__
    """

    props: PropsDictType = {
        "DefaultRetention": (DefaultRetention, False),
    }


class ObjectLockConfiguration(AWSProperty):
    """
    `ObjectLockConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-objectlockconfiguration.html>`__
    """

    props: PropsDictType = {
        "ObjectLockEnabled": (str, False),
        "Rule": (ObjectLockRule, False),
    }


class OwnershipControlsRule(AWSProperty):
    """
    `OwnershipControlsRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrolsrule.html>`__
    """

    props: PropsDictType = {
        "ObjectOwnership": (str, False),
    }


class OwnershipControls(AWSProperty):
    """
    `OwnershipControls <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrols.html>`__
    """

    props: PropsDictType = {
        "Rules": ([OwnershipControlsRule], True),
    }


class DeleteMarkerReplication(AWSProperty):
    """
    `DeleteMarkerReplication <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-deletemarkerreplication.html>`__
    """

    props: PropsDictType = {
        "Status": (str, False),
    }


class AccessControlTranslation(AWSProperty):
    """
    `AccessControlTranslation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-accesscontroltranslation.html>`__
    """

    props: PropsDictType = {
        "Owner": (str, True),
    }


class EncryptionConfiguration(AWSProperty):
    """
    `EncryptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-encryptionconfiguration.html>`__
    """

    props: PropsDictType = {
        "ReplicaKmsKeyID": (str, True),
    }


class ReplicationTimeValue(AWSProperty):
    """
    `ReplicationTimeValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationtimevalue.html>`__
    """

    props: PropsDictType = {
        "Minutes": (integer, True),
    }


class Metrics(AWSProperty):
    """
    `Metrics <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-metrics.html>`__
    """

    props: PropsDictType = {
        "EventThreshold": (ReplicationTimeValue, False),
        "Status": (str, True),
    }


class ReplicationTime(AWSProperty):
    """
    `ReplicationTime <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationtime.html>`__
    """

    props: PropsDictType = {
        "Status": (str, True),
        "Time": (ReplicationTimeValue, True),
    }


class ReplicationConfigurationRulesDestination(AWSProperty):
    """
    `ReplicationConfigurationRulesDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules-destination.html>`__
    """

    props: PropsDictType = {
        "AccessControlTranslation": (AccessControlTranslation, False),
        "Account": (str, False),
        "Bucket": (str, True),
        "EncryptionConfiguration": (EncryptionConfiguration, False),
        "Metrics": (Metrics, False),
        "ReplicationTime": (ReplicationTime, False),
        "StorageClass": (str, False),
    }


class ReplicationRuleAndOperator(AWSProperty):
    """
    `ReplicationRuleAndOperator <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationruleandoperator.html>`__
    """

    props: PropsDictType = {
        "Prefix": (str, False),
        "TagFilters": ([TagFilter], False),
    }


class ReplicationRuleFilter(AWSProperty):
    """
    `ReplicationRuleFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationrulefilter.html>`__
    """

    props: PropsDictType = {
        "And": (ReplicationRuleAndOperator, False),
        "Prefix": (str, False),
        "TagFilter": (TagFilter, False),
    }


class ReplicaModifications(AWSProperty):
    """
    `ReplicaModifications <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicamodifications.html>`__
    """

    props: PropsDictType = {
        "Status": (str, True),
    }


class SseKmsEncryptedObjects(AWSProperty):
    """
    `SseKmsEncryptedObjects <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ssekmsencryptedobjects.html>`__
    """

    props: PropsDictType = {
        "Status": (str, True),
    }


class SourceSelectionCriteria(AWSProperty):
    """
    `SourceSelectionCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-sourceselectioncriteria.html>`__
    """

    props: PropsDictType = {
        "ReplicaModifications": (ReplicaModifications, False),
        "SseKmsEncryptedObjects": (SseKmsEncryptedObjects, False),
    }


class ReplicationConfigurationRules(AWSProperty):
    """
    `ReplicationConfigurationRules <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules.html>`__
    """

    props: PropsDictType = {
        "DeleteMarkerReplication": (DeleteMarkerReplication, False),
        "Destination": (ReplicationConfigurationRulesDestination, True),
        "Filter": (ReplicationRuleFilter, False),
        "Id": (str, False),
        "Prefix": (str, False),
        "Priority": (integer, False),
        "SourceSelectionCriteria": (SourceSelectionCriteria, False),
        "Status": (str, True),
    }


class ReplicationConfiguration(AWSProperty):
    """
    `ReplicationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration.html>`__
    """

    props: PropsDictType = {
        "Role": (str, True),
        "Rules": ([ReplicationConfigurationRules], True),
    }


class VersioningConfiguration(AWSProperty):
    """
    `VersioningConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-versioningconfig.html>`__
    """

    props: PropsDictType = {
        "Status": (str, True),
    }


class RedirectAllRequestsTo(AWSProperty):
    """
    `RedirectAllRequestsTo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-redirectallrequeststo.html>`__
    """

    props: PropsDictType = {
        "HostName": (str, True),
        "Protocol": (str, False),
    }


class RedirectRule(AWSProperty):
    """
    `RedirectRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules-redirectrule.html>`__
    """

    props: PropsDictType = {
        "HostName": (str, False),
        "HttpRedirectCode": (str, False),
        "Protocol": (str, False),
        "ReplaceKeyPrefixWith": (str, False),
        "ReplaceKeyWith": (str, False),
    }


class RoutingRuleCondition(AWSProperty):
    """
    `RoutingRuleCondition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules-routingrulecondition.html>`__
    """

    props: PropsDictType = {
        "HttpErrorCodeReturnedEquals": (str, False),
        "KeyPrefixEquals": (str, False),
    }


class RoutingRule(AWSProperty):
    """
    `RoutingRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html>`__
    """

    props: PropsDictType = {
        "RedirectRule": (RedirectRule, True),
        "RoutingRuleCondition": (RoutingRuleCondition, False),
    }


class WebsiteConfiguration(AWSProperty):
    """
    `WebsiteConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration.html>`__
    """

    props: PropsDictType = {
        "ErrorDocument": (str, False),
        "IndexDocument": (str, False),
        "RedirectAllRequestsTo": (RedirectAllRequestsTo, False),
        "RoutingRules": ([RoutingRule], False),
    }


class Bucket(AWSObject):
    """
    `Bucket <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html>`__
    """

    resource_type = "AWS::S3::Bucket"

    props: PropsDictType = {
        "AccelerateConfiguration": (AccelerateConfiguration, False),
        "AccessControl": (str, False),
        "AnalyticsConfigurations": ([AnalyticsConfiguration], False),
        "BucketEncryption": (BucketEncryption, False),
        "BucketName": (validate_s3_bucket_name, False),
        "CorsConfiguration": (CorsConfiguration, False),
        "IntelligentTieringConfigurations": ([IntelligentTieringConfiguration], False),
        "InventoryConfigurations": ([InventoryConfiguration], False),
        "LifecycleConfiguration": (LifecycleConfiguration, False),
        "LoggingConfiguration": (LoggingConfiguration, False),
        "MetricsConfigurations": ([MetricsConfiguration], False),
        "NotificationConfiguration": (NotificationConfiguration, False),
        "ObjectLockConfiguration": (ObjectLockConfiguration, False),
        "ObjectLockEnabled": (boolean, False),
        "OwnershipControls": (OwnershipControls, False),
        "PublicAccessBlockConfiguration": (PublicAccessBlockConfiguration, False),
        "ReplicationConfiguration": (ReplicationConfiguration, False),
        "Tags": (Tags, False),
        "VersioningConfiguration": (VersioningConfiguration, False),
        "WebsiteConfiguration": (WebsiteConfiguration, False),
    }

    def validate(self):
        validate_bucket(self)


class BucketPolicy(AWSObject):
    """
    `BucketPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-bucketpolicy.html>`__
    """

    resource_type = "AWS::S3::BucketPolicy"

    props: PropsDictType = {
        "Bucket": (str, True),
        "PolicyDocument": (policytypes, True),
    }


class Region(AWSProperty):
    """
    `Region <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-region.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "BucketAccountId": (str, False),
    }


class MultiRegionAccessPoint(AWSObject):
    """
    `MultiRegionAccessPoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html>`__
    """

    resource_type = "AWS::S3::MultiRegionAccessPoint"

    props: PropsDictType = {
        "Name": (str, False),
        "PublicAccessBlockConfiguration": (PublicAccessBlockConfiguration, False),
        "Regions": ([Region], True),
    }


class MultiRegionAccessPointPolicy(AWSObject):
    """
    `MultiRegionAccessPointPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspointpolicy.html>`__
    """

    resource_type = "AWS::S3::MultiRegionAccessPointPolicy"

    props: PropsDictType = {
        "MrapName": (str, True),
        "Policy": (policytypes, True),
    }


class ActivityMetrics(AWSProperty):
    """
    `ActivityMetrics <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-activitymetrics.html>`__
    """

    props: PropsDictType = {
        "IsEnabled": (boolean, False),
    }


class AdvancedCostOptimizationMetrics(AWSProperty):
    """
    `AdvancedCostOptimizationMetrics <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-advancedcostoptimizationmetrics.html>`__
    """

    props: PropsDictType = {
        "IsEnabled": (boolean, False),
    }


class AdvancedDataProtectionMetrics(AWSProperty):
    """
    `AdvancedDataProtectionMetrics <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-advanceddataprotectionmetrics.html>`__
    """

    props: PropsDictType = {
        "IsEnabled": (boolean, False),
    }


class DetailedStatusCodesMetrics(AWSProperty):
    """
    `DetailedStatusCodesMetrics <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-detailedstatuscodesmetrics.html>`__
    """

    props: PropsDictType = {
        "IsEnabled": (boolean, False),
    }


class SelectionCriteria(AWSProperty):
    """
    `SelectionCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-selectioncriteria.html>`__
    """

    props: PropsDictType = {
        "Delimiter": (str, False),
        "MaxDepth": (integer, False),
        "MinStorageBytesPercentage": (double, False),
    }


class PrefixLevelStorageMetrics(AWSProperty):
    """
    `PrefixLevelStorageMetrics <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-prefixlevelstoragemetrics.html>`__
    """

    props: PropsDictType = {
        "IsEnabled": (boolean, False),
        "SelectionCriteria": (SelectionCriteria, False),
    }


class PrefixLevel(AWSProperty):
    """
    `PrefixLevel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-prefixlevel.html>`__
    """

    props: PropsDictType = {
        "StorageMetrics": (PrefixLevelStorageMetrics, True),
    }


class BucketLevel(AWSProperty):
    """
    `BucketLevel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-bucketlevel.html>`__
    """

    props: PropsDictType = {
        "ActivityMetrics": (ActivityMetrics, False),
        "AdvancedCostOptimizationMetrics": (AdvancedCostOptimizationMetrics, False),
        "AdvancedDataProtectionMetrics": (AdvancedDataProtectionMetrics, False),
        "DetailedStatusCodesMetrics": (DetailedStatusCodesMetrics, False),
        "PrefixLevel": (PrefixLevel, False),
    }


class StorageLensGroupSelectionCriteria(AWSProperty):
    """
    `StorageLensGroupSelectionCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensgroupselectioncriteria.html>`__
    """

    props: PropsDictType = {
        "Exclude": ([str], False),
        "Include": ([str], False),
    }


class StorageLensGroupLevel(AWSProperty):
    """
    `StorageLensGroupLevel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensgrouplevel.html>`__
    """

    props: PropsDictType = {
        "StorageLensGroupSelectionCriteria": (StorageLensGroupSelectionCriteria, False),
    }


class AccountLevel(AWSProperty):
    """
    `AccountLevel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-accountlevel.html>`__
    """

    props: PropsDictType = {
        "ActivityMetrics": (ActivityMetrics, False),
        "AdvancedCostOptimizationMetrics": (AdvancedCostOptimizationMetrics, False),
        "AdvancedDataProtectionMetrics": (AdvancedDataProtectionMetrics, False),
        "BucketLevel": (BucketLevel, True),
        "DetailedStatusCodesMetrics": (DetailedStatusCodesMetrics, False),
        "StorageLensGroupLevel": (StorageLensGroupLevel, False),
    }


class AwsOrg(AWSProperty):
    """
    `AwsOrg <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-awsorg.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, True),
    }


class BucketsAndRegions(AWSProperty):
    """
    `BucketsAndRegions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-bucketsandregions.html>`__
    """

    props: PropsDictType = {
        "Buckets": ([str], False),
        "Regions": ([str], False),
    }


class CloudWatchMetrics(AWSProperty):
    """
    `CloudWatchMetrics <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-cloudwatchmetrics.html>`__
    """

    props: PropsDictType = {
        "IsEnabled": (boolean, True),
    }


class SSEKMS(AWSProperty):
    """
    `SSEKMS <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-ssekms.html>`__
    """

    props: PropsDictType = {
        "KeyId": (str, True),
    }


class Encryption(AWSProperty):
    """
    `Encryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-encryption.html>`__
    """

    props: PropsDictType = {
        "SSEKMS": (SSEKMS, False),
        "SSES3": (dict, False),
    }


class S3BucketDestination(AWSProperty):
    """
    `S3BucketDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-s3bucketdestination.html>`__
    """

    props: PropsDictType = {
        "AccountId": (str, True),
        "Arn": (str, True),
        "Encryption": (Encryption, False),
        "Format": (str, True),
        "OutputSchemaVersion": (str, True),
        "Prefix": (str, False),
    }


class StorageLensDataExport(AWSProperty):
    """
    `StorageLensDataExport <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-dataexport.html>`__
    """

    props: PropsDictType = {
        "CloudWatchMetrics": (CloudWatchMetrics, False),
        "S3BucketDestination": (S3BucketDestination, False),
    }


class StorageLensConfiguration(AWSProperty):
    """
    `StorageLensConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensconfiguration.html>`__
    """

    props: PropsDictType = {
        "AccountLevel": (AccountLevel, True),
        "AwsOrg": (AwsOrg, False),
        "DataExport": (StorageLensDataExport, False),
        "Exclude": (BucketsAndRegions, False),
        "Id": (str, True),
        "Include": (BucketsAndRegions, False),
        "IsEnabled": (boolean, True),
        "StorageLensArn": (str, False),
    }


class StorageLens(AWSObject):
    """
    `StorageLens <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-storagelens.html>`__
    """

    resource_type = "AWS::S3::StorageLens"

    props: PropsDictType = {
        "StorageLensConfiguration": (StorageLensConfiguration, True),
        "Tags": (Tags, False),
    }


class MatchObjectAge(AWSProperty):
    """
    `MatchObjectAge <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelensgroup-matchobjectage.html>`__
    """

    props: PropsDictType = {
        "DaysGreaterThan": (integer, False),
        "DaysLessThan": (integer, False),
    }


class MatchObjectSize(AWSProperty):
    """
    `MatchObjectSize <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelensgroup-matchobjectsize.html>`__
    """

    props: PropsDictType = {
        "BytesGreaterThan": (integer, False),
        "BytesLessThan": (integer, False),
    }


class And(AWSProperty):
    """
    `And <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelensgroup-and.html>`__
    """

    props: PropsDictType = {
        "MatchAnyPrefix": ([str], False),
        "MatchAnySuffix": ([str], False),
        "MatchAnyTag": (Tags, False),
        "MatchObjectAge": (MatchObjectAge, False),
        "MatchObjectSize": (MatchObjectSize, False),
    }


class Or(AWSProperty):
    """
    `Or <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelensgroup-or.html>`__
    """

    props: PropsDictType = {
        "MatchAnyPrefix": ([str], False),
        "MatchAnySuffix": ([str], False),
        "MatchAnyTag": (Tags, False),
        "MatchObjectAge": (MatchObjectAge, False),
        "MatchObjectSize": (MatchObjectSize, False),
    }


class StorageLensFilter(AWSProperty):
    """
    `StorageLensFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelensgroup-filter.html>`__
    """

    props: PropsDictType = {
        "And": (And, False),
        "MatchAnyPrefix": ([str], False),
        "MatchAnySuffix": ([str], False),
        "MatchAnyTag": (Tags, False),
        "MatchObjectAge": (MatchObjectAge, False),
        "MatchObjectSize": (MatchObjectSize, False),
        "Or": (Or, False),
    }


class StorageLensGroup(AWSObject):
    """
    `StorageLensGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-storagelensgroup.html>`__
    """

    resource_type = "AWS::S3::StorageLensGroup"

    props: PropsDictType = {
        "Filter": (StorageLensFilter, True),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class PolicyStatus(AWSProperty):
    """
    `PolicyStatus <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspointpolicy-policystatus.html>`__
    """

    props: PropsDictType = {
        "IsPublic": (str, True),
    }
