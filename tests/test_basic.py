import unittest
from troposphere import AWSObject, AWSProperty, Output, Parameter
from troposphere import Join, Ref, Split, Sub, Template
from troposphere.ec2 import Instance, SecurityGroupRule
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

    def test_required_title_error(self):
        with self.assertRaisesRegexp(ValueError, "title:"):
            t = Template()
            t.add_resource(Instance('ec2instance'))
            t.to_json()


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


class FakeAWSProperty(AWSProperty):
    props = {}


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

    def test_exception(self):
        def ExceptionValidator(x):
            raise ValueError

        class ExceptionAWSProperty(AWSProperty):
            props = {
                'foo': (ExceptionValidator, True),
            }

        with self.assertRaises(ValueError):
            ExceptionAWSProperty(foo='bar')


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


class TestOutput(unittest.TestCase):

    def test_noproperty(self):
        t = Output("MyOutput", Value="myvalue")
        d = t.to_dict()
        with self.assertRaises(KeyError):
            d['Properties']

    def test_empty_awsproperty_outputs_empty_object(self):
        t = FakeAWSProperty()
        d = t.to_dict()
        self.assertEquals(len(d), 0)


class TestParameter(unittest.TestCase):

    def test_noproperty(self):
        t = Parameter("MyParameter", Type="String")
        d = t.to_dict()
        with self.assertRaises(KeyError):
            d['Properties']

    def test_property_validator(self):
        p = Parameter("BasicString", Type="String", MaxLength=10)
        p.validate()

        p = Parameter("BasicString", Type="String", MaxValue=10)
        with self.assertRaises(ValueError):
            p.validate()

        p = Parameter("BasicNumber", Type="Number", MaxValue=10)
        p.validate()

        p = Parameter("BasicNumber", Type="Number", AllowedPattern=".*")
        with self.assertRaises(ValueError):
            p.validate()

    def test_invalid_parameter_property_in_template(self):
        t = Template()
        p = Parameter("BasicNumber", Type="Number", AllowedPattern=".*")
        t.add_parameter(p)
        with self.assertRaises(ValueError):
            t.to_json()


class TestProperty(unittest.TestCase):

    def test_noproperty(self):
        t = SecurityGroupRule(
            IpProtocol="tcp",
            FromPort="22",
            ToPort="22",
            CidrIp="0.0.0.0/0",
        )
        d = t.to_dict()
        with self.assertRaises(KeyError):
            d['Properties']

    def test_awsproperty_invalid_property(self):
        t = FakeAWSProperty()
        with self.assertRaises(AttributeError) as context:
            t.badproperty = 5
        self.assertTrue('FakeAWSProperty' in context.exception.args[0])
        self.assertTrue('badproperty' in context.exception.args[0])


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
        ref = t.to_dict()
        self.assertEqual(ref['Ref'], 'param')


class TestName(unittest.TestCase):

    def test_ref(self):
        name = 'fake'
        t = Template()
        resource = t.add_resource(Instance(name))
        self.assertEqual(resource.name, name)


class TestSub(unittest.TestCase):

    def test_sub_with_vars(self):
        s = 'foo ${AWS::Region}'
        raw = Sub(s)
        actual = raw.to_dict()
        expected = {'Fn::Sub': 'foo ${AWS::Region}'}
        self.assertEqual(expected, actual)

    def test_sub_without_vars(self):
        s = 'foo ${AWS::Region} ${sub1} ${sub2}'
        values = {'sub1': 'uno', 'sub2': 'dos'}
        raw = Sub(s, **values)
        actual = raw.to_dict()
        expected = {'Fn::Sub': ['foo ${AWS::Region} ${sub1} ${sub2}', values]}
        self.assertEqual(expected, actual)


class TestSplit(unittest.TestCase):

    def test_split(self):
        delimiter = ','
        source_string = ('{ "Fn::ImportValue": { "Fn::Sub": '
                         '"${VpcStack}-PublicSubnets" }')
        raw = Split(delimiter, source_string)
        actual = raw.to_dict()
        expected = (
                {'Fn::Split': [',', '{ "Fn::ImportValue": { '
                 '"Fn::Sub": "${VpcStack}-PublicSubnets" }']}
        )
        self.assertEqual(expected, actual)

        with self.assertRaises(ValueError):
            Join(10, "foobar")


class TestJoin(unittest.TestCase):

    def test_join(self):
        delimiter = ','
        source_string = (
                '{ [ "arn:aws:lambda:",{ "Ref": "AWS::Region" },":",'
                '{ "Ref": "AWS::AccountId" },'
                '":function:cfnRedisEndpointLookup" ] }'
        )
        raw = Join(delimiter, source_string)
        actual = raw.to_dict()
        expected = (
            {'Fn::Join': [',', '{ [ "arn:aws:lambda:",{ "Ref": '
                          '"AWS::Region" },":",{ "Ref": "AWS::AccountId" },'
                          '":function:cfnRedisEndpointLookup" ] }']}

        )
        self.assertEqual(expected, actual)

        with self.assertRaises(ValueError):
            Join(10, "foobar")


if __name__ == '__main__':
    unittest.main()
