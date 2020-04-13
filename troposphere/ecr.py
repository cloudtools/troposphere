from . import AWSObject, AWSProperty, Tags
from .compat import policytypes


class LifecyclePolicy(AWSProperty):
    props = {
        'LifecyclePolicyText': (basestring, False),
        'RegistryId': (basestring, False),
    }


class Repository(AWSObject):
    resource_type = "AWS::ECR::Repository"

    props = {
        'LifecyclePolicy': (LifecyclePolicy, False),
        'RepositoryName': (basestring, False),
        'RepositoryPolicyText': (policytypes, False),
        'Tags': (Tags, False),
    }
