# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from ..compat import validate_policytype


def policytypes(policy):
    """
    Property: PublicRepository.RepositoryPolicyText
    Property: RegistryPolicy.PolicyText
    Property: Repository.RepositoryPolicyText
    """
    return validate_policytype(policy)
