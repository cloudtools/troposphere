import unittest

from troposphere import Output, Ref, Sub, Template, s3
from troposphere.cloudformation import WaitCondition

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

cond_string = """My
special multiline
Handle"""

cond_normal = """Resources:
  MyWaitCondition:
    Properties:
      Handle: !Sub "My\\nspecial multiline\\nHandle"
      Timeout: '30'
    Type: AWS::CloudFormation::WaitCondition
"""

cond_long = """Resources:
  MyWaitCondition:
    Properties:
      Handle:
        Fn::Sub: "My\\nspecial multiline\\nHandle"
      Timeout: '30'
    Type: AWS::CloudFormation::WaitCondition
"""

cond_clean = """Resources:
  MyWaitCondition:
    Properties:
      Handle: !Sub |-
        My
        special multiline
        Handle
      Timeout: '30'
    Type: AWS::CloudFormation::WaitCondition
"""


class TestYAML(unittest.TestCase):
    def test_s3_bucket(self):
        t = Template()
        t.set_description("S3 Bucket Example")
        s3bucket = t.add_resource(
            s3.Bucket(
                "S3Bucket",
                AccessControl=s3.PublicRead,
            )
        )
        t.add_output(
            Output(
                "BucketName",
                Value=Ref(s3bucket),
                Description="Name of S3 bucket to hold website content",
            )
        )
        self.assertEqual(s3_bucket_yaml, t.to_yaml())

    def test_yaml_long_form(self):
        t = Template()
        t.add_resource(
            WaitCondition("MyWaitCondition", Timeout=30, Handle=Sub(cond_string))
        )
        self.assertEqual(cond_normal, t.to_yaml())
        self.assertEqual(cond_long, t.to_yaml(long_form=True))
        self.assertEqual(cond_long, t.to_yaml(False, True))
        self.assertEqual(cond_clean, t.to_yaml(clean_up=True))
        self.assertEqual(cond_clean, t.to_yaml(True))
