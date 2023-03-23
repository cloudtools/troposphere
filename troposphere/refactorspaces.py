# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean


class ApiGatewayProxyInput(AWSProperty):
    """
    `ApiGatewayProxyInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-application-apigatewayproxyinput.html>`__
    """

    props: PropsDictType = {
        "EndpointType": (str, False),
        "StageName": (str, False),
    }


class Application(AWSObject):
    """
    `Application <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html>`__
    """

    resource_type = "AWS::RefactorSpaces::Application"

    props: PropsDictType = {
        "ApiGatewayProxy": (ApiGatewayProxyInput, False),
        "EnvironmentIdentifier": (str, True),
        "Name": (str, True),
        "ProxyType": (str, True),
        "Tags": (Tags, False),
        "VpcId": (str, True),
    }


class Environment(AWSObject):
    """
    `Environment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html>`__
    """

    resource_type = "AWS::RefactorSpaces::Environment"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "NetworkFabricType": (str, True),
        "Tags": (Tags, False),
    }


class DefaultRouteInput(AWSProperty):
    """
    `DefaultRouteInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-defaultrouteinput.html>`__
    """

    props: PropsDictType = {
        "ActivationState": (str, True),
    }


class UriPathRouteInput(AWSProperty):
    """
    `UriPathRouteInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html>`__
    """

    props: PropsDictType = {
        "ActivationState": (str, True),
        "IncludeChildPaths": (boolean, False),
        "Methods": ([str], False),
        "SourcePath": (str, False),
    }


class Route(AWSObject):
    """
    `Route <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html>`__
    """

    resource_type = "AWS::RefactorSpaces::Route"

    props: PropsDictType = {
        "ApplicationIdentifier": (str, True),
        "DefaultRoute": (DefaultRouteInput, False),
        "EnvironmentIdentifier": (str, True),
        "RouteType": (str, True),
        "ServiceIdentifier": (str, True),
        "Tags": (Tags, False),
        "UriPathRoute": (UriPathRouteInput, False),
    }


class LambdaEndpointInput(AWSProperty):
    """
    `LambdaEndpointInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-lambdaendpointinput.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, True),
    }


class UrlEndpointInput(AWSProperty):
    """
    `UrlEndpointInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-urlendpointinput.html>`__
    """

    props: PropsDictType = {
        "HealthUrl": (str, False),
        "Url": (str, True),
    }


class Service(AWSObject):
    """
    `Service <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html>`__
    """

    resource_type = "AWS::RefactorSpaces::Service"

    props: PropsDictType = {
        "ApplicationIdentifier": (str, True),
        "Description": (str, False),
        "EndpointType": (str, True),
        "EnvironmentIdentifier": (str, True),
        "LambdaEndpoint": (LambdaEndpointInput, False),
        "Name": (str, True),
        "Tags": (Tags, False),
        "UrlEndpoint": (UrlEndpointInput, False),
        "VpcId": (str, False),
    }
