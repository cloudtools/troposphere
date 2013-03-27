import unittest
from troposphere import AWSObject, Template
from troposphere.ec2 import Instance


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


def call_correct(x):
    return x


def call_incorrect(x):
    raise ValueError


class FakeAWSObject(AWSObject):
    props = {
        'callcorrect': (call_correct, False),
        'callincorrect': (call_incorrect, False),
        'singlelist': (list, False),
        'multilist': ([bool, int, float], False),
        'multituple': ((basestring, int), False),
    }

    def __init__(self, name, **kwargs):
        self.type = "Fake::AWS::Object"
        sup = super(FakeAWSObject, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)

    def validate(self):
        properties = self.properties
        name = self.name
        type = self.type
        if 'callcorrect' in properties and 'singlelist' in properties:
            raise ValueError(
                ("Cannot specify both 'callcorrect and 'singlelist' in "
                 "object %s (type %s)" % (name, type))
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
        FakeAWSObject('fake', multituple='a')
        FakeAWSObject('fake', multituple=10)
        with self.assertRaises(TypeError):
            FakeAWSObject('fake', multituple=0.1)


if __name__ == '__main__':
    unittest.main()
