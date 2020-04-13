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
        'ClientId': (basestring, True),
        'ClientSecret': (basestring, True),
        'RefreshToken': (basestring, True),
    }


class SkillPackage(AWSProperty):
    props = {
        'Overrides': (Overrides, False),
        'S3Bucket': (basestring, True),
        'S3BucketRole': (basestring, False),
        'S3Key': (basestring, True),
        'S3ObjectVersion': (basestring, False),
    }


class Skill(AWSObject):
    resource_type = "Alexa::ASK::Skill"

    props = {
        'AuthenticationConfiguration': (AuthenticationConfiguration, True),
        'SkillPackage': (SkillPackage, True),
        'VendorId': (basestring, True),
    }
