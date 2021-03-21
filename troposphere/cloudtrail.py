from . import AWSObject, Tags, AWSProperty
from .validators import boolean


class DataResource(AWSProperty):
    props = {
        'Type': (str, True),
        'Values': ([str], False),
    }


class EventSelector(AWSProperty):
    props = {
        'DataResources': ([DataResource], False),
        'IncludeManagementEvents': (boolean, False),
        'ReadWriteType': (str, False),
    }


class Trail(AWSObject):
    resource_type = "AWS::CloudTrail::Trail"

    props = {
        'CloudWatchLogsLogGroupArn': (str, False),
        'CloudWatchLogsRoleArn': (str, False),
        'EnableLogFileValidation': (boolean, False),
        'EventSelectors': ([EventSelector], False),
        'IncludeGlobalServiceEvents': (boolean, False),
        'IsLogging': (boolean, True),
        'IsMultiRegionTrail': (boolean, False),
        'KMSKeyId': (str, False),
        'S3BucketName': (str, True),
        'S3KeyPrefix': (str, False),
        'SnsTopicName': (str, False),
        'Tags': (Tags, False),
        'TrailName': (str, False),
    }
