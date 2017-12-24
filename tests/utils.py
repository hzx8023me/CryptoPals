#!/usr/bin/env python3

"""
Test for utils.
"""

from unittest import TestCase
from challenges.utils import calculate_hamming_distance

class TestUtils(TestCase):
    """
    Test Class for Utils.
    """

    def test_hamming_distance(self):
        """
        Test for method hamming_distance.
        """

        string1 = 'this is a test'
        string2 = 'wokka wokka!!!'
        expected_hamming_distance = 37

        self.assertEqual(expected_hamming_distance,
                         calculate_hamming_distance(string1, string2))
