# GitHub Copilot Instructions for Troposphere

## Project Overview

**Troposphere** is a Python library for programmatically generating AWS CloudFormation templates. This fork (published as `troppan`) is maintained by Viaplay Group to ensure availability and support for the latest CloudFormation specifications.

### Key Characteristics
- **Auto-generated codebase**: Most AWS service modules are generated from CloudFormation Resource Specification
- **Type-safe**: Extensive use of type hints and validation
- **Comprehensive AWS coverage**: 150+ AWS service modules with full property validation
- **Template-first approach**: Focus on CloudFormation template generation and validation

## Project Structure

```
troposphere/
├── __init__.py           # Core classes: Template, AWSObject, AWSProperty, AWSHelperFn
├── [service].py          # AWS service modules (ec2.py, s3.py, lambda.py, etc.)
├── helpers/              # Utility functions and helper classes
├── validators/           # Validation functions for properties and resources
├── type_defs/            # Type definitions and compatibility layer
└── openstack/            # OpenStack Heat template support

scripts/
├── gen.py               # Code generator from CloudFormation specs
├── regen                # Regeneration script
└── cfn2py               # CloudFormation JSON to Python converter

examples/                # Usage examples for various AWS services
tests/                   # Test suite
docs/                    # Documentation
```

## Core Architecture

### Base Classes
- **`AWSObject`**: Base class for all CloudFormation resources
- **`AWSProperty`**: Base class for resource properties
- **`AWSHelperFn`**: Base class for CloudFormation intrinsic functions
- **`Template`**: Main template container class

### Code Generation
- AWS service modules are auto-generated from CloudFormation Resource Specification
- Generator script: `scripts/gen.py`
- Regeneration: `make spec regen`
- Validation functions in `troposphere/validators/`

## Development Patterns

### Resource Definition Pattern
```python
class MyResource(AWSObject):
    resource_type = "AWS::Service::ResourceType"
    
    props: PropsDictType = {
        'PropertyName': (str, True),     # (type, required)
        'OptionalProperty': (int, False),
        'ValidatedProperty': (validate_function, True),
    }
```

### Property Class Pattern
```python
class MyProperty(AWSProperty):
    props: PropsDictType = {
        'StringProperty': (str, True),
        'IntegerProperty': (integer_range(1, 100), False),
        'BooleanProperty': (boolean, False),
    }
```

### Template Usage Pattern
```python
from troposphere import Template, Ref
from troposphere.ec2 import Instance

t = Template()
t.set_description("My CloudFormation template")

instance = t.add_resource(Instance(
    "MyInstance",
    ImageId="ami-12345678",
    InstanceType="t3.micro"
))

# Use Ref() for references
t.add_output(Output(
    "InstanceId",
    Value=Ref(instance)
))
```

## Validation and Type Safety

### Common Validators
- `boolean`: Convert various formats to boolean
- `integer`: Validate integer values
- `integer_range(min, max)`: Validate integer within range
- `network_port`: Validate network port numbers
- `s3_bucket_name`: Validate S3 bucket naming rules

### Property Validation
```python
props: PropsDictType = {
    'Port': (network_port, True),
    'Enabled': (boolean, False),
    'Count': (integer_range(1, 10), True),
}
```

### Custom Validators
Located in `troposphere/validators/[service].py`:
```python
def my_custom_validator(value):
    """Validator for MyProperty
    
    Property: MyProperty validation
    """
    if not valid_condition(value):
        raise ValueError("Invalid value")
    return value
```

## Code Generation Guidelines

### When Modifying Generated Code
- **DON'T** edit generated service modules directly
- **DO** update the CloudFormation spec: `make spec`
- **DO** regenerate code: `make regen`
- **DO** add custom validators in `troposphere/validators/`

### Manual Code Guidelines
- Follow existing patterns in `__init__.py`
- Use type hints extensively
- Add comprehensive docstrings
- Include validation where appropriate

## Testing Patterns

### Resource Testing
```python
def test_my_resource():
    resource = MyResource(
        "TestResource",
        RequiredProperty="value"
    )
    assert resource.resource_type == "AWS::Service::MyResource"
    assert resource.properties["RequiredProperty"] == "value"
```

### Template Testing
```python
def test_template_generation():
    t = Template()
    resource = t.add_resource(MyResource("Test"))
    
    template_dict = t.to_dict()
    assert "Resources" in template_dict
    assert "Test" in template_dict["Resources"]
```

### Validation Testing
```python
def test_validation():
    with pytest.raises(ValueError):
        MyResource("Test", InvalidProperty="bad_value")
```

## Common Tasks

### Adding a New Validator
1. Create validator function in appropriate `validators/[service].py`
2. Add docstring with "Property: PropertyName validation"
3. Regenerate code: `make regen`

### Supporting New CloudFormation Features
1. Update spec: `make spec`
2. Regenerate: `make regen`
3. Test: `make test`
4. Fix any validation issues

### Creating Examples
1. Add to `examples/` directory
2. Follow naming pattern: `ServiceName_FeatureName.py`
3. Include comprehensive comments
4. Test the generated CloudFormation

## Build and Release

### Development Workflow
```bash
# Setup environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

# Update to latest CloudFormation spec
make spec regen

# Format code
make fix

# Run tests
make test

# Run linting
make lint
```

### Release Process (Viaplay Fork)
1. Update version in `troposphere/__init__.py`
2. Update `CHANGELOG.rst`
3. Test release: `make release-test`
4. Create signed tag: `git tag --sign -m "Release X.Y.Z" X.Y.Z`
5. Build: `python -m build --sdist --wheel .`
6. Upload to JFrog: `twine upload -r cloud-local dist/*`

## CloudFormation Integration

### Intrinsic Functions
```python
from troposphere import Ref, GetAtt, Join, Sub, If

# Reference another resource
Ref("MyResource")

# Get attribute
GetAtt("MyResource", "Arn")

# Join strings
Join("", ["prefix-", Ref("MyParam")])

# Substitute variables
Sub("Hello ${Name}", {"Name": Ref("NameParam")})

# Conditional
If("ConditionName", "value-if-true", "value-if-false")
```

### Template Sections
```python
t = Template()
t.set_description("My template")
t.set_version("2010-09-09")

# Parameters
t.add_parameter(Parameter("Environment", Type="String"))

# Conditions
t.add_condition("IsProd", Equals(Ref("Environment"), "prod"))

# Resources
t.add_resource(MyResource("Resource"))

# Outputs
t.add_output(Output("ResourceId", Value=Ref("Resource")))
```

## Error Handling and Debugging

### Common Issues
- **Missing required properties**: Check resource props definition
- **Type validation errors**: Ensure correct type or validator
- **Reference errors**: Use Ref() for resource references

### Debugging Generated Code
- Check CloudFormation Resource Specification
- Review patch files in `scripts/patches/`
- Validate with AWS CloudFormation

## Best Practices

1. **Use type hints**: Follow existing patterns for type safety
2. **Validate early**: Use appropriate validators for all properties
3. **Test thoroughly**: Include unit tests for custom code
4. **Follow PEP 8**: Use `make fix` to format code
5. **Document changes**: Update docstrings and examples
6. **Leverage auto-generation**: Don't fight the code generator

## Package Information

- **Published as**: `troppan` (not `troposphere`)
- **Python support**: 3.8+
- **Dependencies**: `cfn_flip >= 1.0.2`
- **Optional**: `awacs` for IAM policy generation

This fork ensures compatibility with the latest CloudFormation features while maintaining stability for Viaplay Group's infrastructure-as-code needs.
