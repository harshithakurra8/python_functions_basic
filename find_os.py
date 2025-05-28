#  Write a Python program to find the operating system
#  name, platform and platform release date.
#  Operating system name:
#  posix
#  Platform name:
# Linux
#  Platform release:
#  4.4.0-47-generic

import os
import platform
os_name=os.name
platform_name=platform.system()
platform_release=platform.release()
print("Operating System:",os_name)
print("Platform Name:",platform_name)
print("Platform Realese:",platform_release)