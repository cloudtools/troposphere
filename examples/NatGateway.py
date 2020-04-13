# Example Network with a NAT Gateway

from troposphere import Output, Ref, Template, Parameter, GetAtt
from troposphere import ec2


t = Template()

t.set_description(
    "AWS CloudFormation Sample Template NatGateway: Sample template showing "
    "how to create a public NAT gateway. "
    "**WARNING** This template creates an Amazon NAT gateway. "
    "You will be billed for the AWS resources used if you create "
    "a stack from this template.")

vpc_cidr = t.add_parameter(Parameter(
    'VPCCIDR',
    Default='172.18.0.0/16',
    Description='The IP address space for this VPC, in CIDR notation',
    Type='String',
))

public_subnet = t.add_parameter(Parameter(
    'PublicSubnetCidr',
    Type='String',
    Description='Public Subnet CIDR',
    Default='172.18.0.0/22',
))

private_subnet = t.add_parameter(Parameter(
    'PrivateSubnetCidr',
    Type='String',
    Description='Public Subnet CIDR',
    Default='172.18.32.0/21',
))

vpc = t.add_resource(ec2.VPC(
    'VPC',
    CidrBlock=Ref(vpc_cidr),
))

public_net = t.add_resource(ec2.Subnet(
    'PublicSubnet',
    CidrBlock=Ref(public_subnet),
    MapPublicIpOnLaunch=True,
    VpcId=Ref(vpc),
))

private_net = t.add_resource(ec2.Subnet(
    'PrivateSubnet',
    CidrBlock=Ref(private_subnet),
    MapPublicIpOnLaunch=False,
    VpcId=Ref(vpc),
))

igw = t.add_resource(ec2.InternetGateway('InternetGateway',))

net_gw_vpc_attachment = t.add_resource(ec2.VPCGatewayAttachment(
    "NatAttachment",
    VpcId=Ref(vpc),
    InternetGatewayId=Ref(igw),
))

private_route_table = t.add_resource(ec2.RouteTable(
    'PrivateRouteTable',
    VpcId=Ref(vpc),
))

public_route_table = t.add_resource(ec2.RouteTable(
    'PublicRouteTable',
    VpcId=Ref(vpc),
))

public_route_association = t.add_resource(ec2.SubnetRouteTableAssociation(
    'PublicRouteAssociation',
    SubnetId=Ref(public_net),
    RouteTableId=Ref(public_route_table),
))

default_public_route = t.add_resource(ec2.Route(
    'PublicDefaultRoute',
    RouteTableId=Ref(public_route_table),
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=Ref(igw),
))

private_route_association = t.add_resource(ec2.SubnetRouteTableAssociation(
    'PrivateRouteAssociation',
    SubnetId=Ref(private_net),
    RouteTableId=Ref(private_route_table),
))

nat_eip = t.add_resource(ec2.EIP(
    'NatEip',
    Domain="vpc",
))

nat = t.add_resource(ec2.NatGateway(
    'Nat',
    AllocationId=GetAtt(nat_eip, 'AllocationId'),
    SubnetId=Ref(public_net),
))

t.add_resource(ec2.Route(
    'NatRoute',
    RouteTableId=Ref(private_route_table),
    DestinationCidrBlock='0.0.0.0/0',
    NatGatewayId=Ref(nat),
))

t.add_output(Output(
    'VPCId',
    Value=Ref(vpc),
    Description='VPC Id'
))

t.add_output(Output(
    'NatEip',
    Value=Ref(nat_eip),
    Description='Nat Elastic IP',
))

print(t.to_json())
