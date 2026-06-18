# Troposphere Macro

The `Troposphere` macro adds the ability to create CloudFormation resources from troposphere stacks.

# How to install and use the Macro in your AWS account

## Deploying

1. You will need an S3 bucket to store the CloudFormation artifacts:
    * If you don't have one already, create one with `aws s3 mb s3://<bucket name>`

2. Install all python requirements

    ```shell
    pip install -r source/requirements.txt -t source
    ```

3. Package the CloudFormation template. The provided template uses [the AWS Serverless Application Model](https://aws.amazon.com/about-aws/whats-new/2016/11/introducing-the-aws-serverless-application-model/) so must be transformed before you can deploy it.

    ```shell
    aws cloudformation package \
        --template-file template.yaml \
        --s3-bucket <your bucket name here> \
        --output-template-file template.output
    ```

4. Deploy the packaged CloudFormation template to a CloudFormation stack:

    ```shell
    aws cloudformation deploy \
        --stack-name troposphere-macro \
        --template-file template.output \
        --capabilities CAPABILITY_IAM
    ```

5. To test out the macro's capabilities, try launching the provided example template:

    ```shell
    aws cloudformation deploy \
        --stack-name template-macro-example \
        --template-file example.py
    ```

## Usage
 
Just add your resources to macro_template object, the template object is created by macro itself.
You can provide your troposphere code in Troposphere tag.

```
Transform: [Troposhere]
Description: Example Macro Troposhere.

Parameters:
  InstanceName:
    Type: String
    Default: "MyInstance"
  ImageId:
    Type: String
    Default: "ami-951945d0"
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
```

