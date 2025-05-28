# . Write a Python program to get OS name, platform and
#  release information

import os 
import platform
os_name=os.name
platform_name=platform.system()
release_info=platform.release()

print(f"OS name      : {os_name}")
print(f"Platform     : {platform_name}")
print(f"OS release   : {release_info}")