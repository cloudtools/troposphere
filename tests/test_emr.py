import unittest
from troposphere import Ref
import troposphere.emr as emr

class TestEMRApplication(unittest.TestCase):

    def test_allow_additional_info_dict(self):
        emr_application = emr.Application(
            AdditionalInfo={
                'Foo' : 'Bar'
            }
        )

        emr_application.JSONrepr()

    def test_allow_args_as_list(self):
        emr_application = emr.Application(
            Args=['--foo', '--bar']
        )

        emr_application.JSONrepr()

if __name__ == '__main__':
    unittest.main()
