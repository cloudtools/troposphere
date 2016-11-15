from .dynamodb import (
    AttributeDefinition,
    KeySchema,
    Key,
    ProvisionedThroughput,
    Projection,
    GlobalSecondaryIndex,
    LocalSecondaryIndex,
    StreamSpecification,
    Table,
    attribute_type_validator,
    key_type_validator,
    projection_type_validator,
)

import warnings

# Only way to make pyflakes shut up about unused imports
assert AttributeDefinition
assert KeySchema
assert Key
assert ProvisionedThroughput
assert Projection
assert GlobalSecondaryIndex
assert LocalSecondaryIndex
assert StreamSpecification
assert Table
assert attribute_type_validator
assert key_type_validator
assert projection_type_validator


warnings.warn("This module has replaced by troposphere.dynamodb. Please "
              "import that module instead, as troposphere.dynamodb2 will be "
              "removed soon.")
