ionosphere
==========

|License| |PyPI| |Build Status|

About
=====

Ionosphere - library to create `Azure Resource Manager
Templates <https://docs.microsoft.com/en-us/azure/templates/>`__
descriptions (Ionosphere is porting of troposphere)

The Ionosphere library allows for easier creation of the Azure Resource
Manager templates JSON by writing Python code to describe the Azure
resources.

To facilitate catching ARM templates or JSON errors early the library
has property and type checking built into the classes.

Currently supported Azure resource types
========================================

-  Virtual Machine
-  Virtual Machine Extension
-  Virtual Machine Scale Sets
-  Virtual Machine Scale Set Extension
-  Virtual Network
-  Public IP Address
-  Network Interface
-  Network SecurityGroup
-  Application Security Group
-  Load Balancer
-  Dns Zone
-  Application Gateway
-  Storage Account

Example
=======

The following example will generate an ARM Template that creates a VNet
and an Ubuntu VM with a public IP. The template also exposes port 22 on
the VM to the internet.

.. code:: python

    # Create the object
    template = ARMTemplate()

    # Create VNET object
    vnet = VirtualNetwork("myvnet",
                          addressSpace=AddressSpace(addressPrefixes=['10.0.0.0/24']),
                          subnets=[Subnet('main_subnet', addressPrefix='10.0.0.0/24')],
                          tags={'key1': 'tag-key1', 'key2': 'tag-key2'})

    # Create Network Security Group object with "Allow SSH" rule
    nsg = NetworkSecurityGroup("myNsg",
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
                                                priority=200
                                            )])

    # Create Public IP Address object
    publicIp = PublicIPAddress('my_vm_nic1_pubip', publicIPAllocationMethod='dynamic')

    # Create Network Interface object
    networkInterface = NetworkInterface('myvm_nic1',
                                        ipConfigurations=[NetworkInterfaceIPConfiguration(
                                                'my_vm_nic1_ip_config',
                                                 privateIPAllocationMethod='Dynamic',
                                                 subnet=SubResource(id=vnet.subnet_ref('main_subnet')),
                                                 publicIPAddress=SubResource(id=publicIp.Ref()))],
                                        networkSecurityGroup=SubResource(id=nsg.Ref()))
                                        
    # Set dependencies on VNET & Public IP to the Network Interface
    networkInterface.with_depends_on([publicIp, vnet])

    # Create a parameter for the VM password and add it to the template
    vm_password_param = ARMParameter('vmPassword',
                                     template=template,
                                     type='secureString',
                                     description='The password for the VM access. User is "adminuser"')

    # Create the Virtual Machince object 
    vm = VirtualMachine('myvm',
                        hardwareProfile=HardwareProfile(vmSize='Basic_A0'),
                        storageProfile=StorageProfile(imageReference=ImageReference(publisher='Canonical',
                                                                                    offer='UbuntuServer',
                                                                                    sku='16.04-LTS'),
                                                      osDisk=OsDisk(createOption='FromImage',
                                                                    diskSizeGB=50,
                                                                    managedDisk=ManagedDiskParameters(storageAccountType='Standard_LRS'))),
                        osProfile=OSProfile(computerName='mytestvm',
                                            adminUsername='adminuser',
                                            adminPassword=vm_password_param.Ref(),
                                            linuxConfiguration=LinuxConfiguration(disablePasswordAuthentication=False)),
                        networkProfile=NetworkProfile(networkInterfaces=
                                                      [NetworkInterfaceReference(id=networkInterface.Ref())]))
    # Set dependency for the VM on the Network Interface
    vm.with_depends_on(networkInterface)

    # Add all objects to the arm template
    template.add_resource([vnet, nsg, publicIp, networkInterface, vm])

    # Generate ARM Template
    print(template.to_json())

Contributions
=============

All contributions are welcome.

Licensing
=========

Ionosphere is a fork of troposphere which is licensed under the `BSD
2-Clause license <http://opensource.org/licenses/BSD-2-Clause>`__. See
`LICENSE <https://github.com/cloudtools/ionosphere/blob/master/LICENSE>`__
for the Ionosphere full license text.

.. |License| image:: https://img.shields.io/pypi/l/troposphere.svg
   :target: https://opensource.org/licenses/BSD-2-Clause
.. |PyPI| image:: https://img.shields.io/pypi/v/ionosphere.svg?maxAge=2592000&style=flat
   :target: https://pypi.python.org/pypi/ionosphere/
.. |Build Status| image:: https://travis-ci.org/QualiNext/ionosphere.svg?branch=master
   :target: https://travis-ci.org/QualiNext/ionosphere
