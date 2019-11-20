import unittest
from troposphere import Tags
import troposphere.ecr as ecr


class TestECS(unittest.TestCase):

    def test_ecr_with_tags(self):
        repo = ecr.Repository(
            "ECRRepo",
            RepositoryName="myrepo",
            Tags=Tags(Name='myrepo'),
        )
        repo.to_dict()
