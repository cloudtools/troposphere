from . import AWSObject, Tags
from .validators import boolean


class Trail(AWSObject):
    resource_type = "AWS::CloudTrail::Trail"

    props = {
        'CloudWatchLogsLogGroupArn': (basestring, False),
        'CloudWatchLogsRoleArn': (basestring, False),
        'EnableLogFileValidation': (boolean, False),
        'IncludeGlobalServiceEvents': (boolean, False),
        'IsLogging': (boolean, True),
        'IsMultiRegionTrail': (boolean, False),
        'KMSKeyId': (basestring, False),
        'S3BucketName': (basestring, True),
        'S3KeyPrefix': (basestring, False),
        'SnsTopicName': (basestring, False),
        'Tags': (Tags, False),
    }
