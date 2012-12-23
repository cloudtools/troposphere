# Copyright (c) 2011-2012, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject


class ForwardedValues(AWSHelperFn):
    def __init__(self, querystring):
        if not isinstance(querystring, bool):
            raise TypeError
        self.data = {
            'QueryString': querystring,
        }

    def JSONrepr(self):
        return self.data


class DefaultCacheBehavior(AWSObject):
    props = {
        'TargetOriginId': (basestring, True),
        'ForwardedValues': (ForwardedValues, False),
        'TrustedSigners': (list, False),
        'ViewerProtocolPolicy': (basestring, False),
        'MinTTL': (basestring, False),
    }

    def __init__(self, **kwargs):
        sup = super(DefaultCacheBehavior, self)
        sup.__init__(None, None, None, self.props, **kwargs)


class S3Origin(AWSHelperFn):
    def __init__(self, originaccessidentity):
        if not isinstance(originaccessidentity, basestring):
            raise TypeError
        self.data = {
            'OriginAccessIdentity': originaccessidentity,
        }

    def JSONrepr(self):
        return self.data


class CustomOrigin(AWSObject):
    props = {
        'HTTPPort': (basestring, False),
        'HTTPSPort': (basestring, False),
        'OriginProtocolPolicy': (basestring, True),
    }

    def __init__(self, **kwargs):
        sup = super(CustomOrigin, self)
        sup.__init__(None, None, None, self.props, **kwargs)


class Origin(AWSObject):
    props = {
        'DomainName': (basestring, True),
        'Id': (basestring, True),
        'S3OriginConfig': (S3Origin, False),
        'CustomOriginConfig': (CustomOrigin, False),
    }

    def __init__(self, **kwargs):
        sup = super(Origin, self)
        sup.__init__(None, None, None, self.props, **kwargs)


class Logging(AWSObject):
    props = {
        'Bucket': (basestring, True),
        'Prefix': (basestring, False),
    }

    def __init__(self, **kwargs):
        sup = super(Logging, self)
        sup.__init__(None, None, None, self.props, **kwargs)


class DistributionConfig(AWSObject):
    props = {
        'Aliases': (list, False),
        'CacheBehaviors': (list, False),
        'Comment': (basestring, False),
        'DefaultCacheBehavior': (DefaultCacheBehavior, False),
        'DefaultRootObject': (basestring, False),
        'Enabled': (bool, True),
        'Logging': (Logging, False),
        'Origins': (list, True),
    }

    def __init__(self, **kwargs):
        sup = super(DistributionConfig, self)
        sup.__init__(None, None, None, self.props, **kwargs)


class Distribution(AWSObject):
    props = {
        'DistributionConfig': (DistributionConfig, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::CloudFront::Distribution"
        sup = super(Distribution, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
