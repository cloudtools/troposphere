.PHONY: 2to3 3to2 spec test

PYDIRS=setup.py examples scripts tests troposphere

test:
	flake8 ${PYDIRS}
	TROPO_REAL_BOOL=true python setup.py test

spec:
	curl -O https://d1uauaxba7bl26.cloudfront.net/latest/CloudFormationResourceSpecification.zip
	rm -rf spec
	mkdir spec
	unzip -d spec CloudFormationResourceSpecification.zip
	rm CloudFormationResourceSpecification.zip

spec2:
	curl -O --compress https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json
	/bin/echo -n "Downloaded version: " && jq .ResourceSpecificationVersion CloudFormationResourceSpecification.json

2to3:
	2to3 -n -w examples > 2to3-examples.patch
	2to3 -n -w troposphere > 2to3-troposphere.patch

3to2:
	git -C examples apply ../2to3-examples.patch -R
	git -C troposphere apply ../2to3-troposphere.patch -R

release-test:
	python setup.py sdist
	make release-test-27
	make release-test-38

p27dir=p27
release-test-27:
	@echo "Python 2.7 test"
	ver=`python -c 'import troposphere; print troposphere.__version__'` && \
	rm -rf ${p27dir} && \
	virtualenv ${p27dir} && \
	. ${p27dir}/bin/activate && \
	pip install dist/troposphere-$${ver}.tar.gz && \
	deactivate && \
	rm -rf ${p27dir}

p38dir=p38
release-test-38:
	@echo "Python 3.8 test"
	ver=`python -c 'import troposphere; print troposphere.__version__'` && \
	rm -rf ${p38dir} && \
	python3.8 -m venv ${p38dir} && \
	. ${p38dir}/bin/activate && \
	pip3.8 install dist/troposphere-$${ver}.tar.gz && \
	deactivate && \
	rm -rf ${p38dir}

clean:
	rm -rf ${p27dir} ${p38dir} troposphere.egg-info
