from troposphere import Join, Parameter, Ref, Template
from troposphere import Output, FindInMap, GetAtt
from troposphere import Select, Export, Sub
import troposphere.autoscaling as autoscaling
import troposphere.elasticloadbalancingv2 as elb
import troposphere.route53 as route53

t = Template()


# Windows server 2016 Base
def AddAMI(template):
    t.add_mapping("windowsAMI", {
        "us-east-1": {"AMI": "ami-b06249a7"},
        "us-east-2": {"AMI": "ami-20683245"},
        "us-west-1": {"AMI": "ami-d3a8fdb3"},
        "us-west-2": {"AMI": "ami-b9b71ad9"},
        "eu-west-1": {"AMI": "ami-32792a41"},
        "eu-west-2": {"AMI": "ami-29353f4d"},
        "eu-central-1": {"AMI": "ami-c0f237af"}
    })


def main():
    # Meta
    t.add_version("2010-09-09")
    t.add_description("Template for auto-scaling in an Application"
                      "load balancer target group. "
                      "The ALB will be used as an A Alias target "
                      "for a specified Route53 hosted zone. "
                      "This template also showcases "
                      "Metadata Parameter Grouping, "
                      "Special AWS Parameter Types, "
                      "and Cloudformation Outputs with Exports"
                      "which can be imported into other templates."

                      )
    t.add_metadata({
        "Author": "https://github.com/hmain/",
        "LastUpdated": "2017 01 31",
        "Version": "1",
    })

    # Parameter grouping
    t.add_metadata(
        {
            "AWS::CloudFormation::Interface": {
                "ParameterGroups": [
                    {
                        "Label": {"default": "Global parameters"},
                        "Parameters": ["environment"]
                    },
                    {
                        "Label": {"default": "Application Loadbalancer"},
                        "Parameters": ["albSubnets",
                                       "loadbalancerPrefix",
                                       "loadBalancerArn",
                                       "albPaths",
                                       "albPort"
                                       ]
                    },
                    {
                        "Label": {"default": "VPC"},
                        "Parameters": ["ec2Subnets",
                                       "VPC",
                                       "securityGroup"
                                       ]
                    },
                    {
                        "Label": {"default": "EC2"},
                        "Parameters": ["ec2Name",
                                       "ec2Type",
                                       "ec2Key"
                                       ]
                    },
                    {
                        "Label": {"default": "Auto-scaling"},
                        "Parameters": ["asgCapacity",
                                       "asgMinSize",
                                       "asgMaxSize",
                                       "asgCooldown",
                                       "asgHealthGrace"
                                       ]
                    },
                    {
                        "Label": {"default": "Route53"},
                        "Parameters": ["route53HostedZoneId",
                                       "route53HostedZoneName"
                                       ]
                    }

                ]
            }
        }
    )

    AddAMI(t)

    environment = t.add_parameter(Parameter(
        "environment",
        Default="dev",
        Type="String",
        Description="Development or Production environment",
        AllowedValues=[
            "dev",
            "prod"
        ],
        ConstraintDescription="dev or prod",
    ))
    route53_hosted_zone_id = t.add_parameter(Parameter(
        "route53HostedZoneId",
        Default="",
        Type="AWS::Route53::HostedZone::Id",
        Description="Route53 DNS zone ID"
    ))

    route53_hosted_zone_name = t.add_parameter(Parameter(
        "route53HostedZoneName",
        Default="my.aws.dns.com",
        Type="String",
        Description="Route53 hosted zone name"
    ))
    security_group = t.add_parameter(Parameter(
        "securityGroup",
        Default="",
        Type="List<AWS::EC2::SecurityGroup::Id>",
        Description="Which security groups to use"
    ))
    alb_paths = t.add_parameter(Parameter(
        "albPaths",
        Default="/",
        Type="CommaDelimitedList",
        Description="Path-patterns you want the loadbalancer to point to in "
                    "your application"
    ))
    albPort = t.add_parameter(Parameter(
        "albPort",
        Default="80",
        Type="Number",
        Description="Which loadbalancer port to use"
    ))
    ec2_subnets = t.add_parameter(Parameter(
        "ec2Subnets",
        Default="",
        Type="List<AWS::EC2::Subnet::Id>",
        Description="Private subnets for the instances."
    ))
    alb_subnets = t.add_parameter(Parameter(
        "albSubnets",
        Default="",
        Type="List<AWS::EC2::Subnet::Id>",
        Description="Public subnets for the load balancer."
    ))
    loadbalancer_prefix = t.add_parameter(Parameter(
        "loadbalancerPrefix",
        Default="",
        Type="String",
        Description="Specify a prefix for your loadbalancer",
    ))
    vpc = t.add_parameter(Parameter(
        "VPC",
        Default="",
        Type="AWS::EC2::VPC::Id",
        Description="Environment VPC"
    ))

    # Auto scaling group parameters
    asg_capacity = t.add_parameter(Parameter(
        "asgCapacity",
        Default="0",
        Type="Number",
        Description="Number of instances"
    ))
    asg_min_size = t.add_parameter(Parameter(
        "asgMinSize",
        Default="0",
        Type="Number",
        Description="Minimum size of AutoScalingGroup"
    ))
    asg_max_size = t.add_parameter(Parameter(
        "asgMaxSize",
        Default="1",
        Type="Number",
        Description="Maximum size of AutoScalingGroup"
    ))
    asg_cooldown = t.add_parameter(Parameter(
        "asgCooldown",
        Default="300",
        Type="Number",
        Description="Cooldown before starting/stopping another instance"
    ))
    asg_health_grace = t.add_parameter(Parameter(
        "asgHealthGrace",
        Default="300",
        Type="Number",
        Description="Wait before starting/stopping another instance"
    ))

    # EC2 parameters
    ec2_name = t.add_parameter(Parameter(
        "ec2Name",
        Default="myApplication",
        Type="String",
        Description="Name of the instances"
    ))
    ec2_type = t.add_parameter(Parameter(
        "ec2Type",
        Default="t2.large",
        Type="String",
        Description="Instance type."
    ))
    ec2_key = t.add_parameter(Parameter(
        "ec2Key",
        Default="",
        Type="AWS::EC2::KeyPair::KeyName",
        Description="EC2 Key Pair"
    ))

    # Launchconfiguration
    ec2_launchconfiguration = t.add_resource(autoscaling.LaunchConfiguration(
        "EC2LaunchConfiguration",
        ImageId=FindInMap("windowsAMI", Ref("AWS::Region"), "AMI"),
        KeyName=Ref(ec2_key),
        SecurityGroups=Ref(security_group),
        InstanceType=Ref(ec2_type),
        AssociatePublicIpAddress=False,
    ))

    # Application ELB
    alb_target_group = t.add_resource(elb.TargetGroup(
        "albTargetGroup",
        HealthCheckPath=Select("0", Ref(alb_paths)),
        HealthCheckIntervalSeconds="30",
        HealthCheckProtocol="HTTP",
        HealthCheckTimeoutSeconds="10",
        HealthyThresholdCount="4",
        Matcher=elb.Matcher(
            HttpCode="200"),
        Name=Ref(ec2_name),
        Port=80,
        Protocol="HTTP",
        UnhealthyThresholdCount="3",
        VpcId=Ref(vpc)

    ))

    # Auto scaling group
    t.add_resource(autoscaling.AutoScalingGroup(
        "autoScalingGroup",
        DesiredCapacity=Ref(asg_capacity),
        Tags=autoscaling.Tags(
            Environment=Ref(environment)
        ),
        VPCZoneIdentifier=Ref(ec2_subnets),
        TargetGroupARNs=[Ref(alb_target_group)],
        MinSize=Ref(asg_min_size),
        MaxSize=Ref(asg_max_size),
        Cooldown=Ref(asg_cooldown),
        LaunchConfigurationName=Ref(ec2_launchconfiguration),
        HealthCheckGracePeriod=Ref(asg_health_grace),
        HealthCheckType="EC2",
    ))

    # Application Load Balancer
    application_load_balancer = t.add_resource(elb.LoadBalancer(
        "applicationLoadBalancer",
        Name=Ref(loadbalancer_prefix),
        Scheme="internet-facing",
        Subnets=Ref(alb_subnets),
        SecurityGroups=Ref(security_group)
    ))
    alb_listener = t.add_resource(elb.Listener(
        "albListener",
        Port=Ref(albPort),
        Protocol="HTTP",
        LoadBalancerArn=Ref(application_load_balancer),
        DefaultActions=[elb.Action(
            Type="forward",
            TargetGroupArn=Ref(alb_target_group)
        )]
    ))
    t.add_resource(elb.ListenerRule(
        "albListenerRule",
        ListenerArn=Ref(alb_listener),
        Conditions=[elb.Condition(
            Field="path-pattern",
            Values=Ref(alb_paths)
        )],
        Actions=[elb.Action(
            Type="forward",
            TargetGroupArn=Ref(alb_target_group)
        )],
        Priority="1"
    ))

    # Route53
    t.add_resource(route53.RecordSetGroup(
        "route53RoundRobin",
        HostedZoneId=Ref(route53_hosted_zone_id),
        RecordSets=[
            route53.RecordSet(
                Weight=1,
                SetIdentifier=Join(".", [Ref(environment),
                                         Ref(route53_hosted_zone_name),
                                         "ELB"]),
                Name=Join(".", [Ref(environment),
                                Ref(route53_hosted_zone_name)]),
                Type="A",
                AliasTarget=route53.AliasTarget(
                    GetAtt(application_load_balancer,
                           "CanonicalHostedZoneID"),
                    GetAtt(application_load_balancer,
                           "DNSName")
                )
            )
        ]
    ))

    t.add_output(
        Output(
            "URL",
            Description="URL of the website",
            Value=Join("", [
                "http://",
                GetAtt(application_load_balancer, "DNSName"),
                Select("0", Ref(alb_paths))
            ]),
            Export=Export(Sub("${AWS::StackName}-URL")),
        )
    )

    print(t.to_json())


if __name__ == '__main__':
    main()
