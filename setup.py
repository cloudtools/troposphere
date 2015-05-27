from setuptools import setup

setup(
    name='troposphere',
    version='1.0.0',
    description="AWS CloudFormation creation library",
    author="Mark Peek",
    author_email="mark@peek.org",
    url="https://github.com/cloudtools/troposphere",
    license="New BSD license",
    packages=['troposphere', 'troposphere.openstack'],
    scripts=[
        'scripts/cfn',
        'scripts/cfn2py',
        'scripts/cfn2pyclass',
        'TroposphereClassCreator.py'
    ],
    test_suite="tests",
    tests_require=["awacs"],
    use_2to3=True,
)
