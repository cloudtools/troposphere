patches = [
    # backward compatibility - prefer Campaign.Limits over ApplicationSettings.Limits
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Pinpoint::ApplicationSettings.Limits",
    },
]
