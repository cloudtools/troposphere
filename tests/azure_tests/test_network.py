import unittest

from azure import ARMTemplate
from azure.network import VirtualNetwork, AddressSpace, Subnet, NetworkSecurityGroup, SecurityRule, PublicIPAddress, \
    NetworkInterface, NetworkInterfaceIPConfiguration, SubResource


class TestAzureCompute(unittest.TestCase):
    def test_simple_vm(self):
        vnet = VirtualNetwork("test_vnet",
                              addressSpace=AddressSpace(addressPrefixes=['10.0.0.0/24']),
                              subnets=[Subnet('subnet1', addressPrefix='10.0.0.0/24')],
                              tags={'Key1': 'tag-key1', 'Key2': 'tag-key2', 'Key3': 'tag-key3'})

        nsg = NetworkSecurityGroup("testvmNsg",
                                   securityRules=[
                                       SecurityRule('ssh',
                                                    description='public ssh access',
                                                    protocol='Tcp',
                                                    destinationPortRange="22",
                                                    destinationAddressPrefix="*",
                                                    sourceAddressPrefix='Internet',
                                                    sourcePortRange='*',
                                                    access='Allow',
                                                    direction='Inbound',
                                                    priority=200)])

        public_ip = PublicIPAddress('testvm_nic1_pubip', publicIPAllocationMethod='dynamic')

        network_interface = NetworkInterface('tesmvm_nic1',
                                             ipConfigurations=
                                             [NetworkInterfaceIPConfiguration('tesmvm_nic1_ip_config',
                                                                              privateIPAllocationMethod='Dynamic',
                                                                              subnet=SubResource(
                                                                                  id=vnet.SubnetRef('subnet1')),
                                                                              publicIPAddress=SubResource(
                                                                                  id=public_ip.Ref()))],
                                             networkSecurityGroup=SubResource(id=nsg.Ref()))
        network_interface.with_depends_on([public_ip, vnet])

        template = ARMTemplate(Description='test template')
        template.add_resource([vnet, nsg, public_ip, network_interface])

        self.assertIn(vnet, template.resources)
        self.assertIn(nsg, template.resources)
        self.assertIn(public_ip, template.resources)
        self.assertIn(network_interface, template.resources)

    if __name__ == '__main__':
        unittest.main()
