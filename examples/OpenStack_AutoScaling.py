# This is an example of an AutoScaling/ELB setup for OpenStack.
# It assumes you have a compatible LBaaS setup running.
#
# Available resources are defined at:
#   http://docs.openstack.org/developer/heat/template_guide/openstack.html
#   http://docs.openstack.org/developer/heat/template_guide/cfn.html

from troposphere import Base64, GetAZs, Join, Ref, Template
from troposphere import autoscaling, cloudformation
from troposphere.openstack import heat, neutron


template = Template()

# Define our health monitor
health_mon = template.add_resource(neutron.HealthMonitor(
    "MyHealthMon",
    type="HTTP",
    delay=3,
    max_retries=5,
    timeout=10,
    url_path="/",
    expected_codes="200"
))

# Define our pool and VIP
pool = template.add_resource(neutron.Pool(
    "MyPool",
    name="mypool",
    description="My instance pool",
    lb_method="ROUND_ROBIN",
    monitors=[Ref(health_mon)],
    protocol="HTTP",
    subnet_id="c5b15643-1358-4796-af8f-c9050b0b3e2a",
    vip=neutron.VIP(
        name="my-vip",
        description="My VIP",
        connection_limit=100,
        protocol_port=80
    )
))

# Define the loadbalancer
loadbalancer = template.add_resource(neutron.LoadBalancer(
    "MyLoadBalancer",
    pool_id=Ref(pool),
    protocol_port=80
))

# Define the instance security group, to allow:
#   - SSH from our trusted network
#   - HTTP from the security group used by our LBaaS
#   - ICMP from everywhere
security_group = template.add_resource(
    neutron.SecurityGroup(
        "MySecurityGroup",
        description="Instance Security Group",
        rules=[
            neutron.SecurityGroupRule(
                protocol='tcp',
                port_range_min=22,
                port_range_max=22,
                remote_ip_prefix="192.168.1.0/24",
            ),
            neutron.SecurityGroupRule(
                protocol='tcp',
                port_range_min=80,
                port_range_max=80,
                remote_mode="remote_group_id",
                remote_group_id="faf49966-ffc2-4602-84e9-917ae2ce7b89"
            ),
            neutron.SecurityGroupRule(
                protocol='icmp',
                remote_ip_prefix="0.0.0.0/0",
            ),
        ]
    )
)

# Define our launch configuration (AWS compatibility resource)
launch_config = template.add_resource(autoscaling.LaunchConfiguration(
    "MyLaunchConfig",
    KeyName="bootstrap",
    InstanceType="t1.micro",
    ImageId="Ubuntu",
    SecurityGroups=[Ref(security_group)],
    Metadata=cloudformation.Init({
        "config": cloudformation.InitConfig(
            files=cloudformation.InitFiles({
                "file1": cloudformation.InitFile(
                    content=Join('\n', [
                        "This is a",
                        "test file"
                    ]),
                    mode="000755",
                    owner="root",
                    group="root",
                    context=cloudformation.InitFileContext({
                        "security_group_id": Ref(security_group)
                    })
                )
            }),
            services={
                "sysvinit": cloudformation.InitServices({
                    "service1": cloudformation.InitService(
                        enabled=True,
                        ensureRunning=True,
                        files=['/etc/service1/somefile.conf']
                    )
                })
            }
        )
    }),
    UserData=Base64(Join('\n', [
        "#!/bin/bash",
        "echo \"Upgrade started at $(date)\"",
        "apt-get update",
        "apt-get -y upgrade",
        "echo \"Upgrade complete at $(date)\"",
    ]))
))

# Define our AutoScaling Group, using the AWS compatability layer.
# It's not a native heat type, but it's a clone of the AWS type with fixes to
# work correctly on OpenStack.
# VPCZoneIdentifier here is our OpenStack subnet ID.
autoscaling_group = template.add_resource(heat.AWSAutoScalingGroup(
    "MyAutoScalingGroup",
    LaunchConfigurationName=Ref(launch_config),
    MinSize="1",
    MaxSize="2",
    DesiredCapacity="2",
    AvailabilityZones=GetAZs(""),
    VPCZoneIdentifier=["1016941e-8462-4a3a-a11d-d7836ca7a2df"],
    LoadBalancerNames=Ref(loadbalancer),
))

print(template.to_json())
