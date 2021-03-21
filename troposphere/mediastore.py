# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import AWSObject, Tags
from . import AWSProperty
from .validators import boolean
from .validators import integer, containerlevelmetrics_status


class CorsRule(AWSProperty):
    props = {
        'AllowedHeaders': ([str], False),
        'AllowedMethods': ([str], False),
        'AllowedOrigins': ([str], False),
        'ExposeHeaders': ([str], False),
        'MaxAgeSeconds': (integer, False),
    }


class MetricPolicyRule(AWSProperty):
    props = {
        'ObjectGroup': (str, True),
        'ObjectGroupName': (str, True),
    }


class MetricPolicy(AWSProperty):
    props = {
        'ContainerLevelMetrics': (containerlevelmetrics_status, True),
        'MetricPolicyRules': ([MetricPolicyRule], False),
    }


class Container(AWSObject):
    resource_type = "AWS::MediaStore::Container"

    props = {
        'AccessLoggingEnabled': (boolean, False),
        'ContainerName': (str, True),
        'CorsPolicy': ([CorsRule], False),
        'LifecyclePolicy': (str, False),
        'MetricPolicy': (MetricPolicy, False),
        'Policy': (str, False),
        'Tags': (Tags, False),
    }
