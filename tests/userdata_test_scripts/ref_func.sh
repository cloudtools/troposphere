/opt/aws/bin/cfn-init -v --stack "Ref('AWS::StackName')" \
  --resource LaunchConfig \
  --configsets ConfigCluster \
  --region Ref('AWS::Region')
