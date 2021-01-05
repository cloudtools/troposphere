import unittest
from troposphere import GetAtt, Template, Join, Ref
from troposphere.awslambda import Code, Function, Environment, ImageConfig


class TestAWSLambda(unittest.TestCase):

    def test_exclusive(self):
        lambda_func = Function(
            "AMIIDLookup",
            Handler="index.handler",
            Role=GetAtt("LambdaExecutionRole", "Arn"),
            Code=Code(
                S3Bucket="lambda-functions",
                S3Key="amilookup.zip",
            ),
            Runtime="nodejs",
            Timeout="25",
        )
        t = Template()
        t.add_resource(lambda_func)
        t.to_json()

    def test_zip_file(self):
        lambda_func = Function(
            "AMIIDLookup",
            Handler="index.handler",
            Role=GetAtt("LambdaExecutionRole", "Arn"),
            Code=Code(
                ZipFile=Join("", [
                    "var response = require('cfn-response');",
                    "exports.handler = function(event, context) {",
                    "  var input = parseInt(event.ResourceProperties.Input);",
                    "  var responseData = {Value: input * 5};",
                    "  response.send("
                    "    event, context, response.SUCCESS, responseData"
                    "  );",
                    "};"
                ]),
            ),
            Runtime="nodejs",
            Timeout="25",
        )
        t = Template()
        t.add_resource(lambda_func)
        t.to_json()

    def test_check_zip_file(self):
        positive_tests = [
            'a'*4096,
            Join('', ['a'*4096]),
            Join('', ['a', 10]),
            Join('', ['a'*4096, Ref('EmptyParameter')]),
            Join('ab', ['a'*2047, 'a'*2047]),
            GetAtt('foo', 'bar'),
        ]
        for z in positive_tests:
            Code.check_zip_file(z)
        negative_tests = [
            'a'*4097,
            Join('', ['a'*4097]),
            Join('', ['a'*4097, Ref('EmptyParameter')]),
            Join('abc', ['a'*2047, 'a'*2047]),
        ]
        for z in negative_tests:
            with self.assertRaises(ValueError):
                Code.check_zip_file(z)

    def test_environment_variable_invalid_name(self):
        for var in ['1', '2var', '_var', '/var']:
            with self.assertRaises(ValueError) as context:
                Environment(Variables={var: 'value'})

            self.assertTrue('Invalid environment variable name: %s' % var
                            in context.exception)

    def test_environment_variable_reserved(self):
        for var in ['AWS_ACCESS_KEY', 'AWS_ACCESS_KEY_ID',
                    'AWS_LAMBDA_FUNCTION_MEMORY_SIZE']:
            with self.assertRaises(ValueError) as context:
                Environment(Variables={var: 'value'})

            self.assertTrue("Lambda Function environment variables names "
                            "can't be none of"
                            in context.exception.args[0])

    def test_environment_variable_not_reserved(self):
        for var in ['NODE_PATH', 'NODE_ENV', 'FOO']:
            try:
                Environment(Variables={var: 'value'})
            except ValueError:
                self.fail("Environment() raised ValueError")

    def test_package_type_image(self):
        Function(
            "TestFunction",
            Code=Code(
                ImageUri="something"
            ),
            PackageType="Image",
            Role=GetAtt("LambdaExecutionRole", "Arn"),
        ).validate()

    def test_package_type_invalid(self):
        with self.assertRaises(ValueError):
            Function(
                "TestFunction",
                Code=Code(
                    ImageUri="something"
                ),
                PackageType="Invalid",
                Role=GetAtt("LambdaExecutionRole", "Arn"),
            ).validate()

    def test_package_type_zip(self):
        Function(
            "TestFunction",
            Code=Code(
                ZipFile=Join("", [
                    "var response = require('cfn-response');",
                    "exports.handler = function(event, context) {",
                    "  var input = parseInt(event.ResourceProperties.Input);",
                    "  var responseData = {Value: input * 5};",
                    "  response.send("
                    "    event, context, response.SUCCESS, responseData"
                    "  );",
                    "};"
                ]),
            ),
            Handler="index.handler",
            PackageType="Zip",
            Role=GetAtt("LambdaExecutionRole", "Arn"),
            Runtime="nodejs",
        ).validate()


class TestCode(unittest.TestCase):
    def test_validate_image_uri(self):
        Code(ImageUri="something").validate()

    def test_validate_image_and_zip(self):
        with self.assertRaises(ValueError):
            Code(ImageUri="something", ZipFile="something").validate()

    def test_validate_image_and_s3(self):
        s3_props = [
            {"S3Bucket": "bucket"},
            {"S3Key": "key"},
            {"S3ObjectVersion": "version"},
            {"S3Bucket": "bucket", "S3Key": "key"},
            {"S3Bucket": "bucket", "S3ObjectVersion": "version"},
            {"S3Key": "key", "S3ObjectVersion": "version"},
            {
                "S3Bucket": "bucket",
                "S3Key": "key",
                "S3ObjectVersion": "version"
            },
        ]
        for props in s3_props:
            with self.assertRaises(ValueError):
                Code(ImageUri="something", **props).validate()

    def test_validate_s3(self):
        Code(S3Bucket="bucket", S3Key="key").validate()
        Code(
            S3Bucket="bucket",
            S3Key="key",
            S3ObjectVersion="version"
        ).validate()

    def test_validate_s3_missing_required(self):
        s3_props = [
            {"S3Bucket": "bucket"},
            {"S3Key": "key"},
            {"S3ObjectVersion": "version"},
            {"S3Bucket": "bucket", "S3ObjectVersion": "version"},
            {"S3Key": "key", "S3ObjectVersion": "version"},
        ]
        for props in s3_props:
            with self.assertRaises(ValueError):
                Code(**props).validate()

    def test_validate_zip_and_s3(self):
        s3_props = [
            {"S3Bucket": "bucket"},
            {"S3Key": "key"},
            {"S3ObjectVersion": "version"},
            {"S3Bucket": "bucket", "S3Key": "key"},
            {"S3Bucket": "bucket", "S3ObjectVersion": "version"},
            {"S3Key": "key", "S3ObjectVersion": "version"},
            {
                "S3Bucket": "bucket",
                "S3Key": "key",
                "S3ObjectVersion": "version"
            },
        ]
        for props in s3_props:
            with self.assertRaises(ValueError):
                Code(ZipFile="something", **props).validate()


class TestImageConfig(unittest.TestCase):

    def test_validate_command(self):
        ImageConfig(Command=["something"] * 1500).validate()

    def test_validate_command_too_long(self):
        with self.assertRaises(ValueError):
            ImageConfig(Command=["something"] * 1501).validate()

    def test_validate_empty(self):
        ImageConfig().validate()

    def test_validate_entry_point(self):
        ImageConfig(EntryPoint=["something"] * 1500).validate()

    def test_validate_entry_point_too_long(self):
        with self.assertRaises(ValueError):
            ImageConfig(EntryPoint=["something"] * 1501).validate()

    def test_validate_working_directory(self):
        ImageConfig(WorkingDirectory="x" * 1000).validate()

    def test_validate_working_directory_too_long(self):
        with self.assertRaises(ValueError):
            ImageConfig(WorkingDirectory="x" * 1001).validate()


if __name__ == '__main__':
    unittest.main()
