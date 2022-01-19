import unittest

from troposphere.route53 import AliasTarget


class TestAliasTarget(unittest.TestCase):
    def test_bucket_template(self):
        AliasTarget("zone", "dnsname", True)
        AliasTarget(hostedzoneid="zone", dnsname="dnsname", evaluatetargethealth=True)
        AliasTarget(HostedZoneId="zone", DNSName="dnsname", EvaluateTargetHealth=True)


if __name__ == "__main__":
    unittest.main()
