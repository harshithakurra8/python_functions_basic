#  Write a Python program to find files and skip
#  directories of a given directory


import os
print([f for f in os.listdir('/users/aifa user') if os.path.isfile(os.path.join('/users/aifa user', f))])
