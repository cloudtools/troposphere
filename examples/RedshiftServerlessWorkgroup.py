#!/usr/bin/env python3
from troposphere import Template
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
security_group_ids = ["sg-12345123451234567"]

# Prepare Template
t = Template()
t.set_description("RedshiftServerless: Template and module example")

Namespace = t.add_resource(
    Namespace(
        title="Namespace",
        AdminUsername=admin_username,
        AdminUserPassword=admin_password,
        DbName=default_db_name,
        DefaultIamRoleArn=default_iam_role_arn,
        IamRoles=iam_roles,
        NamespaceName=serverless_namespace_name,
    )
)

Workgroup = t.add_resource(
    Workgroup(
        title="Workgroup",
        EnhancedVpcRouting=True,
        NamespaceName=serverless_namespace_name,
        PubliclyAccessible=False,
        SecurityGroupIds=security_group_ids,
        SubnetIds=subnet_ids,
        WorkgroupName="RedshiftServerlessWorkGroup",
    )
)

# Output all necessary files with the template and stack_details
print(t.to_json())
