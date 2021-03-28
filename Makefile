.PHONY: spec test

PYDIRS=setup.py examples scripts tests troposphere

test:
	flake8 ${PYDIRS}
	python setup.py test
	black --check ${PYDIRS}
	isort --check ${PYDIRS}

spec:
	curl -O https://d1uauaxba7bl26.cloudfront.net/latest/CloudFormationResourceSpecification.zip
	rm -rf spec
	mkdir spec
	unzip -d spec CloudFormationResourceSpecification.zip
	rm CloudFormationResourceSpecification.zip

spec2:
	curl -O --compressed https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json
	/bin/echo -n "Downloaded version: " && jq .ResourceSpecificationVersion CloudFormationResourceSpecification.json

release-test:
	python setup.py sdist
	make release-test-39

p39dir=p39
release-test-39:
	@echo "Python 3.9 test"
	ver=`python -c 'import troposphere; print troposphere.__version__'` && \
	rm -rf ${p39dir} && \
	python3.9 -m venv ${p39dir} && \
	. ${p39dir}/bin/activate && \
	pip3.9 install dist/troposphere-$${ver}.tar.gz && \
	deactivate && \
	rm -rf ${p39dir}

clean:
	rm -rf ${p39dir} troposphere.egg-info
