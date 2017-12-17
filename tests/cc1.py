#!/usr/bin/env python3

"""
Test for Crypto Challenge 1
"""

import random
from unittest import TestCase
from challenges.cc1 import hex_to_base64
from challenges.utils import get_base64

class TestCC1(TestCase):
    """
    Test Class for CC1
    """

    def test_hex_to_base64_short(self):
        """
        Test for method hex_to_base64 with short input
        """

        input_hex = '44616e676572207a6f6e6521'
        self.assertEqual(get_base64(input_hex), hex_to_base64(input_hex))

    def test_hex_to_base64_long(self):
        """
        Test for method hex_to_base64
        """

        input_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        self.assertEqual(get_base64(input_hex), hex_to_base64(input_hex))

    def test_hex_to_base64_random(self):
        """
        Test for method hex_to_base64 with random input
        """

        for i in range(2, 1000, 2):
            input_hex = ''.join(random.choices('0123456789ABCDEF', k=i))
            output_bese64 = get_base64(input_hex)
            self.assertEqual(output_bese64, hex_to_base64(input_hex))
