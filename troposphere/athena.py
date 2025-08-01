# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.athena import validate_encryptionoption, validate_workgroup_state


class CapacityAssignment(AWSProperty):
    """
    `CapacityAssignment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-capacityreservation-capacityassignment.html>`__
    """

    props: PropsDictType = {
        "WorkgroupNames": ([str], True),
    }


class CapacityAssignmentConfiguration(AWSProperty):
    """
    `CapacityAssignmentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-capacityreservation-capacityassignmentconfiguration.html>`__
    """

    props: PropsDictType = {
        "CapacityAssignments": ([CapacityAssignment], True),
    }


class CapacityReservation(AWSObject):
    """
    `CapacityReservation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-capacityreservation.html>`__
    """

    resource_type = "AWS::Athena::CapacityReservation"

    props: PropsDictType = {
        "CapacityAssignmentConfiguration": (CapacityAssignmentConfiguration, False),
        "Name": (str, True),
        "Tags": (Tags, False),
        "TargetDpus": (integer, True),
    }


class DataCatalog(AWSObject):
    """
    `DataCatalog <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html>`__
    """

    resource_type = "AWS::Athena::DataCatalog"

    props: PropsDictType = {
        "ConnectionType": (str, False),
        "Description": (str, False),
        "Error": (str, False),
        "Name": (str, True),
        "Parameters": (dict, False),
        "Status": (str, False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }


class NamedQuery(AWSObject):
    """
    `NamedQuery <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html>`__
    """

    resource_type = "AWS::Athena::NamedQuery"

    props: PropsDictType = {
        "Database": (str, True),
        "Description": (str, False),
        "Name": (str, False),
        "QueryString": (str, True),
        "WorkGroup": (str, False),
    }


class PreparedStatement(AWSObject):
    """
    `PreparedStatement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html>`__
    """

    resource_type = "AWS::Athena::PreparedStatement"

    props: PropsDictType = {
        "Description": (str, False),
        "QueryStatement": (str, True),
        "StatementName": (str, True),
        "WorkGroup": (str, True),
    }


class CustomerContentEncryptionConfiguration(AWSProperty):
    """
    `CustomerContentEncryptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-customercontentencryptionconfiguration.html>`__
    """

    props: PropsDictType = {
        "KmsKey": (str, True),
    }


class EngineVersion(AWSProperty):
    """
    `EngineVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html>`__
    """

    props: PropsDictType = {
        "EffectiveEngineVersion": (str, False),
        "SelectedEngineVersion": (str, False),
    }


class ManagedStorageEncryptionConfiguration(AWSProperty):
    """
    `ManagedStorageEncryptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-managedstorageencryptionconfiguration.html>`__
    """

    props: PropsDictType = {
        "KmsKey": (str, False),
    }


class ManagedQueryResultsConfiguration(AWSProperty):
    """
    `ManagedQueryResultsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-managedqueryresultsconfiguration.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "EncryptionConfiguration": (ManagedStorageEncryptionConfiguration, False),
    }


class AclConfiguration(AWSProperty):
    """
    `AclConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-aclconfiguration.html>`__
    """

    props: PropsDictType = {
        "S3AclOption": (str, True),
    }


class EncryptionConfiguration(AWSProperty):
    """
    `EncryptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html>`__
    """

    props: PropsDictType = {
        "EncryptionOption": (validate_encryptionoption, True),
        "KmsKey": (str, False),
    }


class ResultConfiguration(AWSProperty):
    """
    `ResultConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html>`__
    """

    props: PropsDictType = {
        "AclConfiguration": (AclConfiguration, False),
        "EncryptionConfiguration": (EncryptionConfiguration, False),
        "ExpectedBucketOwner": (str, False),
        "OutputLocation": (str, False),
    }


class WorkGroupConfiguration(AWSProperty):
    """
    `WorkGroupConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html>`__
    """

    props: PropsDictType = {
        "AdditionalConfiguration": (str, False),
        "BytesScannedCutoffPerQuery": (integer, False),
        "CustomerContentEncryptionConfiguration": (
            CustomerContentEncryptionConfiguration,
            False,
        ),
        "EnforceWorkGroupConfiguration": (boolean, False),
        "EngineVersion": (EngineVersion, False),
        "ExecutionRole": (str, False),
        "ManagedQueryResultsConfiguration": (ManagedQueryResultsConfiguration, False),
        "PublishCloudWatchMetricsEnabled": (boolean, False),
        "RequesterPaysEnabled": (boolean, False),
        "ResultConfiguration": (ResultConfiguration, False),
    }


class WorkGroup(AWSObject):
    """
    `WorkGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html>`__
    """

    resource_type = "AWS::Athena::WorkGroup"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "RecursiveDeleteOption": (boolean, False),
        "State": (validate_workgroup_state, False),
        "Tags": (Tags, False),
        "WorkGroupConfiguration": (WorkGroupConfiguration, False),
    }
