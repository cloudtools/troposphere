import unittest

from troposphere.elasticloadbalancingv2 import Action, RedirectActionConfig


class TestListenerActions(unittest.TestCase):
    def test_redirect_action(self):
        Action(
            Type='redirect',
            RedirectConfig=RedirectActionConfig(
                StatusCode='HTTP_301',
                Protocol='HTTPS',
                Host='api.troposphere.org',
                Path='redirect/#{path}'
            )
        ).to_dict()

    def test_forward_action(self):
        Action(
            Type='forward',
            TargetGroupArn=''
        ).to_dict()

    def test_redirect_action_config_one_of(self):
        with self.assertRaises(ValueError):
            RedirectActionConfig(
                StatusCode='HTTP_200'
            ).to_dict()

    def test_forward_action_requires_target_arn(self):
        with self.assertRaises(ValueError):
            Action(
                Type='forward'
            ).to_dict()

    def test_redirect_action_requires_redirect_config(self):
        with self.assertRaises(ValueError):
            Action(
                Type='redirect'
            ).to_dict()

    def test_target_arn_only_forward(self):
        with self.assertRaises(ValueError):
            Action(
                Type='redirect',
                TargetGroupArn=''
            ).to_dict()

    def test_redirect_config_only_with_redirect(self):
        with self.assertRaises(ValueError):
            Action(
                Type='forward',
                RedirectConfig=RedirectActionConfig(
                    StatusCode='HTTP_301',
                )
            ).to_dict()


if __name__ == '__main__':
    unittest.main()
