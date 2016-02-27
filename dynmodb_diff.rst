.. code-block:: diff
  # diff examples/DynamoDB_Table.py examples/DynamoDB2_Table.py
  5,7c5,7
  < from troposphere.dynamodb import (Key, AttributeDefinition,
  <                                   ProvisionedThroughput)
  < from troposphere.dynamodb import Table
  ---
  > from troposphere.dynamodb2 import (KeySchema, AttributeDefinition,
  >                                    ProvisionedThroughput)
  > from troposphere.dynamodb2 import Table
  58c58,61
  <         AttributeDefinition(Ref(hashkeyname), Ref(hashkeytype)),
  ---
  >         AttributeDefinition(
  >             AttributeName=Ref(hashkeyname),
  >             AttributeType=Ref(hashkeytype)
  >         ),
  61c64,67
  <         Key(Ref(hashkeyname), "HASH")
  ---
  >         KeySchema(
  >             AttributeName=Ref(hashkeyname),
  >             KeyType="HASH"
  >         )
  64,65c70,71
  <         Ref(readunits),
  <         Ref(writeunits)
  ---
  >         ReadCapacityUnits=Ref(readunits),
  >         WriteCapacityUnits=Ref(writeunits)
