from . import AWSProperty, validate_pausetime
from .validators import positive_integer, integer, boolean


class AutoScalingRollingUpdate(AWSProperty):
    props = {
        'MaxBatchSize': (positive_integer, False),
        'MinInstancesInService': (integer, False),
        'PauseTime': (validate_pausetime, False),
        'SuspendProcesses': ([basestring], False),
        'WaitOnResourceSignals': (boolean, False),
    }


class AutoScalingScheduledAction(AWSProperty):
    props = {
        'IgnoreUnmodifiedGroupSizeProperties': (boolean, False),
    }


class UpdatePolicy(AWSProperty):
    props = {
        'AutoScalingRollingUpdate': (AutoScalingRollingUpdate, False),
        'AutoScalingScheduledAction': (AutoScalingScheduledAction, False),
    }


class ResourceSignal(AWSProperty):
    props = {
        'Count': (positive_integer, False),
        'Timeout': (validate_pausetime, False),
    }


class CreationPolicy(AWSProperty):
    props = {
        'ResourceSignal': (ResourceSignal, True),
    }
