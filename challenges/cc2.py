#!/usr/bin/env python3

"""
Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c

after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965

should produce:
746865206b696420646f6e277420706c6179
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
    for hex_digit1, hex_digit2 in zip(hex_string1, hex_string2):
        result += format(int(hex_digit1, 16) ^ int(hex_digit2, 16), 'x')

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
