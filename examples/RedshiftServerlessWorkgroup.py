#!/usr/bin/env python3
from troposphere import Output, Ref, Tags, Template, ec2
from troposphere.redshiftserverless import Namespace, Workgroup

app_group = "redshift-serverless".capitalize()
app_group_l = app_group.lower()

# Redshift serverless cluster variables
admin_username = "{{{{resolve:ssm:/redshift_admin_username}}}}"
admin_password = "{{{{resolve:ssm:/redshift_admin_password}}}}"
default_iam_role_arn = "arn:aws:iam::123456789123:role/service-role/AmazonRedshift-CommandsAccessRole-123451234512345"
default_db_name = "dev"
iam_roles = []
serverless_namespace_name = "serverless"
tcp_port = 5439
vpc_id = "vpc-12345678123456789"
subnet_ids = ["subnet-12345678912345678", "subnet-98765432198765432"]

# Prepare Template
t = Template()
t.set_description("RedshiftServerless: Template and module example")

# Private security group
privateSecurityGroup = t.add_resource(
    ec2.SecurityGroup(
        "privateSecurityGroup",
        GroupDescription="Private Security Group",
        VpcId=vpc_id,
        SecurityGroupIngress=[
            ec2.SecurityGroupRule(
                IpProtocol="tcp",
                FromPort=tcp_port,
                ToPort=tcp_port,
                CidrIp="10.0.0.0/8",
                Description="Allow TCP 5439 to Redshift Serverless cluster",
            )
        ],
        Tags=Tags(Name="example-private-sg"),
    )
)

redshiftServerlessClusterNamespace = t.add_resource(
    Namespace(
        "redshiftServerlessClusterNamespace",
        AdminUsername=admin_username,
        AdminUserPassword=admin_password,
        DbName=default_db_name,
        DefaultIamRoleArn=default_iam_role_arn,
        IamRoles=iam_roles,
        NamespaceName=serverless_namespace_name,
    )
)

redshiftServerlessWorkGroup = t.add_resource(
    Workgroup(
        "redshiftServerlessWorkGroup",
        EnhancedVpcRouting=True,
        NamespaceName=Ref("redshiftServerlessClusterNamespace"),
        PubliclyAccessible=False,
        SecurityGroupIds=[Ref("privateSecurityGroup")],
        SubnetIds=subnet_ids,
        WorkgroupName="redshiftServerlessWorkGroup",
    )
)

t.add_output(Output("WorkgroupName", Value=Ref(redshiftServerlessWorkGroup)))

t.add_output(Output("NamespaceName", Value=Ref(redshiftServerlessClusterNamespace)))


# Output all necessary files with the template and stack_details
print(t.to_json())
