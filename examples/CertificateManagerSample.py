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
    )
)

print(t.to_json())
