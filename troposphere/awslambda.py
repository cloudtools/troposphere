from . import AWSObject, AWSProperty, GetAtt
from .validators import positive_integer


class Code(AWSProperty):
    props = {
        'S3Bucket': (basestring, False),
        'S3Key': (basestring, False),
        'S3ObjectVersion': (basestring, False),
        'ZipFile': (basestring, False)
    }

    def validate(self):
        zip_file = self.properties.get('ZipFile')
        s3_bucket = self.properties.get('S3Bucket')
        s3_key = self.properties.get('S3Key')
        s3_object_version = self.properties.get('SS3ObjectVersion')

        if zip_file and s3_bucket:
            raise ValueError("You can't specify both 'S3Bucket' and 'ZipFile'")
        if zip_file and s3_key:
            raise ValueError("You can't specify both 'S3Key' and 'ZipFile'")
        if zip_file and s3_object_version:
            raise ValueError(
                "You can't specify both 'S3ObjectVersion' and 'ZipFile'"
            )
        if not zip_file and not (s3_bucket and s3_key):
            raise ValueError(
                "You must specify a bucket location (both the 'S3Bucket' and "
                "'S3Key' properties) or the 'ZipFile' property"
            )


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
        'Handler': (basestring, True),
        'MemorySize': (positive_integer, False),
        'Role': ([basestring, GetAtt], True),
        'Runtime': (basestring, True),
        'Timeout': (positive_integer, False),
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
