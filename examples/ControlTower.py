from troposphere import Template
from troposphere.controltower import (
    EnabledBaseline,
    EnabledControl,
    EnabledControlParameter,
    Parameter,
)

template = Template()
template.set_version("2010-09-09")

parameters = [
    Parameter(
        Key="IdentityCenterEnabledBaselineArn",
        Value="arn:aws:controltower:eu-west-1:123456789012:enabledbaseline/A1B2C3D4E5F6G7H8I",
    ),
]

enabled_baseline = EnabledBaseline(
    "DemoEnabledBaseline",
    BaselineIdentifier="arn:aws:controltower:eu-west-1::baseline/A1B2C3D4E5F6G7H8I",
    BaselineVersion="4.0",
    Parameters=parameters,
    TargetIdentifier="arn:aws:organizations::123456789012:ou/o-a1b2c3d4e5/ou-1234-a1b2c3d4",
)
template.add_resource(enabled_baseline)

enabled_control_parameters = [
    # array, string, number, object, or boolean
    EnabledControlParameter(
        Key="ArrayParameter",
        Value=["string"],
    ),
    EnabledControlParameter(
        Key="StringParameter",
        Value="string",
    ),
    EnabledControlParameter(
        Key="NumberParameter",
        Value=42,
    ),
    EnabledControlParameter(
        Key="ObjectParameter",
        Value={
            "key1": "value1",
        },
    ),
    EnabledControlParameter(
        Key="BooleanParameter",
        Value=True,
    ),
]

enabled_control = EnabledControl(
    "DemoEnabledControl",
    ControlIdentifier="arn:aws:controltower:us-east-2::control/EXAMPLE_NAME",
    TargetIdentifier="arn:aws:organizations::01234567890:ou/o-EXAMPLE/ou-zzxx-zzx0zzz2",
    Parameters=enabled_control_parameters,
)
template.add_resource(enabled_control)

print(template.to_json())
