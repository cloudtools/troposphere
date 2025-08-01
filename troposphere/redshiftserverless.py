# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class SnapshotCopyConfiguration(AWSProperty):
    """
    `SnapshotCopyConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-snapshotcopyconfiguration.html>`__
    """

    props: PropsDictType = {
        "DestinationKmsKeyId": (str, False),
        "DestinationRegion": (str, True),
        "SnapshotRetentionPeriod": (integer, False),
    }


class Namespace(AWSObject):
    """
    `Namespace <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html>`__
    """

    resource_type = "AWS::RedshiftServerless::Namespace"

    props: PropsDictType = {
        "AdminPasswordSecretKmsKeyId": (str, False),
        "AdminUserPassword": (str, False),
        "AdminUsername": (str, False),
        "DbName": (str, False),
        "DefaultIamRoleArn": (str, False),
        "FinalSnapshotName": (str, False),
        "FinalSnapshotRetentionPeriod": (integer, False),
        "IamRoles": ([str], False),
        "KmsKeyId": (str, False),
        "LogExports": ([str], False),
        "ManageAdminPassword": (boolean, False),
        "NamespaceName": (str, True),
        "NamespaceResourcePolicy": (dict, False),
        "RedshiftIdcApplicationArn": (str, False),
        "SnapshotCopyConfigurations": ([SnapshotCopyConfiguration], False),
        "Tags": (Tags, False),
    }


class Snapshot(AWSObject):
    """
    `Snapshot <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-snapshot.html>`__
    """

    resource_type = "AWS::RedshiftServerless::Snapshot"

    props: PropsDictType = {
        "NamespaceName": (str, False),
        "RetentionPeriod": (integer, False),
        "SnapshotName": (str, True),
        "Tags": (Tags, False),
    }


class ConfigParameter(AWSProperty):
    """
    `ConfigParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html>`__
    """

    props: PropsDictType = {
        "ParameterKey": (str, False),
        "ParameterValue": (str, False),
    }


class PerformanceTarget(AWSProperty):
    """
    `PerformanceTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-performancetarget.html>`__
    """

    props: PropsDictType = {
        "Level": (integer, False),
        "Status": (str, False),
    }


class NetworkInterface(AWSProperty):
    """
    `NetworkInterface <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html>`__
    """

    props: PropsDictType = {
        "AvailabilityZone": (str, False),
        "NetworkInterfaceId": (str, False),
        "PrivateIpAddress": (str, False),
        "SubnetId": (str, False),
    }


class VpcEndpoint(AWSProperty):
    """
    `VpcEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-vpcendpoint.html>`__
    """

    props: PropsDictType = {
        "NetworkInterfaces": ([NetworkInterface], False),
        "VpcEndpointId": (str, False),
        "VpcId": (str, False),
    }


class Endpoint(AWSProperty):
    """
    `Endpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-endpoint.html>`__
    """

    props: PropsDictType = {
        "Address": (str, False),
        "Port": (integer, False),
        "VpcEndpoints": ([VpcEndpoint], False),
    }


class WorkgroupProperty(AWSProperty):
    """
    `WorkgroupProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html>`__
    """

    props: PropsDictType = {
        "BaseCapacity": (integer, False),
        "ConfigParameters": ([ConfigParameter], False),
        "CreationDate": (str, False),
        "Endpoint": (Endpoint, False),
        "EnhancedVpcRouting": (boolean, False),
        "MaxCapacity": (integer, False),
        "NamespaceName": (str, False),
        "PricePerformanceTarget": (PerformanceTarget, False),
        "PubliclyAccessible": (boolean, False),
        "SecurityGroupIds": ([str], False),
        "Status": (str, False),
        "SubnetIds": ([str], False),
        "TrackName": (str, False),
        "WorkgroupArn": (str, False),
        "WorkgroupId": (str, False),
        "WorkgroupName": (str, False),
    }


class Workgroup(AWSObject):
    """
    `Workgroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html>`__
    """

    resource_type = "AWS::RedshiftServerless::Workgroup"

    props: PropsDictType = {
        "BaseCapacity": (integer, False),
        "ConfigParameters": ([ConfigParameter], False),
        "EnhancedVpcRouting": (boolean, False),
        "MaxCapacity": (integer, False),
        "NamespaceName": (str, False),
        "Port": (integer, False),
        "PricePerformanceTarget": (PerformanceTarget, False),
        "PubliclyAccessible": (boolean, False),
        "RecoveryPointId": (str, False),
        "SecurityGroupIds": ([str], False),
        "SnapshotArn": (str, False),
        "SnapshotName": (str, False),
        "SnapshotOwnerAccount": (str, False),
        "SubnetIds": ([str], False),
        "Tags": (Tags, False),
        "TrackName": (str, False),
        "Workgroup": (WorkgroupProperty, False),
        "WorkgroupName": (str, True),
    }


class NamespaceProperty(AWSProperty):
    """
    `NamespaceProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html>`__
    """

    props: PropsDictType = {
        "AdminPasswordSecretArn": (str, False),
        "AdminPasswordSecretKmsKeyId": (str, False),
        "AdminUsername": (str, False),
        "CreationDate": (str, False),
        "DbName": (str, False),
        "DefaultIamRoleArn": (str, False),
        "IamRoles": ([str], False),
        "KmsKeyId": (str, False),
        "LogExports": ([str], False),
        "NamespaceArn": (str, False),
        "NamespaceId": (str, False),
        "NamespaceName": (str, False),
        "Status": (str, False),
    }


class SnapshotProperty(AWSProperty):
    """
    `SnapshotProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-snapshot-snapshot.html>`__
    """

    props: PropsDictType = {
        "AdminUsername": (str, False),
        "KmsKeyId": (str, False),
        "NamespaceArn": (str, False),
        "NamespaceName": (str, False),
        "OwnerAccount": (str, False),
        "RetentionPeriod": (integer, False),
        "SnapshotArn": (str, False),
        "SnapshotCreateTime": (str, False),
        "SnapshotName": (str, False),
        "Status": (str, False),
    }
