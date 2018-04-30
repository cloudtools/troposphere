from base import ARMObject, ARMProperty


class AddressSpace(ARMProperty):
    props = {
        'addressPrefixes': (list, False)
    }


class Subnet(ARMObject):
    props = {
        'addressPrefix': (str, False)
    }


class VirtualNetwork(ARMObject):
    resource_type = 'Microsoft.Network/virtualNetworks'
    apiVersion = "2017-10-01"
    location = True

    props = {
        'addressSpace': (AddressSpace, False),
        'subnets': ((Subnet, list), False),
        'tags': (dict, False)
    }

    def subnet_ref(self, subnet_name):
        return "[resourceId('Microsoft.Network/virtualNetworks/subnets', '{0}', '{1}')]"\
            .format(self.title,
                    self.get_subnet(subnet_name).title)

    def get_subnet(self, subnet_name):
        return next(iter(filter(lambda x: x.title == subnet_name, self.properties['subnets'])))

    SubnetRef = subnet_ref


class SecurityRule(ARMObject):
    props = {
        'description': (str, False),  # todo add validation on length
        'protocol': (str, True),  # todo add valiadtion on valid values: 'Tcp', 'Udp', and '*'
        'sourcePortRange': (str, False),  # todo add validation for all 'range' props
        'destinationPortRange': (str, False),
        'sourceAddressPrefix': (str, False),
        'sourceAddressPrefixes': ((list, str), False),
        # 'sourceApplicationSecurityGroups': (str, False),  # todo implement
        'destinationAddressPrefix': (str, False),
        'destinationAddressPrefixes': ((list, str), False),
        # 'destinationApplicationSecurityGroups': (str, False),  # todo implement
        'sourcePortRanges': (str, False),
        'destinationPortRanges': (str, False),
        'access': (str, True),  # todo add validation on values: 'Allow' and 'Deny'
        'priority': (int, False),
        'direction': (str, True)  # todo add validation on values: 'Inbound' and 'Outbound'
    }


class SubResource(ARMProperty):
    props = {
        'id': (str, False),
    }


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
        'dnsSettings': (PublicIPAddressDnsSettings, False),
        'tags': (dict, False),
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
        # 'applicationSecurityGroups': () - not implemented
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
        'securityRules': ((list, SecurityRule), False),
        'tags': (dict, False)
    }


class NetworkInterface(ARMObject):
    resource_type = 'Microsoft.Network/networkInterfaces'
    apiVersion = "2017-10-01"
    location = True

    props = {
        'virtualMachine': (SubResource, False),
        'networkSecurityGroup': ((SubResource, NetworkSecurityGroup), False),
        'ipConfigurations': ((list, NetworkInterfaceIPConfiguration), False),
        'dnsSettings': (NetworkInterfaceDnsSettings, False),
        'tags': (dict, False)
    }
