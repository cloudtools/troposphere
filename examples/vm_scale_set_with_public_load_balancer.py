from compute import *

from base import ARMTemplate
from network import *

template = ARMTemplate()

vnet = VirtualNetwork("myvnet",
                      addressSpace=AddressSpace(addressPrefixes=['10.0.0.0/24']),
                      subnets=[Subnet('subnet1', addressPrefix='10.0.0.0/24')])

#region load balancer

# needs to be Static so it will be assigned a value immediately
lb_pub_ip = PublicIPAddress('lb_pub_ip', publicIPAllocationMethod='Static')

lb_ip_conf = FrontendIPConfiguration('lb_ip_conf',
                                     privateIPAllocationMethod='Dynamic',
                                     # subnet=SubResource(id=vnet.SubnetRef('subnet1')),
                                     publicIPAddress=SubResource(id=lb_pub_ip.ref()))

backend_address_pool = BackendAddressPool(name='lb_backend')

probe = Probe('testProbe', protocol='Tcp', port=22)

lb = LoadBalancer('my_lb',
                  sku=LoadBalancerSku(name='Basic'),
                  frontendIPConfigurations=[lb_ip_conf],
                  backendAddressPools=[backend_address_pool],
                  probes=[probe],
                  loadBalancingRules=[])

lb_rule = LoadBalancingRule('lbrule',
                            protocol='Tcp',
                            loadDistribution='SourceIP',
                            frontendPort=22,
                            backendPort=22,
                            frontendIPConfiguration=lb.ref_frontend_ip_configuration(lb_ip_conf),
                            probe=lb.ref_probe(probe),
                            backendAddressPool=lb.ref_backend_address_pool(backend_address_pool))

lb.loadBalancingRules.append(lb_rule)

lb.with_depends_on([lb_pub_ip, vnet])

#endregion


#region scaleset

linux_conf = LinuxConfiguration(disablePasswordAuthentication=False)

ip_conf = VirtualMachineScaleSetIPConfiguration('my_ip_config',
                                                subnet=SubResource(id=vnet.SubnetRef('subnet1')),
                                                loadBalancerBackendAddressPools=[BackendAddressPoolRef(load_balancer=lb,
                                                                                                       backend_pool='lb_backend')])
nic_conf = VirtualMachineScaleSetNetworkConfiguration('my_nic',
                                                      primary=True,
                                                      ipConfigurations=[ip_conf])

ss_vm_prof = VirtualMachineScaleSetVMProfile(
    osProfile=VirtualMachineScaleSetOSProfile(computerNamePrefix='testVm',
                                              adminUsername='adminuser',
                                              adminPassword='Welcome1234567+',
                                              linuxConfiguration=linux_conf),
    storageProfile=VirtualMachineScaleSetStorageProfile(imageReference=ImageReference(publisher='Canonical',
                                                                                      offer='UbuntuServer',
                                                                                      sku='16.04-LTS'),
                                                        osDisk=VirtualMachineScaleSetOSDisk(createOption='FromImage')),
    networkProfile=VirtualMachineScaleSetNetworkProfile(networkInterfaceConfigurations=[nic_conf]))

vm_scale_set = VirtualMachineScaleSets('my_scale_set',
                                       # plan=Plan(),
                                       sku=VirtualMachineScaleSetSku(name='Standard_A1', tier='Standard', capacity=2),
                                       overprovision=True,
                                       upgradePolicy=UpgradePolicy(mode='Manual'),
                                       virtualMachineProfile=ss_vm_prof).with_depends_on([vnet, lb])

#endregion


template.add_resource([lb_pub_ip, lb, vm_scale_set, vnet])

print(template.to_json())
