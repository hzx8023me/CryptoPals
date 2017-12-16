#!/usr/bin/env python3

"""
Test for Crypto Challenge 1
"""

import unittest
from challenges import cc1

class TestCC1(unittest.TestCase):
    """
    Test Class for CC1
    """

    def test_hex_to_base64(self):
        """
        Test for method hex_to_base64
        """
        self.assertEqual('sss', cc1.hex_to_base64('Test'))

if __name__ == '__main__':
    unittest.main()
