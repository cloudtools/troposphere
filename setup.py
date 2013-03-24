from setuptools import setup

setup(
    name='troposphere',
    version='0.2.1',
    description="AWS CloudFormation creation library",
    author="Mark Peek",
    author_email="mark@peek.org",
    url="https://github.com/cloudtools/troposphere",
    license="New BSD license",
    packages=['troposphere'],
    test_suite="tests",
    use_2to3=True,
)
