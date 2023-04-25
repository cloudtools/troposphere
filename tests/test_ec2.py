import unittest

import troposphere.ec2 as ec2
import troposphere.validators.ec2 as vec2


class TestEC2(unittest.TestCase):
    def test_securitygroupegress(self):
        egress = ec2.SecurityGroupEgress(
            "egress",
            ToPort="80",
            FromPort="80",
            IpProtocol="tcp",
            GroupId="id",
            CidrIp="0.0.0.0/0",
        )
        egress.to_dict()

        egress = ec2.SecurityGroupEgress(
            "egress",
            ToPort="80",
            FromPort="80",
            IpProtocol="tcp",
            GroupId="id",
            DestinationPrefixListId="id",
        )
        egress.to_dict()

        egress = ec2.SecurityGroupEgress(
            "egress",
            ToPort="80",
            FromPort="80",
            IpProtocol="tcp",
            GroupId="id",
            DestinationSecurityGroupId="id",
        )
        egress.to_dict()

        egress = ec2.SecurityGroupEgress(
            "egress",
            IpProtocol="-1",
            GroupId="id",
            DestinationSecurityGroupId="id",
        )
        egress.to_dict()

        egress = ec2.SecurityGroupEgress(
            "egress",
            IpProtocol="58",
            GroupId="id",
            DestinationSecurityGroupId="id",
        )
        egress.to_dict()

        egress = ec2.SecurityGroupEgress(
            "egress",
            ToPort="80",
            FromPort="80",
            IpProtocol="tcp",
            GroupId="id",
            CidrIp="0.0.0.0/0",
            DestinationPrefixListId="id",
        )
        with self.assertRaises(ValueError):
            egress.to_dict()

        # Test mutually exclusive fields
        egress = ec2.SecurityGroupEgress(
            "egress",
            ToPort="80",
            FromPort="80",
            IpProtocol="tcp",
            GroupId="id",
            CidrIp="0.0.0.0/0",
            DestinationPrefixListId="id",
            DestinationSecurityGroupId="id",
        )
        with self.assertRaises(ValueError):
            egress.to_dict()

        # Test no ToPort
        egress = ec2.SecurityGroupEgress(
            "egress",
            FromPort="80",
            IpProtocol="tcp",
            GroupId="id",
            CidrIp="0.0.0.0/0",
        )
        with self.assertRaises(ValueError):
            egress.to_dict()

        # Test no ToPort or FromPort
        egress = ec2.SecurityGroupEgress(
            "egress",
            IpProtocol="tcp",
            GroupId="id",
            CidrIp="0.0.0.0/0",
        )
        with self.assertRaises(ValueError):
            egress.to_dict()

    def test_vpn_conn_cannot_have_customer_gateway_and_transit_gateway(self):
        vpn = ec2.VPNConnection(
            "VPNConnection",
            CustomerGatewayId="cgw-0e11f167",
            VpnGatewayId="vgw-9a4cacf3",
            TransitGatewayId="tgw-b2b84747",
            Type="ipsec.1",
        )
        with self.assertRaises(ValueError):
            vpn.to_dict()

    def test_vpn_conn_with_correct_props(self):
        vpn = ec2.VPNConnection(
            "VPNConnection",
            StaticRoutesOnly=True,
            TransitGatewayId="tgw-b2b86767",
            CustomerGatewayId="cgw-0e11f167",
            Type="ipsec.1",
            VpnTunnelOptionsSpecifications=[
                ec2.VpnTunnelOptionsSpecification(
                    PreSharedKey="123_23626326236", TunnelInsideCidr="169.254.15.0/30"
                ),
                ec2.VpnTunnelOptionsSpecification(
                    PreSharedKey="asdf_fds12888", TunnelInsideCidr="169.254.16.0/30"
                ),
            ],
        )
        vpn.to_dict()

    def test_vpn_conn_tunnel_options_specification(self):
        ec2.VpnTunnelOptionsSpecification(
            PreSharedKey="12345678", TunnelInsideCidr="169.254.18.0/30"
        )

        with self.assertRaises(ValueError):
            ec2.VpnTunnelOptionsSpecification(
                PreSharedKey="1234567", TunnelInsideCidr="169.254.0.0/30"
            )

        with self.assertRaises(ValueError):
            ec2.VpnTunnelOptionsSpecification(
                PreSharedKey="0SAD_FEA_SDF", TunnelInsideCidr="192.168.16.0/30"
            )

    def test_validate_placement_strategy(self):
        for s in ("cluster", "spread", "partition"):
            vec2.validate_placement_strategy(s)

        with self.assertRaises(ValueError):
            vec2.validate_placement_strategy("notOk")

    def test_validate_placement_spread_level(self):
        for s in ("host", "rack"):
            vec2.validate_placement_spread_level(s)

        with self.assertRaises(ValueError):
            vec2.validate_placement_spread_level("notHostOrRack")
