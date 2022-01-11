# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_clusteringkeycolumn_orderby(clusteringkeycolumn_orderby):
    """
    Property: ClusteringKeyColumn.OrderBy
    """

    VALID_CLUSTERINGKEYCOLUMN_ORDERBY = ("ASC", "DESC")

    if clusteringkeycolumn_orderby not in VALID_CLUSTERINGKEYCOLUMN_ORDERBY:
        raise ValueError(
            "ClusteringKeyColumn OrderBy must be one of: %s"
            % ", ".join(VALID_CLUSTERINGKEYCOLUMN_ORDERBY)
        )
    return clusteringkeycolumn_orderby


def validate_billingmode_mode(billingmode_mode):
    """
    Property: BillingMode.Mode
    """

    VALID_BILLINGMODE_MODE = ("ON_DEMAND", "PROVISIONED")

    if billingmode_mode not in VALID_BILLINGMODE_MODE:
        raise ValueError(
            "BillingMode Mode must be one of: %s" % ", ".join(VALID_BILLINGMODE_MODE)
        )
    return billingmode_mode
