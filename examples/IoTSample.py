from troposphere import Template
from troposphere.iot import (
    Certificate,
    Policy,
    PolicyPrincipalAttachment,
    Thing,
    ThingPrincipalAttachment,
    TopicRule,
    TopicRulePayload,
    Action,
    LambdaAction,
    IotAnalyticsAction,
)


t = Template()

certificate = Certificate(
    'MyCertificate',
    CertificateSigningRequest='CSRParameter',
    Status='StatusParameter',
)

policy = Policy(
    'MyPolicy',
    PolicyDocument={'Version': '2012-10-17'},
    PolicyName='NameParameter',
)

policy_principal = PolicyPrincipalAttachment(
    'MyPolicyPrincipalAttachment',
    PolicyName='NameParameter',
    Principal='arn:aws:iot:ap-southeast-2:123456789012',
)

thing = Thing(
    'MyThing',
    AttributePayload={
        'Attributes': {
            'myAttributeA': 'MyAttributeValueA',
            'myAttributeB': 'MyAttributeValueB',
        }
    },
    ThingName='NameParameter',
)

thing_principal = ThingPrincipalAttachment(
    'MyThingPrincipalAttachment',
    ThingName='NameParameter',
    Principal='arn:aws:iot:ap-southeast-2:123456789012',
)

topic_rule = TopicRule(
    'MyTopicRule',
    RuleName='NameParameter',
    TopicRulePayload=TopicRulePayload(
        RuleDisabled=True,
        Sql='SELECT temp FROM SomeTopic WHERE temp > 60',
        Actions=[
            Action(
                Lambda=LambdaAction(
                    FunctionArn='arn',
                ),
            ),
            Action(
                IotAnalytics=IotAnalyticsAction(
                    ChannelName='mychannel',
                    RoleArn='arn',
                ),
            ),
        ],
    ),
)

t.add_resource(certificate)
t.add_resource(policy)
t.add_resource(policy_principal)
t.add_resource(thing)
t.add_resource(thing_principal)
t.add_resource(topic_rule)

print(t.to_json())
