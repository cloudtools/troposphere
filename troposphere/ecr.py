from . import AWSObject
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


class Repository(AWSObject):
    resource_type = "AWS::ECR::Repository"

    props = {
        'RepositoryName': (basestring, False),
        'RepositoryPolicyText': (policytypes, False),
    }
