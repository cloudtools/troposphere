# Copyright (c) 2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer, double, json_checker


class DataflowEdge(AWSProperty):
    props = {
        'Destination': (str, True),
        'Source': (str, True),
    }


class MissionProfile(AWSObject):
    resource_type = "AWS::GroundStation::MissionProfile"

    props = {
        'ContactPostPassDurationSeconds': (integer, False),
        'ContactPrePassDurationSeconds': (integer, False),
        'DataflowEdges': ([DataflowEdge], True),
        'MinimumViableContactDurationSeconds': (integer, True),
        'Name': (str, True),
        'Tags': (Tags, False),
        'TrackingConfigArn': (str, True),
    }


class SocketAddress(AWSProperty):
    props = {
        'Name': (str, False),
        'Port': (integer, False),
    }


class DataflowEndpoint(AWSProperty):
    props = {
        'Address': (SocketAddress, False),
        'Mtu': (integer, False),
        'Name': (str, False),
    }


class SecurityDetails(AWSProperty):
    props = {
        'RoleArn': (str, False),
        'SecurityGroupIds': ([str], False),
        'SubnetIds': ([str], False),
    }


class EndpointDetails(AWSProperty):
    props = {
        'DataflowEndpoint': (DataflowEndpoint, False),
        'SecurityDetails': (SecurityDetails, False),
    }


class DecodeConfig(AWSProperty):
    props = {
        'UnvalidatedJSON': (json_checker, True),
    }


class DemodulationConfig(AWSProperty):
    props = {
        'UnvalidatedJSON': (json_checker, True),
    }


class Bandwidth(AWSProperty):
    props = {
        'Units': (str, True),
        'Value': (double, True),
    }


class Frequency(AWSProperty):
    props = {
        'Units': (str, True),
        'Value': (double, True),
    }


class SpectrumConfig(AWSProperty):
    props = {
        'Bandwidth': (Bandwidth, True),
        'CenterFrequency': (Frequency, True),
        'Polarization': (str, False),
    }


class AntennaDownlinkConfig(AWSProperty):
    props = {
        'SpectrumConfig': (SpectrumConfig, True),
    }


class AntennaDownlinkDemodDecodeConfig(AWSProperty):
    props = {
        'DecodeConfig': (DecodeConfig, True),
        'DemodulationConfig': (DemodulationConfig, True),
        'SpectrumConfig': (SpectrumConfig, True),
    }


class SpectrumConfig(AWSProperty):
    props = {
        'Bandwidth': (Bandwidth, True),
        'CenterFrequency': (Frequency, True),
        'Polarization': (str, False),
    }


class DataflowEndpointGroup(AWSObject):
    resource_type = "AWS::GroundStation::DataflowEndpointGroup"

    props = {
        'EndpointDetailsList': ([EndpointDetails], True),
        'Tags': (Tags, False),
    }


class Eirp(AWSObject):
    props = {
        'Units': (str, True),
        'Value': (double, True),
    }


class AntennaUplinkConfig(AWSObject):
    props = {
        'SpectrumConfig': (SpectrumConfig, True),
        'TargetEirp': (Eirp, True),
    }


class DataflowEndpointConfig(AWSProperty):
    props = {
        'DataflowEndpointName': (str, True),
        'DataflowEndpointRegion': (str, False),
    }


class TrackingConfig(AWSProperty):
    props = {
        'AutoTrack': (str, True),
    }


class UplinkEchoConfig(AWSProperty):
    props = {
        'AntennaUplinkConfigArn': (str, True),
        'Enabled': (boolean, True),
    }


class ConfigData(AWSProperty):
    props = {
        'AntennaDownlinkConfig': (AntennaDownlinkConfig, False),
        'AntennaDownlinkDemodDecodeConfig': (AntennaDownlinkDemodDecodeConfig, False),  # NOQA
        'AntennaUplinkConfig': (AntennaUplinkConfig, False),
        'DataflowEndpointConfig': (DataflowEndpointConfig, False),
        'TrackingConfig': (TrackingConfig, False),
        'UplinkEchoConfig': (UplinkEchoConfig, False),
    }


class Config(AWSObject):
    resource_type = "AWS::GroundStation::Config"

    props = {
        'ConfigData': (ConfigData, True),
        'Name': (str, True),
        'Tags': (Tags, False),
    }
