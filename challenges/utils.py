#!/usr/bin/env python3

"""
Utils to be used.
"""

import base64
import codecs

def hex_string_to_binary_string(hex_string):
    """
    Convert a Hex String to a Binary String.

    Arguments:
        hex_string {String} -- Hex String to be converted.
    """

    return '{0:0>{1}b}'.format(int(hex_string, 16), len(hex_string) * 4)

def get_base64(hex_string):
    """
    Get Base64 String from Hex String.

    Arguments:
        hex_string {String} -- Hex String to be converted.

    Returns:
        String -- Base64 String.
    """

    return base64.b64encode(codecs.decode(hex_string, 'hex')).decode()
