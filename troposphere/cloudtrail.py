from . import AWSObject, Tags, AWSProperty
from .validators import boolean


class DataResource(AWSProperty):
    props = {
        'Type': (basestring, True),
        'Values': ([basestring], False),
    }


class EventSelector(AWSProperty):
    props = {
        'DataResources': ([DataResource], False),
        'IncludeManagementEvents': (boolean, False),
        'ReadWriteType': (basestring, False),
    }


class Trail(AWSObject):
    resource_type = "AWS::CloudTrail::Trail"

    props = {
        'CloudWatchLogsLogGroupArn': (basestring, False),
        'CloudWatchLogsRoleArn': (basestring, False),
        'EnableLogFileValidation': (boolean, False),
        'EventSelectors': ([EventSelector], False),
        'IncludeGlobalServiceEvents': (boolean, False),
        'IsLogging': (boolean, True),
        'IsMultiRegionTrail': (boolean, False),
        'KMSKeyId': (basestring, False),
        'S3BucketName': (basestring, True),
        'S3KeyPrefix': (basestring, False),
        'SnsTopicName': (basestring, False),
        'Tags': (Tags, False),
        'TrailName': (basestring, False),
    }
