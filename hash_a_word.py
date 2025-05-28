#  Write a Python program to hash a word.

import hashlib

word = input("Enter a word: ")

word_bytes = word.encode()

hash_result = hashlib.sha256(word_bytes).hexdigest()

print("Hashed word:", hash_result)
