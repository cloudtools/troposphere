# Converted from VPC_With_VPN_Connection.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import Join, Output, Parameter, Ref, Tags, Template
from troposphere.ec2 import (
    VPC,
    CustomerGateway,
    NetworkAcl,
    NetworkAclEntry,
    NetworkAclEntryPortRange,
    Route,
    RouteTable,
    Subnet,
    SubnetNetworkAclAssociation,
    SubnetRouteTableAssociation,
    VPCGatewayAttachment,
    VPNConnection,
    VPNConnectionRoute,
    VPNGateway,
)

t = Template()

t.set_version("2010-09-09")

t.set_description(
    """\
AWS CloudFormation Sample Template VPC_With_VPN_Connection.template: \
Sample template showing how to create a private subnet with a VPN connection \
using static routing to an existing VPN endpoint. NOTE: The VPNConnection \
created will define the configuration you need yonk the tunnels to your VPN \
endpoint - you can get the VPN Gateway configuration from the AWS Management \
console. You will be billed for the AWS resources used if you create a stack \
from this template."""
)
VPNAddress = t.add_parameter(
    Parameter(
        "VPNAddress",
        Type="String",
        Description="IP Address of your VPN device",
        MinLength="7",
        AllowedPattern=r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})",
        MaxLength="15",
        ConstraintDescription="must be a valid IP address of the form x.x.x.x",
    )
)

OnPremiseCIDR = t.add_parameter(
    Parameter(
        "OnPremiseCIDR",
        ConstraintDescription=("must be a valid IP CIDR range of the form x.x.x.x/x."),
        Description="IP Address range for your existing infrastructure",
        Default="10.0.0.0/16",
        MinLength="9",
        AllowedPattern=r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})",
        MaxLength="18",
        Type="String",
    )
)

VPCCIDR = t.add_parameter(
    Parameter(
        "VPCCIDR",
        ConstraintDescription=("must be a valid IP CIDR range of the form x.x.x.x/x."),
        Description="IP Address range for the VPN connected VPC",
        Default="10.1.0.0/16",
        MinLength="9",
        AllowedPattern=r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})",
        MaxLength="18",
        Type="String",
    )
)

SubnetCIDR = t.add_parameter(
    Parameter(
        "SubnetCIDR",
        ConstraintDescription=("must be a valid IP CIDR range of the form x.x.x.x/x."),
        Description="IP Address range for the VPN connected Subnet",
        Default="10.1.0.0/24",
        MinLength="9",
        AllowedPattern=r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})",
        MaxLength="18",
        Type="String",
    )
)

PrivateNetworkAcl = t.add_resource(
    NetworkAcl(
        "PrivateNetworkAcl",
        VpcId=Ref("VPC"),
        Tags=Tags(
            Application=Ref("AWS::StackName"),
            Network="Private",
        ),
    )
)

PrivateRoute = t.add_resource(
    Route(
        "PrivateRoute",
        GatewayId=Ref("VPNGateway"),
        DestinationCidrBlock="0.0.0.0/0",
        RouteTableId=Ref("PrivateRouteTable"),
    )
)

VPNGatewayAttachment = t.add_resource(
    VPCGatewayAttachment(
        "VPNGatewayAttachment",
        VpcId=Ref("VPC"),
        VpnGatewayId=Ref("VPNGateway"),
    )
)

PrivateSubnetRouteTableAssociation = t.add_resource(
    SubnetRouteTableAssociation(
        "PrivateSubnetRouteTableAssociation",
        SubnetId=Ref("PrivateSubnet"),
        RouteTableId=Ref("PrivateRouteTable"),
    )
)

PrivateSubnet = t.add_resource(
    Subnet(
        "PrivateSubnet",
        VpcId=Ref("VPC"),
        CidrBlock=Ref(SubnetCIDR),
        Tags=Tags(
            Application=Ref("AWS::StackName"),
            Network="VPN Connected Subnet",
        ),
    )
)

CustomerGatewayResource = t.add_resource(
    CustomerGateway(
        "CustomerGateway",
        BgpAsn="65000",
        IpAddress=Ref(VPNAddress),
        Type="ipsec.1",
        Tags=Tags(
            Application=Ref("AWS::StackName"),
            VPN=Join("", ["Gateway to ", Ref(VPNAddress)]),
        ),
    )
)

VPNConnectionRouteResource = t.add_resource(
    VPNConnectionRoute(
        "VPNConnectionRoute",
        VpnConnectionId=Ref("VPNConnection"),
        DestinationCidrBlock=Ref(OnPremiseCIDR),
    )
)

PrivateRouteTable = t.add_resource(
    RouteTable(
        "PrivateRouteTable",
        VpcId=Ref("VPC"),
        Tags=Tags(
            Application=Ref("AWS::StackName"),
            Network="VPN Connected Subnet",
        ),
    )
)

VPCResource = t.add_resource(
    VPC(
        "VPC",
        EnableDnsSupport="true",
        CidrBlock=Ref(VPCCIDR),
        EnableDnsHostnames="true",
        Tags=Tags(
            Application=Ref("AWS::StackName"),
            Network="VPN Connected VPC",
        ),
    )
)

OutBoundPrivateNetworkAclEntry = t.add_resource(
    NetworkAclEntry(
        "OutBoundPrivateNetworkAclEntry",
        NetworkAclId=Ref(PrivateNetworkAcl),
        RuleNumber="100",
        Protocol="6",
        PortRange=NetworkAclEntryPortRange(To="65535", From="0"),
        Egress="true",
        RuleAction="allow",
        CidrBlock="0.0.0.0/0",
    )
)

VPNGatewayResource = t.add_resource(
    VPNGateway(
        "VPNGateway",
        Type="ipsec.1",
        Tags=Tags(
            Application=Ref("AWS::StackName"),
        ),
    )
)

PrivateSubnetNetworkAclAssociation = t.add_resource(
    SubnetNetworkAclAssociation(
        "PrivateSubnetNetworkAclAssociation",
        SubnetId=Ref(PrivateSubnet),
        NetworkAclId=Ref(PrivateNetworkAcl),
    )
)

t.add_resource(
    VPNConnection(
        "VPNConnection",
        CustomerGatewayId=Ref(CustomerGatewayResource),
        StaticRoutesOnly="true",
        Type="ipsec.1",
        VpnGatewayId=Ref(VPNGatewayResource),
    )
)

InboundPrivateNetworkAclEntry = t.add_resource(
    NetworkAclEntry(
        "InboundPrivateNetworkAclEntry",
        NetworkAclId=Ref(PrivateNetworkAcl),
        RuleNumber="100",
        Protocol="6",
        PortRange=NetworkAclEntryPortRange(To="65535", From="0"),
        Egress="false",
        RuleAction="allow",
        CidrBlock="0.0.0.0/0",
    )
)

PrivateSubnet = t.add_output(
    Output(
        "PrivateSubnet",
        Description="SubnetId of the VPN connected subnet",
        Value=Ref(PrivateSubnet),
    )
)

VPCId = t.add_output(
    Output(
        "VPCId",
        Description="VPCId of the newly created VPC",
        Value=Ref(VPCResource),
    )
)

print(t.to_json())
