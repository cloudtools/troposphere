# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# Copyright (c) 2014, Andy Botting <andy.botting@theguardian.com>
# All rights reserved.
#
# See LICENSE file for full license.


from troposphere import AWSObject, AWSProperty
from troposphere.validators import (
    boolean,
    integer,
    integer_range,
    network_port,
    positive_integer,
)


class Firewall(AWSObject):
    resource_type = "OS::Neutron::Firewall"

    props = {
        "admin_state_up": (boolean, False),
        "description": (str, False),
        "firewall_policy_id": (str, True),
        "name": (str, False),
    }


class FirewallPolicy(AWSObject):
    resource_type = "OS::Neutron::FirewallPolicy"

    props = {
        "audited": (boolean, False),
        "description": (str, False),
        "firewall_rules": (list, True),
        "name": (str, False),
        "shared": (boolean, False),
    }


class FirewallRule(AWSObject):
    resource_type = "OS::Neutron::FirewallRule"

    props = {
        "action": (str, False),
        "description": (str, False),
        "destination_ip_address": (str, False),
        "destination_port": (network_port, False),
        "enabled": (boolean, False),
        "ip_version": (str, False),
        "name": (str, False),
        "protocol": (str, False),
        "shared": (boolean, False),
        "source_ip_address": (str, False),
        "source_port": (network_port, False),
    }

    def validate(self):
        if "action" in self.resource:
            action = self.resource["action"]
            if action not in ["allow", "deny"]:
                raise ValueError("The action attribute must be " "either allow or deny")

        if "ip_version" in self.resource:
            ip_version = self.resource["ip_version"]
            if ip_version not in ["4", "6"]:
                raise ValueError("The ip_version attribute must be " "either 4 or 6")

        if "protocol" in self.resource:
            protocol = self.resource["protocol"]
            if protocol not in ["tcp", "udp", "icmp", None]:
                raise ValueError(
                    "The protocol attribute must be " "either tcp, udp, icmp or None"
                )


class FloatingIP(AWSObject):
    resource_type = "OS::Neutron::FloatingIP"

    props = {
        "fixed_ip_address": (str, False),
        "floating_network_id": (str, True),
        "port_id": (str, False),
        "value_specs": (dict, False),
    }


class FloatingIPAssociation(AWSObject):
    resource_type = "OS::Neutron::FloatingIPAssociation"

    props = {
        "fixed_ip_address": (str, False),
        "floatingip_id": (str, True),
        "port_id": (str, False),
    }


class HealthMonitor(AWSObject):
    resource_type = "OS::Neutron::HealthMonitor"

    props = {
        "admin_state_up": (boolean, False),
        "delay": (positive_integer, True),
        "expected_codes": (str, False),
        "http_method": (str, False),
        "max_retries": (integer, True),
        "timeout": (integer, True),
        "type": (str, True),
        "url_path": (str, False),
    }

    def validate(self):

        if "type" in self.resource:
            mon_type = self.resource["type"]
            if mon_type not in ["PING", "TCP", "HTTP", "HTTPS"]:
                raise ValueError(
                    "The type attribute must be " "either PING, TCP, HTTP or HTTPS"
                )


class SessionPersistence(AWSProperty):
    props = {
        "cookie_name": (str, False),
        "type": (str, False),
    }

    def validate(self):
        if "type" in self.resource:
            if "cookie_name" not in self.resource:
                raise ValueError(
                    "The cookie_name attribute must be "
                    "given if session type is APP_COOKIE"
                )

            session_type = self.resource["type"]
            if session_type not in ["SOURCE_IP", "HTTP_COOKIE", "APP_COOKIE"]:
                raise ValueError(
                    "The type attribute must be "
                    "either SOURCE_IP, HTTP_COOKIE or APP_COOKIE"
                )


class VIP(AWSProperty):
    props = {
        "address": (str, False),
        "admin_state_up": (boolean, False),
        "connection_limit": (integer, True),
        "description": (str, False),
        "name": (str, False),
        "protocol_port": (network_port, True),
        "session_persistence": (SessionPersistence, False),
    }


class Pool(AWSObject):
    resource_type = "OS::Neutron::Pool"

    props = {
        "admin_state_up": (boolean, False),
        "description": (str, False),
        "lb_method": (str, True),
        "monitors": (list, False),
        "name": (str, False),
        "protocol": (str, True),
        "subnet_id": (str, True),
        "vip": (VIP, False),
    }

    def validate(self):

        if "lb_method" in self.resource:
            lb_method = self.resource["lb_method"]
            if lb_method not in ["ROUND_ROBIN", "LEAST_CONNECTIONS", "SOURCE_IP"]:
                raise ValueError(
                    "The lb_method attribute must be "
                    "either ROUND_ROBIN, LEAST_CONNECTIONS "
                    "or SOURCE_IP"
                )

        if "protocol" in self.resource:
            protocol = self.resource["protocol"]
            if protocol not in ["TCP", "HTTP", "HTTPS"]:
                raise ValueError(
                    "The type attribute must be " "either TCP, HTTP or HTTPS"
                )


class LoadBalancer(AWSObject):
    resource_type = "OS::Neutron::LoadBalancer"

    props = {
        "members": (list, False),
        "pool_id": (Pool, True),
        "protocol_port": (network_port, True),
    }


class Net(AWSObject):
    resource_type = "OS::Neutron::Net"

    props = {
        "admin_state_up": (boolean, False),
        "name": (str, False),
        "shared": (boolean, False),
        "tenant_id": (str, False),
        "value_specs": (dict, False),
    }


class PoolMember(AWSObject):
    resource_type = "OS::Neutron::PoolMember"

    props = {
        "address": (str, True),
        "admin_state_up": (boolean, False),
        "pool_id": (Pool, True),
        "protocol_port": (network_port, True),
        "weight": (integer_range(0, 256), False),
    }


class AddressPair(AWSProperty):
    props = {
        "ip_address": (str, True),
        "mac_address": (str, False),
    }


class FixedIP(AWSProperty):
    props = {
        "ip_address": (str, False),
        "subnet_id": (str, False),
    }


class Port(AWSObject):
    resource_type = "OS::Neutron::Port"

    props = {
        "admin_state_up": (boolean, False),
        "allowed_address_pairs": (list, False),
        "device_id": (str, False),
        "fixed_ips": (list, False),
        "mac_address": (str, False),
        "name": (str, False),
        "network_id": (str, True),
        "security_groups": (list, False),
        "value_specs": (dict, False),
    }


class SecurityGroup(AWSObject):
    resource_type = "OS::Neutron::SecurityGroup"

    props = {
        "description": (str, True),
        "name": (str, False),
        "rules": (list, False),
    }


class SecurityGroupRule(AWSProperty):
    props = {
        "direction": (str, False),
        "ethertype": (str, False),
        "port_range_max": (network_port, False),
        "port_range_min": (network_port, False),
        "protocol": (str, False),
        "remote_group_id": (str, False),
        "remote_ip_prefix": (str, False),
        "remote_mode": (str, False),
    }

    def validate(self):
        if "direction" in self.resource:
            direction = self.resource["direction"]
            if direction not in ["ingress", "egress"]:
                raise ValueError(
                    "The direction attribute must be " "either ingress or egress"
                )

        if "ethertype" in self.resource:
            ethertype = self.resource["ethertype"]
            if ethertype not in ["IPv4", "IPv6"]:
                raise ValueError(
                    "The ethertype attribute must be " "either IPv4 or IPv6"
                )

        if "protocol" in self.resource:
            protocol = self.resource["protocol"]
            if protocol not in ["tcp", "udp", "icmp"]:
                raise ValueError(
                    "The protocol attribute must be " "either tcp, udp or icmp"
                )

        if "remote_mode" in self.resource:
            remote_mode = self.resource["remote_mode"]
            if remote_mode not in ["remote_ip_prefix", "remote_group_id"]:
                raise ValueError(
                    "The remote_mode attribute must be "
                    "either remote_ip_prefix or remote_group_id"
                )
