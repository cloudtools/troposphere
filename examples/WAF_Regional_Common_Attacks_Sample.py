# Converted from AWS WAF Sample located at:
# https://s3.amazonaws.com/cloudformation-examples/community/common-attacks.json

from troposphere import (
    Template,
    Parameter,
    Join,
    Ref
)
from troposphere.wafregional import (
    Rule,
    SqlInjectionMatchSet,
    WebACL,
    SizeConstraintSet,
    IPSet,
    XssMatchSet,
    Predicates,
    SqlInjectionMatchTuples,
    FieldToMatch,
    Action,
    Rules,
    SizeConstraint,
    XssMatchTuple
)

t = Template()

t.add_version("2010-09-09")

t.set_description(
    "Creates an AWS WAF configuration that protects against common attacks"
)

WebACLName = t.add_parameter(Parameter(
    "WebACLName",
    Default="CommonAttackProtection",
    Type="String",
    Description="Enter the name you want to use for the WebACL. "
    "This value is also added as a prefix for the names of the rules, "
    "conditions, and CloudWatch metrics created by this template.",
))

SqliMatchSet = t.add_resource(SqlInjectionMatchSet(
    "SqliMatchSet",
    Name=Join("", [Ref(WebACLName), "SqliMatch"]),
    SqlInjectionMatchTuples=[
        SqlInjectionMatchTuples(
            FieldToMatch=FieldToMatch(
                Type="QUERY_STRING"
            ),
            TextTransformation="URL_DECODE"
        ),
        SqlInjectionMatchTuples(
            FieldToMatch=FieldToMatch(
                Type="QUERY_STRING"
            ),
            TextTransformation="HTML_ENTITY_DECODE"
        ),
        SqlInjectionMatchTuples(
            FieldToMatch=FieldToMatch(
                Type="BODY"
            ),
            TextTransformation="URL_DECODE"
        ),
        SqlInjectionMatchTuples(
            FieldToMatch=FieldToMatch(
                Type="BODY"
            ),
            TextTransformation="HTML_ENTITY_DECODE"
        ),
        SqlInjectionMatchTuples(
            FieldToMatch=FieldToMatch(
                Type="URI"
            ),
            TextTransformation="URL_DECODE"
        )
    ]
))

SqliRule = t.add_resource(Rule(
    "SqliRule",
    Predicates=[
        Predicates(
            DataId=Ref(SqliMatchSet),
            Type="SqlInjectionMatch",
            Negated=False
        )
    ],
    Name=Join("", [Ref(WebACLName), "SqliRule"]),
    MetricName=Join("", [Ref(WebACLName), "SqliRule"]),
))

XssMatchSet = t.add_resource(XssMatchSet(
    "XssMatchSet",
    Name=Join("", [Ref(WebACLName), "XssMatch"]),
    XssMatchTuples=[
        XssMatchTuple(
            FieldToMatch=FieldToMatch(
                Type="QUERY_STRING",
            ),
            TextTransformation="URL_DECODE"
        ),
        XssMatchTuple(
            FieldToMatch=FieldToMatch(
                Type="QUERY_STRING",
            ),
            TextTransformation="HTML_ENTITY_DECODE"
        ),
        XssMatchTuple(
            FieldToMatch=FieldToMatch(
                Type="BODY",
            ),
            TextTransformation="URL_DECODE"
        ),
        XssMatchTuple(
            FieldToMatch=FieldToMatch(
                Type="BODY",
            ),
            TextTransformation="HTML_ENTITY_DECODE"
        ),
        XssMatchTuple(
            FieldToMatch=FieldToMatch(
                Type="URI",
            ),
            TextTransformation="URL_DECODE"
        )
    ]
))

XssRule = t.add_resource(Rule(
    "XssRule",
    Name=Join("", [Ref(WebACLName), "XssRule"]),
    Predicates=[
        Predicates(
            DataId=Ref(XssMatchSet),
            Type="XssMatch",
            Negated=False
        )
    ],
    MetricName=Join("", [Ref(WebACLName), "XssRule"]),
))

WAFManualIPBlockSet = t.add_resource(IPSet(
    "WAFManualIPBlockSet",
    Name="Manual IP Block Set",
))

ManualIPBlockRule = t.add_resource(Rule(
    "ManualIPBlockRule",
    Name=Join("", [Ref(WebACLName), "ManualIPBlockRule"]),
    MetricName=Join("", [Ref(WebACLName), "ManualIPBlockRule"]),
    Predicates=[
        Predicates(
            DataId=Ref(WAFManualIPBlockSet),
            Type="IPMatch",
            Negated=False
        )
    ]
))

SizeMatchSet = t.add_resource(SizeConstraintSet(
    "SizeMatchSet",
    Name=Join("", [Ref(WebACLName), "LargeBodyMatch"]),
    SizeConstraints=[
        SizeConstraint(
            ComparisonOperator="GT",
            TextTransformation="NONE",
            FieldToMatch=FieldToMatch(
                Type="BODY"
            ),
            Size="8192"
        )
    ]
))

SizeMatchRule = t.add_resource(Rule(
    "SizeMatchRule",
    Name=Join("", [Ref(WebACLName), "LargeBodyMatchRule"]),
    MetricName=Join("", [Ref(WebACLName), "DetectLargeBody"]),
    Predicates=[
        Predicates(
            DataId=Ref(SizeMatchSet),
            Type="SizeConstraint",
            Negated=False
        )
    ]
))

MyWebACL = t.add_resource(WebACL(
    "MyWebACL",
    Name=Ref(WebACLName),
    DefaultAction=Action(
        Type="ALLOW"
    ),
    Rules=[
        Rules(
            Action=Action(
                Type="BLOCK"
            ),
            Priority=1,
            RuleId=Ref(ManualIPBlockRule)
        ),
        Rules(
            Action=Action(
                Type="COUNT"
            ),
            Priority=2,
            RuleId=Ref(SizeMatchRule)
        ),
        Rules(
            Action=Action(
                Type="BLOCK"
            ),
            Priority=3,
            RuleId=Ref(SqliRule)
        ),
        Rules(
            Action=Action(
                Type="BLOCK"
            ),
            Priority=4,
            RuleId=Ref(XssRule)
        )
    ],
    MetricName=Ref(WebACLName),
))

print(t.to_json())
