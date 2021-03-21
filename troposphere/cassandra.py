# Copyright (c) 2012-2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import AWSObject
from . import AWSProperty
from . import Tags
from .validators import boolean, integer


VALID_CLUSTERINGKEYCOLUMN_ORDERBY = ('ASC', 'DESC')
VALID_BILLINGMODE_MODE = ('ON_DEMAND', 'PROVISIONED')


def validate_clusteringkeycolumn_orderby(clusteringkeycolumn_orderby):
    if clusteringkeycolumn_orderby not in VALID_CLUSTERINGKEYCOLUMN_ORDERBY:
        raise ValueError("ClusteringKeyColumn OrderBy must be one of: %s" %
                         ', '.join(VALID_CLUSTERINGKEYCOLUMN_ORDERBY))
    return clusteringkeycolumn_orderby


def validate_billingmode_mode(billingmode_mode):
    if billingmode_mode not in VALID_BILLINGMODE_MODE:
        raise ValueError("BillingMode Mode must be one of: %s" %
                         ', '.join(VALID_BILLINGMODE_MODE))
    return billingmode_mode


class Keyspace(AWSObject):
    resource_type = "AWS::Cassandra::Keyspace"

    props = {
        'KeyspaceName': (str, False),
        'Tags': (Tags, False),
    }


class Column(AWSProperty):
    props = {
        "ColumnName": (str, True),
        "ColumnType": (str, True),
    }


class ClusteringKeyColumn(AWSProperty):
    props = {
        "Column": (Column, True),
        "OrderBy": (validate_clusteringkeycolumn_orderby, False),
    }


class ProvisionedThroughput(AWSProperty):
    props = {
        "ReadCapacityUnits": (integer, True),
        "WriteCapacityUnits": (integer, True),
    }


class BillingMode(AWSProperty):
    props = {
        "Mode": (validate_billingmode_mode, True),
        "ProvisionedThroughput": (ProvisionedThroughput, False),
    }


class Table(AWSObject):
    resource_type = "AWS::Cassandra::Table"

    props = {
        "BillingMode": (BillingMode, False),
        "ClusteringKeyColumns": ([ClusteringKeyColumn], False),
        "KeyspaceName": (str, True),
        "PartitionKeyColumns": ([Column], True),
        'PointInTimeRecoveryEnabled': (boolean, False),
        "RegularColumns": ([Column], False),
        "TableName": (str, False),
        'Tags': (Tags, False),
    }
