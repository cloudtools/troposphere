patches = [
    # Rename AWS::SES::Template.Template to AWS::SES::Template.EmailTemplate - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::SES::Template.Template",
        "path": "/PropertyTypes/AWS::SES::Template.EmailTemplate",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::SES::Template/Properties/Template/Type",
        "value": "EmailTemplate",
    },
    # Resolve conflict between AWS::SES::ReceiptRule.Rule and AWS::SES::MailManagerRuleSet.Rule
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::SES::MailManagerRuleSet.Rule",
        "path": "/PropertyTypes/AWS::SES::MailManagerRuleSet.MailManagerRule",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::SES::MailManagerRuleSet/Properties/Rules/ItemType",
        "value": "MailManagerRule",
    },
    # Resolve conflict between AWS::SES::ReceiptRule.S3Actio and AWS::SES::MailManagerRuleSet.S3Action
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::SES::MailManagerRuleSet.S3Action",
        "path": "/PropertyTypes/AWS::SES::MailManagerRuleSet.MailManagerS3Action",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::SES::MailManagerRuleSet.RuleAction/Properties/WriteToS3/Type",
        "value": "MailManagerS3Action",
    },
]
