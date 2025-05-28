# . Write a Python function to check whether a string is a
#  pangram or not.
#  Note : Pangrams are words or sentences containing every
#  letter of the alphabet at least once.
#  For example : "The quick brown fox jumps over the lazy dog"

import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)  # Set of all lowercase letters
    return set(s.lower()) >= alphabet  # Check if all letters are in the input string
s = "The quick brown fox jumps over the lazy dog"
if is_pangram(s):
    print("The string is a pangram.")
else:
    print("The string is NOT a pangram.")
