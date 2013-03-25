# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject
from .validators import integer


class AliasTarget(AWSHelperFn):
    def __init__(self, hostedzoneid, dnsname):
        self.data = {
            'HostedZoneId': hostedzoneid,
            'DNSName': dnsname,
        }

    def JSONrepr(self):
        return self.data


class BaseRecordSet(AWSObject):
    props = {
        'AliasTarget': (AliasTarget, False),
        'Comment': (basestring, False),
        'HostedZoneId': (basestring, False),
        'HostedZoneName': (basestring, False),
        'Name': (basestring, True),
        'Region': (basestring, False),
        'ResourceRecords': (list, False),
        'SetIdentifier': (basestring, False),
        'TTL': (integer, False),
        'Type': (basestring, True),
        'Weight': (integer, False),
    }

    def __init__(self, name, type, propname, **kwargs):
        sup = super(BaseRecordSet, self)
        sup.__init__(name, type, propname, self.props, **kwargs)


class RecordSetType(BaseRecordSet):
    # This is a top-level resource
    def __init__(self, name, **kwargs):
        self.type = "AWS::Route53::RecordSet"
        sup = super(RecordSetType, self)
        sup.__init__(name, self.type, "Properties", **kwargs)


class RecordSet(BaseRecordSet):
    # This is for use in a list with RecordSetGroup (below)
    def __init__(self, **kwargs):
        sup = super(RecordSet, self)
        sup.__init__(None, None, None, **kwargs)


class RecordSetGroup(AWSObject):
    props = {
        'HostedZoneId': (basestring, False),
        'HostedZoneName': (basestring, False),
        'RecordSets': (list, False),
        'Comment': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::Route53::RecordSetGroup"
        sup = super(RecordSetGroup, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
