# Copyright (c) 2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import (resourcequery_type)


class TagFilter(AWSProperty):
    props = {
        'Key': (basestring, False),
        'Values': ([basestring], False),
    }


class Query(AWSProperty):
    props = {
        'ResourceTypeFilters': ([basestring], False),
        'StackIdentifier': (basestring, False),
        'TagFilters': ([TagFilter], False),
    }


class ResourceQuery(AWSProperty):
    props = {
        'Query': (Query, False),
        'Type': (resourcequery_type, False),
    }


class Group(AWSObject):
    resource_type = "AWS::ResourceGroups::Group"

    props = {
        'Description': (basestring, False),
        'Name': (basestring, True),
        'ResourceQuery': (ResourceQuery, False),
        'Tags': (Tags, False),
    }
