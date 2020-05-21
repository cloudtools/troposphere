BUCKET=macro-template-default-831650818513-us-east-1

macro:
	pip install -r source/requirements.txt -t source
	aws cloudformation package --template-file template.yaml --s3-bucket $(BUCKET) --output-template-file template.output
	aws cloudformation deploy --template-file template.output --stack-name TroposphereMacro --capabilities CAPABILITY_IAM
	rm -rf template.output

sample:
	aws cloudformation deploy --stack-name template-macro-example --template-file example.py --parameter-overrides InstanceName=NewName