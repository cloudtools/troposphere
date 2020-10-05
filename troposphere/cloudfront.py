# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import (boolean, cloudfront_restriction_type,
                         cloudfront_event_type,
                         cloudfront_forward_type,
                         cloudfront_cache_cookie_behavior,
                         cloudfront_cache_header_behavior,
                         cloudfront_cache_query_string_behavior,
                         cloudfront_origin_request_cookie_behavior,
                         cloudfront_origin_request_header_behavior,
                         cloudfront_origin_request_query_string_behavior,
                         cloudfront_viewer_protocol_policy, integer,
                         positive_integer, priceclass_type, network_port)


class Cookies(AWSProperty):
    props = {
        'Forward': (cloudfront_forward_type, True),
        'WhitelistedNames': ([basestring], False),
    }


class ForwardedValues(AWSProperty):
    props = {
        'Cookies': (Cookies, False),
        'Headers': ([basestring], False),
        'QueryString': (boolean, True),
        'QueryStringCacheKeys': ([basestring], False),
    }


class LambdaFunctionAssociation(AWSProperty):
    props = {
        'EventType': (cloudfront_event_type, False),
        'LambdaFunctionARN': (basestring, False),
    }


class CacheBehavior(AWSProperty):
    props = {
        'AllowedMethods': ([basestring], False),
        'CachePolicyId': (basestring, False),
        'CachedMethods': ([basestring], False),
        'Compress': (boolean, False),
        'DefaultTTL': (integer, False),
        'FieldLevelEncryptionId': (basestring, False),
        'ForwardedValues': (ForwardedValues, False),
        'LambdaFunctionAssociations': ([LambdaFunctionAssociation], False),
        'MaxTTL': (integer, False),
        'MinTTL': (integer, False),
        'OriginRequestPolicyId': (basestring, False),
        'PathPattern': (basestring, True),
        'RealtimeLogConfigArn': (basestring, False),
        'SmoothStreaming': (boolean, False),
        'TargetOriginId': (basestring, True),
        'TrustedSigners': ([basestring], False),
        'ViewerProtocolPolicy': (cloudfront_viewer_protocol_policy, True),
    }


class DefaultCacheBehavior(AWSProperty):
    props = {
        'AllowedMethods': ([basestring], False),
        'CachePolicyId': (basestring, False),
        'CachedMethods': ([basestring], False),
        'Compress': (boolean, False),
        'DefaultTTL': (integer, False),
        'FieldLevelEncryptionId': (basestring, False),
        'ForwardedValues': (ForwardedValues, False),
        'LambdaFunctionAssociations': ([LambdaFunctionAssociation], False),
        'MaxTTL': (integer, False),
        'MinTTL': (integer, False),
        'OriginRequestPolicyId': (basestring, False),
        'RealtimeLogConfigArn': (basestring, False),
        'SmoothStreaming': (boolean, False),
        'TargetOriginId': (basestring, True),
        'TrustedSigners': (list, False),
        'ViewerProtocolPolicy': (cloudfront_viewer_protocol_policy, True),
    }


class S3Origin(AWSProperty):
    props = {
        'DomainName': (basestring, True),
        'OriginAccessIdentity': (basestring, False),
    }


class CustomOriginConfig(AWSProperty):
    props = {
        'HTTPPort': (network_port, False),
        'HTTPSPort': (network_port, False),
        'OriginKeepaliveTimeout': (integer, False),
        'OriginProtocolPolicy': (basestring, True),
        'OriginReadTimeout': (integer, False),
        'OriginSSLProtocols': ([basestring], False),
    }


class OriginCustomHeader(AWSProperty):
    props = {
        'HeaderName': (basestring, True),
        'HeaderValue': (basestring, True),
    }


class S3OriginConfig(AWSProperty):
    props = {
        'OriginAccessIdentity': (basestring, False),
    }


class Origin(AWSProperty):
    props = {
        'ConnectionAttempts': (integer, False),
        'ConnectionTimeout': (integer, False),
        'CustomOriginConfig': (CustomOriginConfig, False),
        'DomainName': (basestring, True),
        'Id': (basestring, True),
        'OriginCustomHeaders': ([OriginCustomHeader], False),
        'OriginPath': (basestring, False),
        'S3OriginConfig': (S3OriginConfig, False),
    }


class Logging(AWSProperty):
    props = {
        'Bucket': (basestring, True),
        'IncludeCookies': (boolean, False),
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
        'RestrictionType': (cloudfront_restriction_type, True),
    }


class Restrictions(AWSProperty):
    props = {
        'GeoRestriction': (GeoRestriction, True),
    }


class ViewerCertificate(AWSProperty):
    props = {
        'AcmCertificateArn': (basestring, False),
        'CloudFrontDefaultCertificate': (boolean, False),
        'IamCertificateId': (basestring, False),
        'MinimumProtocolVersion': (basestring, False),
        'SslSupportMethod': (basestring, False),
    }


class StatusCodes(AWSProperty):
    props = {
        'Items': ([integer], True),
        'Quantity': (integer, True),
    }


class OriginGroupFailoverCriteria(AWSProperty):
    props = {
        'StatusCodes': (StatusCodes, True),
    }


class OriginGroupMember(AWSProperty):
    props = {
        'OriginId': (basestring, True),
    }


class OriginGroupMembers(AWSProperty):
    props = {
        'Items': ([OriginGroupMember], False),
        'Quantity': (integer, False),
    }


class OriginGroup(AWSProperty):
    props = {
        'FailoverCriteria': (OriginGroupFailoverCriteria, True),
        'Id': (basestring, True),
        'Members': (OriginGroupMembers, True),
    }


class OriginGroups(AWSProperty):
    props = {
        'Items': ([OriginGroup], False),
        'Quantity': (integer, False),
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
        'HttpVersion': (basestring, False),
        'IPV6Enabled': (boolean, False),
        'Logging': (Logging, False),
        'Origins': ([Origin], True),
        'OriginGroups': (OriginGroups, False),
        'PriceClass': (priceclass_type, False),
        'Restrictions': (Restrictions, False),
        'ViewerCertificate': (ViewerCertificate, False),
        'WebACLId': (basestring, False),
    }


class Distribution(AWSObject):
    resource_type = "AWS::CloudFront::Distribution"

    props = {
        'DistributionConfig': (DistributionConfig, True),
        'Tags': ((Tags, list), False),
    }


class CloudFrontOriginAccessIdentityConfig(AWSProperty):
    props = {
        'Comment': (basestring, True),
    }


class CloudFrontOriginAccessIdentity(AWSObject):
    resource_type = "AWS::CloudFront::CloudFrontOriginAccessIdentity"

    props = {
        'CloudFrontOriginAccessIdentityConfig': (
            CloudFrontOriginAccessIdentityConfig,
            True,
        ),
    }


class TrustedSigners(AWSProperty):
    props = {
        'AwsAccountNumbers': ([basestring], False),
        'Enabled': (boolean, True),
    }


class StreamingDistributionConfig(AWSProperty):
    props = {
        'Aliases': ([basestring], False),
        'Comment': (basestring, True),
        'Enabled': (boolean, True),
        'Logging': (Logging, False),
        'PriceClass': (priceclass_type, False),
        'S3Origin': (S3Origin, True),
        'TrustedSigners': (TrustedSigners, True),
    }


class StreamingDistribution(AWSObject):
    resource_type = "AWS::CloudFront::StreamingDistribution"

    props = {
        'StreamingDistributionConfig': (StreamingDistributionConfig, True),
        'Tags': ((Tags, list), False),
    }


class CacheCookiesConfig(AWSProperty):
    props = {
        'CookieBehavior': (cloudfront_cache_cookie_behavior, True),
        'Cookies': ([basestring], False),
    }


class CacheHeadersConfig(AWSProperty):
    props = {
        'HeaderBehavior': (cloudfront_cache_header_behavior, True),
        'Headers': ([basestring], False),
    }


class CacheQueryStringsConfig(AWSProperty):
    props = {
        'QueryStringBehavior': (
            cloudfront_cache_query_string_behavior, True),
        'QueryStrings': ([basestring], False),
    }


class ParametersInCacheKeyAndForwardedToOrigin(AWSProperty):
    props = {
        'CookiesConfig': (CacheCookiesConfig, True),
        'EnableAcceptEncodingGzip': (boolean, True),
        'EnableAcceptEncodingBrotli': (boolean, False),
        'HeadersConfig': (CacheHeadersConfig, True),
        'QueryStringsConfig': (CacheQueryStringsConfig, True),
    }


class CachePolicyConfig(AWSProperty):
    props = {
        'Comment': (basestring, False),
        'DefaultTTL': (integer, True),
        'MaxTTL': (integer, True),
        'MinTTL': (integer, True),
        'Name': (basestring, True),
        'ParametersInCacheKeyAndForwardedToOrigin': (
            ParametersInCacheKeyAndForwardedToOrigin, True),
    }


class CachePolicy(AWSObject):
    resource_type = "AWS::CloudFront::CachePolicy"

    props = {
        'CachePolicyConfig': (CachePolicyConfig, True),
    }


class OriginRequestCookiesConfig(AWSProperty):
    props = {
        'CookieBehavior': (cloudfront_origin_request_cookie_behavior, True),
        'Cookies': ([basestring], False),
    }


class OriginRequestHeadersConfig(AWSProperty):
    props = {
        'HeaderBehavior': (cloudfront_origin_request_header_behavior, True),
        'Headers': ([basestring], False),
    }


class OriginRequestQueryStringsConfig(AWSProperty):
    props = {
        'QueryStringBehavior': (
            cloudfront_origin_request_query_string_behavior, True),
        'QueryStrings': ([basestring], False),
    }


class OriginRequestPolicyConfig(AWSProperty):
    props = {
        'Comment': (basestring, False),
        'CookiesConfig': (OriginRequestCookiesConfig, True),
        'HeadersConfig': (OriginRequestHeadersConfig, True),
        'Name': (basestring, True),
        'QueryStringsConfig': (OriginRequestQueryStringsConfig, True),
    }


class OriginRequestPolicy(AWSObject):
    resource_type = "AWS::CloudFront::OriginRequestPolicy"

    props = {
        'OriginRequestPolicyConfig': (OriginRequestPolicyConfig, True),
    }


class KinesisStreamConfig(AWSProperty):
    props = {
        'RoleArn': (basestring, True),
        'StreamArn': (basestring, True),
    }


class EndPoint(AWSProperty):
    props = {
        'KinesisStreamConfig': (KinesisStreamConfig, True),
        'StreamType': (basestring, True),
    }


class RealtimeLogConfig(AWSObject):
    resource_type = "AWS::CloudFront::RealtimeLogConfig"

    props = {
        'EndPoints': ([EndPoint], True),
        'Fields': ([basestring], True),
        'Name': (basestring, True),
        'SamplingRate': (float, True),
    }
