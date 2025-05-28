#  Write a Python program to get a directory listing, sorted
#  by creation date

import os
from datetime import datetime

folder_path = input("Enter the folder path: ")

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

files.sort(key=lambda f: os.path.getctime(os.path.join(folder_path, f)))

print("\nFiles sorted by creation date (oldest to newest):")
for f in files:
    full_path = os.path.join(folder_path, f)
    create_time = os.path.getctime(full_path)
    readable_time = datetime.fromtimestamp(create_time).strftime('%Y-%m-%d %H:%M:%S')
    print(f"{f}  -->  Created on: {readable_time}")
