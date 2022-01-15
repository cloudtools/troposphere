from . import AWSAttribute, AWSProperty, PropsDictType, validate_pausetime
from .validators import boolean, integer, positive_integer


class AutoScalingRollingUpdate(AWSProperty):
    props: PropsDictType = {
        "MaxBatchSize": (positive_integer, False),
        "MinInstancesInService": (integer, False),
        "MinSuccessfulInstancesPercent": (integer, False),
        "PauseTime": (validate_pausetime, False),
        "SuspendProcesses": ([str], False),
        "WaitOnResourceSignals": (boolean, False),
    }


class AutoScalingScheduledAction(AWSProperty):
    props: PropsDictType = {
        "IgnoreUnmodifiedGroupSizeProperties": (boolean, False),
    }


class AutoScalingReplacingUpdate(AWSProperty):
    props: PropsDictType = {
        "WillReplace": (boolean, False),
    }


class CodeDeployLambdaAliasUpdate(AWSProperty):
    props: PropsDictType = {
        "AfterAllowTrafficHook": (str, False),
        "ApplicationName": (boolean, True),
        "BeforeAllowTrafficHook": (str, False),
        "DeploymentGroupName": (boolean, True),
    }


class UpdatePolicy(AWSAttribute):
    props: PropsDictType = {
        "AutoScalingRollingUpdate": (AutoScalingRollingUpdate, False),
        "AutoScalingScheduledAction": (AutoScalingScheduledAction, False),
        "AutoScalingReplacingUpdate": (AutoScalingReplacingUpdate, False),
        "CodeDeployLambdaAliasUpdate": (CodeDeployLambdaAliasUpdate, False),
        "UseOnlineResharding": (boolean, False),
        "EnableVersionUpgrade": (boolean, False),
    }


class ResourceSignal(AWSProperty):
    props: PropsDictType = {
        "Count": (positive_integer, False),
        "Timeout": (validate_pausetime, False),
    }


class AutoScalingCreationPolicy(AWSProperty):
    props: PropsDictType = {
        "MinSuccessfulInstancesPercent": (integer, False),
    }


class CreationPolicy(AWSAttribute):
    props: PropsDictType = {
        "AutoScalingCreationPolicy": (AutoScalingCreationPolicy, False),
        "ResourceSignal": (ResourceSignal, True),
    }
