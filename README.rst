===========
troposphere
===========

This repo includes new functionality for AWS::EC2::NatGateway resource which,
as of 29 Feb 2016, has not been merged into master. This repo is temporary.

About
=====

troposphere - library to create `AWS CloudFormation`_ descriptions

The troposphere library allows for easier creation of the AWS CloudFormation
JSON by writing Python code to describe the AWS resources. Troposphere also
includes some basic support for `OpenStack resources`_ via heat.

To facilitate catching CloudFormation or JSON errors early the library has
property and type checking built into the classes.
