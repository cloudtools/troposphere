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

  list_instances = ["One", "Two", "Three", "Four"]

  instance_name = macro_parameters["InstanceName"]

  for el in list_instances:
    instance = ec2.Instance('MyInstance{}'.format(el))

    instance.ImageId = Ref('ImageId')
    instance.InstanceType = Ref('InstanceType')
    instance.Tags = ec2.Tags(Name = instance_name + el)

    macro_template.add_resource(instance)