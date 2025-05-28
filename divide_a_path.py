#  Write a Python program to divide a path on the extension
#  separator

import os

file_path = "pythonbeginnerlevelquestions/calender.py"

root, ext = os.path.splitext(file_path)
print("Root part:", root)
print("Extension:", ext)
