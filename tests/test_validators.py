import unittest
from troposphere import Parameter, Ref, NoValue
from troposphere.validators import boolean, integer, integer_range
from troposphere.validators import positive_integer, network_port
from troposphere.validators import tg_healthcheck_port
from troposphere.validators import s3_bucket_name, encoding, status
from troposphere.validators import iam_path, iam_names, iam_role_name
from troposphere.validators import iam_group_name, iam_user_name, elb_name
from troposphere.validators import mutually_exclusive, notification_type
from troposphere.validators import notification_event, task_type
from troposphere.validators import compliance_level, operating_system


class TestValidators(unittest.TestCase):

    def test_boolean(self):
        for x in [True, "True", "true", 1, "1"]:
            self.assertEqual(boolean(x), "true", repr(x))
        for x in [False, "False", "false", 0, "0"]:
            self.assertEqual(boolean(x), "false", repr(x))
        for x in ["000", "111", "abc"]:
            with self.assertRaises(ValueError):
                boolean(x)

    def test_integer(self):
        self.assertEqual(integer(-1), -1)
        self.assertEqual(integer("-1"), "-1")
        self.assertEqual(integer(0), 0)
        self.assertEqual(integer("0"), "0")
        self.assertEqual(integer(65535), 65535)
        self.assertEqual(integer("65535"), "65535")
        self.assertEqual(integer(1.0), 1.0)
        with self.assertRaises(ValueError):
            integer("string")
        with self.assertRaises(ValueError):
            integer(object)
        with self.assertRaises(ValueError):
            integer(None)

    def test_positive_integer(self):
        for x in [0, 1, 65535]:
            positive_integer(x)
        for x in [-1, -10]:
            with self.assertRaises(ValueError):
                positive_integer(x)

    def test_integer_range(self):
        between_ten_and_twenty = integer_range(10, 20)
        self.assertEqual(between_ten_and_twenty(10), 10)
        self.assertEqual(between_ten_and_twenty(15), 15)
        self.assertEqual(between_ten_and_twenty(20), 20)
        for i in (-1, 9, 21, 1111111):
            with self.assertRaises(ValueError):
                between_ten_and_twenty(i)

    def test_network_port(self):
        for x in [-1, 0, 1, 1024, 65535]:
            network_port(x)
        for x in [-2, -10, 65536, 100000]:
            with self.assertRaises(ValueError):
                network_port(x)

    def test_network_port_ref(self):
        p = Parameter('myport')
        network_port(Ref(p))

    def test_tg_healthcheck_port(self):
        for x in ["traffic-port"]:
            tg_healthcheck_port(x)
        for x in [-1, 0, 1, 1024, 65535]:
            tg_healthcheck_port(x)
        for x in [-2, -10, 65536, 100000]:
            with self.assertRaises(ValueError):
                tg_healthcheck_port(x)

    def test_tg_healthcheck_port_ref(self):
        p = Parameter('myport')
        tg_healthcheck_port(Ref(p))

    def test_s3_bucket_name(self):
        for b in ['a'*3, 'a'*63, 'wick3d-sweet.bucket']:
            s3_bucket_name(b)
        for b in ['a'*2, 'a'*64, 'invalid_bucket', 'InvalidBucket']:
            with self.assertRaises(ValueError):
                s3_bucket_name(b)
        for b in ['.invalid', 'invalid.', 'invalid..bucket']:
            with self.assertRaises(ValueError):
                s3_bucket_name(b)
        for b in ['1.2.3.4', '11.22.33.44', '111.222.333.444']:
            with self.assertRaises(ValueError):
                s3_bucket_name(b)

    def test_elb_name(self):
        for b in ['a', 'a-a', 'aaa', 'a'*32,
                  'wick3d-elb-name', 'Wick3d-ELB-Name']:
            elb_name(b)
        for b in ['a'*33, 'invalid_elb', '-invalid-elb',
                  'invalid-elb-', '-elb-', '-a', 'a-']:
            with self.assertRaises(ValueError):
                elb_name(b)

    def test_encoding(self):
        for e in ['plain', 'base64']:
            encoding(e)
        for e in ['wrong_encdoing', 'base62']:
            with self.assertRaises(ValueError):
                encoding(e)

    def test_status(self):
        for s in ['Active', 'Inactive']:
            status(s)
        for s in ['active', 'idle']:
            with self.assertRaises(ValueError):
                status(s)

    def test_iam_names(self):
        for s in ['foobar.+=@-,', 'BARfoo789.+=@-,']:
            iam_names(s)
        for s in ['foo%', 'bar$']:
            with self.assertRaises(ValueError):
                iam_names(s)

    def test_iam_path(self):
        for s in ['/%s/' % ('a'*30), '/%s/' % ('a'*510)]:
            iam_path(s)
        for s in ['/%s/' % ('a'*511), '/%s/' % ('a'*1025)]:
            with self.assertRaises(ValueError):
                iam_path(s)

    def test_iam_role_name(self):
        for s in ['a'*30, 'a'*64]:
            iam_role_name(s)
        for s in ['a'*65, 'a'*128]:
            with self.assertRaises(ValueError):
                iam_role_name(s)

    def test_iam_group_name(self):
        for s in ['a'*64, 'a'*128]:
            iam_group_name(s)
        for s in ['a'*129, 'a'*256]:
            with self.assertRaises(ValueError):
                iam_group_name(s)

    def test_iam_user_name(self):
        for s in ['a', 'a'*64, 'A', 'Aa', 'A=,.@-']:
            iam_user_name(s)
        for s in ['', 'a'*65, 'a%', 'a#', 'A a']:
            with self.assertRaises(ValueError):
                iam_user_name(s)

    def test_mutually_exclusive(self):
        conds = ['a', 'b', 'c']
        mutually_exclusive('a', {"a": "apple"}, conds)
        mutually_exclusive('b', {"b": "banana"}, conds)
        mutually_exclusive('c', {"c": "carrot"}, conds)
        with self.assertRaises(ValueError):
            mutually_exclusive('ac', {"a": "apple", "c": "carrot"}, conds)
        with self.assertRaises(ValueError):
            mutually_exclusive(
                'abc', {"a": "apple", "b": "banana", "c": "carrot"}, conds
            )

    def test_mutually_exclusive_novalue(self):
        conds = ['a', 'b', 'c']
        properties = {
            'a': Ref("AWS::NoValue"),
            'b': NoValue,
            'c': "AWS::Region",
        }

        mutually_exclusive("a", properties, conds)

    def test_compliance_level(self):
        for s in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFORMATIONAL',
                  'UNSPECIFIED']:
            compliance_level(s)
        for s in ['crit', '', '%%', 'FORMATIONAL']:
            with self.assertRaises(ValueError):
                compliance_level(s)

    def test_notification_event(self):
        for l in [['All', 'InProgress', 'Success', 'TimedOut', 'Cancelled',
                  'Failed'], ['InProgress', 'TimedOut']]:
            notification_event(l)
        for l in [['', 'timeout', '%'], ['Inprogress', '@ll']]:
            with self.assertRaises(ValueError):
                notification_event(l)

    def test_notification_type(self):
        for s in ['Command', 'Invocation']:
            notification_type(s)
        for s in ['foo', '', 'command', 'Iinvocation']:
            with self.assertRaises(ValueError):
                notification_type(s)

    def test_operating_system(self):
        for s in ['WINDOWS', 'AMAZON_LINUX', 'UBUNTU',
                  'REDHAT_ENTERPRISE_LINUX']:
            operating_system(s)
        for s in ['', 'bar', 'AMAZONLINUX', 'LINUX']:
            with self.assertRaises(ValueError):
                operating_system(s)

    def test_task_type(self):
        for s in ['RUN_COMMAND', 'AUTOMATION', 'LAMBDA', 'STEP_FUNCTION']:
            task_type(s)
        for s in ['', 'foo', 'a', 'l@mbda', 'STEPFUNCTION']:
            with self.assertRaises(ValueError):
                task_type(s)


if __name__ == '__main__':
    unittest.main()
