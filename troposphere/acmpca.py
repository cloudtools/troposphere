# Copyright (c) 2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import (boolean, integer)

VALID_SIGNIN_ALGORITHM = ('SHA256WITHECDSA', 'SHA256WITHRSA',
                          'SHA384WITHECDSA', 'SHA384WITHRSA',
                          'SHA512WITHECDSA', 'SHA512WITHRSA')
VALID_VALIDITY_TYPE = ('ABSOLUTE', 'DAYS', 'END_DATE',
                       'MONTHS', 'YEARS')
VALID_KEY_ALGORITHM = ('EC_prime256v1', 'EC_secp384r1',
                       'RSA_2048', 'RSA_4096')
VALID_CERTIFICATEAUTHORITY_TYPE = ('ROOT', 'SUBORDINATE')


def validate_validity_type(validity_type):
    """Certificate Validity Type validation rule."""
    if validity_type not in VALID_VALIDITY_TYPE:
        raise ValueError("Certificate Validity Type must be one of: %s" %
                         ", ".join(VALID_VALIDITY_TYPE))
    return validity_type


def validate_signing_algorithm(signing_algorithm):
    """Certificate SigningAlgorithm validation rule."""
    if signing_algorithm not in VALID_SIGNIN_ALGORITHM:
        raise ValueError("Certificate SigningAlgorithm must be one of: %s" %
                         ", ".join(VALID_SIGNIN_ALGORITHM))
    return signing_algorithm


def validate_key_algorithm(key_algorithm):
    """CertificateAuthority KeyAlgorithm validation rule."""
    if key_algorithm not in VALID_KEY_ALGORITHM:
        raise ValueError("CertificateAuthority KeyAlgorithm must be one of: %s" %  # NOQA
                         ", ".join(VALID_KEY_ALGORITHM))
    return key_algorithm


def validate_certificateauthority_type(certificateauthority_type):
    """CertificateAuthority Type validation rule."""
    if certificateauthority_type not in VALID_CERTIFICATEAUTHORITY_TYPE:
        raise ValueError("CertificateAuthority Type must be one of: %s" %
                         ", ".join(VALID_CERTIFICATEAUTHORITY_TYPE))
    return certificateauthority_type


class Qualifier(AWSProperty):
    props = {
        'CpsUri': (basestring, True),
    }


class PolicyQualifierInfo(AWSProperty):
    props = {
        'PolicyQualifierId': (basestring, True),
        'Qualifier': (Qualifier, True),
    }


class PolicyQualifierInfoList(AWSProperty):
    props = {
        'PolicyQualifierInfoList': ([PolicyQualifierInfo], False),
    }


class PolicyInformation(AWSProperty):
    props = {
        'CertPolicyId': (basestring, True),
        'PolicyQualifiers': (PolicyQualifierInfoList, False),
    }


class CertificatePolicyList(AWSProperty):
    props = {
        'CertificatePolicyList': ([PolicyInformation], False),
    }


class ExtendedKeyUsage(AWSProperty):
    props = {
        'ExtendedKeyUsageObjectIdentifier': (basestring, False),
        'ExtendedKeyUsageType': (basestring, False),
    }


class ExtendedKeyUsageList(AWSProperty):
    props = {
        'ExtendedKeyUsageList': ([ExtendedKeyUsage], False),
    }


class EdiPartyName(AWSProperty):
    props = {
        'NameAssigner': (basestring, True),
        'PartyName': (basestring, True),
    }


class OtherName(AWSProperty):
    props = {
        'TypeId': (basestring, True),
        'Value': (basestring, True),
    }


class Subject(AWSProperty):
    props = {
        'CommonName': (basestring, False),
        'Country': (basestring, False),
        'DistinguishedNameQualifier': (basestring, False),
        'GenerationQualifier': (basestring, False),
        'GivenName': (basestring, False),
        'Initials': (basestring, False),
        'Locality': (basestring, False),
        'Organization': (basestring, False),
        'OrganizationalUnit': (basestring, False),
        'Pseudonym': (basestring, False),
        'SerialNumber': (basestring, False),
        'State': (basestring, False),
        'Surname': (basestring, False),
        'Title': (basestring, False),
    }


class GeneralName(AWSProperty):
    props = {
        'DirectoryName': (Subject, False),
        'DnsName': (basestring, False),
        'EdiPartyName': (EdiPartyName, False),
        'IpAddress': (basestring, False),
        'OtherName': (OtherName, False),
        'RegisteredId': (basestring, False),
        'Rfc822Name': (basestring, False),
        'UniformResourceIdentifier': (basestring, False),
    }


class GeneralNameList(AWSProperty):
    props = {
        'GeneralNameList': ([GeneralName], False),
    }


class KeyUsage(AWSProperty):
    props = {
        'CRLSign': (boolean, False),
        'DataEncipherment': (boolean, False),
        'DecipherOnly': (boolean, False),
        'DigitalSignature': (boolean, False),
        'EncipherOnly': (boolean, False),
        'KeyAgreement': (boolean, False),
        'KeyCertSign': (boolean, False),
        'KeyEncipherment': (boolean, False),
        'NonRepudiation': (boolean, False),
    }


class Extensions(AWSProperty):
    props = {
        'CertificatePolicies': (CertificatePolicyList, False),
        'ExtendedKeyUsage': (ExtendedKeyUsageList, False),
        'KeyUsage': (KeyUsage, False),
        'SubjectAlternativeNames': (GeneralNameList, False),
    }


class ApiPassthrough(AWSProperty):
    props = {
        'Extensions': (Extensions, False),
        'Subject': (Subject, False),
    }


class Validity(AWSProperty):
    props = {
        'Type': (validate_validity_type, True),
        'Value': (integer, True),
    }


class Certificate(AWSObject):
    resource_type = "AWS::ACMPCA::Certificate"

    props = {
        'ApiPassthrough': (ApiPassthrough, False),
        'CertificateAuthorityArn': (basestring, True),
        'CertificateSigningRequest': (basestring, True),
        'SigningAlgorithm': (validate_signing_algorithm, True),
        'TemplateArn': (basestring, False),
        'Validity': (Validity, True),
        'ValidityNotBefore': (Validity, False),
    }


class CertificateAuthorityActivation(AWSObject):
    resource_type = "AWS::ACMPCA::CertificateAuthorityActivation"

    props = {
        'Certificate': (basestring, True),
        'CertificateAuthorityArn': (basestring, True),
        'CertificateChain': (basestring, False),
        'Status': (basestring, False),
    }


class CrlConfiguration(AWSProperty):
    props = {
        'CustomCname': (basestring, False),
        'Enabled': (boolean, False),
        'ExpirationInDays': (integer, False),
        'S3BucketName': (basestring, False),
    }


class RevocationConfiguration(AWSProperty):
    props = {
        'CrlConfiguration': (CrlConfiguration, False)
    }


class Subject(AWSProperty):
    props = {
        'CommonName': (basestring, False),
        'Country': (basestring, False),
        'DistinguishedNameQualifier': (basestring, False),
        'GenerationQualifier': (basestring, False),
        'GivenName': (basestring, False),
        'Initials': (basestring, False),
        'Locality': (basestring, False),
        'Organization': (basestring, False),
        'OrganizationalUnit': (basestring, False),
        'Pseudonym': (basestring, False),
        'SerialNumber': (basestring, False),
        'State': (basestring, False),
        'Surname': (basestring, False),
        'Title': (basestring, False),
    }


class CertificateAuthority(AWSObject):
    resource_type = "AWS::ACMPCA::CertificateAuthority"

    props = {
        'KeyAlgorithm': (validate_key_algorithm, True),
        'RevocationConfiguration': (RevocationConfiguration, False),
        'SigningAlgorithm': (validate_signing_algorithm, True),
        'Subject': (Subject, True),
        'Tags': (Tags, False),
        'Type': (validate_certificateauthority_type, True),
    }
