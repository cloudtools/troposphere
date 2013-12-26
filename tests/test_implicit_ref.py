import json
import unittest
from troposphere import awsencode, AWSObject, Output, Parameter
from troposphere import Template, Join


def to_json(t, indent=4, sort_keys=True, separators=(', ', ': ')):
    return json.dumps(t, cls=awsencode, indent=indent,
                      sort_keys=sort_keys, separators=separators)


class TestImplicitRef(unittest.TestCase):

    def setUp(self):
        self.maxDiff = 1000

    def assertJsonEquals(self, actual, expected):
        self.assertEqual(
            unicode(actual.to_json()),
            unicode(to_json(expected)))

    def test_implicit_ref_to_parameter_in_property(self):
        t = Template()
        p = Parameter('P', Type='String')
        t.add_parameter(p)
        t.add_resource(FakeAWSObject('fake', prop1=p))
        self.assertJsonEquals(t, {
            'Parameters': {
                'P': {'Type': 'String'}
            },
            'Resources': {
                'fake': {
                    'Type': "Fake::AWS::Object",
                    'Properties': {
                        'prop1': {
                            'Ref': "P"
                        }
                    }
                }
            }
        })

    def test_implicit_ref_in_a_tuple(self):
        t = Template()
        r1 = FakeAWSObject('r1')
        t.add_resource(r1)
        r2 = FakeAWSObject('r2', listproperty=[1, (2, r1)])
        t.add_resource(r2)
        self.assertJsonEquals(t, {
            'Resources': {
                'r1': {
                    'Type': "Fake::AWS::Object",
                },
                'r2': {
                    'Type': "Fake::AWS::Object",
                    'Properties': {
                        'listproperty': [
                            1,
                            [
                                2,
                                {'Ref': 'r1'}
                            ]
                        ]
                    }
                }
            }
        })

    def test_implicit_ref_to_resource_in_property(self):
        t = Template()
        r1 = FakeAWSObject('r1')
        t.add_resource(r1)
        r2 = FakeAWSObject('r2', prop1=r1)
        t.add_resource(r2)
        self.assertJsonEquals(t, {
            'Resources': {
                'r1': {
                    'Type': "Fake::AWS::Object",
                },
                'r2': {
                    'Type': "Fake::AWS::Object",
                    'Properties': {
                        'prop1': {
                            'Ref': "r1"
                        }
                    }
                },
            }
        })

    def test_implicit_ref_to_resource_deep_in_property(self):
        t = Template()
        r1 = FakeAWSObject('r1')
        t.add_resource(r1)
        r2 = FakeAWSObject('r2', listproperty=[{"somekey": r1}])
        t.add_resource(r2)
        self.assertJsonEquals(t, {
            'Resources': {
                'r1': {
                    'Type': "Fake::AWS::Object",
                },
                'r2': {
                    'Type': "Fake::AWS::Object",
                    'Properties': {
                        'listproperty': [{
                            'somekey': {'Ref': "r1"}
                        }]
                    }
                },
            }
        })

    def test_implicit_ref_in_output(self):
        t = Template()
        r1 = FakeAWSObject('r1')
        t.add_resource(r1)
        out = Output('out', Value=r1)
        t.add_output(out)
        self.assertJsonEquals(t, {
            'Outputs': {
                'out': {'Value': {'Ref': 'r1'}}
            },
            'Resources': {
                'r1': {
                    'Type': "Fake::AWS::Object",
                },
            }
        })

    def test_implicit_ref_deep_in_output(self):
        t = Template()
        r1 = FakeAWSObject('r1')
        t.add_resource(r1)
        out = Output('out', Value=Join("", ["Hello, ", r1]))
        t.add_output(out)
        self.assertJsonEquals(t, {
            'Outputs': {
                'out': {
                    'Value': {'Fn::Join': ["", ["Hello, ", {'Ref': 'r1'}]]}
                }
            },
            'Resources': {
                'r1': {
                    'Type': "Fake::AWS::Object",
                },
            }
        })


class FakeAWSObject(AWSObject):
    type = "Fake::AWS::Object"

    props = {
        'prop1': (basestring, False),
        'listproperty': (list, False),
    }


if __name__ == '__main__':
    unittest.main()
