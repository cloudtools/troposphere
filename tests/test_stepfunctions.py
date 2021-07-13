import unittest

from troposphere.stepfunctions import Activity, StateMachine


class TestStepFunctions(unittest.TestCase):
    def test_activity(self):
        activity = Activity(
            "myactivity",
            Name="testactivity",
        )
        self.assertEqual(activity.Name, "testactivity")

    def test_statemachine(self):
        statemachine = StateMachine(
            "mystatemachine",
            DefinitionString="testdefinitionstring",
            RoleArn="testinrolearn",
        )
        self.assertEqual(statemachine.RoleArn, "testinrolearn")

    def test_statemachine_missing_parameter(self):
        StateMachine(
            "mystatemachine",
            DefinitionString="testdefinitionstring",
        )
        self.assertTrue(AttributeError)


if __name__ == "__main__":
    unittest.main()
