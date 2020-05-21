Transform: [Troposhere]
Description: Example Macro Troposhere.

Parameters:
  InstanceName:
    Type: String
    Default: "MyInstance"
  ImageId:
    Type: String
    Default: "ami-eb0c7791"
  InstanceType:
    Type: String
    Default: "t1.micro"

Troposhere: |
  from troposphere import Ref
  import troposphere.ec2 as ec2

  instance = ec2.Instance('MyInstance')

  instance.ImageId = Ref('ImageId')
  instance.InstanceType = Ref('InstanceType')
  instance.Tags = ec2.Tags(Name = Ref('InstanceName'))

  macro_template.add_resource(instance)