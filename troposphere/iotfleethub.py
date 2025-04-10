# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, PropsDictType, Tags


class Application(AWSObject):
    """
    `Application <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html>`__
    """

    resource_type = "AWS::IoTFleetHub::Application"

    props: PropsDictType = {
        "ApplicationDescription": (str, False),
        "ApplicationName": (str, True),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
    }
