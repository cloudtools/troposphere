# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty
from .validators import boolean, integer, positive_integer, network_port


class ForwardedValues(AWSHelperFn):
    def __init__(self, querystring):
        self.data = {
            'QueryString': boolean(querystring),
        }

    def JSONrepr(self):
        return self.data


class CacheBehavior(AWSProperty):
    props = {
        'AllowedMethods': ([basestring], False),
        'TargetOriginId': (basestring, True),
        'ForwardedValues': (ForwardedValues, True),
        'TrustedSigners': ([basestring], False),
        'ViewerProtocolPolicy': (basestring, True),
        'MinTTL': (integer, False),
        'PathPattern': (basestring, True),
        'SmoothStreaming': (boolean, False),
    }


class DefaultCacheBehavior(AWSProperty):
    props = {
        'AllowedMethods': ([basestring], False),
        'TargetOriginId': (basestring, True),
        'ForwardedValues': (ForwardedValues, False),
        'TrustedSigners': (list, False),
        'ViewerProtocolPolicy': (basestring, True),
        'MinTTL': (integer, False),
        'SmoothStreaming': (boolean, False),
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
        'HTTPPort': (network_port, False),
        'HTTPSPort': (network_port, False),
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


class CustomErrorResponse(AWSProperty):
    props = {
        'ErrorCachingMinTTL': (positive_integer, False),
        'ErrorCode': (positive_integer, True),
        'ResponseCode': (positive_integer, False),
        'ResponsePagePath': (basestring, False),
    }


class GeoRestriction(AWSProperty):
    props = {
        'Locations': ([basestring], False),
        'RestrictionType': (basestring, True),
    }


class Restrictions(AWSProperty):
    props = {
        'GeoRestriction': (GeoRestriction, True),
    }


class ViewerCertificate(AWSProperty):
    props = {
        'CloudFrontDefaultCertificate': (boolean, False),
        'IamCertificateId': (basestring, False),
        'SslSupportMethod': (basestring, False),
    }


class DistributionConfig(AWSProperty):
    props = {
        'Aliases': (list, False),
        'CacheBehaviors': ([CacheBehavior], False),
        'Comment': (basestring, False),
        'CustomErrorResponses': ([CustomErrorResponse], False),
        'DefaultCacheBehavior': (DefaultCacheBehavior, True),
        'DefaultRootObject': (basestring, False),
        'Enabled': (boolean, True),
        'Logging': (Logging, False),
        'Origins': (list, True),
        'PriceClass': (basestring, False),
        'Restrictions': (Restrictions, False),
        'ViewerCertificate': (ViewerCertificate, False),
    }


class Distribution(AWSObject):
    type = "AWS::CloudFront::Distribution"

    props = {
        'DistributionConfig': (DistributionConfig, True),
    }
