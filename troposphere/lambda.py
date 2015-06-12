from . import AWSObject, AWSProperty
from .validators import integer


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
        'MemorySize': (integer, False),
        'Role': (basestring, True),
        'Runtime': (basestring, True),
        'Timeout': (integer, False),
    }
