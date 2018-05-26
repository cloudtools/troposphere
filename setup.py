from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='troposphere',
    version='2.2.2',
    description="AWS CloudFormation creation library",
    long_description=readme(),
    author="Mark Peek",
    author_email="mark@peek.org",
    url="https://github.com/cloudtools/troposphere",
    license="New BSD license",
    packages=['troposphere', 'troposphere.openstack', 'troposphere.helpers'],
    scripts=['scripts/cfn', 'scripts/cfn2py'],
    install_requires=["cfn_flip>=1.0.2"],
    test_suite="tests",
    tests_require=["awacs"],
    extras_require={'policy': ['awacs']},
    use_2to3=True,
)
