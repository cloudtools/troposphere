# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


class UpdateError(AWSProperty):
    props = {
        "ErrorCode": (str, False),
        "ErrorMessage": (str, False),
    }


class LastUpdate(AWSProperty):
    props = {
        "CreatedAt": (str, False),
        "Error": (UpdateError, False),
        "Status": (str, False),
    }


class ModuleLoggingConfiguration(AWSProperty):
    props = {
        "CloudWatchLogGroupArn": (str, False),
        "Enabled": (boolean, False),
        "LogLevel": (str, False),
    }


class LoggingConfiguration(AWSProperty):
    props = {
        "DagProcessingLogs": (ModuleLoggingConfiguration, False),
        "SchedulerLogs": (ModuleLoggingConfiguration, False),
        "TaskLogs": (ModuleLoggingConfiguration, False),
        "WebserverLogs": (ModuleLoggingConfiguration, False),
        "WorkerLogs": (ModuleLoggingConfiguration, False),
    }


class NetworkConfiguration(AWSProperty):
    props = {
        "SecurityGroupIds": (list, True),
        "SubnetIds": (list, True),
    }


class Environment(AWSObject):
    resource_type = "AWS::MWAA::Environment"

    props = {
        "AirflowConfigurationOptions": (dict, False),
        "AirflowVersion": (str, False),
        "DagS3Path": (str, False),
        "EnvironmentClass": (str, False),
        "ExecutionRoleArn": (str, False),
        "KmsKey": (str, False),
        "LoggingConfiguration": (LoggingConfiguration, False),
        "MaxWorkers": (integer, False),
        "MinWorkers": (integer, False),
        "Name": (str, True),
        "NetworkConfiguration": (NetworkConfiguration, False),
        "PluginsS3ObjectVersion": (str, False),
        "PluginsS3Path": (str, False),
        "RequirementsS3ObjectVersion": (str, False),
        "RequirementsS3Path": (str, False),
        "Schedulers": (integer, False),
        "SourceBucketArn": (str, False),
        "Tags": (Tags, False),
        "WebserverAccessMode": (str, False),
        "WeeklyMaintenanceWindowStart": (str, False),
    }
