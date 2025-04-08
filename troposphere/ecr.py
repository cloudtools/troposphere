# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean
from .validators.ecr import policytypes


class RepositoryCatalogData(AWSProperty):
    """
    `RepositoryCatalogData <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-publicrepository-repositorycatalogdata.html>`__
    """

    props: PropsDictType = {
        "AboutText": (str, False),
        "Architectures": ([str], False),
        "OperatingSystems": ([str], False),
        "RepositoryDescription": (str, False),
        "UsageText": (str, False),
    }


class PublicRepository(AWSObject):
    """
    `PublicRepository <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-publicrepository.html>`__
    """

    resource_type = "AWS::ECR::PublicRepository"

    props: PropsDictType = {
        "RepositoryCatalogData": (RepositoryCatalogData, False),
        "RepositoryName": (str, False),
        "RepositoryPolicyText": (policytypes, False),
        "Tags": (Tags, False),
    }


class PullThroughCacheRule(AWSObject):
    """
    `PullThroughCacheRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-pullthroughcacherule.html>`__
    """

    resource_type = "AWS::ECR::PullThroughCacheRule"

    props: PropsDictType = {
        "CredentialArn": (str, False),
        "CustomRoleArn": (str, False),
        "EcrRepositoryPrefix": (str, False),
        "UpstreamRegistry": (str, False),
        "UpstreamRegistryUrl": (str, False),
        "UpstreamRepositoryPrefix": (str, False),
    }


class RegistryPolicy(AWSObject):
    """
    `RegistryPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-registrypolicy.html>`__
    """

    resource_type = "AWS::ECR::RegistryPolicy"

    props: PropsDictType = {
        "PolicyText": (policytypes, True),
    }


class ReplicationDestination(AWSProperty):
    """
    `ReplicationDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationdestination.html>`__
    """

    props: PropsDictType = {
        "Region": (str, True),
        "RegistryId": (str, True),
    }


class RepositoryFilter(AWSProperty):
    """
    `RepositoryFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-repositoryfilter.html>`__
    """

    props: PropsDictType = {
        "Filter": (str, True),
        "FilterType": (str, True),
    }


class ReplicationRule(AWSProperty):
    """
    `ReplicationRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationrule.html>`__
    """

    props: PropsDictType = {
        "Destinations": ([ReplicationDestination], True),
        "RepositoryFilters": ([RepositoryFilter], False),
    }


class ReplicationConfigurationProperty(AWSProperty):
    """
    `ReplicationConfigurationProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationconfiguration.html>`__
    """

    props: PropsDictType = {
        "Rules": ([ReplicationRule], True),
    }


class ReplicationConfiguration(AWSObject):
    """
    `ReplicationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-replicationconfiguration.html>`__
    """

    resource_type = "AWS::ECR::ReplicationConfiguration"

    props: PropsDictType = {
        "ReplicationConfiguration": (ReplicationConfigurationProperty, True),
    }


class EncryptionConfiguration(AWSProperty):
    """
    `EncryptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repositorycreationtemplate-encryptionconfiguration.html>`__
    """

    props: PropsDictType = {
        "EncryptionType": (str, True),
        "KmsKey": (str, False),
    }


class ImageScanningConfiguration(AWSProperty):
    """
    `ImageScanningConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-imagescanningconfiguration.html>`__
    """

    props: PropsDictType = {
        "ScanOnPush": (boolean, False),
    }


class LifecyclePolicy(AWSProperty):
    """
    `LifecyclePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html>`__
    """

    props: PropsDictType = {
        "LifecyclePolicyText": (str, False),
        "RegistryId": (str, False),
    }


class Repository(AWSObject):
    """
    `Repository <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html>`__
    """

    resource_type = "AWS::ECR::Repository"

    props: PropsDictType = {
        "EmptyOnDelete": (boolean, False),
        "EncryptionConfiguration": (EncryptionConfiguration, False),
        "ImageScanningConfiguration": (ImageScanningConfiguration, False),
        "ImageTagMutability": (str, False),
        "LifecyclePolicy": (LifecyclePolicy, False),
        "RepositoryName": (str, False),
        "RepositoryPolicyText": (policytypes, False),
        "Tags": (Tags, False),
    }


class RepositoryCreationTemplate(AWSObject):
    """
    `RepositoryCreationTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repositorycreationtemplate.html>`__
    """

    resource_type = "AWS::ECR::RepositoryCreationTemplate"

    props: PropsDictType = {
        "AppliedFor": ([str], True),
        "CustomRoleArn": (str, False),
        "Description": (str, False),
        "EncryptionConfiguration": (EncryptionConfiguration, False),
        "ImageTagMutability": (str, False),
        "LifecyclePolicy": (str, False),
        "Prefix": (str, True),
        "RepositoryPolicy": (str, False),
        "ResourceTags": (Tags, False),
    }
