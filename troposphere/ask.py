# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty


class Overrides(AWSProperty):
    props = {
        'Manifest': (dict, False),
    }


class AuthenticationConfiguration(AWSProperty):
    props = {
        'ClientId': (str, True),
        'ClientSecret': (str, True),
        'RefreshToken': (str, True),
    }


class SkillPackage(AWSProperty):
    props = {
        'Overrides': (Overrides, False),
        'S3Bucket': (str, True),
        'S3BucketRole': (str, False),
        'S3Key': (str, True),
        'S3ObjectVersion': (str, False),
    }


class Skill(AWSObject):
    resource_type = "Alexa::ASK::Skill"

    props = {
        'AuthenticationConfiguration': (AuthenticationConfiguration, True),
        'SkillPackage': (SkillPackage, True),
        'VendorId': (str, True),
    }
