#  Write a Python program to get an absolute file path

import os
file_name = input("Enter the file name or relative path: ")
absolute_path = os.path.abspath(file_name)
print("Absolute file path is:", absolute_path)
