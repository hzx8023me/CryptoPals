#!/usr/bin/env python3

"""
Module to decrypt the message from Hex String.
"""

import string
from challenges.constants import ENGLISH_LETTER_SCORE

def _calculate_score(possible_sentence):
    """
    Use method at
    https://crypto.stackexchange.com/questions/30209/developing-algorithm-for-detecting-plain-text-via-frequency-analysis
    """

    lower_case_possible_sentence = possible_sentence.lower()
    character_counts = {}
    character_length = 0
    for lower_character in lower_case_possible_sentence:
        if lower_character in string.ascii_lowercase + ' ':
            character_length += 1
            character_counts[lower_character] = character_counts.get(lower_character, 0) + 1
        # Not printable, should not be a valid sentence
        elif lower_character not in string.printable:
            return 0

    score = 0
    for character, count in character_counts.items():
        score += count * ENGLISH_LETTER_SCORE[character]

    return score

def single_byte_xor_cipher(hex_string, top=3, print_result=False):
    """
    Decrypt the message from Hex String.

    Arguments:
        hex_string {String} -- Hex String to be decrypted.
    """

    possible_results = []
    for character in (chr(index) for index in range(128)):
        possible_result = ''
        # Two characters at a time in order to convert to Integer
        for char1, char2 in zip(hex_string[::2], hex_string[1::2]):
            # unicode_code_for_hex_number = int(char1 + char2, 16)
            # unicode_code_for_character = ord(character)
            # Use chr() to convert Integer to Character
            possible_result += chr(int(char1 + char2, 16) ^ ord(character))

        possible_result_score = _calculate_score(possible_result)
        possible_result = possible_result.strip()
        if possible_result_score != 0:
            possible_results.append((character, possible_result, possible_result_score))

    most_possible_result = None
    for index, (key, result, score) in enumerate(sorted(possible_results, key=lambda result: result[2], reverse=True)):
        if index >= top:
            break
        if index == 0:
            most_possible_result = (key, result, score)
        if print_result:
            print("Result {} with Key {} has Score: {}".format(result, key, score))

    return most_possible_result
