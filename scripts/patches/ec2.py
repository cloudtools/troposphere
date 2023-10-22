def tagspecification_patches():
    patches = [
        # backward compatibility
        {
            "op": "copy",
            "from": "/PropertyTypes/AWS::EC2::CapacityReservation.TagSpecification",
            "path": "/PropertyTypes/AWS::EC2::CapacityReservation.TagSpecifications",
        },
    ]

    resources = [
        ("CapacityReservation", "TagSpecification", None),
        ("CapacityReservationFleet", "TagSpecification", None),
        ("ClientVpnEndpoint", "TagSpecification", None),
        ("EC2Fleet", "TagSpecification", None),
        ("LaunchTemplate", "LaunchTemplateTagSpecification", None),
        # ("SpotFleet", "SpotFleetTagSpecification", "SpotFleetLaunchSpecification"),
    ]
    for resource, property, property_name in resources:
        patches.append(
            {
                "op": "remove",
                "path": f"/PropertyTypes/AWS::EC2::{resource}.{property}",
            }
        )
        if property_name is not None:
            path = f"/PropertyTypes/AWS::EC2::{resource}.{property_name}/Properties/TagSpecifications/ItemType"
        else:
            path = f"/ResourceTypes/AWS::EC2::{resource}/Properties/TagSpecifications/ItemType"

        patches.append(
            {
                "op": "replace",
                "path": path,
                "value": "TagSpecifications",
            }
        ),

    patches += [
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::LaunchTemplate.TagSpecification",
        },
        {
            "op": "replace",
            "path": "/PropertyTypes/AWS::EC2::LaunchTemplate.LaunchTemplateData/Properties/TagSpecifications/ItemType",
            "value": "TagSpecifications",
        },
    ]

    return patches


def blockdevice_patches():
    # There are 3 different BlockDeviceMappings in EC2 with different essociated EBS
    # EC2 Instance:
    #   Spec: uses BlockDeviceMapping and Ebs (without throughput)
    #   troposphere: uses BlockDeviceMapping and EBSBlockDevice
    # EC2 LaunchTemplate:
    #   Spec: BlockDeviceMapping and Ebs (with throughput)
    #   troposphere: uses
    # EC2 SpotFleet which used BlockDeviceMapping with
    # However, both
    patches = [
        # backward compatibility - EbsBlockDevice => EBSBlockDevice
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::LaunchTemplate.Ebs",
            "path": "/PropertyTypes/AWS::EC2::LaunchTemplate.EBSBlockDevice",
        },
        {
            "op": "replace",
            "path": "/PropertyTypes/AWS::EC2::Instance.BlockDeviceMapping/Properties/Ebs/Type",
            "value": "EBSBlockDevice",
        },
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::Instance.Ebs",
        },
        {
            "op": "replace",
            "path": "/PropertyTypes/AWS::EC2::LaunchTemplate.BlockDeviceMapping/Properties/Ebs/Type",
            "value": "EBSBlockDevice",
        },
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::SpotFleet.BlockDeviceMapping",
        },
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::LaunchTemplate.BlockDeviceMapping",
            "path": "/PropertyTypes/AWS::EC2::LaunchTemplate.LaunchTemplateBlockDeviceMapping",
        },
        {
            "op": "replace",
            "path": "/PropertyTypes/AWS::EC2::LaunchTemplate.LaunchTemplateData/Properties/BlockDeviceMappings/ItemType",
            "value": "LaunchTemplateBlockDeviceMapping",
        },
        # backward compatibility - NoDevice
        {
            "op": "add",
            "path": "/PropertyTypes/AWS::EC2::Instance.BlockDeviceMapping/Properties/NoDevice/PrimitiveType",
            "value": "dict",
        },
    ]

    return patches


def launchspecification_patches():
    patches = [
        # backward compatibility - SpotFleetLaunchSpecification => LaunchSpecifications
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::SpotFleet.SpotFleetLaunchSpecification",
            "path": "/PropertyTypes/AWS::EC2::SpotFleet.LaunchSpecifications",
        },
        {
            "op": "replace",
            "path": "/PropertyTypes/AWS::EC2::SpotFleet.SpotFleetRequestConfigData/Properties/LaunchSpecifications/ItemType",
            "value": "LaunchSpecifications",
        },
        # {
        #     "op": "move",
        #     "from": "/PropertyTypes/AWS::EC2::SpotFleet.IamInstanceProfileSpecification",
        #     "path": "/PropertyTypes/AWS::EC2::SpotFleet.IamInstanceProfile",
        # },
        # {
        #     "op": "replace",
        #     "path": "/PropertyTypes/AWS::EC2::SpotFleet.LaunchSpecifications/Properties/IamInstanceProfile/Type",
        #     "value": "IamInstanceProfile",
        # },
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::SpotFleet.SpotFleetMonitoring",
            "path": "/PropertyTypes/AWS::EC2::SpotFleet.Monitoring",
        },
        {
            "op": "replace",
            "path": "/PropertyTypes/AWS::EC2::SpotFleet.LaunchSpecifications/Properties/Monitoring/Type",
            "value": "Monitoring",
        },
        # {
        #     "op": "move",
        #     "from": "/PropertyTypes/AWS::EC2::SpotFleet.InstanceNetworkInterfaceSpecification",
        #     "path": "/PropertyTypes/AWS::EC2::SpotFleet.NetworkInterfaces",
        # },
        # {
        #     "op": "replace",
        #     "path": "/PropertyTypes/AWS::EC2::SpotFleet.LaunchSpecifications/Properties/NetworkInterfaces/ItemType",
        #     "value": "NetworkInterfaces",
        # },
        # {
        #     "op": "move",
        #     "from": "/PropertyTypes/AWS::EC2::SpotFleet.SpotPlacement",
        #     "path": "/PropertyTypes/AWS::EC2::SpotFleet.Placement",
        # },
        # {
        #     "op": "replace",
        #     "path": "/PropertyTypes/AWS::EC2::SpotFleet.LaunchSpecifications/Properties/Placement/Type",
        #     "value": "Placement",
        # },
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::SpotFleet.GroupIdentifier",
            "path": "/PropertyTypes/AWS::EC2::SpotFleet.SecurityGroups",
        },
        {
            "op": "replace",
            "path": "/PropertyTypes/AWS::EC2::SpotFleet.LaunchSpecifications/Properties/SecurityGroups/ItemType",
            "value": "SecurityGroups",
        },
    ]

    return patches


def networkinterfaces_patches():
    patches = [
        # backward compatibility
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::Instance.NetworkInterface",
            "path": "/PropertyTypes/AWS::EC2::Instance.NetworkInterfaceProperty",
        },
        {
            "op": "replace",
            "path": "/ResourceTypes/AWS::EC2::Instance/Properties/NetworkInterfaces/ItemType",
            "value": "NetworkInterfaceProperty",
        },
        # backward compatibility and needed for two NetworkInterface properties
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::LaunchTemplate.NetworkInterface",
            "path": "/PropertyTypes/AWS::EC2::LaunchTemplate.NetworkInterfaces",
        },
        {
            "op": "replace",
            "path": "/PropertyTypes/AWS::EC2::LaunchTemplate.LaunchTemplateData/Properties/NetworkInterfaces/ItemType",
            "value": "NetworkInterfaces",
        },
        # backward compatibility
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::LaunchTemplate.PrivateIpAdd",
            "path": "/PropertyTypes/AWS::EC2::LaunchTemplate.PrivateIpAddressSpecification",
        },
        {
            "op": "replace",
            "path": "/PropertyTypes/AWS::EC2::LaunchTemplate.NetworkInterfaces/Properties/PrivateIpAddresses/ItemType",
            "value": "PrivateIpAddressSpecification",
        },
    ]

    return patches


def networkinsightsanalysis_patches():
    patches = [
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::NetworkInsightsAnalysis.AlternatePathHint",
        },
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::NetworkInsightsAnalysis.AnalysisAclRule",
        },
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::NetworkInsightsAnalysis.AnalysisComponent",
        },
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::NetworkInsightsAnalysis.AnalysisLoadBalancerListener",
        },
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::NetworkInsightsAnalysis.AnalysisLoadBalancerTarget",
        },
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::NetworkInsightsAnalysis.AnalysisPacketHeader",
        },
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::NetworkInsightsAnalysis.AnalysisRouteTableRoute",
        },
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::NetworkInsightsAnalysis.AnalysisSecurityGroupRule",
        },
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::NetworkInsightsAnalysis.Explanation",
        },
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::NetworkInsightsAnalysis.PathComponent",
        },
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::NetworkInsightsAnalysis.PortRange",
        },
    ]

    return patches


def targetgroupconfig_patches():
    patches = [
        # backward compatibility
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::SpotFleet.TargetGroupsConfig",
            "path": "/PropertyTypes/AWS::EC2::SpotFleet.TargetGroupConfig",
        },
        {
            "op": "replace",
            "path": "/PropertyTypes/AWS::EC2::SpotFleet.LoadBalancersConfig/Properties/TargetGroupsConfig/Type",
            "value": "TargetGroupConfig",
        },
    ]

    return patches


def transitgatewaymulicast_patches():
    patches = [
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::TransitGatewayMulticastDomain.Options",
            "path": "/PropertyTypes/AWS::EC2::TransitGatewayMulticastDomain.MulticastDomainOptions",
        },
        {
            "op": "replace",
            "path": "/ResourceTypes/AWS::EC2::TransitGatewayMulticastDomain/Properties/Options/Type",
            "value": "MulticastDomainOptions",
        },
    ]

    return patches


patches = (
    tagspecification_patches()
    + blockdevice_patches()
    + launchspecification_patches()
    + networkinterfaces_patches()
    + targetgroupconfig_patches()
    + transitgatewaymulicast_patches()
    + networkinsightsanalysis_patches()
    + [
        # backward compatibility - a combined SecurityGroupRule was used for both Egress and Ingress
        {
            "op": "copy",
            "from": "/PropertyTypes/AWS::EC2::SecurityGroup.Ingress",
            "path": "/PropertyTypes/AWS::EC2::SecurityGroup.SecurityGroupRule",
        },
        # now add some properties from Egress
        {
            "op": "add",
            "path": "/PropertyTypes/AWS::EC2::SecurityGroup.SecurityGroupRule/Properties/DestinationPrefixListId",
            "value": {
                "PrimitiveType": "String",
                "Required": False,
            },
        },
        {
            "op": "add",
            "path": "/PropertyTypes/AWS::EC2::SecurityGroup.SecurityGroupRule/Properties/DestinationSecurityGroupId",
            "value": {
                "PrimitiveType": "String",
                "Required": False,
            },
        },
        # backward compatibility - use list type for egress and ingress
        {
            "op": "add",
            "path": "/ResourceTypes/AWS::EC2::SecurityGroup/Properties/SecurityGroupEgress/PrimitiveType",
            "value": "list",
        },
        {
            "op": "add",
            "path": "/ResourceTypes/AWS::EC2::SecurityGroup/Properties/SecurityGroupIngress/PrimitiveType",
            "value": "list",
        },
        # backward compatibility
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::Instance.AssociationParameter",
            "path": "/PropertyTypes/AWS::EC2::Instance.AssociationParameters",
        },
        {
            "op": "replace",
            "path": "/PropertyTypes/AWS::EC2::Instance.SsmAssociation/Properties/AssociationParameters/ItemType",
            "value": "AssociationParameters",
        },
        # backward compatibility
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::Instance.SsmAssociation",
            "path": "/PropertyTypes/AWS::EC2::Instance.SsmAssociations",
        },
        {
            "op": "replace",
            "path": "/ResourceTypes/AWS::EC2::Instance/Properties/SsmAssociations/ItemType",
            "value": "SsmAssociations",
        },
        # backward compatibility - add MountPoint for Volumes item
        {
            "op": "copy",
            "from": "/PropertyTypes/AWS::EC2::Instance.Volume",
            "path": "/PropertyTypes/AWS::EC2::Instance.MountPoint",
        },
        {
            "op": "add",
            "path": "/ResourceTypes/AWS::EC2::Instance/Properties/Volumes/PrimitiveType",
            "value": "list",
        },
        # backward compatibility - template generator hack
        {
            "op": "add",
            "path": "/ResourceTypes/AWS::EC2::Instance/Properties/SecurityGroupIds/PrimitiveType",
            "value": "list",
        },
        # backward compatibility
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::NetworkAclEntry.Icmp",
            "path": "/PropertyTypes/AWS::EC2::NetworkAclEntry.ICMP",
        },
        {
            "op": "replace",
            "path": "/ResourceTypes/AWS::EC2::NetworkAclEntry/Properties/Icmp/Type",
            "value": "ICMP",
        },
        # Handle duplicate CreditSpecification
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::LaunchTemplate.CreditSpecification",
            "path": "/PropertyTypes/AWS::EC2::LaunchTemplate.LaunchTemplateCreditSpecification",
        },
        {
            "op": "replace",
            "path": "/PropertyTypes/AWS::EC2::LaunchTemplate.LaunchTemplateData/Properties/CreditSpecification/Type",
            "value": "LaunchTemplateCreditSpecification",
        },
        # backward compatibility - LaunchTemplateConfig => LaunchTemplateConfigs
        {
            "op": "move",
            "from": "/PropertyTypes/AWS::EC2::SpotFleet.LaunchTemplateConfig",
            "path": "/PropertyTypes/AWS::EC2::SpotFleet.LaunchTemplateConfigs",
        },
        {
            "op": "replace",
            "path": "/PropertyTypes/AWS::EC2::SpotFleet.SpotFleetRequestConfigData/Properties/LaunchTemplateConfigs/ItemType",
            "value": "LaunchTemplateConfigs",
        },
        {
            "op": "remove",
            "path": "/PropertyTypes/AWS::EC2::NetworkInsightsAnalysis.AdditionalDetail",
        },
    ]
)
