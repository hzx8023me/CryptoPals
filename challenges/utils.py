#!/usr/bin/env python3

"""
Utils to be used.
"""

def hex_string_to_binary_string(hex_string):
    """
    Convert a Hex String to a Binary String. Hex String can be any length.

    Arguments:
        hex_string {String} -- Hex String to be converted.
    """

    return '{0:0>{1}b}'.format(int(hex_string, 16), len(hex_string) * 4)


def binary_string_to_hex_string(bin_string):
    """
    Convert a Binary String to a Hex String.

    Arguments:
        bin_string {String} -- Binary String to be converted.
    """
    return '{0:x}'.format(int(bin_string, 2))


def xor_hex_digits(hex_digit1, hex_digit2):
    """
    [description]

    Arguments:
        hex_digit1 {String} -- Hex Digit 1 to be converted.
        hex_digit2 {String} -- Hex Digit 2 to be converted.
    """

    bin_string_for_digit1 = hex_string_to_binary_string(hex_digit1)
    bin_string_for_digit2 = hex_string_to_binary_string(hex_digit2)

    xor_bin_output = ''
    for bin1_digit, bin2_digit in zip(bin_string_for_digit1, bin_string_for_digit2):
        xor_bin_output += '0' if bin1_digit == bin2_digit else '1'

    return binary_string_to_hex_string(xor_bin_output)

def string_to_hex_string(string):
    """
    Convert a normal String to a Hex String without "0x" at the front.
    For example: "Zhexin Han" to "5a686578696e2048616e" (5a:68:65:78:69:6e:20:48:61:6e)

    Arguments:
        string {String} -- String to be converted.
    """

    return ''.join('{:2x}'.format(character) for character in string.encode())

def string_to_binary_string(string):
    """
    Convert a normal String to a Binary String without "0b" at the front.
    For example: "Z" to "01011010"

    Arguments:
        string {String} -- String to be converted.
    """

    return ''.join('{:0>8b}'.format(character) for character in string.encode())

def xor_two_characters(character1, character2):
    """
    Returns the XOR value of two characters in Hex format without "0x".

    Arguments:
        character1 {String} -- Character 1 to be XORed.
        character2 {String} -- Character 2 to be XORed.

    Returns:
        String -- The Hex String of the XOR value.
    """

    return format(ord(character1) ^ ord(character2), '02x')
