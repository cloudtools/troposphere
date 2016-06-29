import json
import unittest

from troposphere import awsencode, Parameter, Ref
from troposphere.autoscaling import AutoScalingGroup
from troposphere.policies import CreationPolicy, ResourceSignal, UpdatePolicy
from troposphere.policies import AutoScalingRollingUpdate


class TestCreationPolicy(unittest.TestCase):

    def test_pausetime(self):
        with self.assertRaises(ValueError):
            CreationPolicy(ResourceSignal=ResourceSignal(Count=2,
                                                         Timeout='90'))

    def test_works(self):
        policy = CreationPolicy(
            ResourceSignal=ResourceSignal(
                Count=2,
                Timeout='PT10M'
            )
        )
        self.assertEqual(policy.ResourceSignal.Count, 2)
        self.assertEqual(policy.ResourceSignal.Timeout, 'PT10M')

    def test_json(self):
        policy = CreationPolicy(
            ResourceSignal=ResourceSignal(
                Count=2,
                Timeout='PT10M'
            )
        )
        p = json.loads(json.dumps(policy, cls=awsencode))
        self.assertEqual(p['ResourceSignal']['Count'], 2)
        self.assertEqual(p['ResourceSignal']['Timeout'], 'PT10M')


class TestUpdatePolicy(unittest.TestCase):

    def test_pausetime(self):
        with self.assertRaises(ValueError):
            UpdatePolicy(AutoScalingRollingUpdate=AutoScalingRollingUpdate(
                PauseTime='90'
            ))

    def test_works(self):
        p = UpdatePolicy(
            AutoScalingRollingUpdate=AutoScalingRollingUpdate(
                MaxBatchSize=2,
                MinInstancesInService=1,
                PauseTime='PT90S',
                WaitOnResourceSignals=True))
        self.assertEqual(p.AutoScalingRollingUpdate.MaxBatchSize, 2)
        self.assertEqual(p.AutoScalingRollingUpdate.MinInstancesInService, 1)
        self.assertEqual(p.AutoScalingRollingUpdate.PauseTime, 'PT90S')
        self.assertTrue(p.AutoScalingRollingUpdate.WaitOnResourceSignals)

    def test_mininstances(self):
        group = AutoScalingGroup(
            'mygroup',
            LaunchConfigurationName="I'm a test",
            MaxSize=1,
            MinSize=1,
            UpdatePolicy=UpdatePolicy(
                AutoScalingRollingUpdate=AutoScalingRollingUpdate(
                    PauseTime='PT1M5S',
                    MinInstancesInService='1',
                    MaxBatchSize='1'
                )
            )
        )
        with self.assertRaises(ValueError):
            self.assertTrue(group.validate())

    def test_mininstances_maxsize_is_ref(self):
        paramMaxSize = Parameter(
            "ParamMaxSize",
            Type="String"
        )
        group = AutoScalingGroup(
            'mygroup',
            AvailabilityZones=['eu-west-1a', 'eu-west-1b'],
            LaunchConfigurationName="I'm a test",
            MaxSize=Ref(paramMaxSize),
            MinSize="2",
            UpdatePolicy=UpdatePolicy(
                AutoScalingRollingUpdate=AutoScalingRollingUpdate(
                    PauseTime='PT1M5S',
                    MinInstancesInService='2',
                    MaxBatchSize="1"
                )
            )
        )
        self.assertTrue(group.validate())

    def test_mininstances_mininstancesinservice_is_ref(self):
        paramMinInstancesInService = Parameter(
            "ParamMinInstancesInService",
            Type="String"
        )
        group = AutoScalingGroup(
            'mygroup',
            AvailabilityZones=['eu-west-1a', 'eu-west-1b'],
            LaunchConfigurationName="I'm a test",
            MaxSize="4",
            MinSize="2",
            UpdatePolicy=UpdatePolicy(
                AutoScalingRollingUpdate=AutoScalingRollingUpdate(
                    PauseTime='PT1M5S',
                    MinInstancesInService=Ref(paramMinInstancesInService),
                    MaxBatchSize="2",
                )
            )
        )
        self.assertTrue(group.validate())

    def test_json(self):
        p = UpdatePolicy(
            AutoScalingRollingUpdate=AutoScalingRollingUpdate(
                MaxBatchSize=2,
                MinInstancesInService=1,
                PauseTime='PT90S',
                WaitOnResourceSignals=True))
        p = json.loads(json.dumps(p, cls=awsencode))
        self.assertEqual(p['AutoScalingRollingUpdate']['MaxBatchSize'], 2)
        self.assertEqual(
            p['AutoScalingRollingUpdate']['MinInstancesInService'], 1
        )
        self.assertEqual(p['AutoScalingRollingUpdate']['PauseTime'], 'PT90S')
        self.assertTrue(p['AutoScalingRollingUpdate']['WaitOnResourceSignals'])
