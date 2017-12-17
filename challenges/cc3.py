#!/usr/bin/env python3

"""
Module to decrypt the message from Hex String.
"""

import string
from collections import OrderedDict
from challenges.constants import ENGLISH_LETTER_FREQUENCY

def _calculate_score(possible_sentence):
    """
    Use method at
    https://crypto.stackexchange.com/questions/30209/developing-algorithm-for-detecting-plain-text-via-frequency-analysis
    """

    lower_case_possible_sentence = possible_sentence.lower()
    character_counts = {}
    character_length = 0
    for lower_character in lower_case_possible_sentence:
        if lower_character in string.ascii_lowercase:
            character_length += 1
            character_counts[lower_character] = character_counts.get(lower_character, 0) + 1
        # Not printable, should not be a valid sentence
        elif lower_character not in string.printable:
            return 0

    chi_square_score = 0
    for character, obversed_count in character_counts.items():
        expected_count = character_length * ENGLISH_LETTER_FREQUENCY[character]
        difference = obversed_count - expected_count
        chi_square_score += difference * difference / expected_count

    return chi_square_score

def single_byte_xor_cipher(hex_string, top=3, print_result=False):
    """
    Decrypt the message from Hex String.

    Arguments:
        hex_string {String} -- Hex String to be decrypted.
    """

    possible_results = {}
    for character in string.printable:
        possible_result = ''
        # Two characters at a time in order to convert to Integer
        for char1, char2 in zip(hex_string[::2], hex_string[1::2]):
            base10_number = int(char1 + char2, 16)
            unicode_code_for_character = ord(character)
            # Use chr() to convert Integer to Character
            possible_result += chr(base10_number ^ unicode_code_for_character)
        print(character, possible_result)
        possible_result_score = _calculate_score(possible_result)
        if possible_result_score != 0:
            possible_results[(possible_result, character)] = possible_result_score

    most_possible_result = None
    for index, (result, score) in enumerate(OrderedDict(sorted(possible_results.items(), key=lambda pair: pair[1])).items()):
        if index >= top:
            break
        if index == 0:
            most_possible_result = result
        if print_result:
            print("Result {} with Key {} has Score: {}".format(result[0], result[1], score))

    return most_possible_result
