
"""
Break repeating-key XOR

It is officially on, now.
This challenge isn't conceptually hard, but it involves actual error-prone coding.
The other challenges in this set are there to bring you up to speed.
This one is there to qualify you.
If you can do this one, you're probably just fine up to Set 6.

There's a file here (data/cc6.txt).
It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:
1. Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

2. Write a function to compute the edit distance/Hamming distance between two strings.
The Hamming distance is just the number of differing bits.
The distance between: "this is a test" and "wokka wokka!!!" is 37.
Make sure your code agrees before you proceed.

3. For each KEYSIZE,
take the first KEYSIZE worth of bytes,
and the second KEYSIZE worth of bytes,
and find the edit distance between them.
Normalize this result by dividing by KEYSIZE.

4. The KEYSIZE with the smallest normalized edit distance is probably the key.
You could proceed perhaps with the smallest 2-3 KEYSIZE values.
Or take 4 KEYSIZE blocks instead of 2 and average the distances.

5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.

6. Now transpose the blocks:
make a block that is the first byte of every block,
and a block that is the second byte of every block, and so on.

7. Solve each block as if it was single-character XOR.
You already have code to do this.

8. For each block:
the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block.
Put them together and you have the key.

This code is going to turn out to be surprisingly useful later on.
Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing.
But more people "know how" to break it than can actually break it,
and a similar technique breaks something much more important.

No, that's not a mistake.
We get more tech support questions for this challenge than any of the other ones.
We promise, there aren't any blatant errors in this text.
In particular: the "wokka wokka!!!" edit distance really is 37.
"""

import base64
import itertools
from challenges.utils import calculate_hamming_distance, string_to_hex_string, hex_string_to_string
from challenges.cc3 import single_byte_xor_cipher
from challenges.cc5 import repeating_key_xor

def break_repeating_key_xor(data_file_path):
    """
    Breaks repeating key XOR in the data file.

    Arguments:
        data_file_path {String} -- Path of the data file.

    Returns:
        String -- Most possible result message.
    """

    with open(data_file_path, 'r') as data_file:
        key_size_hamming_distance_map = {}
        # b64decode() retuens byte array, use decode() to convert to String.
        base64_decoded_data = base64.b64decode(data_file.read()).decode()
        # Step 1.
        for key_size in range(2, 41):
            # Get the first 4 blocks, with each block has key_size bytes.
            blocks = [base64_decoded_data[i : i+key_size] for i in range(0, 4*key_size, key_size)]
            hamming_distances = []
            # Get all possible combinations for the 4 blocks.
            for combination in itertools.combinations(blocks, 2):
                # Calculate normalized hamming distance for each combination.
                hamming_distances.append(calculate_hamming_distance(combination[0], combination[1]) / key_size)
            # Store the average hamming distance for the current key_size.
            key_size_hamming_distance_map[key_size] = sum(hamming_distances) / len(hamming_distances)
        # Find the most possible key with the lowest hamming distance.
        most_possible_key = sorted(key_size_hamming_distance_map.items(), key=lambda x: x[1])[0][0]
        overall_key = ''
        for i in range(most_possible_key):
            # Step 6.
            block = base64_decoded_data[i::most_possible_key]
            overall_key += single_byte_xor_cipher(string_to_hex_string(block))[0]
        result_hex = repeating_key_xor(base64_decoded_data, overall_key)
        return overall_key, hex_string_to_string(result_hex)
