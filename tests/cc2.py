#!/usr/bin/env python3

"""
Test for Crypto Challenge 2
"""

import random
from unittest import TestCase
from challenges.cc2 import xor_strings_easy, xor_strings_hard

class TestCC2(TestCase):
    """
    Test Class for Crypto Challenge 2
    """

    def test_xor_strings_short(self):
        """
        Test for method xor_strings_easy and xor_strings_hard with short input
        """

        input_hex1 = '1c0111001f010100061a024b53535009181c'
        input_hex2 = '686974207468652062756c6c277320657965'
        self.assertEqual(xor_strings_hard(input_hex1, input_hex2),
                         xor_strings_easy(input_hex1, input_hex2))

    def test_xor_strings_long(self):
        """
        Test for method xor_strings_easy and xor_strings_hard with long input
        """

        input_hex1 = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        input_hex2 = '4206c696b65206120706f69736f6e6f7573206d757368726f6f6d9276d206b696c6c696e6720796f757220627261696e'
        self.assertEqual(xor_strings_hard(input_hex1, input_hex2),
                         xor_strings_easy(input_hex1, input_hex2))

    def test_xor_strings_random(self):
        """
        Test for method xor_strings_easy and xor_strings_hard with random input
        """

        for index in range(1, 1000):
            input_hex1 = ''.join(random.choices('0123456789abcdef', k=index))
            input_hex2 = ''.join(random.choices('0123456789abcdef', k=index))
            self.assertEqual(xor_strings_hard(input_hex1, input_hex2),
                             xor_strings_easy(input_hex1, input_hex2))
