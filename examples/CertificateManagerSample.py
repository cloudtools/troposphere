from troposphere import Template
from troposphere.certificatemanager import Certificate, DomainValidationOption

t = Template()

t.add_resource(
    Certificate(
        'mycert',
        DomainName='example.com',
        DomainValidationOptions=[
            DomainValidationOption(
                DomainName='example.com',
                ValidationDomain='example.com',
            ),
        ],
        Tags=[
            {
                'Key': 'tag-key',
                'Value': 'tag-value'
            },
        ],
    )
)

print(t.to_json())
