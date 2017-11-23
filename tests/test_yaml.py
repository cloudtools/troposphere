import unittest
from troposphere import Template, Output, Ref
from troposphere import s3


s3_bucket_yaml = """\
Description: S3 Bucket Example
Outputs:
  BucketName:
    Description: Name of S3 bucket to hold website content
    Value: !Ref 'S3Bucket'
Resources:
  S3Bucket:
    Properties:
      AccessControl: PublicRead
    Type: AWS::S3::Bucket
"""


class TestYAML(unittest.TestCase):

    def test_s3_bucket(self):
        t = Template()
        t.add_description("S3 Bucket Example")
        s3bucket = t.add_resource(s3.Bucket(
            "S3Bucket", AccessControl=s3.PublicRead,))
        t.add_output(Output(
            "BucketName",
            Value=Ref(s3bucket),
            Description="Name of S3 bucket to hold website content"
        ))
        self.assertEqual(s3_bucket_yaml, t.to_yaml())
