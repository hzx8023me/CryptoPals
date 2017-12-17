#!/usr/bin/env python3

"""
Utils to be used.
"""

def hex_string_to_binary_string(hex_string):
    """
    Convert a Hex String to a Binary String.

    Arguments:
        hex_string {String} -- Hex String to be converted.
    """

    return '{0:0>{1}b}'.format(int(hex_string, 16), len(hex_string) * 4)
