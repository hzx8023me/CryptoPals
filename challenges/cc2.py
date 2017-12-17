#!/usr/bin/env python3

"""
Module to XOR two Hex Strings with the same length.
"""

from challenges.utils import xor_hex_digits

def xor_strings_easy(hex_string1, hex_string2):
    """
    XOR two Hex Strings with the same length.

    Arguments:
        hex_string1 {String} -- Hex String 1 to be XORed.
        hex_string2 {String} -- Hex String 2 to be XORed.
    """

    result = ''
    for hex1, hex2 in zip(hex_string1, hex_string2):
        result += format(int(hex1, 16) ^ int(hex2, 16), 'x')

    return result


def xor_strings_hard(hex_string1, hex_string2):
    """
    XOR two Hex Strings with the same length. Using self-implemented XOR instead of ^.

    Arguments:
        hex_string1 {String} -- Hex String 1 to be XORed.
        hex_string2 {String} -- Hex String 2 to be XORed.
    """

    result = ''
    for hex_digit1, hex_digit2 in zip(hex_string1, hex_string2):
        result += xor_hex_digits(hex_digit1, hex_digit2)

    return result
