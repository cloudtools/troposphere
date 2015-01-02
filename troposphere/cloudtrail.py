from . import AWSObject
from .validators import boolean


class Trail(AWSObject):
    resource_type = "AWS::CloudTrail::Trail"

    props = {
        'IncludeGlobalServiceEvents': (boolean, False),
        'IsLogging': (boolean, True),
        'S3BucketName': (basestring, True),
        'S3KeyPrefix': (basestring, False),
        'SnsTopicName': (basestring, False),
    }
