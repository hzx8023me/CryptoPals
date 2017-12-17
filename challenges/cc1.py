#!/usr/bin/env python3

"""
Module to convert a hex String to a base64 String
"""

from challenges.utils import hex_string_to_binary_string
from challenges.constants import BASE64_TABLE

def hex_to_base64(hex_string):
    """
    Convert a hex String into a base64 String.

    Arguments:
        hex_string {String} -- Hex String to be converted.
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
