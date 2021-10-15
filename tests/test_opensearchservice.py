import unittest

import troposphere.opensearchservice as opensearchservice


class TestOpenSearchServiceValidators(unittest.TestCase):
    def test_validate_search_service_engine_version(self):
        valid_values = [
            "OpenSearch_1.1",
            "OpenSearch_10.123",
            "Elasticsearch_7.10",
            "Elasticsearch_6.5",
        ]
        for x in valid_values:
            opensearchservice.validate_search_service_engine_version(x)

        invalid_values = [
            "openSearch_1.1",
            "apenSearch_10.123",
            "elasticsearch_7.10",
            "Elasticsearch_x.x",
            "latest",
        ]
        for x in invalid_values:
            with self.assertRaises(ValueError):
                opensearchservice.validate_search_service_engine_version(x)
