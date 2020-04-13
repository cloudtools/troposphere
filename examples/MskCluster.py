from troposphere import Template
import troposphere.msk as msk


t = Template()

t.add_resource(
    msk.Cluster(
        "TestCluster",
        ClusterName="MyMskCluster",
        KafkaVersion="2.1.0",
        NumberOfBrokerNodes=3,
        EnhancedMonitoring="PER_BROKER",
        BrokerNodeGroupInfo=msk.BrokerNodeGroupInfo(
            BrokerAZDistribution="DEFAULT",
            InstanceType="kafka.m5.large",
            SecurityGroups=[
                "sg-c73ebda3"
            ],
            StorageInfo=msk.StorageInfo(
                EBSStorageInfo=msk.EBSStorageInfo(
                    VolumeSize=100
                )
            ),
            ClientSubnets=[
                "subnet-ce49ff7bcd",
                "subnet-2541a68474",
                "subnet-1d6b6f39da",
            ]
        ),
        EncryptionInfo=msk.EncryptionInfo(
            EncryptionAtRest=msk.EncryptionAtRest(
                DataVolumeKMSKeyId="ReplaceWithKmsKeyArn"
            ),
            EncryptionInTransit=msk.EncryptionInTransit(
                ClientBroker="TLS",
                InCluster=True,
            ),
        ),
        ClientAuthentication=msk.ClientAuthentication(
            Tls=msk.Tls(
                CertificateAuthorityArnList=[
                    "ReplaceWithCAArn"
                ]
            )
        ),
        ConfigurationInfo=msk.ConfigurationInfo(
            Arn=(
                "arn:aws:kafka:us-east-1:123456789012:configuration/"
                "example-configuration-name/"
                "abcdabcd-1234-abcd-1234-abcd123e8e8e-1"
            ),
            Revision=1,
        ),
        Tags=dict(
            MyTagName="MyTagValue"
        )
    )
)

print(t.to_json())
