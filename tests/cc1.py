#!/usr/bin/env python3

"""
Test for Crypto Challenge 1
"""

import base64
import codecs
import random
from unittest import TestCase
from challenges.cc1 import hex_to_base64

class TestCC1(TestCase):
    """
    Test Class for CC1
    """

    def _get_base64(self, hex_string):
        return base64.b64encode(codecs.decode(hex_string, 'hex')).decode()

    def test_hex_to_base64_short(self):
        """
        Test for method hex_to_base64 with short input
        """

        input_hex = '44616e676572207a6f6e6521'
        self.assertEqual(self._get_base64(input_hex), hex_to_base64(input_hex))

    def test_hex_to_base64_long(self):
        """
        Test for method hex_to_base64
        """

        input_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        self.assertEqual(self._get_base64(input_hex), hex_to_base64(input_hex))

    def test_hex_to_base64_random(self):
        """
        Test for method hex_to_base64 with random input
        """

        for i in range(0, 1000, 2):
            input_hex = ''.join(random.choices('0123456789ABCDEF', k=i))
            output_bese64 = self._get_base64(input_hex)

        self.assertEqual(output_bese64, hex_to_base64(input_hex))
