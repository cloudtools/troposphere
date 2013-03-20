# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty


class ForwardedValues(AWSHelperFn):
    def __init__(self, querystring):
        if not isinstance(querystring, bool):
            raise TypeError
        self.data = {
            'QueryString': querystring,
        }

    def JSONrepr(self):
        return self.data


class DefaultCacheBehavior(AWSProperty):
    props = {
        'TargetOriginId': (basestring, True),
        'ForwardedValues': (ForwardedValues, False),
        'TrustedSigners': (list, False),
        'ViewerProtocolPolicy': (basestring, True),
        'MinTTL': (basestring, False),
    }


class S3Origin(AWSHelperFn):
    def __init__(self, originaccessidentity):
        if not isinstance(originaccessidentity, basestring):
            raise TypeError
        self.data = {
            'OriginAccessIdentity': originaccessidentity,
        }

    def JSONrepr(self):
        return self.data


class CustomOrigin(AWSProperty):
    props = {
        'HTTPPort': (basestring, False),
        'HTTPSPort': (basestring, False),
        'OriginProtocolPolicy': (basestring, True),
    }


class Origin(AWSProperty):
    props = {
        'DomainName': (basestring, True),
        'Id': (basestring, True),
        'S3OriginConfig': (S3Origin, False),
        'CustomOriginConfig': (CustomOrigin, False),
    }


class Logging(AWSProperty):
    props = {
        'Bucket': (basestring, True),
        'Prefix': (basestring, False),
    }


class DistributionConfig(AWSProperty):
    props = {
        'Aliases': (list, False),
        'CacheBehaviors': (list, False),
        'Comment': (basestring, False),
        'DefaultCacheBehavior': (DefaultCacheBehavior, True),
        'DefaultRootObject': (basestring, False),
        'Enabled': (bool, True),
        'Logging': (Logging, False),
        'Origins': (list, True),
    }


class Distribution(AWSObject):
    props = {
        'DistributionConfig': (DistributionConfig, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::CloudFront::Distribution"
        sup = super(Distribution, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
