import os
from setuptools import setup


def version():
    with open(os.path.join('version.txt')) as version_file:
        return version_file.read().strip()


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='ionosphere',
    version=version(),
    description="Azure Resource Manager Template creation library",
    long_description=readme(),
    author="Mark Peek",
    author_email="mark@peek.org",
    url="https://github.com/qualinext/ionosphere",
    license="New BSD license",
    packages=['ionosphere', 'ionosphere.helpers'],
    scripts=['scripts/cfn', 'scripts/cfn2py'],
    install_requires=["cfn_flip>=0.2.5"],
    test_suite="tests",
    tests_require=["awacs"],
    extras_require={'policy': ['awacs']},
    use_2to3=True,
)
