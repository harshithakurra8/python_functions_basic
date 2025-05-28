#  . Write a Python program to get height and width of the
#  console window

import os
size = os.get_terminal_size()

print("Console width:",size.columns)
print("Console height:",size.lines)