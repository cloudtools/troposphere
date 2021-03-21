from . import AWSObject, AWSProperty
from .validators import boolean


class ParameterObjectAttribute(AWSProperty):
    props = {
        'Key': (str, True),
        'StringValue': (str, False),
    }


class ParameterObject(AWSProperty):
    props = {
        'Attributes': ([ParameterObjectAttribute], True),
        'Id': (str, True),
    }


class ParameterValue(AWSProperty):
    props = {
        'Id': (str, True),
        'StringValue': (str, True),
    }


class ObjectField(AWSProperty):
    props = {
        'Key': (str, True),
        'RefValue': (str, False),
        'StringValue': (str, False),
    }


class PipelineObject(AWSProperty):
    props = {
        'Fields': ([ObjectField], True),
        'Id': (str, True),
        'Name': (str, True),
    }


class PipelineTag(AWSProperty):
    props = {
        'Key': (str, True),
        'Value': (str, True),
    }


class Pipeline(AWSObject):
    resource_type = "AWS::DataPipeline::Pipeline"

    props = {
        'Activate': (boolean, False),
        'Description': (str, False),
        'Name': (str, True),
        'ParameterObjects': ([ParameterObject], False),
        'ParameterValues': ([ParameterValue], False),
        'PipelineObjects': ([PipelineObject], True),
        'PipelineTags': ([PipelineTag], False),
    }
