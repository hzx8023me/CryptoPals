"""
Test for Crypto Challenge 1
"""
from unittest import TestCase
from challenges import cc1

class TestCC1(TestCase):
    """
    Test Class for CC1
    """

    def test_hex_to_base64(self):
        """
        Test for method hex_to_base64
        """
        input_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        output_bese64 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        self.assertEqual(output_bese64, cc1.hex_to_base64(input_hex))
