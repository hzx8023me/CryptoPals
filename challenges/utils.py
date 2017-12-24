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


def string_to_hex_string(string):
    """
    Convert a normal String to a Hex String without "0x" at the front.
    For example: "Zhexin Han" to "5a686578696e2048616e" (5a:68:65:78:69:6e:20:48:61:6e)

    Arguments:
        string {String} -- String to be converted.
    """

    return ''.join('{:2x}'.format(character) for character in string.encode())


def hex_string_to_string(hex_string):
    """
    [description]

    Arguments:
        hex_string {String} -- Hex String to be converted.
    """
    return bytearray.fromhex(hex_string).decode()


def string_to_binary_string(string):
    """
    Convert a normal String to a Binary String without "0b" at the front.
    For example: "Z" to "01011010"

    Arguments:
        string {String} -- String to be converted.
    """

    return ''.join('{:0>8b}'.format(character) for character in string.encode())


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


def xor_hex_strings_easy(hex_string1, hex_string2):
    """
    XOR two Hex Strings with the same length.

    Arguments:
        hex_string1 {String} -- Hex String 1 to be XORed.
        hex_string2 {String} -- Hex String 2 to be XORed.

    Returns:
        String -- XORed string.
    """

    result = ''
    for hex_digit1, hex_digit2 in zip(hex_string1, hex_string2):
        result += format(int(hex_digit1, 16) ^ int(hex_digit2, 16), 'x')

    return result


def calculate_hamming_distance(string1, string2):
    """
    Calculate the Edit String/Hamming Distance of two strings.

    Arguments:
        string1 {String} -- string1 to use to calculate Hamming Distance.
        string2 {String} -- string2 to use to calculate Hamming Distance.

    Returns:
        Integer -- Hsmming Distance.
    """

    string1_encoded_byte_array = string1.encode()
    string2_encoded_byte_array = string2.encode()
    hamming_distance = 0

    for byte1, byte2 in zip(string1_encoded_byte_array, string2_encoded_byte_array):
        hamming_distance += bin(byte1 ^ byte2).count('1')

    return hamming_distance
