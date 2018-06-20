import json
import unittest

from base import ARMTemplate, SubResource
from ionosphere import depends_on_helper
from network import DnsZone, VirtualNetwork, ARecord, DnsZoneA, ZoneType


class TestDns(unittest.TestCase):

    def test_private_dns(self):
        sandbox = '654321'
        vnet_name = '{}_vnet'.format(sandbox)
        dns_name = '{}.sandbox.com'.format(sandbox)

        template = ARMTemplate()

        vnet = VirtualNetwork(vnet_name, template=template)

        dns = DnsZone(dns_name,
                      template=template,
                      registrationVirtualNetworks=[SubResource(id=vnet.ref())],
                      zoneType=ZoneType.Private.name,
                      dependsOn=vnet)

        dns_a = DnsZoneA('/'.join([dns_name, 'app1']),
                         template=template,
                         TTL=3600,
                         ARecords=[ARecord(ipv4Address="[reference('crumbNIC').ipConfigurations[0].properties.privateIPAddress]")],
                         dependsOn=dns)

        j = template.to_json()

        print(j)

