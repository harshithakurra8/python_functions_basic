#  Write a Python program to determine if a Python shell is
#  executing in 32bit or 64bit mode on OS

import platform
arch = platform.architecture()[0]
print(f"Python is running in {arch} mode.")