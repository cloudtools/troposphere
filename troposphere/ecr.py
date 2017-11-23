from . import AWSObject
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


class LifecyclePolicy(AWSObject):
    props = {
        'LifecyclePolicyText': (basestring, False),
        'RegistryId': (basestring, False),
    }


class Repository(AWSObject):
    resource_type = "AWS::ECR::Repository"

    props = {
        'LifecyclePolicy': (basestring, False),
        'RepositoryName': (basestring, False),
        'RepositoryPolicyText': (policytypes, False),
    }
