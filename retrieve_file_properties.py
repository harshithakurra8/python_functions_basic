#  Write a Python program to retrieve file properties.

import os
import time

file_path = input("Enter the file path: ")

if os.path.exists(file_path):
    print("\nFile Properties:")
    print("File name:", os.path.basename(file_path))
    print("Size (in bytes):", os.path.getsize(file_path))
    print("Last accessed:", time.ctime(os.path.getatime(file_path)))
    print("Last modified:", time.ctime(os.path.getmtime(file_path)))
    print("Creation time:", time.ctime(os.path.getctime(file_path)))
else:
    print("File does not exist.")
