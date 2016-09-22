from __future__ import print_function

from troposphere import (
    Template, Parameter, Ref, Condition, Equals, And, Or, Not, If
)
from troposphere import ec2


parameters = {
    "One": Parameter(
        "One",
        Type="String",
    ),
    "Two": Parameter(
        "Two",
        Type="String",
    ),
    "Three": Parameter(
        "Three",
        Type="String",
    ),
    "Four": Parameter(
        "Four",
        Type="String",
    ),
    "SshKeyName": Parameter(
        "SshKeyName",
        Type="String",
    )
}

conditions = {
    "OneEqualsFoo": Equals(
        Ref("One"),
        "Foo"
    ),
    "NotOneEqualsFoo": Not(
        Condition("OneEqualsFoo")
    ),
    "BarEqualsTwo": Equals(
        "Bar",
        Ref("Two")
    ),
    "ThreeEqualsFour": Equals(
        Ref("Three"),
        Ref("Four")
    ),
    "OneEqualsFooOrBarEqualsTwo": Or(
        Condition("OneEqualsFoo"),
        Condition("BarEqualsTwo")
    ),
    "OneEqualsFooAndNotBarEqualsTwo": And(
        Condition("OneEqualsFoo"),
        Not(Condition("BarEqualsTwo"))
    ),
    "OneEqualsFooAndBarEqualsTwoAndThreeEqualsPft": And(
        Condition("OneEqualsFoo"),
        Condition("BarEqualsTwo"),
        Equals(Ref("Three"), "Pft")
    ),
    "OneIsQuzAndThreeEqualsFour": And(
        Equals(Ref("One"), "Quz"),
        Condition("ThreeEqualsFour")
    ),
    "LaunchInstance": And(
        Condition("OneEqualsFoo"),
        Condition("NotOneEqualsFoo"),
        Condition("BarEqualsTwo"),
        Condition("OneEqualsFooAndNotBarEqualsTwo"),
        Condition("OneIsQuzAndThreeEqualsFour")
    ),
    "LaunchWithGusto": And(
        Condition("LaunchInstance"),
        Equals(Ref("One"), "Gusto")
    )
}

resources = {
    "Ec2Instance": ec2.Instance(
        "Ec2Instance",
        Condition="LaunchInstance",
        ImageId=If("ConditionNameEqualsFoo", "ami-12345678", "ami-87654321"),
        InstanceType="t1.micro",
        KeyName=Ref("SshKeyName"),
        SecurityGroups=["default"],
    )
}

t = Template()

for p in parameters.values():
    t.add_parameter(p)
for k in conditions:
    t.add_condition(k, conditions[k])
for r in resources.values():
    t.add_resource(r)

print(t.to_json())
