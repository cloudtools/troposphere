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
        "AirflowConfigurationOptions": (str, False),
        "AirflowVersion": (str, False),
        "DagS3Path": (str, True),
        "EnvironmentClass": (str, False),
        "ExecutionRoleArn": (str, True),
        "KmsKey": (str, False),
        "LoggingConfiguration": (LoggingConfiguration, False),
        "MaxWorkers": (integer, False),
        "NetworkConfiguration": (NetworkConfiguration, True),
        "PluginsS3ObjectVersion": (str, False),
        "PluginsS3Path": (str, False),
        "RequirementsS3ObjectVersion": (str, False),
        "RequirementsS3Path": (str, False),
        "SourceBucketArn": (str, True),
        "WebserverAccessMode": (str, False),
        "WebserverUrl": (str, False),
        "WeeklyMaintenanceWindowStart": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }
