from . import AWSObject, AWSProperty


class DomainValidationOption(AWSProperty):
    props = {
        'DomainName': (basestring, True),
        'ValidationDomain': (basestring, True),
    }


class Certificate(AWSObject):
    resource_type = "AWS::CertificateManager::Certificate"

    props = {
        'DomainName': (basestring, True),
        'DomainValidationOptions': ([DomainValidationOption], False),
        'SubjectAlternativeNames': ([basestring], False),
        'Tags': (list, False)
    }
