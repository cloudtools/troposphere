# Copyright (c) 2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import (integer, boolean, canary_runtime_version)


class VPCConfig(AWSProperty):
    props = {
        'SecurityGroupIds': ([str], True),
        'SubnetIds': ([str], True),
        'VpcId': (str, False),
    }


class Schedule(AWSProperty):
    props = {
        'DurationInSeconds': (str, False),
        'Expression': (str, True),
    }


class RunConfig(AWSProperty):
    props = {
        'MemoryInMB': (integer, False),
        'TimeoutInSeconds': (integer, True),
    }


class Code(AWSProperty):
    props = {
        'Handler': (str, False),
        'S3Bucket': (str, False),
        'S3Key': (str, False),
        'S3ObjectVersion': (str, False),
        'Script': (str, False),
    }


class Canary(AWSObject):
    resource_type = "AWS::Synthetics::Canary"

    props = {
        'ArtifactS3Location': (str, True),
        'Code': (Code, True),
        'ExecutionRoleArn': (str, True),
        'FailureRetentionPeriod': (integer, False),
        'Name': (str, True),
        'RunConfig': (RunConfig, False),
        'RuntimeVersion': (canary_runtime_version, True),
        'Schedule': (Schedule, True),
        'StartCanaryAfterCreation': (boolean, True),
        'SuccessRetentionPeriod': (integer, False),
        'Tags': (Tags, False),
        'VPCConfig': (VPCConfig, False),
    }
