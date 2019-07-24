# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import AWSObject
from . import AWSProperty
from .validators import boolean
from .validators import integer


class CorsRule(AWSProperty):
    props = {
        'AllowedHeaders': ([basestring], False),
        'AllowedMethods': ([basestring], False),
        'AllowedOrigins': ([basestring], False),
        'ExposeHeaders': ([basestring], False),
        'MaxAgeSeconds': (integer, False),
    }


class Container(AWSObject):
    resource_type = "AWS::MediaStore::Container"

    props = {
        'AccessLoggingEnabled': (boolean, False),
        'ContainerName': (basestring, True),
        'CorsPolicy': ([CorsRule], False),
        'LifecyclePolicy': (basestring, False),
        'Policy': (basestring, False),
    }
