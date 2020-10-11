# Copyright (c) 2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import (integer, boolean, canary_runtime_version)


class VPCConfig(AWSProperty):
    props = {
        'SecurityGroupIds': ([basestring], True),
        'SubnetIds': ([basestring], True),
        'VpcId': (basestring, False),
    }


class Schedule(AWSProperty):
    props = {
        'DurationInSeconds': (basestring, False),
        'Expression': (basestring, True),
    }


class RunConfig(AWSProperty):
    props = {
        'MemoryInMB': (integer, False),
        'TimeoutInSeconds': (integer, True),
    }


class Code(AWSProperty):
    props = {
        'Handler': (basestring, False),
        'S3Bucket': (basestring, False),
        'S3Key': (basestring, False),
        'S3ObjectVersion': (basestring, False),
        'Script': (basestring, False),
    }


class Canary(AWSObject):
    resource_type = "AWS::Synthetics::Canary"

    props = {
        'ArtifactS3Location': (basestring, True),
        'Code': (Code, True),
        'ExecutionRoleArn': (basestring, True),
        'FailureRetentionPeriod': (integer, False),
        'Name': (basestring, True),
        'RunConfig': (RunConfig, False),
        'RuntimeVersion': (canary_runtime_version, True),
        'Schedule': (Schedule, True),
        'StartCanaryAfterCreation': (boolean, True),
        'SuccessRetentionPeriod': (integer, False),
        'Tags': (Tags, False),
        'VPCConfig': (VPCConfig, False),
    }
