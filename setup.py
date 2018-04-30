from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='ionosphere',
    version='1.0.0',
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
