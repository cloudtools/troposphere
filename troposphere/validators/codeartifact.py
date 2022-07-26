# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from ..compat import validate_policytype


def policytypes(policy):
    """
    Property: Domain.PermissionsPolicyDocument
    Property: Repository.PermissionsPolicyDocument
    """
    return validate_policytype(policy)
