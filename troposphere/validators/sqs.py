# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from ..compat import validate_policytype


def policytypes(policy):
    """
    Property: QueuePolicy.PolicyDocument
    """
    return validate_policytype(policy)


def validate_queue(self):
    """
    Class: Queue
    """
    from .. import AWSHelperFn

    if self.properties.get("FifoQueue"):
        queuename = self.properties.get("QueueName")
        if queuename is None or isinstance(queuename, AWSHelperFn):
            pass
        elif not queuename.endswith(".fifo"):
            raise ValueError(
                "SQS: FIFO queues need to provide a " "QueueName that ends with '.fifo'"
            )
