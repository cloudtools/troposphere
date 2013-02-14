# Copyright (c) 2013, Bob Van Zant <bob@veznat.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags


class WebsiteConfiguration(AWSProperty):
    props = {
        'IndexDocument': (basestring, False),
        'ErrorDocument': (basestring, False),
    }


class Bucket(AWSObject):
    props = {
        'AccessControl': (basestring, False),
        'Tags': (Tags, False),
        'WebsiteConfiguration': (WebsiteConfiguration, False)
    }

    access_control_types = [
        'Private',
        'PublicRead',
        'PublicReadWrite',
        'AuthenticatedRead',
        'BucketOwnerRead',
        'BucketOwnerFullControl',
    ]

    def __init__(self, name, **kwargs):
        self.type = "AWS::S3::Bucket"
        sup = super(Bucket, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)

        if 'AccessControl' in kwargs:
            if kwargs['AccessControl'] not in self.access_control_types:
                raise ValueError('AccessControl must be one of "%s"' % (
                    ', '.join(self.access_control_types)))


