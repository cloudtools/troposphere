from . import AWSObject, AWSProperty
from .validators import boolean


class ParameterObjectAttribute(AWSProperty):
    props = {
        'Key': (basestring, True),
        'StringValue': (basestring, False),
    }


class ParameterObject(AWSProperty):
    props = {
        'Attributes': ([ParameterObjectAttribute], True),
        'Id': (basestring, True),
    }


class ParameterValue(AWSProperty):
    props = {
        'Id': (basestring, True),
        'StringValue': (basestring, True),
    }


class ObjectField(AWSProperty):
    props = {
        'Key': (basestring, True),
        'RefValue': (basestring, False),
        'StringValue': (basestring, False),
    }


class PipelineObject(AWSProperty):
    props = {
        'Fields': ([ObjectField], True),
        'Id': (basestring, True),
        'Name': (basestring, True),
    }


class PipelineTag(AWSProperty):
    props = {
        'Key': (basestring, True),
        'Value': (basestring, True),
    }


class Pipeline(AWSObject):
    resource_type = "AWS::DataPipeline::Pipeline"

    props = {
        'Activate': (boolean, False),
        'Description': (basestring, False),
        'Name': (basestring, True),
        'ParameterObjects': ([ParameterObject], False),
        'ParameterValues': ([ParameterValue], False),
        'PipelineObjects': ([PipelineObject], True),
        'PipelineTags': ([PipelineTag], False),
    }
