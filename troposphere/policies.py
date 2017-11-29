from . import AWSProperty, AWSAttribute, validate_pausetime
from .validators import positive_integer, integer, boolean


class AutoScalingRollingUpdate(AWSProperty):
    props = {
        'MaxBatchSize': (positive_integer, False),
        'MinInstancesInService': (integer, False),
        'MinSuccessfulInstancesPercent': (integer, False),
        'PauseTime': (validate_pausetime, False),
        'SuspendProcesses': ([basestring], False),
        'WaitOnResourceSignals': (boolean, False),
    }


class AutoScalingScheduledAction(AWSProperty):
    props = {
        'IgnoreUnmodifiedGroupSizeProperties': (boolean, False),
    }


class AutoScalingReplacingUpdate(AWSProperty):
    props = {
        'WillReplace': (boolean, False),
    }


class CodeDeployLambdaAliasUpdate(AWSProperty):
    props = {
        'AfterAllowTrafficHook': (basestring, False),
        'ApplicationName': (boolean, True),
        'BeforeAllowTrafficHook': (basestring, False),
        'DeploymentGroupName': (boolean, True),
    }


class UpdatePolicy(AWSAttribute):
    props = {
        'AutoScalingRollingUpdate': (AutoScalingRollingUpdate, False),
        'AutoScalingScheduledAction': (AutoScalingScheduledAction, False),
        'AutoScalingReplacingUpdate': (AutoScalingReplacingUpdate, False),
        'CodeDeployLambdaAliasUpdate': (CodeDeployLambdaAliasUpdate, False),
    }


class ResourceSignal(AWSProperty):
    props = {
        'Count': (positive_integer, False),
        'Timeout': (validate_pausetime, False),
    }


class AutoScalingCreationPolicy(AWSProperty):
    props = {
        'MinSuccessfulInstancesPercent': (integer, False),
    }


class CreationPolicy(AWSAttribute):
    props = {
        'AutoScalingCreationPolicy': (AutoScalingCreationPolicy, False),
        'ResourceSignal': (ResourceSignal, True),
    }
