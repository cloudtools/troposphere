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
        'ChangeDescription': (str, False),
        'Data': (str, False),
        'Description': (str, False),
        'KmsKeyId': (str, False),
        'Name': (str, True),
        'Platform': (component_platforms, True),
        'Tags': (dict, False),
        'Uri': (str, False),
        'Version': (str, True),
    }


class ComponentConfiguration(AWSProperty):
    props = {
        'ComponentArn': (str, False),
    }


class TargetContainerRepository(AWSProperty):
    props = {
        'RepositoryName': (str, False),
        'Service': (str, False),
    }


class ContainerRecipe(AWSObject):
    resource_type = "AWS::ImageBuilder::ContainerRecipe"

    props = {
        'Components': ([ComponentConfiguration], True),
        'ContainerType': (str, True),
        'Description': (str, False),
        'DockerfileTemplateData': (str, False),
        'DockerfileTemplateUri': (str, False),
        'ImageOsVersionOverride': (str, False),
        'KmsKeyId': (str, False),
        'Name': (str, True),
        'ParentImage': (str, True),
        'PlatformOverride': (str, False),
        'Tags': (Tags, False),
        'TargetRepository': (TargetContainerRepository, True),
        'Version': (str, True),
        'WorkingDirectory': (str, False),
    }


class Distribution(AWSProperty):
    props = {
        'AmiDistributionConfiguration': (dict, False),
        'LicenseConfigurationArns': ([str], False),
        'Region': (str, False),
    }


class DistributionConfiguration(AWSObject):
    resource_type = "AWS::ImageBuilder::DistributionConfiguration"

    props = {
        'Description': (str, False),
        'Distributions': ([Distribution], True),
        'Name': (str, True),
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
        'DistributionConfigurationArn': (str, False),
        'ImageRecipeArn': (str, True),
        'ImageTestsConfiguration': (ImageTestsConfiguration, True),
        'InfrastructureConfigurationArn': (str, True),
        'Tags': (dict, False),
    }


class S3Logs(AWSProperty):
    props = {
        "S3BucketName": (str, False),
        "S3KeyPrefix": (str, False),
    }


class Logging(AWSProperty):
    props = {
        'S3Logs': (S3Logs, False),
    }


class InfrastructureConfiguration(AWSObject):
    resource_type = "AWS::ImageBuilder::InfrastructureConfiguration"

    props = {
        'Description': (str, False),
        'InstanceProfileName': (str, True),
        'InstanceTypes': ([str], False),
        'KeyPair': (str, False),
        'Logging': (Logging, False),
        'Name': (str, True),
        'SecurityGroupIds': ([str], False),
        'SnsTopicArn': (str, False),
        'SubnetId': (str, False),
        'Tags': (dict, False),
        'TerminateInstanceOnFailure': (boolean, False)
    }


class EbsInstanceBlockDeviceSpecification(AWSProperty):
    props = {
        'DeleteOnTermination': (boolean, False),
        'Encrypted': (boolean, False),
        'Iops': (integer, False),
        'KmsKeyId': (str, False),
        'SnapshotId': (str, False),
        'VolumeSize': (integer, False),
        'VolumeType': (ebsinstanceblockdevicespecification_volume_type, False),
    }


class InstanceBlockDeviceMapping(AWSProperty):
    props = {
        'DeviceName': (str, False),
        'Ebs': (EbsInstanceBlockDeviceSpecification, False),
        'NoDevice': (str, False),
        'VirtualName': (str, False),
    }


class ComponentConfiguration(AWSProperty):
    props = {
        'ComponentArn': (str, False),
    }


class ImageRecipe(AWSObject):
    resource_type = "AWS::ImageBuilder::ImageRecipe"

    props = {
        'BlockDeviceMappings': ([InstanceBlockDeviceMapping], False),
        'Components': ([ComponentConfiguration], True),
        'Description': (str, False),
        'Name': (str, True),
        'ParentImage': (str, True),
        'Tags': (dict, False),
        'Version': (str, True)
    }


class Schedule(AWSProperty):
    props = {
        'PipelineExecutionStartCondition': (schedule_pipelineexecutionstartcondition, False),  # NOQA
        'ScheduleExpression': (str, False),
    }


class ImagePipeline(AWSObject):
    resource_type = "AWS::ImageBuilder::ImagePipeline"

    props = {
        'Description': (str, False),
        'DistributionConfigurationArn': (str, False),
        'ImageRecipeArn': (str, True),
        'ImageTestsConfiguration': (ImageTestsConfiguration, False),
        'InfrastructureConfigurationArn': (str, True),
        'Name': (str, True),
        'Schedule': (Schedule, False),
        'Status': (imagepipeline_status, False),
        'Tags': (dict, False),
    }
