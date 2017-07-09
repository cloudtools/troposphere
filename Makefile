.PHONY: 2to3 3to2 test

PYDIRS=setup.py examples tests troposphere

test:
	pycodestyle ${PYDIRS}
	pyflakes ${PYDIRS}
	python setup.py test

2to3:
	2to3 -n -w examples > 2to3-examples.patch
	2to3 -n -w troposphere > 2to3-troposphere.patch

3to2:
	git -C examples apply ../2to3-examples.patch -R
	git -C troposphere apply ../2to3-troposphere.patch -R
