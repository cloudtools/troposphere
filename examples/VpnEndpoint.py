from troposphere import Template, Tags
import troposphere.ec2 as ec2


t = Template()

t.add_resource(
    ec2.ClientVpnEndpoint(
        "myClientVpnEndpoint",
        AuthenticationOptions=[
            ec2.ClientAuthenticationRequest(
                Type="directory-service-authentication",
                ActiveDirectory=ec2.DirectoryServiceAuthenticationRequest(
                    DirectoryId="d-926example"
                ),
            )
        ],
        ClientCidrBlock="10.0.0.0/22",
        ConnectionLogOptions=ec2.ConnectionLogOptions(Enabled=False),
        Description="My Client VPN Endpoint",
        DnsServers=["11.11.0.1"],
        ServerCertificateArn=(
            "arn:aws:acm:us-east-1:111122223333:certificate/"
            "12345678-1234-1234-1234-123456789012"
        ),
        TagSpecifications=[
            ec2.TagSpecifications(
                ResourceType="client-vpn-endpoint",
                Tags=Tags(Purpose="Production"),
            )
        ],
        TransportProtocol="udp",
    )
)

print(t.to_json())
