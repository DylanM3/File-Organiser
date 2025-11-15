# Python File Organiser
# ------ ---- ---------

# IMPORT MODULES
import os

# GET FILE PATH AND VIEW INFORMATION

while True:
    # Ask user for file path
    file_path = input("File Path: ")

    try:
        print(os.listdir(file_path))
        break
    except FileNotFoundError:
        print("Please check your file path is correct... ")