from . import AWSObject, AWSProperty
from .validators import boolean, json_checker


class Device(AWSObject):
    resource_type = "AWS::IoT1Click::Device"

    props = {
        'DeviceId': (basestring, True),
        'Enabled': (boolean, True),
    }


class Placement(AWSObject):
    resource_type = "AWS::IoT1Click::Placement"

    props = {
        'AssociatedDevices': (json_checker, False),
        'Attributes': (json_checker, False),
        'PlacementName': (basestring, False),
        'ProjectName': (basestring, True),
    }


class PlacementTemplate(AWSProperty):
    props = {
        'DefaultAttributes': (json_checker, False),
        'DeviceTemplates': (json_checker, False),
    }


class Project(AWSObject):
    resource_type = "AWS::IoT1Click::Project"

    props = {
        'Description': (basestring, False),
        'PlacementTemplate': (PlacementTemplate, True),
        'ProjectName': (basestring, False),
    }
