# Copyright (c) 2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import (integer, boolean, component_platforms,
                         imagepipeline_status,
                         schedule_pipelineexecutionstartcondition,
                         ebsinstanceblockdevicespecification_volume_type)


class Component(AWSObject):
    resource_type = "AWS::ImageBuilder::Component"

    props = {
        'ChangeDescription': (basestring, False),
        'Data': (basestring, False),
        'Description': (basestring, False),
        'KmsKeyId': (basestring, False),
        'Name': (basestring, True),
        'Platform': (component_platforms, True),
        'Tags': (dict, False),
        'Uri': (basestring, False),
        'Version': (basestring, True),
    }


class ComponentConfiguration(AWSProperty):
    props = {
        'ComponentArn': (basestring, False),
    }


class TargetContainerRepository(AWSProperty):
    props = {
        'RepositoryName': (basestring, False),
        'Service': (basestring, False),
    }


class ContainerRecipe(AWSObject):
    resource_type = "AWS::ImageBuilder::ContainerRecipe"

    props = {
        'Components': ([ComponentConfiguration], True),
        'ContainerType': (basestring, True),
        'Description': (basestring, False),
        'DockerfileTemplateData': (basestring, False),
        'DockerfileTemplateUri': (basestring, False),
        'ImageOsVersionOverride': (basestring, False),
        'KmsKeyId': (basestring, False),
        'Name': (basestring, True),
        'ParentImage': (basestring, True),
        'PlatformOverride': (basestring, False),
        'Tags': (Tags, False),
        'TargetRepository': (TargetContainerRepository, True),
        'Version': (basestring, True),
        'WorkingDirectory': (basestring, False),
    }


class Distribution(AWSProperty):
    props = {
        'AmiDistributionConfiguration': (dict, False),
        'LicenseConfigurationArns': ([basestring], False),
        'Region': (basestring, False),
    }


class DistributionConfiguration(AWSObject):
    resource_type = "AWS::ImageBuilder::DistributionConfiguration"

    props = {
        'Description': (basestring, False),
        'Distributions': ([Distribution], True),
        'Name': (basestring, True),
        'Tags': (dict, False),
    }


class ImageTestsConfiguration(AWSProperty):
    props = {
        'ImageTestsEnabled': (boolean, False),
        'TimeoutMinutes': (integer, False),
    }


class Image(AWSObject):
    resource_type = "AWS::ImageBuilder::Image"

    props = {
        'DistributionConfigurationArn': (basestring, False),
        'ImageRecipeArn': (basestring, True),
        'ImageTestsConfiguration': (ImageTestsConfiguration, True),
        'InfrastructureConfigurationArn': (basestring, True),
        'Tags': (dict, False),
    }


class S3Logs(AWSProperty):
    props = {
        "S3BucketName": (basestring, False),
        "S3KeyPrefix": (basestring, False),
    }


class Logging(AWSProperty):
    props = {
        'S3Logs': (S3Logs, False),
    }


class InfrastructureConfiguration(AWSObject):
    resource_type = "AWS::ImageBuilder::InfrastructureConfiguration"

    props = {
        'Description': (basestring, False),
        'InstanceProfileName': (basestring, True),
        'InstanceTypes': ([basestring], False),
        'KeyPair': (basestring, False),
        'Logging': (Logging, False),
        'Name': (basestring, True),
        'SecurityGroupIds': ([basestring], False),
        'SnsTopicArn': (basestring, False),
        'SubnetId': (basestring, False),
        'Tags': (dict, False),
        'TerminateInstanceOnFailure': (boolean, False)
    }


class EbsInstanceBlockDeviceSpecification(AWSProperty):
    props = {
        'DeleteOnTermination': (boolean, False),
        'Encrypted': (boolean, False),
        'Iops': (integer, False),
        'KmsKeyId': (basestring, False),
        'SnapshotId': (basestring, False),
        'VolumeSize': (integer, False),
        'VolumeType': (ebsinstanceblockdevicespecification_volume_type, False),
    }


class InstanceBlockDeviceMapping(AWSProperty):
    props = {
        'DeviceName': (basestring, False),
        'Ebs': (EbsInstanceBlockDeviceSpecification, False),
        'NoDevice': (basestring, False),
        'VirtualName': (basestring, False),
    }


class ComponentConfiguration(AWSProperty):
    props = {
        'ComponentArn': (basestring, False),
    }


class ImageRecipe(AWSObject):
    resource_type = "AWS::ImageBuilder::ImageRecipe"

    props = {
        'BlockDeviceMappings': ([InstanceBlockDeviceMapping], False),
        'Components': ([ComponentConfiguration], True),
        'Description': (basestring, False),
        'Name': (basestring, True),
        'ParentImage': (basestring, True),
        'Tags': (dict, False),
        'Version': (basestring, True)
    }


class Schedule(AWSProperty):
    props = {
        'PipelineExecutionStartCondition': (schedule_pipelineexecutionstartcondition, False),  # NOQA
        'ScheduleExpression': (basestring, False),
    }


class ImagePipeline(AWSObject):
    resource_type = "AWS::ImageBuilder::ImagePipeline"

    props = {
        'Description': (basestring, False),
        'DistributionConfigurationArn': (basestring, False),
        'ImageRecipeArn': (basestring, True),
        'ImageTestsConfiguration': (ImageTestsConfiguration, False),
        'InfrastructureConfigurationArn': (basestring, True),
        'Name': (basestring, True),
        'Schedule': (Schedule, False),
        'Status': (imagepipeline_status, False),
        'Tags': (dict, False),
    }
