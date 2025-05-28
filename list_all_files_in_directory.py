#  Write a Python program to list all files in a directory
#  in Python.

# import OS module
import os
folder_path = input("Enter the path to the directory: ")
if os.path.exists(folder_path):
    print("\nFiles in the directory:")
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        if os.path.isfile(full_path):
            print(item)
else:
    print("The directory does not exist.")


