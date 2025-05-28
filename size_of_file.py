# . Write a Python program to get the size of a file

import os
file_size = os.path.getsize("calender.py")
print("\nThe size of calender.py is:",file_size,"Bytes")