patches = [
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Cognito::IdentityPoolRoleAttachment.RulesConfigurationType",
        "path": "/PropertyTypes/AWS::Cognito::IdentityPoolRoleAttachment.RulesConfiguration",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Cognito::IdentityPoolRoleAttachment.RoleMapping/Properties/RulesConfiguration/Type",
        "value": "RulesConfiguration",
    },
]
