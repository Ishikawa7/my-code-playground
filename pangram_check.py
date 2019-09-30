'''
Write a Python function to check whether a string is pangram or not.

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
'''
import string


def pangram_check(s):
    alphabet = set()
    index = 0
    while len(alphabet) < len(string.ascii_lowercase) and index < len(s):
        if s[index].lower() in string.ascii_lowercase:
            alphabet.update(s[index])
        index += 1
    # print(len(alphabet))
    return len(alphabet) >= len(string.ascii_lowercase)
