import unittest

import troposphere.guardduty as guardduty


class TestGuardDuty(unittest.TestCase):
    def test_guardduty_detector(self):
        detector = guardduty.Detector("detector")

        with self.assertRaises(ValueError):
            detector.to_dict()

        detector = guardduty.Detector("detector", Enable=True)

        result = detector.to_dict()
        self.assertEqual(result["Type"], "AWS::GuardDuty::Detector")

    def test_guardduty_ipset(self):
        ipset = guardduty.IPSet("ipset")

        with self.assertRaises(ValueError):
            ipset.to_dict()

        ipset = guardduty.IPSet(
            "ipset",
            Activate=True,
            DetectorId="aaaabbbbccccddddeeeeffff11112222",
            Format="TXT",
            Location="http://example.com/ipset.txt",
            Name="guardduty-name",
        )

        result = ipset.to_dict()

        self.assertEqual(result["Type"], "AWS::GuardDuty::IPSet")

    def test_guardduty_threatintelset(self):
        threat_intel_set = guardduty.ThreatIntelSet("threatintelset")

        with self.assertRaises(ValueError):
            threat_intel_set.to_dict()

        threat_intel_set = guardduty.ThreatIntelSet(
            "threatintelset",
            Activate=True,
            DetectorId="aaaabbbbccccddddeeeeffff11112222",
            Format="TXT",
            Location="http://example.com/threatintelset.txt",
            Name="guardduty-name",
        )

        result = threat_intel_set.to_dict()
        self.assertEqual(result["Type"], "AWS::GuardDuty::ThreatIntelSet")
