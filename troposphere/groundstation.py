# Copyright (c) 2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer, double, json_checker


class DataflowEdge(AWSProperty):
    props = {
        'Destination': (basestring, True),
        'Source': (basestring, True),
    }


class MissionProfile(AWSObject):
    resource_type = "AWS::GroundStation::MissionProfile"

    props = {
        'ContactPostPassDurationSeconds': (integer, False),
        'ContactPrePassDurationSeconds': (integer, False),
        'DataflowEdges': ([DataflowEdge], True),
        'MinimumViableContactDurationSeconds': (integer, True),
        'Name': (basestring, True),
        'Tags': (Tags, False),
        'TrackingConfigArn': (basestring, True),
    }


class SocketAddress(AWSProperty):
    props = {
        'Name': (basestring, False),
        'Port': (integer, False),
    }


class DataflowEndpoint(AWSProperty):
    props = {
        'Address': (SocketAddress, False),
        'Mtu': (integer, False),
        'Name': (basestring, False),
    }


class SecurityDetails(AWSProperty):
    props = {
        'RoleArn': (basestring, False),
        'SecurityGroupIds': ([basestring], False),
        'SubnetIds': ([basestring], False),
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
        'Units': (basestring, True),
        'Value': (double, True),
    }


class Frequency(AWSProperty):
    props = {
        'Units': (basestring, True),
        'Value': (double, True),
    }


class SpectrumConfig(AWSProperty):
    props = {
        'Bandwidth': (Bandwidth, True),
        'CenterFrequency': (Frequency, True),
        'Polarization': (basestring, False),
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
        'Polarization': (basestring, False),
    }


class DataflowEndpointGroup(AWSObject):
    resource_type = "AWS::GroundStation::DataflowEndpointGroup"

    props = {
        'EndpointDetailsList': ([EndpointDetails], True),
        'Tags': (Tags, False),
    }


class Eirp(AWSObject):
    props = {
        'Units': (basestring, True),
        'Value': (double, True),
    }


class AntennaUplinkConfig(AWSObject):
    props = {
        'SpectrumConfig': (SpectrumConfig, True),
        'TargetEirp': (Eirp, True),
    }


class DataflowEndpointConfig(AWSProperty):
    props = {
        'DataflowEndpointName': (basestring, True),
        'DataflowEndpointRegion': (basestring, False),
    }


class TrackingConfig(AWSProperty):
    props = {
        'AutoTrack': (basestring, True),
    }


class UplinkEchoConfig(AWSProperty):
    props = {
        'AntennaUplinkConfigArn': (basestring, True),
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
        'Name': (basestring, True),
        'Tags': (Tags, False),
    }
