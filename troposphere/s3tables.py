# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import integer


class EncryptionConfiguration(AWSProperty):
    """
    `EncryptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-tablebucket-encryptionconfiguration.html>`__
    """

    props: PropsDictType = {
        "KMSKeyArn": (str, False),
        "SSEAlgorithm": (str, False),
    }


class UnreferencedFileRemoval(AWSProperty):
    """
    `UnreferencedFileRemoval <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-tablebucket-unreferencedfileremoval.html>`__
    """

    props: PropsDictType = {
        "NoncurrentDays": (integer, False),
        "Status": (str, False),
        "UnreferencedDays": (integer, False),
    }


class TableBucket(AWSObject):
    """
    `TableBucket <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucket.html>`__
    """

    resource_type = "AWS::S3Tables::TableBucket"

    props: PropsDictType = {
        "EncryptionConfiguration": (EncryptionConfiguration, False),
        "TableBucketName": (str, True),
        "UnreferencedFileRemoval": (UnreferencedFileRemoval, False),
    }


class TableBucketPolicy(AWSObject):
    """
    `TableBucketPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucketpolicy.html>`__
    """

    resource_type = "AWS::S3Tables::TableBucketPolicy"

    props: PropsDictType = {
        "ResourcePolicy": (dict, True),
        "TableBucketARN": (str, True),
    }
