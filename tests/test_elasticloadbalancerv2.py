import unittest

from troposphere.elasticloadbalancingv2 import (
    Action,
    FixedResponseConfig,
    RedirectConfig,
    TargetGroup,
)


class TestListenerActions(unittest.TestCase):
    def test_redirect_action(self):
        Action(
            Type="redirect",
            RedirectConfig=RedirectConfig(
                StatusCode="HTTP_301",
                Protocol="HTTPS",
                Host="api.troposphere.org",
                Path="redirect/#{path}",
            ),
        ).to_dict()

    def test_fixed_response_action(self):
        Action(
            Type="fixed-response",
            FixedResponseConfig=FixedResponseConfig(
                ContentType="text/plain",
                MessageBody="I am a fixed response",
                StatusCode="200",
            ),
        ).to_dict()

    def test_forward_action(self):
        Action(Type="forward", TargetGroupArn="").to_dict()

    def test_redirect_action_config_one_of(self):
        with self.assertRaises(ValueError):
            RedirectConfig(StatusCode="HTTP_200").to_dict()

    def test_fixed_response_config_one_of(self):
        with self.assertRaises(ValueError):
            FixedResponseConfig(
                ContentType="application/octet-stream",
            ).to_dict()

    def test_forward_action_requires_target_arn(self):
        with self.assertRaises(ValueError):
            Action(Type="forward").to_dict()

    def test_fixed_response_requires_fixed_response_config(self):
        with self.assertRaises(ValueError):
            Action(Type="fixed-response").to_dict()

    def test_redirect_action_requires_redirect_config(self):
        with self.assertRaises(ValueError):
            Action(Type="redirect").to_dict()

    def test_target_arn_only_forward(self):
        with self.assertRaises(ValueError):
            Action(Type="redirect", TargetGroupArn="").to_dict()

    def test_redirect_config_only_with_redirect(self):
        with self.assertRaises(ValueError):
            Action(
                Type="forward",
                RedirectConfig=RedirectConfig(
                    StatusCode="HTTP_301",
                ),
            ).to_dict()

    def test_fixed_response_config_only_with_fixed_response(self):
        with self.assertRaises(ValueError):
            Action(
                Type="forward",
                FixedResponseConfig=FixedResponseConfig(
                    ContentType="text/plain",
                ),
            ).to_dict()


class TestTargetGroup(unittest.TestCase):
    def test_lambda_targettype_rejects_properties(self):
        with self.assertRaises(ValueError) as valueError:
            TargetGroup(
                "targetGroup",
                TargetType="lambda",
                Port=433,
                Protocol="HTTPS",
                VpcId="unknown",
            ).to_dict()
        self.assertEqual(
            'TargetType of "lambda" in "TargetGroup" must not contain '
            + "definitions of 'Port', 'Protocol', 'VpcId'",
            str(valueError.exception),
        )

    def test_instance_targettype_requires_properties(self):
        with self.assertRaises(ValueError) as valueError:
            TargetGroup("targetGroup", TargetType="instance").to_dict()
        self.assertEqual(
            'TargetType of "instance" in "TargetGroup" requires '
            + "definitions of 'Port', 'Protocol', 'VpcId'",
            str(valueError.exception),
        )

    def test_ip_targettype_requires_properties(self):
        with self.assertRaises(ValueError) as valueError:
            TargetGroup("targetGroup", TargetType="ip").to_dict()
        self.assertEqual(
            'TargetType of "ip" in "TargetGroup" '
            + "requires definitions of 'Port', 'Protocol', 'VpcId'",
            str(valueError.exception),
        )

    def test_no_targettype_requires_properties(self):
        with self.assertRaises(ValueError) as valueError:
            TargetGroup("targetGroup").to_dict()
        self.assertEqual(
            'Omitting TargetType in "TargetGroup" '
            + "requires definitions of 'Port', 'Protocol', 'VpcId'",
            str(valueError.exception),
        )

    def test_invalid_targettype_is_rejected(self):
        with self.assertRaises(ValueError) as valueError:
            TargetGroup(
                "targetGroup",
                TargetType="invalid",
                Port=433,
                Protocol="HTTPS",
                VpcId="unknown",
            ).to_dict()
        self.assertEqual(
            'TargetGroup.TargetType must be one of: "alb, instance, ip, lambda"',
            str(valueError.exception),
        )


if __name__ == "__main__":
    unittest.main()
