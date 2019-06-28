import unittest
import troposphere.ecr as ecr


class TestECS(unittest.TestCase):

    def test_ecr_with_tags(self):
        repo = ecr.Repository(
            "ECRRepo",
            RepositoryName="myrepo",
            Tags=[
                {
                    'Key': 'Name',
                    'Value': 'myrepo',
                },
            ]
        )
        repo.to_dict()
