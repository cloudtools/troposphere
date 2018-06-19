import unittest

from base import ARMTemplate, SubResource
from network import DnsZone, VirtualNetwork, ARecord, DnsZoneA


class TestDns(unittest.TestCase):

    def test_private_dns(self):
        sandbox = '654321'
        vnet_name = '{}_vnet'.format(sandbox)
        dns_name = '{}.sandbox.com'.format(sandbox)

        template = ARMTemplate()

        vnet = VirtualNetwork(vnet_name, template=template)

        dns = DnsZone(dns_name, template=template).with_depends_on(vnet)
        dns.registrationVirtualNetworks = [SubResource(id=vnet.ref())]

        dns_a = DnsZoneA('/'.join([dns_name, 'app1']), template=template)
        dns_a.TTL = 3600
        dns_a.ARecords = [
            ARecord(ipv4Address="[reference('crumbNIC').ipConfigurations[0].properties.privateIPAddress]")
        ]
        dns_a.with_depends_on(dns)

        json = template.to_json()

        print(json)

