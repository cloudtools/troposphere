try:
    from awacs.aws import Policy, PolicyDocument

    policytypes = (dict, Policy, PolicyDocument)  # type: tuple
except ImportError:
    try:
        # A future release of awacs might remove `Policy` in which case
        # `PolicyDocument` should still be supported.  This ensures forward
        # compatibility of current releases of troposphere with future
        # releases of awacs.
        from awacs.aws import PolicyDocument

        policytypes = (dict, PolicyDocument)
    except ImportError:
        policytypes = (dict,)


def validate_policytype(policy):
    if not isinstance(policy, policytypes):
        raise TypeError(
            "Invalid policy type: is %s, expected %s" % type(policy), policytypes
        )
    return policy


__all__ = ["policytypes", "validate_policytype"]
