# Contributing to troposphere

# How to Get Help
We have a Google Group, [cloudtools-dev](https://groups.google.com/forum/#!forum/cloudtools-dev),
where you can ask questions and engage with the troposphere community. Issues and pull requests are always
welcome!

# Contributing Example Code
New example code should go into `troposphere/examples`. The expected
CloudFormation Template should be stored in `troposphere/tests/examples_output/`.
When tests are run the output of the code in the examples directory will
be compared with the expected results in the `example_output` directory.

# Core troposphere code base

## A brief historical comment

When the project was first created each class was handcoded from the CloudFormation documentation.
Thus the code base grew organically as new validation routines and features were added. This was a
bit challenging to know what new resources and properties were added periodically from AWS.

Eventually AWS added the Resource Specification and started publishing machine readable versions but
initially it had quite a few errors and inconsistencies. An early code generator was used for adding
new resources and delta changes to existing code but still needed hand tweaking.

An updated code generator is now available but may require tweaks to handle inconsistencies or backward compatibility.
There is use of jsonpatch to handle some of these changes within the Resource Specification and the validation code has
been moved into separate code files to allow the code generator to more easily update the generated classes.

## About backward compatibility

The troposphere authors strive to maintain backward compatibility within
a single major versions of this library (i.e., 2.1.0 to 2.2.0 would be backward compatible but not for 2.1.0 to 3.0.0).
However, there may be some minor breaks that occur in minor versions to correct errors, fix CloudFormation compatibility, and/or clarify usage.

## Generating troposphere code

The code that gets generated is for the Resources and Properties associated with CloudFormation to help determine the type of each
property and whether it is a *required* field. There is other code to perform more thorough class or property validation.

To download a new Resource Specification:
```
make spec
```
To generate code, the current process is roughly, scan the CloudFormation history to identify changes and then run (using S3 as an example):

```
python3 scripts/gen.py s3 > troposphere/s3.py
```
Use the auto-formatters to clean up the generated code using:
```
make fix
```

Verify the changes using:
```
git diff
```
Further verification can be done via:
```
make lint test
```

If everything looks ok, further tests can be run prior to a PR such as:
```
make lint
```

## Handling errors in the Resource Specification

Let's walk through some of the issues that may need to be tweaked in the Resource Specification.
The application of jsonpatch changes are done by the code generator by applying all of the changes
locationed in `scripts/patches` looking for a `patch` list in each file.

### Resource and Properties using the same name

The Python classes used by troposphere must have unique names. But occaisionally CloudFormation services will reuse the same name. 
Here is one example of a Resource and Property needing to be renamed:

```
# Rename AWS::IoTSiteWise::AccessPolicy.Portal to AWS::IoTSiteWise::AccessPolicy.PortalProperty due to conflict with Portal resource name
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::IoTSiteWise::AccessPolicy.Portal",
        "path": "/PropertyTypes/AWS::IoTSiteWise::AccessPolicy.PortalProperty",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::IoTSiteWise::AccessPolicy.AccessPolicyResource/Properties/Portal/Type",
        "value": "PortalProperty",
    },
```
The first patch will move (rename) the Property from Portal to PortalProperty.
The second patch will adjust the usage of this new name within the Property that contains it.

The above example replaces the *Type* field. But sometimes there is a need to use *ItemType* in cases where there is a List or Map of a type.

```
    # Rename AWS::Lightsail::Instance.Disk to AWS::Lightsail::Instance.DiskProperty
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Lightsail::Instance.Disk",
        "path": "/PropertyTypes/AWS::Lightsail::Instance.DiskProperty",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Lightsail::Instance.Hardware/Properties/Disks/ItemType",
        "value": "DiskProperty",
    },
```

### Backward compatibility

Early on it was not always clear what AWS wanted Resources and Properties named. These
names have been kept historically for backward compatibility (although these might change
 in a future release). Thus, the names used in code generation must be maintained.
 An S3 example to maintain the seage of `S3Key` instead of the current name `S3KeyFilter`.

```
    # Rename AWS::S3::Bucket.S3KeyFilter to AWS::S3::Bucket.S3Key - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::S3::Bucket.S3KeyFilter",
        "path": "/PropertyTypes/AWS::S3::Bucket.S3Key",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.NotificationFilter/Properties/S3Key/Type",
        "value": "S3Key",
    },
```

### Same name, different property

Usually the same name for a property will be the same within the same service But occasionally this is not the case.
Thus names need to be made unique within a given service (file). In this example, *FieldToMatch* is used 3 times within
WAFv2 with 2 different Property contents. This renames the LoggingConfiguration *FieldToMatch* to *LoggingConfigurationFieldToMatch*.

```
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFv2::LoggingConfiguration.FieldToMatch",
        "path": "/PropertyTypes/AWS::WAFv2::LoggingConfiguration.LoggingConfigurationFieldToMatch",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAFv2::LoggingConfiguration/Properties/RedactedFields/ItemType",
        "value": "LoggingConfigurationFieldToMatch",
    },
```

## Validating types and classes

One of the core reasons to use troposphere is to help with the validation of the CloudFormation template prior to applying it into AWS.
The code generator will usually do type validation to ensure the correct type is used for a property and tje *required* field which will
warn if there are missing required fields. The other validators allow for functions to do further type and value validation along with
class validation.

### Property type function validators

For some primitive types (Boolean, Integer, Double, String), the code generator will insert a type validator automatically.
This helps ensure the given value can be coerced into a the correct type. Here are two examples for boolean and integer validation:

```
def boolean(x):
    if x in [True, 1, "1", "true", "True"]:
        return True
    if x in [False, 0, "0", "false", "False"]:
        return False
    raise ValueError


def integer(x):
    try:
        int(x)
    except (ValueError, TypeError):
        raise ValueError("%r is not a valid integer" % x)
    else:
        return x
```

Another one is to verfify a network port is an integer and checks for either -1 or the port to be between 0 and 65535:

```
def network_port(x):
    from .. import AWSHelperFn

    # Network ports can be Ref items
    if isinstance(x, AWSHelperFn):
        return x

    i = integer(x)
    if int(i) < -1 or int(i) > 65535:
        raise ValueError("network port %r must been between 0 and 65535" % i)
    return x
```

Most properties can have a helper function (If, FindInMap, Ref, etc.) so there is a check for those included.

### Property value function validators

Another use of validators is to ensure the value is correct. This is usually fields that accept a limited set
of strings for their value. Here is an example for
[AWS::S3::Bucket AccelerateConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-accelerateconfiguration.html)
which requires the field to be either "Enabled" or "Suspended":

```
def s3_transfer_acceleration_status(value):
    """
    Property: AccelerateConfiguration.AccelerationStatus
    """
    valid_status = ["Enabled", "Suspended"]
    if value not in valid_status:
        raise ValueError(
            'AccelerationStatus must be one of: "%s"' % (", ".join(valid_status))
        )
    return value
```

In the past these validators were included in the main code base (`troposphere/*.py`) but are now located in
`troposphere/validators` directory with corresponding names (`troposphere/validators/s3.py`) in the case of the above.
Note the docstring contains `Property: AccelerateConfiguration.AccelerationStatus` which is parse by the code generator
to apply this validator to the correct Property. This can be used multiple times since the same validator could apply in
several different places.

### Class function validators

A class function validator will usually look at several different properties to determine if the class is valid.
As mentioned above, these used to be in the main code but are now in the validation directory.

Some simple examples from CodeDeploy:

The LoadBalancerInfo property must have either an ElbInfoList or TargetGroupInfoList defined.
```
def validate_load_balancer_info(self):
    """
    Class: LoadBalancerInfo
    """
    conds = ["ElbInfoList", "TargetGroupInfoList"]
    exactly_one(self.__class__.__name__, self.properties, conds)
```

This shows where fields must be mutually exclusive.
```
def validate_deployment_group(self):
    """
    Class: DeploymentGroup
    """
    ec2_conds = ["EC2TagFilters", "Ec2TagSet"]
    onPremises_conds = ["OnPremisesInstanceTagFilters", "OnPremisesTagSet"]
    mutually_exclusive(self.__class__.__name__, self.properties, ec2_conds)
    mutually_exclusive(self.__class__.__name__, self.properties, onPremises_conds)
```
