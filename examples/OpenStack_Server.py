# This is a simple example of how to provision an OpenStack Server using Heat
# native OpenStack resources

from troposphere import Base64, Join
from troposphere import Parameter, Ref, Template
from troposphere.openstack import neutron, nova


template = Template()

keyname_param = template.add_parameter(Parameter(
    "KeyName",
    Description="Name of an existing OpenStack KeyPair to enable SSH "
                "access to the instance",
    Type="String",
))

# Define the instance security group, to allow:
#   - SSH from our trusted network
#   - ICMP from everywhere
security_group = template.add_resource(
    neutron.SecurityGroup(
        "OpenStackSecurityGroup",
        description="Instance Security Group",
        rules=[
            neutron.SecurityGroupRule(
                protocol='tcp',
                port_range_min=22,
                port_range_max=22,
                remote_ip_prefix="192.168.1.0/24",
            ),
            neutron.SecurityGroupRule(
                protocol='icmp',
                remote_ip_prefix="0.0.0.0/0",
            ),
        ]
    )
)


openstack_instance = template.add_resource(nova.Server(
    "OpenStackInstance",
    image="MyImage",
    flavor="t1.micro",
    key_name=Ref(keyname_param),
    networks=[neutron.Port(
        "OpenStackPort",
        fixed_ips=[neutron.FixedIP(
            ip_address="192.168.1.20"
        )],
        network_id="3e47c369-7007-472e-9e96-7dadb51e3e99",
        security_groups=[Ref(security_group)],
    )],
    user_data=Base64(Join('\n', [
        "#!/bin/bash",
        "echo \"Upgrade started at $(date)\"",
        "apt-get update",
        "apt-get -y upgrade",
        "echo \"Upgrade complete at $(date)\"",
    ]))
))

print(template.to_json())
