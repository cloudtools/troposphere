# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


VALID_TAINT_EFFECT = ["NO_EXECUTE", "NO_SCHEDULE", "PREFER_NO_SCHEDULE"]


def validate_taint_effect(taint_effect):
    """
    Taint Effect validation rule.
    Property: Taint.Effect
    """
    if taint_effect not in VALID_TAINT_EFFECT:
        raise ValueError(
            "Taint Effect must be one of: %s" % ", ".join(VALID_TAINT_EFFECT)
        )
    return taint_effect


def validate_taint_key(taint_key):
    """
    Taint Key validation rule.
    Property: Taint.Key
    """
    if len(taint_key) < 1 or len(taint_key) > 63:
        raise ValueError(
            "Taint Key must be at least 1 character and maximum 63 characters"
        )
    return taint_key


def validate_taint_value(taint_value):
    """
    Taint Value validation rule.
    Property: Taint.Value
    """
    if len(taint_value) > 63:
        raise ValueError("Taint Value maximum characters is 63")
    return taint_value


def validate_cluster_logging(self):
    """
    Class: ClusterLogging
    """
    enabled_types = set(
        [x.properties["Type"] for x in self.properties.get("EnabledTypes")]
    )
    conditionals = [
        "api",
        "audit",
        "authenticator",
        "controllerManager",
        "scheduler",
    ]
    if not (enabled_types.issubset(conditionals)):
        raise ValueError(
            "%s must be one of: %s"
            % (", ".join(enabled_types), ", ".join(conditionals))
        )
