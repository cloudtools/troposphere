from base import ARMObject, ARMProperty, SubResource, SubResourceRef


class AddressSpace(ARMProperty):
    props = {
        'addressPrefixes': (list, False)
    }


class Subnet(ARMObject):
    props = {
        'addressPrefix': (str, True),
        'networkSecurityGroup': (SubResource, False)
    }


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
        return "[resourceId('Microsoft.Network/virtualNetworks/subnets', '{0}', '{1}')]" \
            .format(self.title,
                    self.get_subnet(subnet_name).title)

    def get_subnet(self, subnet_name):
        return next(iter(filter(lambda x: x.title == subnet_name, self.properties['subnets'])))

    SubnetRef = subnet_ref


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
        'tags': (dict, False)
    }


class NetworkInterfaceIPConfiguration(ARMObject):
    props = {
        # 'applicationGatewayBackendAddressPools': () - not implemented
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
        'ipConfigurations': (list, True),  # type: list[NetworkInterfaceIPConfiguration]
        'dnsSettings': (NetworkInterfaceDnsSettings, False)
    }

    root_props = {
        'tags': (dict, False)
    }

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


class BackendAddressPool(ARMProperty):
    props = {'name': (str, True)}


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
    }
