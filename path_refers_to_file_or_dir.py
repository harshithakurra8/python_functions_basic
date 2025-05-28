#  Write a Python program to find path refers to a file or
#  directory when you encounter a path name

import os

path = input("Enter the path: ")

if os.path.isfile(path):
    print("The path refers to a file.")
elif os.path.isdir(path):
    print("The path refers to a directory.")
else:
    print("The path does not exist.")
