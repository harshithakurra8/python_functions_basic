#  Write a Python program to check whether a file exists

import os
file_path = "hello.py"
if os.path.exists(file_path):
    print("File Exists")
else:
    print("File does not exists")