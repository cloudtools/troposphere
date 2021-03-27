#!/usr/bin/python

import os
import unittest

import troposphere.ec2 as ec2
from troposphere import Base64, Join
from troposphere.helpers import userdata


class TestUserdata(unittest.TestCase):
    def setUp(self):
        self.instance = ec2.Instance("Instance", UserData="")
        dir = os.path.dirname(__file__)
        self.filepath = os.path.join(dir, "userdata_test_scripts/")

    def create_result(self, file, delimiter=""):
        file = os.path.join(self.filepath, file)
        self.instance.UserData = userdata.from_file(file, delimiter)
        return self.instance.UserData.to_dict()

    def create_answer(self, command_list, delimiter=""):
        return Base64(Join(delimiter, command_list)).to_dict()

    def test_simple(self):
        result = self.create_result("simple.sh")
        answer = self.create_answer(["#!/bin/bash\n", 'echo "Hello world"'])
        self.assertEqual(result, answer)

    def test_empty_file(self):
        result = self.create_result("empty.sh")
        answer = self.create_answer([])
        self.assertEqual(result, answer)

    def test_one_line_file(self):
        result = self.create_result("one_line.sh")
        answer = self.create_answer(["#!/bin/bash"])
        self.assertEqual(result, answer)

    def test_char_escaping(self):
        result = self.create_result("char_escaping.sh")
        answer = self.create_answer(
            [
                "\\n\n",
                "\\\n",
                "    \n",
                "?\n",
                '""\n',
                "\n",
                "<>\n",
            ]
        )

        self.assertEqual(result, answer)

    def test_nonexistant_file(self):
        self.assertRaises(IOError, self.create_result, "nonexistant.sh")


if __name__ == "__main__":
    unittest.main()
