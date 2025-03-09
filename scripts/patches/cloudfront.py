patches = [
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CloudFront::CachePolicy.CookiesConfig",
        "path": "/PropertyTypes/AWS::CloudFront::CachePolicy.CacheCookiesConfig",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CloudFront::CachePolicy.ParametersInCacheKeyAndForwardedToOrigin/Properties/CookiesConfig/Type",
        "value": "CacheCookiesConfig",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CloudFront::CachePolicy.HeadersConfig",
        "path": "/PropertyTypes/AWS::CloudFront::CachePolicy.CacheHeadersConfig",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CloudFront::CachePolicy.ParametersInCacheKeyAndForwardedToOrigin/Properties/HeadersConfig/Type",
        "value": "CacheHeadersConfig",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CloudFront::CachePolicy.QueryStringsConfig",
        "path": "/PropertyTypes/AWS::CloudFront::CachePolicy.CacheQueryStringsConfig",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CloudFront::CachePolicy.ParametersInCacheKeyAndForwardedToOrigin/Properties/QueryStringsConfig/Type",
        "value": "CacheQueryStringsConfig",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CloudFront::OriginRequestPolicy.CookiesConfig",
        "path": "/PropertyTypes/AWS::CloudFront::OriginRequestPolicy.OriginRequestCookiesConfig",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CloudFront::OriginRequestPolicy.OriginRequestPolicyConfig/Properties/CookiesConfig/Type",
        "value": "OriginRequestCookiesConfig",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CloudFront::OriginRequestPolicy.HeadersConfig",
        "path": "/PropertyTypes/AWS::CloudFront::OriginRequestPolicy.OriginRequestHeadersConfig",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CloudFront::OriginRequestPolicy.OriginRequestPolicyConfig/Properties/HeadersConfig/Type",
        "value": "OriginRequestHeadersConfig",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CloudFront::OriginRequestPolicy.QueryStringsConfig",
        "path": "/PropertyTypes/AWS::CloudFront::OriginRequestPolicy.OriginRequestQueryStringsConfig",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CloudFront::OriginRequestPolicy.OriginRequestPolicyConfig/Properties/QueryStringsConfig/Type",
        "value": "OriginRequestQueryStringsConfig",
    },
    # backward compatibility
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::CloudFront::Function/Properties/FunctionMetadata",
        "value": {
            "Type": "FunctionMetadata",
            "Required": False,
        },
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CloudFront::StreamingDistribution.Logging",
        "path": "/PropertyTypes/AWS::CloudFront::StreamingDistribution.StreamingDistributioniLogging",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CloudFront::StreamingDistribution.StreamingDistributionConfig/Properties/Logging/Type",
        "value": "StreamingDistributioniLogging",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::CloudFront::StreamingDistribution/Properties/Tags/Required",
        "value": False,
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CloudFront::StreamingDistribution.S3Origin/Properties/OriginAccessIdentity/Required",
        "value": False,
    },
    # CloudFront introduced yet another way to specify Tags. Since this conflicts with other uses of Tags in CloudFront,
    # We will remove it and handle it via a custom validator.
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::CloudFront::AnycastIpList.Tags",
    },
]
