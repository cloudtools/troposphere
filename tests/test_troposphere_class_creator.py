import unittest
from TroposphereClassCreator import TroposphereClassCreator


class test_troposphere_class_creator(unittest.TestCase):

    def testBadClassInstantiate(self):
        with self.assertRaises(TypeError):
            TroposphereClassCreator()

    def testGetMethod(self):
        tropo = TroposphereClassCreator('test', 'test')
        methodStr = 'sgSGAWSUTILSCI = t.add_resource(SecurityGroup('
        method = tropo.getMethod(methodStr)
        self.assertEqual(method, 't.add_resource')

    def testGetName(self):
        tropo = TroposphereClassCreator('test', 'test')
        method = tropo.getName('"topicPHPAutoscaleStartupQueueQA"')
        self.assertEqual(method, 'topicPHPAutoscaleStartupQueueQA')

    def testIsSecurityGroups(self):
        tropo = TroposphereClassCreator('test', 'test')
        testTrue = [
             'SecurityGroup',
             'SecurityGroupIngress',
             'SecurityGroupEgress'
        ]
        testFail = ['test', '', ' ', '122', 'securityGroup']
        for test in testTrue:
            self.assertTrue(tropo.isSecurityGroupType(test))
        for test in testFail:
            self.assertFalse(tropo.isSecurityGroupType(test))

if __name__ == '__main__':
    unittest.main()
