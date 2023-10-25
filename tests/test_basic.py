import pickle
import unittest

from troposphere import (
    AWSHelperFn,
    AWSObject,
    AWSProperty,
    Cidr,
    GenericHelperFn,
    If,
    Join,
    NoValue,
    Output,
    Parameter,
    Ref,
    Region,
    Split,
    Sub,
    Template,
    cloudformation,
    depends_on_helper,
)
from troposphere.ec2 import Instance, NetworkInterface, Route, SecurityGroupRule
from troposphere.elasticloadbalancing import HealthCheck
from troposphere.s3 import Bucket, PublicRead
from troposphere.validators import positive_integer


class TypeComparator:
    """ Helper to test the __eq__ protocol """

    def __init__(self, valid_types):
        self.valid_types = valid_types

    def __eq__(self, other):
        return isinstance(other, self.valid_types)

    def __ne__(self, other):
        return not self == other


def double(x):
    return positive_integer(x) * 2


def call_correct(x):
    return x


def call_incorrect(x):
    raise ValueError


class FakeAWSProperty(AWSProperty):
    props = {}


class FakeAWSObject(AWSObject):
    type = "Fake::AWS::Object"

    props = {
        "callcorrect": (call_correct, False),
        "callincorrect": (call_incorrect, False),
        "singlelist": (list, False),
        "multilist": ([bool, int, float], False),
        "multituple": ((bool, int), False),
        "helperfun": (positive_integer, False),
        "listhelperfun": ([double], False),
    }

    def validate(self):
        properties = self.properties
        title = self.title
        type = self.type
        if "callcorrect" in properties and "singlelist" in properties:
            raise ValueError(
                (
                    "Cannot specify both 'callcorrect and 'singlelist' in "
                    "object %s (type %s)" % (title, type)
                )
            )


class TestBasic(unittest.TestCase):
    def test___eq__(self):
        """Test __eq__."""
        assert FakeAWSObject("foobar", callcorrect=True) == FakeAWSObject(
            "foobar", callcorrect=True
        )
        assert FakeAWSObject("foobar", callcorrect=True) == {
            "title": "foobar",
            "Properties": {"callcorrect": True},
        }
        assert FakeAWSObject("foobar", callcorrect=True) == TypeComparator(AWSObject)
        assert TypeComparator(AWSObject) == FakeAWSObject("foobar", callcorrect=True)

        assert GenericHelperFn("foobar") == GenericHelperFn("foobar")
        assert GenericHelperFn({"foo": "bar"}) == {"foo": "bar"}
        assert GenericHelperFn("foobar") == TypeComparator(AWSHelperFn)
        assert TypeComparator(AWSHelperFn) == GenericHelperFn("foobar")

    def test___ne__(self):
        """Test __ne__."""
        assert FakeAWSObject("foo", callcorrect=True) != FakeAWSObject(
            "bar", callcorrect=True
        )
        assert FakeAWSObject("foobar", callcorrect=True) != FakeAWSObject(
            "foobar", callcorrect=False
        )
        assert FakeAWSObject("foobar", callcorrect=True) != FakeAWSProperty("foobar")
        assert FakeAWSObject("foobar", callcorrect=True) != TypeComparator(AWSHelperFn)
        assert TypeComparator(AWSHelperFn) != FakeAWSObject("foobar", callcorrect=True)

        assert GenericHelperFn("foobar") != GenericHelperFn("bar")
        assert GenericHelperFn("foobar") != "foobar"
        assert GenericHelperFn("foobar") != FakeAWSProperty("foobar")
        assert GenericHelperFn("foobar") != TypeComparator(AWSObject)
        assert TypeComparator(AWSObject) != GenericHelperFn("foobar")

    def test_badproperty(self):
        with self.assertRaises(AttributeError):
            Instance(
                "ec2instance",
                foobar=True,
            )

    def test_badrequired(self):
        with self.assertRaises(ValueError):
            t = Template()
            t.add_resource(NetworkInterface("networkinterface"))
            t.to_json()

    def test_badtype(self):
        with self.assertRaises(AttributeError):
            Instance("ec2instance", image_id=0.11)

    def test_goodrequired(self):
        NetworkInterface("interface", SubnetId="abc123")

    def test_extraattribute(self):
        class ExtendedInstance(Instance):
            def __init__(self, *args, **kwargs):
                self.attribute = None
                super().__init__(*args, **kwargs)

        instance = ExtendedInstance("ec2instance", attribute="value")
        self.assertEqual(instance.attribute, "value")

    def test_depends_on_helper_with_resource(self):
        resource_name = "Bucket1"
        b1 = Bucket(resource_name)
        self.assertEqual(depends_on_helper(b1), resource_name)

    def test_depends_on_helper_with_string(self):
        resource_name = "Bucket1"
        self.assertEqual(depends_on_helper(resource_name), resource_name)

    def test_resource_depends_on(self):
        b1 = Bucket("B1")
        b2 = Bucket("B2", DependsOn=b1)
        self.assertEqual(b1.title, b2.resource["DependsOn"])

    def test_resource_depends_on_attr(self):
        b1 = Bucket("B1")
        b2 = Bucket("B2", DependsOn=b1)
        self.assertEqual(b1.title, b2.DependsOn)

    def test_resource_depends_on_list(self):
        b1 = Bucket("B1")
        b2 = Bucket("B2")
        b3 = Bucket("B3", DependsOn=[b1, b2])
        self.assertEqual(b1.title, b3.DependsOn[0])
        self.assertEqual(b2.title, b3.DependsOn[1])

    def test_pickle_ok(self):
        # tests that objects can be pickled/un-pickled without hitting issues
        bucket_name = "test-bucket"
        b = Bucket("B1", BucketName=bucket_name)
        p = pickle.dumps(b)
        b2 = pickle.loads(p)
        self.assertEqual(b2.BucketName, b.BucketName)


class TestValidators(unittest.TestCase):
    def test_callcorrect(self):
        FakeAWSObject("fake", callcorrect=True)

    def test_callincorrect(self):
        with self.assertRaises(ValueError):
            FakeAWSObject("fake", callincorrect=True)

    def test_list(self):
        FakeAWSObject("fake", singlelist=["a", 1])

    def test_badlist(self):
        with self.assertRaises(TypeError):
            FakeAWSObject("fake", singlelist=True)

    def test_multilist(self):
        FakeAWSObject("fake", multilist=[1, True, 2, 0.3])

    def test_badmultilist(self):
        with self.assertRaises(TypeError):
            FakeAWSObject("fake", multilist=True)
        with self.assertRaises(TypeError):
            FakeAWSObject("fake", multilist=[1, "a"])

    def test_mutualexclusion(self):
        t = Template()
        t.add_resource(FakeAWSObject("fake", callcorrect=True, singlelist=[10]))
        with self.assertRaises(ValueError):
            t.to_json()

    def test_tuples(self):
        FakeAWSObject("fake", multituple=True)
        FakeAWSObject("fake", multituple=10)
        with self.assertRaises(TypeError):
            FakeAWSObject("fake", multituple=0.1)

    def test_helperfun(self):
        FakeAWSObject("fake", helperfun=Ref("fake_ref"))

    def test_listhelperfun(self):
        with self.assertRaises(TypeError):
            FakeAWSObject("fake", listhelperfun=1)

        x = FakeAWSObject("fake", listhelperfun=[1, 2])
        if x.listhelperfun != [2, 4]:
            raise ValueError

        with self.assertRaises(ValueError):
            FakeAWSObject("fake", listhelperfun=[1, -2])

        with self.assertRaises(ValueError):
            FakeAWSObject("fake", listhelperfun=[1, "foo"])

    def test_exception(self):
        def ExceptionValidator(x):
            raise ValueError

        class ExceptionAWSProperty(AWSProperty):
            props = {
                "foo": (ExceptionValidator, True),
            }

        with self.assertRaises(ValueError):
            ExceptionAWSProperty(foo="bar")

    def test_error_message(self):
        from troposphere.cloudfront import CustomHeader

        with self.assertRaisesRegex(ValueError, "troposphere.cloudfront.CustomHeader"):
            CustomHeader(Header="Cache-Policy", Value="no-cache").to_dict()


class TestHealthCheck(unittest.TestCase):
    def test_healthy_interval_ok(self):
        HealthCheck(
            HealthyThreshold="2",
            Interval="2",
            Target="HTTP:80/index.html",
            Timeout="4",
            UnhealthyThreshold="9",
        )

    def test_healthy_interval_too_low(self):
        with self.assertRaises(ValueError):
            HealthCheck(
                HealthyThreshold="1",
                Interval="2",
                Target="HTTP:80/index.html",
                Timeout="4",
                UnhealthyThreshold="9",
            )


class TestOutput(unittest.TestCase):
    def test_noproperty(self):
        t = Output("MyOutput", Value="myvalue")
        d = t.to_dict()
        with self.assertRaises(KeyError):
            d["Properties"]

    def test_empty_awsproperty_outputs_empty_object(self):
        t = FakeAWSProperty()
        d = t.to_dict()
        self.assertEqual(len(d), 0)


class TestParameter(unittest.TestCase):
    def test_noproperty(self):
        t = Parameter("MyParameter", Type="String")
        d = t.to_dict()
        with self.assertRaises(KeyError):
            d["Properties"]

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

    def test_get_or_add_adds(self):
        t = Template()
        p = Parameter("param", Type="String", Default="foo")
        result = t.get_or_add_parameter(p)
        self.assertEqual(t.parameters["param"], p)
        self.assertEqual(result, p)

    def test_add_or_get_returns_with_out_adding_duplicate(self):
        t = Template()
        p = Parameter("param", Type="String", Default="foo")
        t.add_parameter(p)
        result = t.get_or_add_parameter(p)
        self.assertEqual(t.parameters["param"], p)
        self.assertEqual(result, p)
        self.assertEqual(len(t.parameters), 1)

    def test_property_default(self):
        p = Parameter("param", Type="String", Default="foo")
        p.validate()

        p = Parameter("param", Type="Number", Default=1)
        p.validate()

        p = Parameter("param", Type="Number", Default=1.0)
        p.validate()

        p = Parameter("param", Type="Number", Default=0.1)
        p.validate()

        p = Parameter("param", Type="List<Number>", Default="1, 2, 3")
        p.validate()

        p = Parameter("param", Type="List<Number>", Default=" 0.1 , 2 , 1.1 ")
        p.validate()

        with self.assertRaises(ValueError):
            p = Parameter("param", Type="String", Default=1)
            p.validate()

        with self.assertRaises(ValueError):
            p = Parameter("param", Type="Number", Default="foo")
            p.validate()

        with self.assertRaises(TypeError):
            p = Parameter("param", Type="Number", Default=["foo"])
            p.validate()

        with self.assertRaises(ValueError):
            p = Parameter("param", Type="List<Number>", Default="foo")
            p.validate()

        with self.assertRaises(ValueError):
            p = Parameter("param", Type="List<Number>", Default="1, 2, foo")
            p.validate()

        with self.assertRaises(TypeError):
            p = Parameter("param", Type="List<Number>", Default=["1", "2"])
            p.validate()


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
            d["Properties"]

    def test_awsproperty_invalid_property(self):
        t = FakeAWSProperty()
        with self.assertRaises(AttributeError) as context:
            t.badproperty = 5
        self.assertTrue("FakeAWSProperty" in context.exception.args[0])
        self.assertTrue("badproperty" in context.exception.args[0])


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
        r = FakeAWSObject("fake", callcorrect=True)
        t.add_resource(r)
        with self.assertRaises(ValueError):
            t.add_resource(r)


class TestRef(unittest.TestCase):
    def test_ref(self):
        param = Parameter("param", Description="description", Type="String")
        t = Ref(param)
        ref = t.to_dict()
        self.assertEqual(ref["Ref"], "param")

    def test_ref_eq(self):
        s = "AWS::NoValue"
        r = Ref(s)

        wch = cloudformation.WaitConditionHandle("TestResource")

        self.assertEqual(s, r)
        self.assertEqual(s, NoValue)
        self.assertEqual(r, NoValue)
        self.assertEqual(wch.Ref(), "TestResource")

        self.assertNotEqual(r, "AWS::Region")
        self.assertNotEqual(r, Region)
        self.assertNotEqual(r, Ref)
        self.assertNotEqual(wch.Ref(), "NonexistantResource")

    def test_ref_hash(self):
        s = hash("AWS::NoValue")
        r = hash(Ref("AWS::NoValue"))

        wch = cloudformation.WaitConditionHandle("TestResource")

        self.assertEqual(s, r)
        self.assertEqual(s, hash(NoValue))
        self.assertEqual(r, hash(NoValue))
        self.assertEqual(hash(wch.Ref()), hash("TestResource"))

        self.assertNotEqual(r, hash("AWS::Region"))
        self.assertNotEqual(r, hash(Region))
        self.assertNotEqual(r, hash(Ref))
        self.assertNotEqual(hash(wch.Ref()), hash("NonexistantResource"))


class TestName(unittest.TestCase):
    def test_ref(self):
        name = "fake"
        t = Template()
        resource = t.add_resource(Instance(name))
        self.assertEqual(resource.name, name)


class TestCidr(unittest.TestCase):
    def test_getcidr(self):
        raw = Cidr("10.1.10.1/24", 2)
        actual = raw.to_dict()
        expected = {"Fn::Cidr": ["10.1.10.1/24", 2]}
        self.assertEqual(expected, actual)

    def test_getcidr_withsizemask(self):
        raw = Cidr("10.1.10.1/24", 2, 10)
        actual = raw.to_dict()
        expected = {"Fn::Cidr": ["10.1.10.1/24", 2, 10]}
        self.assertEqual(expected, actual)


class TestSub(unittest.TestCase):
    def test_sub_without_vars(self):
        s = "foo ${AWS::Region}"
        raw = Sub(s)
        actual = raw.to_dict()
        expected = {"Fn::Sub": "foo ${AWS::Region}"}
        self.assertEqual(expected, actual)

    def test_sub_with_vars_unpakaged(self):
        s = "foo ${AWS::Region} ${sub1} ${sub2}"
        values = {"sub1": "uno", "sub2": "dos"}
        raw = Sub(s, **values)
        actual = raw.to_dict()
        expected = {"Fn::Sub": ["foo ${AWS::Region} ${sub1} ${sub2}", values]}
        self.assertEqual(expected, actual)

    def test_sub_with_vars_not_unpakaged(self):
        s = "foo ${AWS::Region} ${sub1} ${sub2}"
        values = {"sub1": "uno", "sub2": "dos"}
        raw = Sub(s, values)
        actual = raw.to_dict()
        expected = {"Fn::Sub": ["foo ${AWS::Region} ${sub1} ${sub2}", values]}
        self.assertEqual(expected, actual)

    def test_sub_with_vars_mix(self):
        s = "foo ${AWS::Region} ${sub1} ${sub2} ${sub3}"
        values = {"sub1": "uno", "sub2": "dos"}
        raw = Sub(s, values, sub3="tres")
        actual = raw.to_dict()
        expected = {
            "Fn::Sub": [
                "foo ${AWS::Region} ${sub1} ${sub2} ${sub3}",
                {"sub1": "uno", "sub2": "dos", "sub3": "tres"},
            ]
        }
        self.assertEqual(expected, actual)


class TestSplit(unittest.TestCase):
    def test_split(self):
        delimiter = ","
        source_string = (
            '{ "Fn::ImportValue": { "Fn::Sub": ' '"${VpcStack}-PublicSubnets" }'
        )
        raw = Split(delimiter, source_string)
        actual = raw.to_dict()
        expected = {
            "Fn::Split": [
                ",",
                '{ "Fn::ImportValue": { ' '"Fn::Sub": "${VpcStack}-PublicSubnets" }',
            ]
        }
        self.assertEqual(expected, actual)

        with self.assertRaises(ValueError):
            Split(10, "foobar")


class TestJoin(unittest.TestCase):
    def test_join(self):
        delimiter = ","
        source_string = (
            '{ [ "arn:aws:lambda:",{ "Ref": "AWS::Region" },":",'
            '{ "Ref": "AWS::AccountId" },'
            '":function:cfnRedisEndpointLookup" ] }'
        )
        raw = Join(delimiter, source_string)
        actual = raw.to_dict()
        expected = {
            "Fn::Join": [
                ",",
                '{ [ "arn:aws:lambda:",{ "Ref": '
                '"AWS::Region" },":",{ "Ref": "AWS::AccountId" },'
                '":function:cfnRedisEndpointLookup" ] }',
            ]
        }
        self.assertEqual(expected, actual)

        with self.assertRaises(ValueError):
            Join(10, "foobar")


class TestValidation(unittest.TestCase):
    def test_validation(self):
        route = Route(
            "Route66",
            DestinationCidrBlock="0.0.0.0/0",
            RouteTableId=Ref("RouteTable66"),
            InstanceId=If("UseNat", Ref("AWS::NoValue"), Ref("UseNat")),
            NatGatewayId=If("UseNat", Ref("UseNat"), Ref("AWS::NoValue")),
        )
        t = Template()
        t.add_resource(route)
        with self.assertRaises(ValueError):
            t.to_json()

    def test_novalidation(self):
        route = Route(
            "Route66",
            validation=False,
            DestinationCidrBlock="0.0.0.0/0",
            RouteTableId=Ref("RouteTable66"),
            InstanceId=If("UseNat", Ref("AWS::NoValue"), Ref("UseNat")),
            NatGatewayId=If("UseNat", Ref("UseNat"), Ref("AWS::NoValue")),
        )
        t = Template()
        t.add_resource(route)
        t.to_json()

    def test_no_validation_method(self):
        route = Route(
            "Route66",
            DestinationCidrBlock="0.0.0.0/0",
            RouteTableId=Ref("RouteTable66"),
            InstanceId=If("UseNat", Ref("AWS::NoValue"), Ref("UseNat")),
            NatGatewayId=If("UseNat", Ref("UseNat"), Ref("AWS::NoValue")),
        ).no_validation()
        t = Template()
        t.add_resource(route)
        t.to_json()


test_updatereplacepolicy_yaml = """\
Resources:
  S3Bucket:
    Properties:
      AccessControl: PublicRead
    Type: AWS::S3::Bucket
    UpdateReplacePolicy: Retain
"""


class TestAttributes(unittest.TestCase):
    def test_BogusAttribute(self):
        t = Template()
        with self.assertRaises(AttributeError):
            t.add_resource(Bucket("S3Bucket", Bogus="Retain"))

    def test_UpdateReplacePolicy(self):
        t = Template()
        t.add_resource(
            Bucket(
                "S3Bucket",
                AccessControl=PublicRead,
                UpdateReplacePolicy="Retain",
            )
        )
        t.to_yaml()
        self.assertEqual(t.to_yaml(), test_updatereplacepolicy_yaml)


if __name__ == "__main__":
    unittest.main()
