# PYTHON FILE ORGANISER
# ====== ==== =========

# === IMPORT MODULES AND DEFINE VARIABLES ===
import os
files = []

# === CREATE LIST OF FOLDER CONTENTS ===

while True:
    # Ask user for file path
    filePath = input("File Path: ")

    try:
        # Append contents to content list
        folderContents = os.listdir(filePath)
        break
    except FileNotFoundError:
        # If file not found then reprompt with clear error
        print("Please check your file path is correct... ")

# === REMOVE DIRECTORYS ===

for item in folderContents:
    # Reconstruct a file path to use with isFile()
    itemPath = os.path.join(filePath, item)

    # Append to a new file only directory
    if os.path.isfile(itemPath) == True:
        files.append(item)

print(folderContents) # Everything
print(files) # Only Files