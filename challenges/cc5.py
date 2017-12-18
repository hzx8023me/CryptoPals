#!/usr/bin/env python3

"""
Module to encrypt message with repeating xor key.
"""

from challenges.utils import xor_two_characters

def repeating_key_xor(message, key):
    """
    Encrypt message with repeating xor key.

    Arguments:
        message {String} -- Message to be encrypted.
        key {String} -- Key to be used to do repeating XOR.

    Returns:
        String -- Encrypted message in Hex.
    """

    encrypted_message_in_hex = ''
    for index, character in enumerate(message):
        encrypted_message_in_hex += xor_two_characters(character, key[index % len(key)])

    return encrypted_message_in_hex
