# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import double, integer


class ConditionBasedCollectionScheme(AWSProperty):
    """
    `ConditionBasedCollectionScheme <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html>`__
    """

    props: PropsDictType = {
        "ConditionLanguageVersion": (integer, False),
        "Expression": (str, True),
        "MinimumTriggerIntervalMs": (double, False),
        "TriggerMode": (str, False),
    }


class TimeBasedCollectionScheme(AWSProperty):
    """
    `TimeBasedCollectionScheme <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timebasedcollectionscheme.html>`__
    """

    props: PropsDictType = {
        "PeriodMs": (double, True),
    }


class CollectionScheme(AWSProperty):
    """
    `CollectionScheme <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-collectionscheme.html>`__
    """

    props: PropsDictType = {
        "ConditionBasedCollectionScheme": (ConditionBasedCollectionScheme, False),
        "TimeBasedCollectionScheme": (TimeBasedCollectionScheme, False),
    }


class SignalInformation(AWSProperty):
    """
    `SignalInformation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html>`__
    """

    props: PropsDictType = {
        "MaxSampleCount": (double, False),
        "MinimumSamplingIntervalMs": (double, False),
        "Name": (str, True),
    }


class Campaign(AWSObject):
    """
    `Campaign <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html>`__
    """

    resource_type = "AWS::IoTFleetWise::Campaign"

    props: PropsDictType = {
        "Action": (str, True),
        "CollectionScheme": (CollectionScheme, True),
        "Compression": (str, False),
        "DataExtraDimensions": ([str], False),
        "Description": (str, False),
        "DiagnosticsMode": (str, False),
        "ExpiryTime": (str, False),
        "Name": (str, True),
        "PostTriggerCollectionDuration": (double, False),
        "Priority": (integer, False),
        "SignalCatalogArn": (str, True),
        "SignalsToCollect": ([SignalInformation], False),
        "SpoolingMode": (str, False),
        "StartTime": (str, False),
        "Tags": (Tags, False),
        "TargetArn": (str, True),
    }


class CanInterface(AWSProperty):
    """
    `CanInterface <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "ProtocolName": (str, False),
        "ProtocolVersion": (str, False),
    }


class ObdInterface(AWSProperty):
    """
    `ObdInterface <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html>`__
    """

    props: PropsDictType = {
        "DtcRequestIntervalSeconds": (str, False),
        "HasTransmissionEcu": (str, False),
        "Name": (str, True),
        "ObdStandard": (str, False),
        "PidRequestIntervalSeconds": (str, False),
        "RequestMessageId": (str, True),
        "UseExtendedIds": (str, False),
    }


class NetworkInterfacesItems(AWSProperty):
    """
    `NetworkInterfacesItems <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html>`__
    """

    props: PropsDictType = {
        "CanInterface": (CanInterface, False),
        "InterfaceId": (str, True),
        "ObdInterface": (ObdInterface, False),
        "Type": (str, True),
    }


class CanSignal(AWSProperty):
    """
    `CanSignal <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html>`__
    """

    props: PropsDictType = {
        "Factor": (str, True),
        "IsBigEndian": (str, True),
        "IsSigned": (str, True),
        "Length": (str, True),
        "MessageId": (str, True),
        "Name": (str, False),
        "Offset": (str, True),
        "StartBit": (str, True),
    }


class ObdSignal(AWSProperty):
    """
    `ObdSignal <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html>`__
    """

    props: PropsDictType = {
        "BitMaskLength": (str, False),
        "BitRightShift": (str, False),
        "ByteLength": (str, True),
        "Offset": (str, True),
        "Pid": (str, True),
        "PidResponseLength": (str, True),
        "Scaling": (str, True),
        "ServiceMode": (str, True),
        "StartByte": (str, True),
    }


class SignalDecodersItems(AWSProperty):
    """
    `SignalDecodersItems <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html>`__
    """

    props: PropsDictType = {
        "CanSignal": (CanSignal, False),
        "FullyQualifiedName": (str, True),
        "InterfaceId": (str, True),
        "ObdSignal": (ObdSignal, False),
        "Type": (str, True),
    }


class DecoderManifest(AWSObject):
    """
    `DecoderManifest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html>`__
    """

    resource_type = "AWS::IoTFleetWise::DecoderManifest"

    props: PropsDictType = {
        "Description": (str, False),
        "ModelManifestArn": (str, True),
        "Name": (str, True),
        "NetworkInterfaces": ([NetworkInterfacesItems], False),
        "SignalDecoders": ([SignalDecodersItems], False),
        "Status": (str, False),
        "Tags": (Tags, False),
    }


class Fleet(AWSObject):
    """
    `Fleet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html>`__
    """

    resource_type = "AWS::IoTFleetWise::Fleet"

    props: PropsDictType = {
        "Description": (str, False),
        "Id": (str, True),
        "SignalCatalogArn": (str, True),
        "Tags": (Tags, False),
    }


class ModelManifest(AWSObject):
    """
    `ModelManifest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html>`__
    """

    resource_type = "AWS::IoTFleetWise::ModelManifest"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "Nodes": ([str], False),
        "SignalCatalogArn": (str, True),
        "Status": (str, False),
        "Tags": (Tags, False),
    }


class Actuator(AWSProperty):
    """
    `Actuator <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html>`__
    """

    props: PropsDictType = {
        "AllowedValues": ([str], False),
        "AssignedValue": (str, False),
        "DataType": (str, True),
        "Description": (str, False),
        "FullyQualifiedName": (str, True),
        "Max": (double, False),
        "Min": (double, False),
        "Unit": (str, False),
    }


class Attribute(AWSProperty):
    """
    `Attribute <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html>`__
    """

    props: PropsDictType = {
        "AllowedValues": ([str], False),
        "AssignedValue": (str, False),
        "DataType": (str, True),
        "DefaultValue": (str, False),
        "Description": (str, False),
        "FullyQualifiedName": (str, True),
        "Max": (double, False),
        "Min": (double, False),
        "Unit": (str, False),
    }


class Branch(AWSProperty):
    """
    `Branch <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-branch.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "FullyQualifiedName": (str, True),
    }


class Sensor(AWSProperty):
    """
    `Sensor <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html>`__
    """

    props: PropsDictType = {
        "AllowedValues": ([str], False),
        "DataType": (str, True),
        "Description": (str, False),
        "FullyQualifiedName": (str, True),
        "Max": (double, False),
        "Min": (double, False),
        "Unit": (str, False),
    }


class Node(AWSProperty):
    """
    `Node <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html>`__
    """

    props: PropsDictType = {
        "Actuator": (Actuator, False),
        "Attribute": (Attribute, False),
        "Branch": (Branch, False),
        "Sensor": (Sensor, False),
    }


class NodeCounts(AWSProperty):
    """
    `NodeCounts <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html>`__
    """

    props: PropsDictType = {
        "TotalActuators": (double, False),
        "TotalAttributes": (double, False),
        "TotalBranches": (double, False),
        "TotalNodes": (double, False),
        "TotalSensors": (double, False),
    }


class SignalCatalog(AWSObject):
    """
    `SignalCatalog <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html>`__
    """

    resource_type = "AWS::IoTFleetWise::SignalCatalog"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, False),
        "NodeCounts": (NodeCounts, False),
        "Nodes": ([Node], False),
        "Tags": (Tags, False),
    }


class Vehicle(AWSObject):
    """
    `Vehicle <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html>`__
    """

    resource_type = "AWS::IoTFleetWise::Vehicle"

    props: PropsDictType = {
        "AssociationBehavior": (str, False),
        "Attributes": (dict, False),
        "DecoderManifestArn": (str, True),
        "ModelManifestArn": (str, True),
        "Name": (str, True),
        "Tags": (Tags, False),
    }
