#!/usr/bin/env python3

"""
Test for Crypto Challenge 4.
"""

import os
from unittest import TestCase
from challenges.cc4 import detect_single_byte_xor

class TestCC4(TestCase):
    """
    Test Class for CC4.
    """

    def test_detect_single_byte_xor(self):
        """
        Test for method detect_single_byte_xor.
        """

        tests_suite_path = os.path.dirname(__file__)
        package_path = os.path.dirname(tests_suite_path)
        data_file_path = os.path.join(package_path, 'data', 'cc4.txt')

        expected_string = "Now that the party is jumping"
        self.assertEqual(expected_string, detect_single_byte_xor(data_file_path))
