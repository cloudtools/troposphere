Quick Start
===========

Troposphere closely follows CloudFormation, so there isn't much documentation
specific to Troposphere.  In this documentation there are various examples but
for the most part the CloudFormation docs should be used.

CloudFormation Basics
---------------------

* `Template Anatomy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`_
  - structure of a CloudFormation template.
* `Resources  <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`_
  are the basic blocks and required in any template.
* `Outputs <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html>`_
  are optional but can be used to create cross-stack references. Having everything
  in one stack will make it very hard to manage the infrastructure.  Instead,
  values from one stack (for example, network setup) can be exported in this
  section and `imported <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html>`_
  by another stack (for example, EC2 setup). This way a stack used to set up a
  certain application can be managed or deleted without affecting other
  applications that might be present on the same network.
* `Intrinsic Functions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html>`_
  should be used to manipulate values that are only available at runtime. For
  example, assume a template that creates a subnet and attaches a routing table
  and network ACL to that subnet. The subnet doesn't exist when the template is
  created, so it's ID can't be known. Instead, the route and network ACL resources
  are going to get the ID at runtime, by using the
  `Ref <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html>`_
  function against the subnet.

Basic Usage
-----------

The following two pieces of code are intended to demonstrate basic usage of
Troposphere and CloudFormation templates. First template will create two subnets
and export their IDs. The second one will create an EC2 instance in one of the
subnets. The comments explain how it works and where to find documentation
regarding the use of CloudFormation and Troposphere.

.. code:: python

    #!/usr/bin/env python3
    #
    # learncf_subnet.py
    #
    # Generate a CloudFormation template that will create two subnets. This
    # template exports the subnet IDs to be used by a second template which
    # will create an EC2 instance in one of those subnets.
    #
    from troposphere import ec2
    from troposphere import Tags, GetAtt, Ref, Sub, Export
    from troposphere import Template, Output

    # Create the object that will generate our template
    t = Template()

    # Define resources that CloudFormation will generate for us
    # https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html

    # Define the first subnet. We know that 'Subnet()' is in the ec2 module
    # because in CloudFormation the Subnet resource is defined under EC2:
    # https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html
    net_learncf_1a = ec2.Subnet("netLearnCf1a")

    # Information about the possible properties of Subnet() can be found
    # in CloudFormation docs:
    # https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#aws-resource-ec2-subnet-properties
    net_learncf_1a.AvailabilityZone = "eu-west-1a"
    net_learncf_1a.CidrBlock = "172.30.126.80/28"            # ADJUST THIS VALUE
    net_learncf_1a.VpcId = "vpc-abcdefgh"                    # ADJUST THIS VALUE
    # Tags can be declared in two ways. One way is
    # (1) in AWS/boto format, as a list of dictionaries where each item in the
    # list has (at least) two elements. The "Key" key will be the tag key and
    # the "Value" key will be the tag's Value. Confusing, but it allows for
    # additional settings to be specified for each tag. For example, if a tag
    # attached to an autoscaling group should be inherited by the EC2 instances
    # the group launches or not.
    net_learncf_1a.Tags = [
            {"Key": "Name", "Value": "learncf-1a"},
            {"Key": "Comment", "Value": "CloudFormation+Troposphere test"}]

    # The subnet resource defined above must be added to the template
    t.add_resource(net_learncf_1a)

    # The same thing can be achieved by setting parameters to Subnet() function
    # instead of properties of the object created by Subnet(). Shown below.
    #
    # For the second subnet we use the other method of defining tags,
    # (2) by using the Tags helper function, which is defined in Troposphere
    # and doesn't have an equivalent in CloudFormation.
    #
    # Also, we use GetAtt to read the value of an attribute from a previously
    # created resource, i.e. VPC ID from the first subnet. For demo purposes.
    #
    # The attributes returned by each resource can be found in the CloudFormation
    # documentation, in the Returns section for that resource:
    # https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#aws-resource-ec2-subnet-getatt
    #
    # GetAtt documentation:
    # https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html
    net_learncf_1b = ec2.Subnet(
            "netLearnCf1b",
            AvailabilityZone="eu-west-1b",
            CidrBlock="172.30.126.96/28",                   # ADJUST THIS VALUE
            VpcId=GetAtt(net_learncf_1a, "VpcId"),
            Tags=Tags(
                Name="learncf-1b",
                Comment="CloudFormation+Troposphere test"))

    t.add_resource(net_learncf_1b)

    # Outputs section will export the subnet IDs to be used by other stacks
    # https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html
    out_net_learncf_1a = Output("outNetLearnCf1a")

    # Ref is another CloudFormation intrinsic function:
    # https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html
    # If pointed to a subnet, Ref will return the subnet ID:
    # https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#aws-resource-ec2-subnet-ref
    out_net_learncf_1a.Value = Ref(net_learncf_1a)
    # Append the subnet title (Logical ID) to the stack name and set that as the
    # exported property. Importing it in another stack will return the Value
    # we set above to that stack.
    #
    # Sub stands for 'substitute', another CloudFormation intrinsic function.
    out_net_learncf_1a.Export = Export(Sub(
        "${AWS::StackName}-" + net_learncf_1a.title))

    # Similar output for the second subnet
    out_net_learncf_1b = Output("outNetLearnCf1b")
    out_net_learncf_1b.Value = Ref(net_learncf_1b)
    out_net_learncf_1b.Export = Export(Sub(
        "${AWS::StackName}-" + net_learncf_1b.title))

    # Add outputs to template
    t.add_output(out_net_learncf_1a)
    t.add_output(out_net_learncf_1b)

    # Finally, write the template to a file
    with open('learncf-subnet.yaml', 'w') as f:
        f.write(t.to_yaml())


And the EC2 instance template:

.. code:: python

    #!/usr/bin/env python3
    #
    # learncf_ec2.py
    #
    # Generate a CloudFormation template that creates an EC2 instance in a
    # subnet which was created previously by another template (learncf-subnet)
    #
    from troposphere import ec2
    from troposphere import Tags, ImportValue
    from troposphere import Template

    # create the object that will generate our template
    t = Template()

    ec2_learncf_1a = ec2.Instance("ec2LearnCf1a")
    ec2_learncf_1a.ImageId = "ami-e487179d"                 # ADJUST IF NEEDED
    ec2_learncf_1a.InstanceType = "t2.micro"
    # We set the subnet to start this instance in by importing the subnet ID
    # from the other CloudFormation stack, which previously created it.
    # An example of cross-stack reference used to split stacks into
    # manageable pieces. Each export must have a unique name in its account
    # and region, so the template name was prepended to the resource name.
    ec2_learncf_1a.SubnetId = ImportValue("learncf-subnet-netLearnCf1a")
    ec2_learncf_1a.Tags = Tags(
            Name="learncf",
            Comment="Learning CloudFormation and Troposphere")

    t.add_resource(ec2_learncf_1a)

    # Finally, write the template to a file
    with open('learncf-ec2.yaml', 'w') as f:
        f.write(t.to_yaml())


After the .yaml files are generated using the code above stacks can be created
from the command line like this:

.. code:: sh

    aws cloudformation create-stack --stack-name learncf-subnet --template-body file://learncf-subnet.yaml
    aws cloudformation create-stack --stack-name learncf-ec2    --template-body file://learncf-ec2.yaml
