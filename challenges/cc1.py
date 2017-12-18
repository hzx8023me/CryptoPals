#!/usr/bin/env python3

"""
Convert hex to base64

The string:
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

So go ahead and make that happen.
You'll need to use this code for the rest of the exercises.

Cryptopals Rule
Always operate on raw bytes, never on encoded strings.
Only use hex and base64 for pretty-printing.
"""

import base64
import codecs
from challenges.utils import hex_string_to_binary_string
from challenges.constants import BASE64_TABLE

def hex_to_base64(hex_string):
    """
    Convert a hex String into a base64 String.

    Arguments:
        hex_string {String} -- Hex String to be converted.

    Returns:
        String -- Base64 String.
    """

    binary_string = hex_string_to_binary_string(hex_string)
    padding = 0

    while len(binary_string) % 6 != 0:
        binary_string += '00000000'
        padding += 1

    base64_string = ''
    for i in range(0, (len(binary_string)) // 6 - padding):
        base64_index = int(binary_string[6*i : 6*(i+1)], 2)
        base64_string += BASE64_TABLE[int(base64_index)]

    for i in range(0, padding):
        base64_string += '='

    return base64_string


def hex_to_base64_builtin(hex_string):
    """
    Get Base64 String from Hex String.

    Arguments:
        hex_string {String} -- Hex String to be converted.

    Returns:
        String -- Base64 String.
    """

    return base64.b64encode(codecs.decode(hex_string, 'hex')).decode()
