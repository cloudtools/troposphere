from troposphere import Template
from troposphere.codedeploy import AutoRollbackConfiguration, \
    DeploymentStyle, DeploymentGroup, ElbInfoList, LoadBalancerInfo


template = Template()
template.add_version('2010-09-09')


auto_rollback_configuration = AutoRollbackConfiguration(
    Enabled=True,
    Events=['DEPLOYMENT_FAILURE']
)

deployment_style = DeploymentStyle(
    DeploymentOption='WITH_TRAFFIC_CONTROL'
)

elb_info_list = ElbInfoList(
    Name='DemoLoadBalancer'
)

load_balancer_info = LoadBalancerInfo(
    ElbInfoList=[elb_info_list]
)

deployment_group = DeploymentGroup(
    "DemoDeploymentGroup",
    ApplicationName='DemoApplication',
    AutoRollbackConfiguration=auto_rollback_configuration,
    DeploymentStyle=deployment_style,
    LoadBalancerInfo=load_balancer_info,
    ServiceRoleArn='arn:aws:iam::0123456789:role/codedeploy-role'
)
template.add_resource(deployment_group)

print(template.to_json())
