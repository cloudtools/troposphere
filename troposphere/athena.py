# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags


class NamedQuery(AWSObject):
    resource_type = "AWS::Athena::NamedQuery"

    props = {
        'Database': (basestring, True),
        'Description': (basestring, False),
        'Name': (basestring, False),
        'QueryString': (basestring, True),
    }


class EncryptionConfiguration(AWSProperty):
    props = {
        'EncryptionOption': (basestring, True),
        'KmsKey': (basestring, False)
    }


class ResultConfiguration(AWSProperty):
    props = {
        'EncryptionConfiguration': (EncryptionConfiguration, False),
        'OutputLocation': (basestring, False)
    }


class ResultConfigurationUpdates(AWSProperty):
    props = {
        'EncryptionConfiguration': (EncryptionConfiguration, False),
        'OutputLocation': (basestring, False),
        'RemoveEncryptionConfiguration': (bool, False),
        'RemoveOutputLocation': (bool, False)
    }


class WorkGroupConfiguration(AWSProperty):
    props = {
        'BytesScannedCutoffPerQuery': (int, False),
        'EnforceWorkGroupConfiguration': (bool, False),
        'PublishCloudWatchMetricsEnabled': (bool, False),
        'RequesterPaysEnabled': (bool, False),
        'ResultConfiguration': (ResultConfiguration, False)
    }


class WorkGroupConfigurationUpdates(AWSProperty):
    props = {
        'BytesScannedCutoffPerQuery': (int, False),
        'EnforceWorkGroupConfiguration': (bool, False),
        'PublishCloudWatchMetricsEnabled': (bool, False),
        'RequesterPaysEnabled': (bool, False),
        'ResultConfigurationUpdates': (ResultConfigurationUpdates, False)
    }


class WorkGroup(AWSObject):
    resource_type = "AWS::Athena::WorkGroup"

    props = {
        'Description': (basestring, False),
        'Name': (basestring, True),
        'RecursiveDeleteOption': (bool, False),
        'State': (basestring, False),
        'Tags': (Tags, False),
        'WorkGroupConfiguration': (WorkGroupConfiguration, False),
        'WorkGroupConfigurationUpdates': (WorkGroupConfigurationUpdates, False)
    }
