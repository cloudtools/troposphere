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
]
