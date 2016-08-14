from . import AWSObject, AWSProperty, Join
from .validators import positive_integer

MEMORY_VALUES = [x for x in range(128, 1600, 64)]


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
            return 0, True

        if isinstance(zip_file, basestring):
            zlength = len(zip_file)
            if zlength > maxlength:
                raise ValueError(toolong % (maxlength, zlength))
            return
        elif isinstance(zip_file, Join):
            # This code tries to determine if this is a Join with all
            # strings. If so, we try (best effort) to check the length.
            delimiter, values = zip_file.data['Fn::Join']
            if not isinstance(delimiter, basestring):
                return

            zlength = 0
            for v in values:
                # if it's not a list of strings, just return
                if not isinstance(v, basestring):
                    return
                zlength += len(v)
            zlength += (len(values)-1) * len(delimiter)

            if zlength > maxlength:
                raise ValueError(toolong % (maxlength, zlength))

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


class EventSourceMapping(AWSObject):
    resource_type = "AWS::Lambda::EventSourceMapping"

    props = {
        'BatchSize': (positive_integer, False),
        'Enabled': (bool, False),
        'EventSourceArn': (basestring, True),
        'FunctionName': (basestring, True),
        'StartingPosition': (basestring, True),
    }


class Function(AWSObject):
    resource_type = "AWS::Lambda::Function"

    props = {
        'Code': (Code, True),
        'Description': (basestring, False),
        'FunctionName': (basestring, False),
        'Handler': (basestring, True),
        'MemorySize': (validate_memory_size, False),
        'Role': (basestring, True),
        'Runtime': (basestring, True),
        'Timeout': (positive_integer, False),
        'VpcConfig': (VPCConfig, False),
    }


class Permission(AWSObject):
    resource_type = "AWS::Lambda::Permission"

    props = {
        'Action': (basestring, True),
        'FunctionName': (basestring, True),
        'Principal': (basestring, True),
        'SourceAccount': (basestring, False),
        'SourceArn': (basestring, False),
    }


class Alias(AWSObject):
    resource_type = "AWS::Lambda::Alias"

    props = {
        'Description': (basestring, False),
        'FunctionName': (basestring, True),
        'FunctionVersion': (basestring, True),
        'Name': (basestring, True),
    }


class Version(AWSObject):
    resource_type = "AWS::Lambda::Version"

    props = {
        'CodeSha256': (basestring, False),
        'Description': (basestring, False),
        'FunctionName': (basestring, True),
    }
