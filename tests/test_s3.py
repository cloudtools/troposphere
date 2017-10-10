import unittest
from troposphere import Parameter, Ref, Template
from troposphere.s3 import AccelerateConfiguration, Bucket, Private


class TestBucketTemplate(unittest.TestCase):
    def test_bucket_template(self):
        title = 'PlaylistsFailoverS3Bucket'
        template = Template()
        Bucket(
            title,
            template,
            AccessControl=Private,
            BucketName="test-bucket",
        )
        self.assertIn(title, template.resources)


class TestBucket(unittest.TestCase):
    def test_bucket_accesscontrol(self):
        Bucket('b', AccessControl='AuthenticatedRead').validate()

    def test_bucket_accesscontrol_bad_string(self):
        with self.assertRaises(ValueError):
            Bucket('b', AccessControl='FooBar').validate()

    def test_bucket_accesscontrol_bad_type(self):
        with self.assertRaises(TypeError):
            Bucket('b', AccessControl=123).validate()

    def test_bucket_accesscontrol_ref(self):
        bucket_acl = Parameter('acl', Type='String', Default='Private')
        Bucket('b', AccessControl=Ref(bucket_acl)).validate()


class TestS3AccelerateConfiguration(unittest.TestCase):
    def test_accelerate_configuration_enabled(self):
        ac = AccelerateConfiguration(
            AccelerationStatus='Enabled',
        )
        self.assertEqual('Enabled', ac.AccelerationStatus)

    def test_accelerate_configuration_suspended(self):
        ac = AccelerateConfiguration(
            AccelerationStatus='Suspended',
        )
        self.assertEqual('Suspended', ac.AccelerationStatus)

    def test_accelerate_configuration_invalid_value(self):
        with self.assertRaises(ValueError):
            AccelerateConfiguration(AccelerationStatus='Invalid Value')

    def test_s3_bucket_accelerate_configuration(self):
        t = Template()
        ac = AccelerateConfiguration(AccelerationStatus="Enabled")

        b = Bucket("s3Bucket", AccelerateConfiguration=ac)
        t.add_resource(b)
        output = t.to_json()
        self.assertIn('"AccelerationStatus": "Enabled"', output)


if __name__ == '__main__':
    unittest.main()
