import json
import unittest
from troposphere import awsencode, AWSObject, Output, Parameter
from troposphere import Template, UpdatePolicy, Ref
from troposphere.ec2 import Instance, SecurityGroupRule
from troposphere.autoscaling import AutoScalingGroup
from troposphere.elasticloadbalancing import HealthCheck
from troposphere.validators import positive_integer


class TestBasic(unittest.TestCase):

    def test_badproperty(self):
        with self.assertRaises(AttributeError):
            Instance('ec2instance', foobar=True,)

    def test_badrequired(self):
        with self.assertRaises(ValueError):
            t = Template()
            t.add_resource(Instance('ec2instance'))
            t.to_json()

    def test_badtype(self):
        with self.assertRaises(AttributeError):
            Instance('ec2instance', image_id=0.11)

    def test_goodrequired(self):
        Instance('ec2instance', ImageId="ami-xxxx", InstanceType="m1.small")

    def test_extraattribute(self):

        class ExtendedInstance(Instance):
            def __init__(self, *args, **kwargs):
                self.attribute = None
                super(ExtendedInstance, self).__init__(*args, **kwargs)

        instance = ExtendedInstance('ec2instance', attribute='value')
        self.assertEqual(instance.attribute, 'value')


def call_correct(x):
    return x


def call_incorrect(x):
    raise ValueError


class FakeAWSObject(AWSObject):
    type = "Fake::AWS::Object"

    props = {
        'callcorrect': (call_correct, False),
        'callincorrect': (call_incorrect, False),
        'singlelist': (list, False),
        'multilist': ([bool, int, float], False),
        'multituple': ((bool, int), False),
        'helperfun': (positive_integer, False),
    }

    def validate(self):
        properties = self.properties
        title = self.title
        type = self.type
        if 'callcorrect' in properties and 'singlelist' in properties:
            raise ValueError(
                ("Cannot specify both 'callcorrect and 'singlelist' in "
                 "object %s (type %s)" % (title, type))
            )


class TestValidators(unittest.TestCase):

    def test_callcorrect(self):
        FakeAWSObject('fake', callcorrect=True)

    def test_callincorrect(self):
        with self.assertRaises(ValueError):
            FakeAWSObject('fake', callincorrect=True)

    def test_list(self):
        FakeAWSObject('fake', singlelist=['a', 1])

    def test_badlist(self):
        with self.assertRaises(TypeError):
            FakeAWSObject('fake', singlelist=True)

    def test_multilist(self):
        FakeAWSObject('fake', multilist=[1, True, 2, 0.3])

    def test_badmultilist(self):
        with self.assertRaises(TypeError):
            FakeAWSObject('fake', multilist=True)
        with self.assertRaises(TypeError):
            FakeAWSObject('fake', multilist=[1, 'a'])

    def test_mutualexclusion(self):
        t = Template()
        t.add_resource(FakeAWSObject(
            'fake', callcorrect=True, singlelist=[10])
        )
        with self.assertRaises(ValueError):
            t.to_json()

    def test_tuples(self):
        FakeAWSObject('fake', multituple=True)
        FakeAWSObject('fake', multituple=10)
        with self.assertRaises(TypeError):
            FakeAWSObject('fake', multituple=0.1)

    def test_helperfun(self):
        FakeAWSObject('fake', helperfun=Ref('fake_ref'))


class TestHealthCheck(unittest.TestCase):
    def test_healthy_interval_ok(self):
        HealthCheck(
            HealthyThreshold='2',
            Interval='2',
            Target='HTTP:80/index.html',
            Timeout='4',
            UnhealthyThreshold='9'
        )

    def test_healthy_interval_too_low(self):
        with self.assertRaises(ValueError):
            HealthCheck(
                HealthyThreshold='1',
                Interval='2',
                Target='HTTP:80/index.html',
                Timeout='4',
                UnhealthyThreshold='9'
            )


class TestUpdatePolicy(unittest.TestCase):

    def test_pausetime(self):
        with self.assertRaises(ValueError):
            UpdatePolicy('AutoScalingRollingUpdate', PauseTime='90')

    def test_type(self):
        with self.assertRaises(ValueError):
            UpdatePolicy('MyCoolPolicy')

    def test_works(self):
        policy = UpdatePolicy(
            'AutoScalingRollingUpdate',
            PauseTime='PT1M5S',
            MinInstancesInService='2',
            MaxBatchSize='1',
        )
        self.assertEqual(policy.PauseTime, 'PT1M5S')

    def test_mininstances(self):
        group = AutoScalingGroup(
            'mygroup',
            LaunchConfigurationName="I'm a test",
            MaxSize="1",
            MinSize="1",
            UpdatePolicy=UpdatePolicy(
                'AutoScalingRollingUpdate',
                PauseTime='PT1M5S',
                MinInstancesInService='1',
                MaxBatchSize='1',
            )
        )
        with self.assertRaises(ValueError):
            self.assertTrue(group.validate())

    def test_working(self):
        group = AutoScalingGroup(
            'mygroup',
            LaunchConfigurationName="I'm a test",
            MaxSize="4",
            MinSize="2",
            UpdatePolicy=UpdatePolicy(
                'AutoScalingRollingUpdate',
                PauseTime='PT1M5S',
                MinInstancesInService='2',
                MaxBatchSize='1',
            )
        )
        self.assertTrue(group.validate())

    def test_updatepolicy_noproperty(self):
        t = UpdatePolicy('AutoScalingRollingUpdate', PauseTime='PT1M0S')
        d = json.loads(json.dumps(t, cls=awsencode))
        with self.assertRaises(KeyError):
            d['Properties']

    def test_updatepolicy_dictname(self):
        t = UpdatePolicy('AutoScalingRollingUpdate', PauseTime='PT1M0S')
        d = json.loads(json.dumps(t, cls=awsencode))
        self.assertIn('AutoScalingRollingUpdate', d)


class TestOutput(unittest.TestCase):

    def test_noproperty(self):
        t = Output("MyOutput", Value="myvalue")
        d = json.loads(json.dumps(t, cls=awsencode))
        with self.assertRaises(KeyError):
            d['Properties']


class TestParameter(unittest.TestCase):

    def test_noproperty(self):
        t = Parameter("MyParameter", Type="String")
        d = json.loads(json.dumps(t, cls=awsencode))
        with self.assertRaises(KeyError):
            d['Properties']


class TestProperty(unittest.TestCase):

    def test_noproperty(self):
        t = SecurityGroupRule(
            IpProtocol="tcp",
            FromPort="22",
            ToPort="22",
            CidrIp="0.0.0.0/0",
        )
        d = json.loads(json.dumps(t, cls=awsencode))
        with self.assertRaises(KeyError):
            d['Properties']


class TestDuplicate(unittest.TestCase):

    def test_output(self):
        t = Template()
        o = Output("MyOutput", Value="myvalue")
        t.add_output(o)
        with self.assertRaises(ValueError):
            t.add_output(o)

    def test_parameter(self):
        t = Template()
        p = Parameter("MyParameter", Type="String")
        t.add_parameter(p)
        with self.assertRaises(ValueError):
            t.add_parameter(p)

    def test_resource(self):
        t = Template()
        r = FakeAWSObject('fake', callcorrect=True)
        t.add_resource(r)
        with self.assertRaises(ValueError):
            t.add_resource(r)


class TestRef(unittest.TestCase):

    def test_ref(self):
        param = Parameter("param", Description="description", Type="String")
        t = Ref(param)
        ref = json.loads(json.dumps(t, cls=awsencode))
        self.assertEqual(ref['Ref'], 'param')


class TestName(unittest.TestCase):

    def test_ref(self):
        name = 'fake'
        t = Template()
        resource = t.add_resource(Instance(name))
        self.assertEqual(resource.name, name)


if __name__ == '__main__':
    unittest.main()
