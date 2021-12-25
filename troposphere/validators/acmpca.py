# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_validity_type(validity_type):
    """
    Certificate Validity Type validation rule.
    Property: Validity.Type
    """
    VALID_VALIDITY_TYPE = ("ABSOLUTE", "DAYS", "END_DATE", "MONTHS", "YEARS")

    if validity_type not in VALID_VALIDITY_TYPE:
        raise ValueError(
            "Certificate Validity Type must be one of: %s"
            % ", ".join(VALID_VALIDITY_TYPE)
        )
    return validity_type


def validate_signing_algorithm(signing_algorithm):
    """
    Certificate SigningAlgorithm validation rule.
    Property: Certificate.SigningAlgorithm
    Property: CertificateAuthority.SigningAlgorithm
    """

    VALID_SIGNIN_ALGORITHM = [
        "SHA256WITHECDSA",
        "SHA256WITHRSA",
        "SHA384WITHECDSA",
        "SHA384WITHRSA",
        "SHA512WITHECDSA",
        "SHA512WITHRSA",
    ]

    if signing_algorithm not in VALID_SIGNIN_ALGORITHM:
        raise ValueError(
            "Certificate SigningAlgorithm must be one of: %s"
            % ", ".join(VALID_SIGNIN_ALGORITHM)
        )
    return signing_algorithm


def validate_key_algorithm(key_algorithm):
    """
    CertificateAuthority KeyAlgorithm validation rule.
    Property: CertificateAuthority.KeyAlgorithm
    """

    VALID_KEY_ALGORITHM = ("EC_prime256v1", "EC_secp384r1", "RSA_2048", "RSA_4096")

    if key_algorithm not in VALID_KEY_ALGORITHM:
        raise ValueError(
            "CertificateAuthority KeyAlgorithm must be one of: %s"
            % ", ".join(VALID_KEY_ALGORITHM)  # NOQA
        )
    return key_algorithm


def validate_certificateauthority_type(certificateauthority_type):
    """
    CertificateAuthority Type validation rule.
    Property: CertificateAuthority.Type
    """

    VALID_CERTIFICATEAUTHORITY_TYPE = ("ROOT", "SUBORDINATE")

    if certificateauthority_type not in VALID_CERTIFICATEAUTHORITY_TYPE:
        raise ValueError(
            "CertificateAuthority Type must be one of: %s"
            % ", ".join(VALID_CERTIFICATEAUTHORITY_TYPE)
        )
    return certificateauthority_type
