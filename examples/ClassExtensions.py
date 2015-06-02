import troposphere
import troposphere.ec2

template = troposphere.Template()


class TrustyInstance(troposphere.ec2.Instance):
    ImageId = "ami-xxxx"
    Monitoring = True


class FrontendInstance(TrustyInstance):
    SecurityGroups = ["frontend"]
    InstanceType = "t1.micro"


class ProcessingInstance(TrustyInstance):
    SecurityGroups = ["processing"]
    InstanceType = "m3.large"


template.add_resource(FrontendInstance('jones1'))
template.add_resource(ProcessingInstance('williams1', InstanceType="m2.large"))

print(template.to_json())
