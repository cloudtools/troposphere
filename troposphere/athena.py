# Copyright (c) 2012-2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer

VALID_WORKGROUP_STATE = ('ENABLED', 'DISABLED')
VALID_ENCRYPTIONCONFIGURATION_ENCRYPTIONOPTION = ('CSE_KMS', 'SSE_KMS',
                                                  'SSE_S3')


def validate_workgroup_state(workgroup_state):
    """Validate State for Workgroup"""

    if workgroup_state not in VALID_WORKGROUP_STATE:
        raise ValueError("Workgroup State must be one of: %s" %
                         ", ".join(VALID_WORKGROUP_STATE))
    return workgroup_state


def validate_encryptionconfiguration_encryptionoption(encryptionconfiguration_encryptionoption):  # NOQA
    """Validate EncryptionOption for EncryptionConfiguration"""

    if encryptionconfiguration_encryptionoption not in VALID_ENCRYPTIONCONFIGURATION_ENCRYPTIONOPTION:  # NOQA
        raise ValueError("EncryptionConfiguration EncryptionOption must be one of: %s" %  # NOQA
                         ", ".join(VALID_ENCRYPTIONCONFIGURATION_ENCRYPTIONOPTION))  # NOQA
    return encryptionconfiguration_encryptionoption


class DataCatalog(AWSObject):
    resource_type = "AWS::Athena::DataCatalog"

    props = {
        'Description': (str, False),
        'Name': (str, True),
        'Parameters': (dict, False),
        'Tags': (Tags, False),
        'Type': (str, True),
    }


class NamedQuery(AWSObject):
    resource_type = "AWS::Athena::NamedQuery"

    props = {
        'Database': (str, True),
        'Description': (str, False),
        'Name': (str, False),
        'QueryString': (str, True),
    }


class EncryptionConfiguration(AWSProperty):
    props = {
        'EncryptionOption': (validate_encryptionconfiguration_encryptionoption,
                             False),
        'KmsKey': (str, False),
    }


class ResultConfiguration(AWSProperty):
    props = {
        'EncryptionConfiguration': (EncryptionConfiguration, False),
        'OutputLocation': (str, False),
    }


class WorkGroupConfiguration(AWSProperty):
    props = {
        'BytesScannedCutoffPerQuery': (integer, False),
        'EnforceWorkGroupConfiguration': (boolean, False),
        'PublishCloudWatchMetricsEnabled': (boolean, False),
        'RequesterPaysEnabled': (boolean, False),
        'ResultConfiguration': (ResultConfiguration, False),
    }


class ResultConfigurationUpdates(AWSProperty):
    props = {
        'EncryptionConfiguration': (EncryptionConfiguration, False),
        'OutputLocation': (str, False),
        'RemoveEncryptionConfiguration': (boolean, False),
        'RemoveOutputLocation': (boolean, False),
    }


class WorkGroupConfigurationUpdates(AWSProperty):
    props = {
        'BytesScannedCutoffPerQuery': (integer, False),
        'EnforceWorkGroupConfiguration': (boolean, False),
        'PublishCloudWatchMetricsEnabled': (boolean, False),
        'RemoveBytesScannedCutoffPerQuery': (boolean, False),
        'RequesterPaysEnabled': (boolean, False),
        'ResultConfigurationUpdates': (ResultConfigurationUpdates, False),
    }


class WorkGroup(AWSObject):
    resource_type = "AWS::Athena::WorkGroup"

    props = {
        'Description': (str, False),
        'Name': (str, True),
        'RecursiveDeleteOption': (boolean, False),
        'State': (validate_workgroup_state, False),
        'Tags': (Tags, False),
        'WorkGroupConfiguration': (WorkGroupConfiguration, False),
        'WorkGroupConfigurationUpdates': (WorkGroupConfigurationUpdates,
                                          False),
    }
