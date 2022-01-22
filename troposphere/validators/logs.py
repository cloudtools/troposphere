# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


import json

from ..compat import policytypes
from ..constants import LOGS_ALLOWED_RETENTION_DAYS as RETENTION_DAYS
from . import integer_list_item, json_checker

policytypes = policytypes + (str,)


def validate_resource_policy(policy_document):
    """
    validate policy_document. Between 1 to 5120
    Property: ResourcePolicy.PolicyDocument
    """

    if not isinstance(policy_document, policytypes):
        raise ValueError("PolicyDocument must be a valid policy document")

    if isinstance(policy_document, str) and not json_checker(policy_document):
        raise ValueError("PolicyDocument must be a valid JSON formated string")

    if isinstance(policy_document, dict):
        policy_document_text = json.dumps(policy_document)
    elif isinstance(policy_document, str):
        policy_document_text = policy_document
    else:
        policy_document_text = policy_document.to_json()

    # NB: {} empty dict is 2 length
    if len(policy_document_text) < 3:
        raise ValueError("PolicyDocument must not be empty")

    if len(policy_document_text) > 5120:
        raise ValueError("PolicyDocument maximum length must not exceed 5120")

    return policy_document


def validate_loggroup_retention_in_days(x):
    """
    Property: LogGroup.RetentionInDays
    """
    return integer_list_item(RETENTION_DAYS)(x)
