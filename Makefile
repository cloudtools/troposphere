.PHONY: 2to3 3to2 spec test

PYDIRS=setup.py examples tests troposphere

test:
	pycodestyle ${PYDIRS}
	pyflakes ${PYDIRS}
	python setup.py test

spec:
	curl -O https://d1uauaxba7bl26.cloudfront.net/latest/CloudFormationResourceSpecification.zip
	rm -rf spec
	mkdir spec
	unzip -d spec CloudFormationResourceSpecification.zip
	rm CloudFormationResourceSpecification.zip

2to3:
	2to3 -n -w examples > 2to3-examples.patch
	2to3 -n -w troposphere > 2to3-troposphere.patch

3to2:
	git -C examples apply ../2to3-examples.patch -R
	git -C troposphere apply ../2to3-troposphere.patch -R

release-test:
	python setup.py sdist
	make release-test-27
	make release-test-37

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

p37dir=p37
release-test-37:
	@echo "Python 3.7 test"
	ver=`python -c 'import troposphere; print troposphere.__version__'` && \
	rm -rf ${p37dir} && \
	python3.7 -m venv ${p37dir} && \
	. ${p37dir}/bin/activate && \
	pip3.7 install dist/troposphere-$${ver}.tar.gz && \
	deactivate && \
	rm -rf ${p37dir}

clean:
	rm -rf ${p27dir} ${p37dir} troposphere.egg-info
