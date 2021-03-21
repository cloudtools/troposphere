from troposphere import Parameter, Template
import troposphere.elasticloadbalancingv2 as elb


def main():
    template = Template()

    subnetA = template.add_parameter(Parameter("subnetA", Type="String"))
    subnetB = template.add_parameter(Parameter("subnetB", Type="String"))

    alb = template.add_resource(
        elb.LoadBalancer(
            "ALB",
            Scheme="internet-facing",
            Subnets=[subnetA.ref(), subnetB.ref()],
        )
    )

    listener = template.add_resource(
        elb.Listener(
            "Listener",
            Port="80",
            Protocol="HTTP",
            LoadBalancerArn=alb.ref(),
            DefaultActions=[
                elb.Action(
                    Type="fixed-response",
                    FixedResponseConfig=elb.FixedResponseConfig(
                        StatusCode="200",
                        MessageBody=(
                            "This is a fixed response for the default "
                            "ALB action"
                        ),
                        ContentType="text/plain",
                    ),
                )
            ],
        )
    )

    template.add_resource(
        [
            elb.ListenerRule(
                "ListenerRuleApi",
                ListenerArn=listener.ref(),
                Conditions=[
                    elb.Condition(
                        Field="host-header", Values=["api.example.com"]
                    ),
                    elb.Condition(
                        Field="http-header",
                        HttpHeaderConfig=elb.HttpHeaderConfig(
                            HttpHeaderName="X-Action", Values=["Create"]
                        ),
                    ),
                    elb.Condition(
                        Field="path-pattern",
                        PathPatternConfig=elb.PathPatternConfig(
                            Values=["/api/*"]
                        ),
                    ),
                    elb.Condition(
                        Field="http-request-method",
                        HttpRequestMethodConfig=elb.HttpRequestMethodConfig(
                            Values=["POST"]
                        ),
                    ),
                ],
                Actions=[
                    elb.Action(
                        Type="fixed-response",
                        FixedResponseConfig=elb.FixedResponseConfig(
                            StatusCode="200",
                            MessageBody=(
                                "This is a fixed response for any API POST "
                                "request with header X-Action: Create"
                            ),
                            ContentType="text/plain",
                        ),
                    )
                ],
                Priority="10",
            ),
            elb.ListenerRule(
                "ListenerRuleWeb",
                ListenerArn=listener.ref(),
                Conditions=[
                    elb.Condition(
                        Field="host-header",
                        HostHeaderConfig=elb.HostHeaderConfig(
                            Values=["www.example.com"]
                        ),
                    ),
                    elb.Condition(
                        Field="path-pattern",
                        PathPatternConfig=elb.PathPatternConfig(
                            Values=["/web/*"]
                        ),
                    ),
                ],
                Actions=[
                    elb.Action(
                        Type="fixed-response",
                        FixedResponseConfig=elb.FixedResponseConfig(
                            StatusCode="200",
                            MessageBody=(
                                "This is a fixed response for any WEB "
                                "request"
                            ),
                            ContentType="text/plain",
                        ),
                    )
                ],
                Priority="20",
            ),
            elb.ListenerRule(
                "ListenerRuleMetrics",
                ListenerArn=listener.ref(),
                Conditions=[
                    elb.Condition(Field="path-pattern", Values=["/metrics/*"])
                ],
                Actions=[
                    elb.Action(
                        Type="redirect",
                        RedirectConfig=elb.RedirectConfig(
                            StatusCode="HTTP_301", Protocol="HTTPS", Port="443"
                        ),
                    )
                ],
                Priority="30",
            ),
            elb.ListenerRule(
                "ListenerRuleSourceIp",
                ListenerArn=listener.ref(),
                Conditions=[
                    elb.Condition(
                        Field="source-ip",
                        SourceIpConfig=elb.SourceIpConfig(
                            Values=["52.30.12.16/28"]
                        ),
                    )
                ],
                Actions=[
                    elb.Action(
                        Type="fixed-response",
                        FixedResponseConfig=elb.FixedResponseConfig(
                            StatusCode="200",
                            MessageBody=(
                                "The request came from IP range "
                                "52.30.12.16/28"
                            ),
                            ContentType="text/plain",
                        ),
                    )
                ],
                Priority="40",
            ),
        ]
    )

    print(template.to_json())


if __name__ == '__main__':
    main()
