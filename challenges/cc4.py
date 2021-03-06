#!/usr/bin/env python3

"""
Detect single-character XOR

One of the 60-character strings in data/cc4.txt has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
"""

from challenges.cc3 import single_byte_xor_cipher

def detect_single_byte_xor(data_file_path):
    """
    Find the String that is encrypted by single-character XOR in a given file.

    Arguments:
        data_file_path {String} -- Path of the data file.

    Returns:
        String -- Decrypted message.
    """

    with open(data_file_path, 'r') as data_file:
        results = []
        for current_line in data_file:
            line_result = single_byte_xor_cipher(current_line.strip())
            if line_result:
                results.append(line_result)

    sorted_results = sorted(results, key=lambda result: result[2], reverse=True)
    return sorted_results[0][1]
