from troposphere import Template
from troposphere.codedeploy import AutoRollbackConfiguration, \
    DeploymentStyle, DeploymentGroup, ElbInfoList, LoadBalancerInfo, \
    OnPremisesInstanceTagFilters


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

# On premises
deployment_group_on_premises = DeploymentGroup(
    "DemoDeploymentGroupOnPremises",
    DeploymentGroupName='DemoApplicationOnPremises',
    ApplicationName='DemoApplicationOnPremises',
    AutoRollbackConfiguration=auto_rollback_configuration,
    DeploymentStyle=DeploymentStyle(
        DeploymentOption='WITHOUT_TRAFFIC_CONTROL'
    ),
    ServiceRoleArn='arn:aws:iam::0123456789:role/codedeploy-role',
    OnPremisesInstanceTagFilters=[OnPremisesInstanceTagFilters(
        Key='Service',
        Value='DemoApplicationOnPremises',
        Type='KEY_AND_VALUE'
    )]
)
template.add_resource(deployment_group_on_premises)

print(template.to_json())
