# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# Copyright (c) 2014, Andy Botting <andy.botting@theguardian.com>
# All rights reserved.
#
# See LICENSE file for full license.


from . import AWSObject, AWSProperty
from .validators import boolean, integer, integer_range, positive_integer
from .validators import network_port


class Firewall(AWSObject):
    type = "OS::Neutron::Firewall"

    props = {
        'admin_state_up': (boolean, False),
        'description': (basestring, False),
        'firewall_policy_id': (basestring, True),
        'name': (basestring, False),
    }


class FirewallPolicy(AWSObject):
    type = "OS::Neutron::FirewallPolicy"

    props = {
        'audited': (boolean, False),
        'description': (basestring, False),
        'firewall_rules': (list, True),
        'name': (basestring, False),
        'shared': (boolean, False),
    }


class HealthMonitor(AWSObject):
    type = "OS::Neutron::HealthMonitor"

    props = {
        'type': (basestring, True),
        'url_path': (basestring, False),
        'delay': (positive_integer, True),
        'max_retries': (positive_integer, True),
        'timeout': (positive_integer, True),
        'expected_codes': (basestring, False),
    }


class SessionPersistence(AWSProperty):
    props = {
        'cookie_name': (basestring, False),
        'type': (basestring, False),
    }

    def validate(self):
        if 'type' in self.resource:
            if 'cookie_name' not in self.resource:
                raise ValueError(
                    "The cookie_name attribute must be "
                    "given if session type is APP_COOKIE")

            session_type = self.resource['type']
            if session_type not in ['SOURCE_IP', 'HTTP_COOKIE', 'APP_COOKIE']:
                raise ValueError(
                    "The type attribute must be "
                    "either SOURCE_IP, HTTP_COOKIE or APP_COOKIE")

        return True


class VIP(AWSProperty):
    props = {
        'address': (basestring, False),
        'admin_state_up': (boolean, False),
        'connection_limit': (integer, True),
        'description': (basestring, False),
        'name': (basestring, False),
        'protocol_port': (network_port, True),
        'session_persistence': (SessionPersistence, False),
    }


class Pool(AWSObject):
    type = "OS::Neutron::Pool"

    props = {
        'admin_state_up': (boolean, False),
        'description': (basestring, False),
        'lb_method': (basestring, True),
        'monitors': (list, False),
        'name': (basestring, False),
        'protocol': (basestring, True),
        'subnet_id': (basestring, True),
        'vip': (VIP, False),
    }

    def validate(self):

        if 'lb_method' in self.resource:
            lb_method = self.resource['lb_method']
            if lb_method not in ['ROUND_ROBIN', 'LEAST_CONNECTIONS',
                                 'SOURCE_IP']:
                raise ValueError(
                    "The lb_method attribute must be "
                    "either ROUND_ROBIN, LEAST_CONNECTIONS "
                    "or SOURCE_IP")

        if 'protocol' in self.resource:
            protocol = self.resource['protocol']
            if protocol not in ['TCP', 'HTTP', 'HTTPS']:
                raise ValueError(
                    "The type attribute must be "
                    "either TCP, HTTP or HTTPS")

        return True


class PoolMember(AWSObject):
    type = "OS::Neutron::PoolMember"

    props = {
        'address': (basestring, True),
        'admin_state_up': (boolean, False),
        'pool_id': (Pool, True),
        'protocol_port': (network_port, True),
        'weight': (integer_range(0, 256), False),
    }


class LoadBalancer(AWSObject):
    type = "OS::Neutron::LoadBalancer"

    props = {
        'members': (list, False),
        'pool_id': (Pool, True),
        'protocol_port': (network_port, True),
    }


class AddressPair(AWSProperty):
    props = {
        'ip_address': (basestring, True),
        'mac_address': (basestring, False),
    }


class FixedIP(AWSProperty):
    props = {
        'ip_address': (basestring, False),
        'subnet_id': (basestring, False),
    }


class Port(AWSObject):
    type = "OS::Neutron::Port"

    props = {
        'admin_state_up': (boolean, False),
        'allowed_address_pairs': (list, False),
        'security_groups': (list, True),
        'device_id': (basestring, False),
        'fixed_ips': (list, False),
        'mac_address': (basestring, False),
        'name': (basestring, False),
        'network_id': (basestring, True),
        'security_groups': (list, False),
        'value_specs': (dict, False),
    }


class SecurityGroupRule(AWSProperty):
    props = {
        'direction': (basestring, False),
        'ethertype': (basestring, False),
        'port_range_max': (network_port, False),
        'port_range_min': (network_port, False),
        'protocol': (basestring, False),
        'remote_group_id': (basestring, False),
        'remote_ip_prefix': (basestring, False),
        'remote_mode': (basestring, False),
    }

    def validate(self):
        if 'direction' in self.resource:
            direction = self.resource['direction']
            if direction not in ['ingress', 'egress']:
                raise ValueError(
                    "The direction attribute must be "
                    "either ingress or egress")

        if 'ethertype' in self.resource:
            ethertype = self.resource['ethertype']
            if ethertype not in ['IPv4', 'IPv6']:
                raise ValueError(
                    "The ethertype attribute must be "
                    "either IPv4 or IPv6")

        if 'protocol' in self.resource:
            protocol = self.resource['protocol']
            if protocol not in ['tcp', 'udp', 'icmp']:
                raise ValueError(
                    "The protocol attribute must be "
                    "either tcp, udp or icmp")

        if 'remote_mode' in self.resource:
            remote_mode = self.resource['remote_mode']
            if remote_mode not in ['remote_ip_prefix', 'remote_group_id']:
                raise ValueError(
                    "The remote_mode attribute must be "
                    "either remote_ip_prefix or remote_group_id")

        return True


class SecurityGroup(AWSObject):
    type = "OS::Neutron::SecurityGroup"

    props = {
        'description': (basestring, True),
        'name': (basestring, False),
        'rules': (list, False),
    }
