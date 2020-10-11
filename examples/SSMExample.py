from troposphere import Ref, Template, Parameter
from troposphere.constants import STRING
import troposphere.ssm as ssm

t = Template()
t.set_description("2012-09-09")

rhel_patch_group_name = t.add_parameter(Parameter(
    "RHELPatchGroupName",
    Type=STRING,
    Description="The value of the RHEL patch group tag "
                "that will have the baseline applied to them."
        ))

windows_patch_group_name = t.add_parameter(Parameter(
    "WindowsPatchGroupName",
    Type=STRING,
    Description="The value of the Windows patch group tag"
                "that will have baseline applied to them."
))

linux_filter_group = ssm.PatchFilterGroup(
    "LinuxGroup",
    PatchFilters=[ssm.PatchFilter(
        "Linuxfilter",
        Key="CLASSIFICATION",
        Values=["Security"])]
)

windows_filter_group = ssm.PatchFilterGroup(
    "windowsGroup",
    PatchFilters=[ssm.PatchFilter(
        "WindowsFilter",
        Key="CLASSIFICATION",
        Values=["SecurityUpdates"])]
)

linux_rule_group = ssm.RuleGroup(
    "LinuxRuleGroup",
    PatchRules=[ssm.Rule(
                "LinuxBaseRule",
                ApproveAfterDays=90,
                ComplianceLevel="CRITICAL",
                PatchFilterGroup=linux_filter_group
                )]
        )

windows_rule_group = ssm.RuleGroup(
    "WindowsRuleGroup",
    PatchRules=[ssm.Rule(
                "WindowsBaseRule",
                ApproveAfterDays=90,
                ComplianceLevel="CRITICAL",
                PatchFilterGroup=windows_filter_group
                )]
)

t.add_resource(ssm.PatchBaseline(
            "RHELBASELINE",
            ApprovalRules=linux_rule_group,
            Description="Baseline containing all updates approved",
            Name=Ref(rhel_patch_group_name),
            OperatingSystem="REDHAT_ENTERPRISE_LINUX",
            PatchGroups=[Ref(rhel_patch_group_name)]

        ))

t.add_resource(ssm.PatchBaseline(
            "WINDOWSBASELINE",
            ApprovalRules=windows_rule_group,
            Description="Baseline containing all updates approved",
            Name=Ref(windows_patch_group_name),
            OperatingSystem="WINDOWS",
            PatchGroups=[Ref(windows_patch_group_name)]
        ))

t.add_resource(ssm.Parameter(
        "WindowsBaselineTimestampParameter",
        Name="/OS/WINDOWS",
        Type="String",
        Value="Windows TIMESTAMP_VALUE"
    ))

t.add_resource(ssm.Parameter(
        "LinuxBaselineTimestampParameter",
        Name="/OS/REDHAT",
        Type="String",
        Value="Redhat TIME_STAMP_VALUE"
    ))

print(t.to_json())
