from . import AWSObject, AWSProperty, GetAtt
from .validators import positive_integer


class Code(AWSProperty):
    props = {
        'S3Bucket': (basestring, True),
        'S3Key': (basestring, True),
        'S3ObjectVersion': (basestring, False),
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
