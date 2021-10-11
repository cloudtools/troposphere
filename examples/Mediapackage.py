from troposphere import Template
from troposphere.mediapackage import Channel, OriginEndpoint, OriginEndpointHlsPackage

t = Template()
t.set_version()

t.add_resource(Channel("MediaPackage", Id="MediaPackageChannel"))

t.add_resource(
    OriginEndpoint(
        "MediaPackageOriginEndpoint",
        ChannelId="MediaPackageChannel",
        Description="MediaPackage HLS endpoint",
        HlsPackage=OriginEndpointHlsPackage(
            ProgramDateTimeIntervalSeconds=0,
            PlaylistWindowSeconds=60,
            PlaylistType="NONE",
            IncludeIframeOnlyStream=False,
            SegmentDurationSeconds=6,
            UseAudioRenditionGroup=False,
        ),
        Id="MediaPackageOriginEndpoint",
        ManifestName="MediaPackageOriginEndpoint",
        Origination="ALLOW",
    )
)

print(t.to_json())
