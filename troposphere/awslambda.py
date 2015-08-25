from . import AWSObject, AWSProperty, GetAtt
from .validators import positive_integer


class Code(AWSProperty):
    props = {
        'S3Bucket': (basestring, False),
        'S3Key': (basestring, False),
        'S3ObjectVersion': (basestring, False),
        'ZipFile': (basestring, False)
    }

    def __init__(self, title=None, **kwargs):
        super(Code, self).__init__(title, **kwargs)

        if 'ZipFile' in kwargs:
            if 'S3Bucket' in kwargs:
                raise ValueError(
                    "You can't specify both 'S3Bucket' and 'ZipFile'"
                )
            elif 'S3Key' in kwargs:
                raise ValueError(
                    "You can't specify both 'S3Key' and 'ZipFile'"
                )
            elif 'S3ObjectVersion' in kwargs:
                raise ValueError(
                    "You can't specify both 'S3ObjectVersion' and 'ZipFile'"
                )
        else:  # ZipFile not specified
            if 'S3Bucket' not in kwargs or 'S3Key' not in kwargs:
                raise ValueError(
                    'You must specify a bucket location (both the S3Bucket '
                    'and S3Key properties) or the ZipFile property'
                )


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
