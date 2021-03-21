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
        'WhitelistedNames': ([str], False),
    }


class ForwardedValues(AWSProperty):
    props = {
        'Cookies': (Cookies, False),
        'Headers': ([str], False),
        'QueryString': (boolean, True),
        'QueryStringCacheKeys': ([str], False),
    }


class LambdaFunctionAssociation(AWSProperty):
    props = {
        'EventType': (cloudfront_event_type, False),
        'IncludeBody': (boolean, False),
        'LambdaFunctionARN': (str, False),
    }


class CacheBehavior(AWSProperty):
    props = {
        'AllowedMethods': ([str], False),
        'CachePolicyId': (str, False),
        'CachedMethods': ([str], False),
        'Compress': (boolean, False),
        'DefaultTTL': (integer, False),
        'FieldLevelEncryptionId': (str, False),
        'ForwardedValues': (ForwardedValues, False),
        'LambdaFunctionAssociations': ([LambdaFunctionAssociation], False),
        'MaxTTL': (integer, False),
        'MinTTL': (integer, False),
        'OriginRequestPolicyId': (str, False),
        'PathPattern': (str, True),
        'RealtimeLogConfigArn': (str, False),
        'SmoothStreaming': (boolean, False),
        'TargetOriginId': (str, True),
        'TrustedKeyGroups': ([str], False),
        'TrustedSigners': ([str], False),
        'ViewerProtocolPolicy': (cloudfront_viewer_protocol_policy, True),
    }


class DefaultCacheBehavior(AWSProperty):
    props = {
        'AllowedMethods': ([str], False),
        'CachePolicyId': (str, False),
        'CachedMethods': ([str], False),
        'Compress': (boolean, False),
        'DefaultTTL': (integer, False),
        'FieldLevelEncryptionId': (str, False),
        'ForwardedValues': (ForwardedValues, False),
        'LambdaFunctionAssociations': ([LambdaFunctionAssociation], False),
        'MaxTTL': (integer, False),
        'MinTTL': (integer, False),
        'OriginRequestPolicyId': (str, False),
        'RealtimeLogConfigArn': (str, False),
        'SmoothStreaming': (boolean, False),
        'TargetOriginId': (str, True),
        'TrustedKeyGroups': ([str], False),
        'TrustedSigners': (list, False),
        'ViewerProtocolPolicy': (cloudfront_viewer_protocol_policy, True),
    }


class S3Origin(AWSProperty):
    props = {
        'DomainName': (str, True),
        'OriginAccessIdentity': (str, False),
    }


class CustomOriginConfig(AWSProperty):
    props = {
        'HTTPPort': (network_port, False),
        'HTTPSPort': (network_port, False),
        'OriginKeepaliveTimeout': (integer, False),
        'OriginProtocolPolicy': (str, True),
        'OriginReadTimeout': (integer, False),
        'OriginSSLProtocols': ([str], False),
    }


class OriginCustomHeader(AWSProperty):
    props = {
        'HeaderName': (str, True),
        'HeaderValue': (str, True),
    }


class S3OriginConfig(AWSProperty):
    props = {
        'OriginAccessIdentity': (str, False),
    }


class OriginShield(AWSProperty):
    props = {
        'Enabled': (boolean, True),
        'OriginShieldRegion': (str, False),
    }


class Origin(AWSProperty):
    props = {
        'ConnectionAttempts': (integer, False),
        'ConnectionTimeout': (integer, False),
        'CustomOriginConfig': (CustomOriginConfig, False),
        'DomainName': (str, True),
        'Id': (str, True),
        'OriginCustomHeaders': ([OriginCustomHeader], False),
        'OriginPath': (str, False),
        'OriginShield': (OriginShield, False),
        'S3OriginConfig': (S3OriginConfig, False),
    }


class Logging(AWSProperty):
    props = {
        'Bucket': (str, True),
        'IncludeCookies': (boolean, False),
        'Prefix': (str, False),
    }


class CustomErrorResponse(AWSProperty):
    props = {
        'ErrorCachingMinTTL': (positive_integer, False),
        'ErrorCode': (positive_integer, True),
        'ResponseCode': (positive_integer, False),
        'ResponsePagePath': (str, False),
    }


class GeoRestriction(AWSProperty):
    props = {
        'Locations': ([str], False),
        'RestrictionType': (cloudfront_restriction_type, True),
    }


class Restrictions(AWSProperty):
    props = {
        'GeoRestriction': (GeoRestriction, True),
    }


class ViewerCertificate(AWSProperty):
    props = {
        'AcmCertificateArn': (str, False),
        'CloudFrontDefaultCertificate': (boolean, False),
        'IamCertificateId': (str, False),
        'MinimumProtocolVersion': (str, False),
        'SslSupportMethod': (str, False),
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
        'OriginId': (str, True),
    }


class OriginGroupMembers(AWSProperty):
    props = {
        'Items': ([OriginGroupMember], False),
        'Quantity': (integer, False),
    }


class OriginGroup(AWSProperty):
    props = {
        'FailoverCriteria': (OriginGroupFailoverCriteria, True),
        'Id': (str, True),
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
        'Comment': (str, False),
        'CustomErrorResponses': ([CustomErrorResponse], False),
        'DefaultCacheBehavior': (DefaultCacheBehavior, True),
        'DefaultRootObject': (str, False),
        'Enabled': (boolean, True),
        'HttpVersion': (str, False),
        'IPV6Enabled': (boolean, False),
        'Logging': (Logging, False),
        'Origins': ([Origin], True),
        'OriginGroups': (OriginGroups, False),
        'PriceClass': (priceclass_type, False),
        'Restrictions': (Restrictions, False),
        'ViewerCertificate': (ViewerCertificate, False),
        'WebACLId': (str, False),
    }


class Distribution(AWSObject):
    resource_type = "AWS::CloudFront::Distribution"

    props = {
        'DistributionConfig': (DistributionConfig, True),
        'Tags': ((Tags, list), False),
    }


class CloudFrontOriginAccessIdentityConfig(AWSProperty):
    props = {
        'Comment': (str, True),
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
        'AwsAccountNumbers': ([str], False),
        'Enabled': (boolean, True),
    }


class StreamingDistributionConfig(AWSProperty):
    props = {
        'Aliases': ([str], False),
        'Comment': (str, True),
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
        'Cookies': ([str], False),
    }


class CacheHeadersConfig(AWSProperty):
    props = {
        'HeaderBehavior': (cloudfront_cache_header_behavior, True),
        'Headers': ([str], False),
    }


class CacheQueryStringsConfig(AWSProperty):
    props = {
        'QueryStringBehavior': (
            cloudfront_cache_query_string_behavior, True),
        'QueryStrings': ([str], False),
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
        'Comment': (str, False),
        'DefaultTTL': (integer, True),
        'MaxTTL': (integer, True),
        'MinTTL': (integer, True),
        'Name': (str, True),
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
        'Cookies': ([str], False),
    }


class OriginRequestHeadersConfig(AWSProperty):
    props = {
        'HeaderBehavior': (cloudfront_origin_request_header_behavior, True),
        'Headers': ([str], False),
    }


class OriginRequestQueryStringsConfig(AWSProperty):
    props = {
        'QueryStringBehavior': (
            cloudfront_origin_request_query_string_behavior, True),
        'QueryStrings': ([str], False),
    }


class OriginRequestPolicyConfig(AWSProperty):
    props = {
        'Comment': (str, False),
        'CookiesConfig': (OriginRequestCookiesConfig, True),
        'HeadersConfig': (OriginRequestHeadersConfig, True),
        'Name': (str, True),
        'QueryStringsConfig': (OriginRequestQueryStringsConfig, True),
    }


class OriginRequestPolicy(AWSObject):
    resource_type = "AWS::CloudFront::OriginRequestPolicy"

    props = {
        'OriginRequestPolicyConfig': (OriginRequestPolicyConfig, True),
    }


class KeyGroupConfig(AWSProperty):
    props = {
        'Comment': (str, False),
        'Items': ([str], True),
        'Name': (str, True),
    }


class KeyGroup(AWSObject):
    resource_type = "AWS::CloudFront::KeyGroup"

    props = {
        'KeyGroupConfig': (KeyGroupConfig, True),
    }


class PublicKeyConfig(AWSProperty):
    props = {
        'CallerReference': (str, True),
        'Comment': (str, False),
        'EncodedKey': (str, True),
        'Name': (str, True),
    }


class PublicKey(AWSObject):
    resource_type = "AWS::CloudFront::PublicKey"

    props = {
        'PublicKeyConfig': (PublicKeyConfig, True),
    }


class KinesisStreamConfig(AWSProperty):
    props = {
        'RoleArn': (str, True),
        'StreamArn': (str, True),
    }


class EndPoint(AWSProperty):
    props = {
        'KinesisStreamConfig': (KinesisStreamConfig, True),
        'StreamType': (str, True),
    }


class RealtimeLogConfig(AWSObject):
    resource_type = "AWS::CloudFront::RealtimeLogConfig"

    props = {
        'EndPoints': ([EndPoint], True),
        'Fields': ([str], True),
        'Name': (str, True),
        'SamplingRate': (float, True),
    }
