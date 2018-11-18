import re
from enum import Enum, IntEnum
from typing import List

from base import ARMObject, ARMProperty, SubResource, SubResourceRef


class AddressSpace(ARMProperty):
    props = {
        'addressPrefixes': (list, False)
    }


class ServiceEndpointProperties(ARMProperty):
    props = {
        'service': (str, True),
        'locations': (list, True)
    }


class Subnet(ARMObject):
    # resource_type = 'Microsoft.Network/virtualNetworks/subnets'
    # apiVersion = "2018-04-01"
    props = {
        'addressPrefix': (str, True),
        'networkSecurityGroup': (SubResource, False),
        'serviceEndpoints': ((list, ServiceEndpointProperties), False)
    }

    @property
    def address_prefix(self) -> str:
        return self.properties['addressPrefix']


class VirtualNetwork(ARMObject):
    resource_type = 'Microsoft.Network/virtualNetworks'
    apiVersion = "2017-10-01"
    location = True

    props = {
        'addressSpace': (AddressSpace, False),
        'subnets': ((Subnet, list), False),
    }

    root_props = {
        'tags': (dict, False)
    }

    def subnet_ref(self, subnet_name):
        return "[{}]".format(self.subnet_id(subnet_name=subnet_name))

    def subnet_id(self, subnet_name):
        resource_group = self.source_resource_group
        if not resource_group and self.template:
            resource_group = self.template.designated_resource_group
        subnet_title = self.get_subnet(subnet_name).title
        if resource_group:
            return "resourceId('{0}', 'Microsoft.Network/virtualNetworks/subnets', '{1}', '{2}')" \
                .format(resource_group, self.title, subnet_title)
        else:
            return "resourceId('Microsoft.Network/virtualNetworks/subnets', '{0}', '{1}')" \
                .format(self.title, subnet_title)

    def get_subnet(self, subnet_name):
        return next(iter([x for x in self.properties['subnets'] if x.title == subnet_name]))


class ApplicationSecurityGroup(ARMObject):
    resource_type = 'Microsoft.Network/applicationSecurityGroups'
    apiVersion = "2017-10-01"
    location = True

    props = {}


class SecurityRule(ARMObject):
    props = {
        'description': (str, False),  # todo add validation on length
        'protocol': (str, True),  # todo add valiadtion on valid values: 'Tcp', 'Udp', and '*'
        'sourcePortRange': (str, False),  # todo add validation for all 'range' props
        'destinationPortRange': (str, False),
        'sourceAddressPrefix': (str, False),
    # only one of sourceAddressPrefix, sourceAddressPrefixes, sourceApplicationSecurityGroups should be non empty
        'sourceAddressPrefixes': ((list, str), False),
        'sourceApplicationSecurityGroups': ((list, SubResource), False),
        'destinationAddressPrefix': (str, False),
        'destinationAddressPrefixes': ((list, str), False),
        'destinationApplicationSecurityGroups': ((list, SubResource), False),
        'sourcePortRanges': ((list, str), False),
        'destinationPortRanges': ((list, str), False),
        'access': (str, True),  # todo add validation on values: 'Allow' and 'Deny'
        'priority': (int, False),
        'direction': (str, True)  # todo add validation on values: 'Inbound' and 'Outbound'
    }

    def validate(self):
        if 'destinationAddressPrefix' not in self.properties and \
           'destinationAddressPrefixes' not in self.properties and \
           'destinationApplicationSecurityGroups' not in self.properties:
            raise ValueError('Required security rule parameters are missing for security rule with name "{}". '
                             'Security rule must specify DestinationAddressPrefixes, DestinationAddressPrefix, or '
                             'DestinationApplicationSecurityGroups'.format(self.title))

        if 'sourceAddressPrefix' not in self.properties and \
           'sourceAddressPrefixes' not in self.properties and \
           'sourceApplicationSecurityGroups' not in self.properties:
            raise ValueError('Required security rule parameters are missing for security rule with name "{}". '
                             'Security rule must specify SourceAddressPrefixes, SourceAddressPrefix, or '
                             'SourceApplicationSecurityGroups'.format(self.title))


class PublicIPAddressDnsSettings(ARMProperty):
    props = {
        'domainNameLabel': (str, False),
        'fqdn': (str, False),
        'reverseFqdn': (str, False)
    }


class PublicIPAddressSku(ARMProperty):
    props = {
        'name': (str, True),
        'tier': (str, True)
    }


class PublicIPAddress(ARMObject):
    resource_type = 'Microsoft.Network/publicIPAddresses'
    apiVersion = "2017-10-01"
    location = True

    props = {
        'publicIPAllocationMethod': (str, False),  # todo add validation on values: 'Static' and 'Dynamic'
        'publicIPAddressVersion': (str, False),  # todo add validation on values: 'IPv4' and 'IPv6'. Default is 'IPv4'
        'dnsSettings': (PublicIPAddressDnsSettings, False)
    }

    root_props = {
        'tags': (dict, False),
        'sku': (PublicIPAddressSku, False)
    }


class NetworkInterfaceIPConfiguration(ARMObject):
    props = {
        'applicationGatewayBackendAddressPools': (SubResource, False),
        # 'loadBalancerBackendAddressPools': () - not implemented
        # 'loadBalancerInboundNatRules': () - not implemented
        'privateIPAddress': (str, False),
        'privateIPAllocationMethod': (str, False),  # todo add validation on values: 'Static' and 'Dynamic'
        'privateIPAddressVersion': (str, False),  # todo add validation on values: 'IPv4' and 'IPv6'. Default is 'IPv4'
        'subnet': (SubResource, False),
        'primary': (bool, False),
        'publicIPAddress': (SubResource, False),
        'applicationSecurityGroups': ((list, SubResource), False)
    }

    @property
    def backend_address_pools(self):
        return self.properties['applicationGatewayBackendAddressPools']

    @property
    def public_ip_address(self):
        return self.properties['privateIPAddress']

    @backend_address_pools.setter
    def backend_address_pools(self, value):
        self.properties['applicationGatewayBackendAddressPools'] = value

    @public_ip_address.setter
    def public_ip_address(self, value):
        self.properties['privateIPAddress'] = value


class NetworkInterfaceIPConfigurationRef(SubResourceRef):
    def __init__(self, nic_name: str, nic_ip_conf: NetworkInterfaceIPConfiguration):
        super(NetworkInterfaceIPConfigurationRef, self).__init__(NetworkInterface, 'ipConfigurations', nic_name, nic_ip_conf)

class NetworkInterfaceDnsSettings(ARMProperty):
    props = {
        'dnsServers': ((list, str), False),
        'appliedDnsServers': ((list, str), False),
        'internalDnsNameLabel': (str, False),
        'internalFqdn': (str, False),
        'internalDomainNameSuffix': (str, False),
    }


class NetworkSecurityGroup(ARMObject):
    resource_type = 'Microsoft.Network/networkSecurityGroups'
    apiVersion = "2017-10-01"
    location = True

    props = {
        'securityRules': ((list, SecurityRule), False)
    }

    root_props = {
        'tags': (dict, False)
    }


class NetworkInterface(ARMObject):
    resource_type = 'Microsoft.Network/networkInterfaces'
    apiVersion = "2017-10-01"
    location = True

    props = {
        'virtualMachine': (SubResource, False),
        'networkSecurityGroup': ((SubResource, NetworkSecurityGroup), False),
        'ipConfigurations': ([NetworkInterfaceIPConfiguration], True),
        'dnsSettings': (NetworkInterfaceDnsSettings, False)
    }

    root_props = {
        'tags': (dict, False)
    }

    @property
    def ip_configurations(self) -> List[NetworkInterfaceIPConfiguration]:
        return self.properties['ipConfigurations']

    def validate(self):
        # validate ipConfigurations list item types
        if self.properties['ipConfigurations']:
            ip_confs = self.properties['ipConfigurations']
            for ip_conf in ip_confs:
                if not isinstance(ip_conf, NetworkInterfaceIPConfiguration):
                    raise ValueError("ipConfigurations in NetworkInterface must contain "
                                     "NetworkInterfaceIPConfiguration objects")


class LoadBalancerSku(ARMProperty):
    props = {'name': (str, True)}

    def validate(self):
        if self.resource['name'] not in ["Basic", "Standard"]:
            raise ValueError("Name of a load balancer SKU is not correct. Possible values are Basic or Standard")


class FrontendIPConfiguration(ARMObject):
    resource_type = 'Microsoft.Network/applicationGateways/frontendIPConfigurations'
    props = {
        'privateIPAddress': (str, False),
        'privateIPAllocationMethod': (str, False),  # Possible values are: 'Static' and 'Dynamic'
        'subnet': (SubResource, False),
        'publicIPAddress': (SubResource, False),
        'zones': ([str], False)
    }

    def to_dict(self):
        self._move_prop_to_root('zones')
        return ARMObject.to_dict(self)


class FrontendIPConfigurationRef(SubResourceRef):
    def __init__(self, load_balancer, ip_conf):
        super(FrontendIPConfigurationRef, self).__init__(LoadBalancer, 'frontendIpConfigurations', load_balancer,
                                                         ip_conf)

# class FrontendPortRef(SubResourceRef):
#     def __init__(self, app_gateway, ip_conf):
#         super(FrontendPortRef, self).__init__(ApplicationGatway, 'frontendPorts', app_gateway, frontend_port)

class ProbeRef(SubResourceRef):
    def __init__(self, load_balancer, probe):
        super(ProbeRef, self).__init__(LoadBalancer, 'probes', load_balancer, probe)


class BackendAddressPoolRef(SubResourceRef):
    def __init__(self, load_balancer, backend_pool):
        super(BackendAddressPoolRef, self).__init__(LoadBalancer, 'backendAddressPools', load_balancer, backend_pool)


class LoadBalancingRule(ARMObject):
    props = {
        'frontendIPConfiguration': (FrontendIPConfigurationRef, False),
        'backendAddressPool': (BackendAddressPoolRef, False),
        'probe': (ProbeRef, False),
        'protocol': (str, True),  # Udp, Tcp, All
        'loadDistribution': (str, False),  # Possible values are 'Default', 'SourceIP', and 'SourceIPProtocol'
        'frontendPort': (int, True),  # 0-65534, when 0 is "Any port"
        'backendPort': (int, False),  # 0-65534, when 0 is "Any port"
        'idleTimeoutInMinutes': (int, False),
    # The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP.
        'enableFloatingIP': (bool, False),
        'disableOutboundSnat': (False, False),
    }


class Probe(ARMObject):
    props = {
        'protocol': (str, True),  # The protocol of the end point. Possible values are: 'Http' or 'Tcp'. If 'Tcp' is specified, a received ACK is required for the probe to be successful. If 'Http' is specified, a 200 OK response from the specifies URI is required for the probe to be successful. - Http or Tcp
        'port': (int, True),  # The port for communicating the probe. Possible values range from 1 to 65535, inclusive.
        'intervalInSeconds': (int, False),  # The interval, in seconds, for how frequently to probe the endpoint for health status. Typically, the interval is slightly less than half the allocated timeout period (in seconds) which allows two full probes before taking the instance out of rotation. The default value is 15, the minimum value is 5.
        'numberOfProbes': (int, False),  # The number of probes where if no response, will result in stopping further traffic from being delivered to the endpoint. This values allows endpoints to be taken out of rotation faster or slower than the typical times used in Azure.
        'requestPath': (str, False),  # The URI used for requesting health status from the VM. Path is required if a protocol is set to http. Otherwise, it is not allowed. There is no default value.
    }


class ApplicationGatewayBackendAddress(ARMProperty):
    props = {
      'ipAddress': (str, True)
    }


class BackendAddressPool(ARMObject):
    resource_type = 'Microsoft.Network/applicationGateways/backendAddressPools'
    props = {
      'backendAddresses': ([ApplicationGatewayBackendAddress], False),
      'backendIPConfigurations': ([NetworkInterfaceIPConfigurationRef], False)
    }

    @property
    def backend_addresses(self) -> [ApplicationGatewayBackendAddress]:
        return self.properties['backendAddresses']


class LoadBalancer(ARMObject):
    resource_type = 'Microsoft.Network/loadBalancers'
    apiVersion = "2017-10-01"
    location = True

    props = {
        'frontendIPConfigurations': ([FrontendIPConfiguration], False),
        'backendAddressPools': ([BackendAddressPool], False),
        'loadBalancingRules': ([LoadBalancingRule], False),
        'probes': ([Probe], False),
        # 'inboundNatRules': ([InboundNatRule], False),
        # 'inboundNatPools': ([InboundNatPool], False),
        # 'outboundNatRules': ([OutboundNatRule], False),
        # 'resources': [inboundNatRules]
    }

    root_props = {
        'sku': (LoadBalancerSku, True),
        'tags': (dict, False)
    }


class ARecord(ARMProperty):
    props = {
        'ipv4Address': (str, True)
    }


class DnsZoneA(ARMObject):
    resource_type = 'Microsoft.Network/dnsZones/A'
    apiVersion = '2017-10-01'

    name_pattern = re.compile(r'^([a-zA-Z0-9]+(-[a-zA-Z0-9]+)*\.)+[a-zA-Z]{2,}\/([a-zA-Z0-9]+(-[a-zA-Z0-9]+)*)+$')

    props = {
        'TTL': (int, False),
        'ARecords': ([ARecord], False)
    }

    def validate_title(self):
        if not DnsZoneA.name_pattern.match(self.title):
            raise ValueError('Name "%s" is not valid' % self.title)


class ZoneType(Enum):
    Private = 0
    Public = 1


class DnsZone(ARMObject):
    resource_type = 'Microsoft.Network/dnsZones'
    apiVersion = '2017-10-01'
    location = True
    domain_name_pattern = re.compile(r'^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$')

    props = {
        'registrationVirtualNetworks': ([SubResource], False),
        'resolutionVirtualNetworks': ([SubResource], False),
        'zoneType': (str, False)
    }

    root_props = {
        'location': (str, True),
        'tags': (dict, False)
    }

    def validate_title(self):
        if not DnsZone.domain_name_pattern.match(self.title):
            raise ValueError('Name "%s" is not valid' % self.title)


class ApplicationGatewayFrontendPort(ARMObject):
    resource_type = 'Microsoft.Network/applicationGateways/frontendPorts'
    props = {
        'port': (int, True)
    }


class ApplicationGatewayConnectionDraining(ARMProperty):
    props = {
        'enabled': (bool, False),
        'drainTimeoutInSec': (int, False)
    }


class ApplicationGatewayBackendHttpSettings(ARMObject):
    resource_type = 'Microsoft.Network/applicationGateways/backendHttpSettingsCollection'
    props = {
        'port': (int, True),
        'protocol': (str, True), # Http / Https
        'cookieBasedAffinity': (str, False), # Enabled / Disabled
        'connectionDraining': (ApplicationGatewayConnectionDraining, False),
        'requestTimeout': (int, True),
    }


class ApplicationGatewayHttpListener(ARMObject):
    resource_type =  'Microsoft.Network/applicationGateways/httpListeners'
    props = {
        'frontendIPConfiguration': (SubResourceRef, True),
        'frontendPort': (SubResourceRef, True),
        'protocol': (str, True), # Http / Https
    }


class ApplicationGatewayRequestRoutingRule(ARMObject):
    resource_type =  'Microsoft.Network/applicationGateways/requestRoutingRules'
    props = {
        'ruleType': (str, True), # Basic / PathBasedRouting
        'httpListener': (SubResourceRef, True),
        'backendAddressPool': (SubResourceRef, True),
        'backendHttpSettings': (SubResourceRef, True),
    }


class AutoScaleConfiguration(ARMProperty):
    props = {
        'minCapacity': (int, True)
    }


class ApplicationGatewaySku(ARMProperty):
    props = {
        'name': (str, True),
        'tier': (str, True),
        'capacity': (int, False),
    }

    def validate(self):
        tier = self.properties['tier']
        name = self.properties['name']
        capacity = self.properties.get('capacity', 0)
        if tier in ['Standard', 'WAF']:
            if tier == 'Standard' and name not in ['Standard_Small', 'Standard_Medium', 'Standard_Large']:
                raise ValueError('ApplicationGateway->sku->name is "{}", but expected "Standard_Small", "Standard_Medium" or "Standard_Large"'.format(name))
            if tier == 'WAF' and name not in ['WAF_Medium', 'WAF_Large']:
                raise ValueError('ApplicationGateway->sku->name is "{}", but expected "WAF_Medium" or "WAF_Large"'.format(name))
            if capacity > 10 or capacity < 2:
                raise ValueError('ApplicationGateway->sku->capacity is "{}", but expected to be between 2 to 10'.format(capacity))
        elif tier in ['Standard_v2', 'WAF_v2']:
            if tier != name:
                raise ValueError('ApplicationGateway->sku->tier must be equals to ApplicationGateway->sku->name, when using "Standard_v2" or "WAF_v2"'.format(tier))
        else:
            raise ValueError('ApplicationGateway->sku->tier is "{}", but expected "Standard" or "WAF"'.format(tier))


class ApplicationGatewayIPConfiguration(ARMObject):
    resource_type = 'Microsoft.Network/applicationGateways/gatewayIPConfigurations'
    props = {
        'subnet': (SubResource, False)
    }


class ApplicationGateway(ARMObject):
    resource_type = 'Microsoft.Network/applicationGateways'
    apiVersion = '2018-08-01'
    location = True
    props = {
        'sku': (ApplicationGatewaySku, True),
        'gatewayIPConfigurations': ([ApplicationGatewayIPConfiguration], True),
        'frontendIPConfigurations': ([FrontendIPConfiguration], True),
        'frontendPorts': ([ApplicationGatewayFrontendPort], True),
        'backendAddressPools': ([BackendAddressPool], True),
        'backendHttpSettingsCollection': ([ApplicationGatewayBackendHttpSettings], True),
        'httpListeners': ([ApplicationGatewayHttpListener], True),
        'requestRoutingRules': ([ApplicationGatewayRequestRoutingRule], True),
        'autoscaleConfiguration': (AutoScaleConfiguration, False)
    }

    def ref_gateway_ip_configuration(self, gateway_ip_configuration: ApplicationGatewayIPConfiguration):
        return SubResourceRef(ApplicationGateway, 'gatewayIPConfigurations', self.title, gateway_ip_configuration)

    def ref_frontend_ip_configuration(self, frontend_ip_configuration: FrontendIPConfiguration):
        return SubResourceRef(ApplicationGateway, 'frontendIPConfigurations', self.title, frontend_ip_configuration)

    def ref_frontend_port(self, frontend_port: ApplicationGatewayFrontendPort):
        return SubResourceRef(ApplicationGateway, 'frontendPorts', self.title, frontend_port)

    def ref_backend_address_pool(self, backend_address_pool: BackendAddressPool):
        return SubResourceRef(ApplicationGateway, 'backendAddressPools', self.title, backend_address_pool)

    def ref_backend_http_settings(self, backend_http_settings: ApplicationGatewayBackendHttpSettings):
        return SubResourceRef(ApplicationGateway, 'backendHttpSettingsCollection', self.title, backend_http_settings)

    def ref_http_listener(self, http_listener: ApplicationGatewayHttpListener):
        return SubResourceRef(ApplicationGateway, 'httpListeners', self.title, http_listener)

    @property
    def gateway_ip_configurationsn(self) -> List[ApplicationGatewayIPConfiguration]:
        return self.properties['gatewayIPConfigurations']

    @property
    def frontend_ip_configurations(self) -> List[FrontendIPConfiguration]:
        return self.properties['frontendIPConfigurations']

    @property
    def frontend_ports(self) -> List[ApplicationGatewayFrontendPort]:
        return self.properties['frontendPorts']

    @property
    def backend_address_pools(self) -> List[BackendAddressPool]:
        return self.properties['backendAddressPools']

    @property
    def backend_http_settings(self) -> List[ApplicationGatewayBackendHttpSettings]:
        return self.properties['backendHttpSettingsCollection']

    @property
    def http_listeners(self) -> List[ApplicationGatewayHttpListener]:
        return self.properties['httpListeners']

    @property
    def request_routing_rules(self) -> List[ApplicationGatewayRequestRoutingRule]:
        return self.properties['requestRoutingRules']
