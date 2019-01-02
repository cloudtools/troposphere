# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import json_checker


class AuthenticationConfiguration(AWSProperty):
    props = {
        'DefaultAttributes': (json_checker, False),
        'DeviceTemplates': (json_checker, False),
    }


class SkillPackage(AWSProperty):
    props = {
        'ClientId': (basestring, True),
        'ClientSecret': (basestring, True),
        'RefreshToken': (basestring, True),
    }


class Skill(AWSObject):
    resource_type = "Alexa::ASK::Skill"

    props = {
        'AuthenticationConfiguration': (AuthenticationConfiguration, True),
        'SkillPackage': (SkillPackage, True),
        'VendorId': (basestring, True),
    }
