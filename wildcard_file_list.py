#  Write a Python program to make file lists from current
#  directory using a wildcard

import glob

py_files = glob.glob("*.py")

print("python files in current directory:")
for file in py_files:
    print(file)
