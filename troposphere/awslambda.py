import re
from . import AWSObject, AWSProperty, Join, Tags
from .validators import boolean, integer, positive_integer

MEMORY_VALUES = [x for x in range(128, 3009, 64)]
RESERVED_ENVIRONMENT_VARIABLES = [
    'AWS_ACCESS_KEY',
    'AWS_ACCESS_KEY_ID',
    'AWS_DEFAULT_REGION',
    'AWS_EXECUTION_ENV',
    'AWS_LAMBDA_FUNCTION_MEMORY_SIZE',
    'AWS_LAMBDA_FUNCTION_NAME',
    'AWS_LAMBDA_FUNCTION_VERSION',
    'AWS_LAMBDA_LOG_GROUP_NAME',
    'AWS_LAMBDA_LOG_STREAM_NAME',
    'AWS_REGION',
    'AWS_SECRET_ACCESS_KEY',
    'AWS_SECRET_KEY',
    'AWS_SECURITY_TOKEN',
    'AWS_SESSION_TOKEN',
    'LAMBDA_RUNTIME_DIR',
    'LAMBDA_TASK_ROOT',
    'TZ'
]
ENVIRONMENT_VARIABLES_NAME_PATTERN = r'[a-zA-Z][a-zA-Z0-9_]+'


def validate_memory_size(memory_value):
    """ Validate memory size for Lambda Function
    :param memory_value: The memory size specified in the Function
    :return: The provided memory size if it is valid
    """
    memory_value = int(positive_integer(memory_value))
    if memory_value not in MEMORY_VALUES:
        raise ValueError("Lambda Function memory size must be one of:\n %s" %
                         ", ".join(str(mb) for mb in MEMORY_VALUES))
    return memory_value


def validate_variables_name(variables):
    for name in variables:
        if name in RESERVED_ENVIRONMENT_VARIABLES:
            raise ValueError("Lambda Function environment variables names"
                             " can't be none of:\n %s" %
                             ", ".join(RESERVED_ENVIRONMENT_VARIABLES))
        elif not re.match(ENVIRONMENT_VARIABLES_NAME_PATTERN, name):
            raise ValueError("Invalid environment variable name: %s" % name)

    return variables


class Code(AWSProperty):
    props = {
        'S3Bucket': (basestring, False),
        'S3Key': (basestring, False),
        'S3ObjectVersion': (basestring, False),
        'ZipFile': (basestring, False)
    }

    @staticmethod
    def check_zip_file(zip_file):
        maxlength = 4096
        toolong = (
            "ZipFile length cannot exceed %d characters. For larger "
            "source use S3Bucket/S3Key properties instead. "
            "Current length: %d"
        )

        if zip_file is None:
            return

        if isinstance(zip_file, basestring):
            z_length = len(zip_file)
            if z_length > maxlength:
                raise ValueError(toolong % (maxlength, z_length))
            return

        if isinstance(zip_file, Join):
            # This code tries to combine the length of all the strings in a
            # join. If a part is not a string, we do not count it (length 0).
            delimiter, values = zip_file.data['Fn::Join']

            # Return if there are no values to join
            if not values or len(values) <= 0:
                return

            # Get the length of the delimiter
            if isinstance(delimiter, basestring):
                d_length = len(delimiter)
            else:
                d_length = 0

            # Get the length of each value that will be joined
            v_lengths = [len(v) for v in values if isinstance(v, basestring)]

            # Add all the lengths together
            z_length = sum(v_lengths)
            z_length += (len(values)-1) * d_length

            if z_length > maxlength:
                raise ValueError(toolong % (maxlength, z_length))
            return

    def validate(self):
        zip_file = self.properties.get('ZipFile')
        s3_bucket = self.properties.get('S3Bucket')
        s3_key = self.properties.get('S3Key')
        s3_object_version = self.properties.get('S3ObjectVersion')

        if zip_file and s3_bucket:
            raise ValueError("You can't specify both 'S3Bucket' and 'ZipFile'")
        if zip_file and s3_key:
            raise ValueError("You can't specify both 'S3Key' and 'ZipFile'")
        if zip_file and s3_object_version:
            raise ValueError(
                "You can't specify both 'S3ObjectVersion' and 'ZipFile'"
            )
        Code.check_zip_file(zip_file)
        if not zip_file and not (s3_bucket and s3_key):
            raise ValueError(
                "You must specify a bucket location (both the 'S3Bucket' and "
                "'S3Key' properties) or the 'ZipFile' property"
            )


class VPCConfig(AWSProperty):

    props = {
        'SecurityGroupIds': (list, True),
        'SubnetIds': (list, True),
    }


class OnFailure(AWSProperty):
    props = {
        'Destination': (basestring, True),
    }


class OnSuccess(AWSProperty):
    props = {
        'Destination': (basestring, True),
    }


class DestinationConfig(AWSProperty):
    props = {
        'OnFailure': (OnFailure, False),
        'OnSuccess': (OnSuccess, False),
    }


class EventInvokeConfig(AWSObject):
    resource_type = "AWS::Lambda::EventInvokeConfig"

    props = {
        'DestinationConfig': (DestinationConfig, False),
        'FunctionName': (basestring, True),
        'MaximumEventAgeInSeconds': (integer, False),
        'MaximumRetryAttempts': (integer, False),
        'Qualifier': (basestring, True),
    }


class EventSourceMapping(AWSObject):
    resource_type = "AWS::Lambda::EventSourceMapping"

    props = {
        'BatchSize': (integer, False),
        'BisectBatchOnFunctionError': (boolean, False),
        'DestinationConfig': (DestinationConfig, False),
        'Enabled': (boolean, False),
        'EventSourceArn': (basestring, True),
        'FunctionName': (basestring, True),
        'MaximumBatchingWindowInSeconds': (integer, False),
        'MaximumRecordAgeInSeconds': (integer, False),
        'MaximumRetryAttempts': (integer, False),
        'ParallelizationFactor': (integer, False),
        'StartingPosition': (basestring, False),
        'Topics': ([basestring], False),
    }


class DeadLetterConfig(AWSProperty):
    props = {
        'TargetArn': (basestring, False),
    }


class Environment(AWSProperty):
    props = {
        'Variables': (validate_variables_name, True),
    }


class FileSystemConfig(AWSProperty):
    props = {
        'Arn': (basestring, True),
        'LocalMountPath': (basestring, True),
    }


class TracingConfig(AWSProperty):
    props = {
        'Mode': (basestring, False),
    }


class Function(AWSObject):
    resource_type = "AWS::Lambda::Function"

    props = {
        'Code': (Code, True),
        'Description': (basestring, False),
        'DeadLetterConfig': (DeadLetterConfig, False),
        'Environment': (Environment, False),
        'FileSystemConfigs': ([FileSystemConfig], False),
        'FunctionName': (basestring, False),
        'Handler': (basestring, True),
        'KmsKeyArn': (basestring, False),
        'MemorySize': (validate_memory_size, False),
        'Layers': ([basestring], False),
        'ReservedConcurrentExecutions': (positive_integer, False),
        'Role': (basestring, True),
        'Runtime': (basestring, True),
        'Tags': (Tags, False),
        'Timeout': (positive_integer, False),
        'TracingConfig': (TracingConfig, False),
        'VpcConfig': (VPCConfig, False),
    }


class Permission(AWSObject):
    resource_type = "AWS::Lambda::Permission"

    props = {
        'Action': (basestring, True),
        'EventSourceToken': (basestring, False),
        'FunctionName': (basestring, True),
        'Principal': (basestring, True),
        'SourceAccount': (basestring, False),
        'SourceArn': (basestring, False),
    }


class VersionWeight(AWSProperty):

    props = {
        'FunctionVersion': (basestring, True),
        'FunctionWeight': (float, True),
    }


class AliasRoutingConfiguration(AWSProperty):

    props = {
        'AdditionalVersionWeights': ([VersionWeight], True),
    }


class ProvisionedConcurrencyConfiguration(AWSProperty):

    props = {
        'ProvisionedConcurrentExecutions': (integer, True),
    }


class Alias(AWSObject):
    resource_type = "AWS::Lambda::Alias"

    props = {
        'Description': (basestring, False),
        'FunctionName': (basestring, True),
        'FunctionVersion': (basestring, True),
        'Name': (basestring, True),
        'ProvisionedConcurrencyConfig':
            (ProvisionedConcurrencyConfiguration, False),
        'RoutingConfig': (AliasRoutingConfiguration, False),
    }


class Version(AWSObject):
    resource_type = "AWS::Lambda::Version"

    props = {
        'CodeSha256': (basestring, False),
        'Description': (basestring, False),
        'FunctionName': (basestring, True),
        'ProvisionedConcurrencyConfig':
            (ProvisionedConcurrencyConfiguration, False),
    }


class Content(AWSProperty):
    props = {
        'S3Bucket': (basestring, True),
        'S3Key': (basestring, True),
        'S3ObjectVersion': (basestring, False),
    }


class LayerVersion(AWSObject):
    resource_type = "AWS::Lambda::LayerVersion"

    props = {
        'CompatibleRuntimes': ([basestring], False),
        'Content': (Content, True),
        'Description': (basestring, False),
        'LayerName': (basestring, False),
        'LicenseInfo': (basestring, False),
    }


class LayerVersionPermission(AWSObject):
    resource_type = "AWS::Lambda::LayerVersionPermission"

    props = {
        'Action': (basestring, True),
        'LayerVersionArn': (basestring, True),
        'OrganizationId': (basestring, False),
        'Principal': (basestring, True),
    }
