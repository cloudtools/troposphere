# Copyright (c) 2016, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty, Tags


class S3(AWSProperty):
    props = {
        'Bucket': (basestring, True),
        'Key': (basestring, True),
        'ObjectVersion': (basestring, False),
    }


class Code(AWSProperty):
    props = {
        'BranchName': (basestring, False),
        'S3': (S3, True)
    }


class Trigger(AWSProperty):
    props = {
        'Branches': ([basestring], False),
        'CustomData': (basestring, False),
        'DestinationArn': (basestring, False),
        'Events': ([basestring], False),
        'Name': (basestring, False),
    }

    def validate(self):
        valid = [
            'all',
            'createReference',
            'deleteReference',
            'updateReference',
        ]
        events = self.properties.get('Events')
        if events and not isinstance(events, AWSHelperFn):
            if 'all' in events and len(events) != 1:
                raise ValueError('Trigger events: all must be used alone')
            else:
                for e in events:
                    if e not in valid and not isinstance(e, AWSHelperFn):
                        raise ValueError('Trigger: invalid event %s' % e)


class Repository(AWSObject):
    resource_type = "AWS::CodeCommit::Repository"

    props = {
        'Code': (Code, False),
        'RepositoryDescription': (basestring, False),
        'RepositoryName': (basestring, True),
        'Tags': (Tags, False),
        'Triggers': ([Trigger], False),
    }
