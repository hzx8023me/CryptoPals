#!/usr/bin/env python3

"""
Test for Crypto Challenge 3
"""

from unittest import TestCase
from challenges.cc3 import single_byte_xor_cipher


class TestCC3(TestCase):
    """
    Test Class for CC3
    """

    def test_single_byte_xor_cipher_short_input(self):
        """
        Test for method single_byte_xor_cipher with short input
        """

        input_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        expected_string = "Cooking MC's like a pound of bacon"
        expected_key = 'X'
        self.assertEqual(expected_string, single_byte_xor_cipher(input_hex)[0])
        self.assertEqual(expected_key, single_byte_xor_cipher(input_hex)[1])
