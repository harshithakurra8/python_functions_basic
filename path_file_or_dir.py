#  Write a Python program to check whether a file path is a
#  file or a directory

import os
path = input("Enter a file or directory path: ")
if os.path.isfile(path):
    print("This is a file.")

elif os.path.isdir(path):
    print("This is a directory.")

else:
    print("This path does not exist or is neither a file nor a directory.")
