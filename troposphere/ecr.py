from . import AWSObject, AWSProperty
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


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
    }
