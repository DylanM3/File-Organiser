# PYTHON FILE ORGANISER
# ====== ==== =========

# === Milestone 1 - Basic Setup ===

# Import modules
import os
import shutil

# Define variables
folderFiles = []
nameList = []
extensionList = []

# Define extensionMap (reversed dict)
extensionMap = {
    # Documents
    ".txt": "Documents",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",

    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".svg": "Images",

    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".aac": "Audio",

    # Video
    ".mp4": "Video",
    ".mkv": "Video",
    ".avi": "Video",
    ".mov": "Video",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",

    # Code
    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".java": "Code",
    ".c": "Code",
    ".cpp": "Code",
    ".rb": "Code",
    ".php": "Code",
    ".sh": "Code"
}

# === Milestone 2 - Get Folder Contents ===

while True:
    # Prompt user for folder path
    folderPath = input("Folder Path: ")

    # Prepare log
    log = open(os.path.join(folderPath, "log.txt"), 'w')
    log.write(f"Folder Path: {folderPath} \n")
    
    # Get folder contents
    try:
        folderContents = os.listdir(folderPath)
        log.write("Successfully fetched folder contents. \n")
        break

    # Validate path exists (FileNotFoundError)
    except FileNotFoundError:
        log.write("Cannot find folder. \n")
        print("Please confirm folder exists...")

    # Validate permissions (PermissionError)
    except PermissionError:
        log.write("Insuffient privileges. \n")
        print("Please confirm you have privileges to access this folder...")

# List all files (ignore directories)
for item in folderContents:
    # Reconstruct file path for use with isfile()
    itemPath = os.path.join(folderPath, item)

    # If item is a file than append to file only list
    if os.path.isfile(itemPath):
        folderFiles.append(item)

# === Milestone 3 - Split Files into Name + Extension ===

# For each file:
for file in folderFiles:

    # Split base name and extension
    baseName, extension = os.path.splitext(file)

    # Normalize extension with .lower()
    extension = extension.lower()

    # Append to name and extension lists
    nameList.append(baseName)
    extensionList.append(extension)

# === Milestone 4 - Create Folders Using extensionMap ===

# Build a set of unique extensions (lowercase)
uniqueExtensions = set(extensionList)

# Loop through each unique extension
for extension in uniqueExtensions:
    # Lookup folder in extensionMap
    currentCategory = extensionMap.get(extension)

    # Create "Other" folder for unknown files
    if currentCategory == None:
        try:
            os.mkdir(os.path.join(folderPath, "Other"))
            log.write("Successfully created 'other' catch-all folder. \n")
        except FileExistsError:
            log.write("'Other' folder already exists. \n")
            continue
    else:
        try:
            os.mkdir(os.path.join(folderPath, currentCategory))
            log.write(f"Successfully created '{currentCategory}' folder. \n")
        except FileExistsError:
            log.write(f"'{currentCategory}' folder already exists. \n")
            continue

# === Milestone 5 - Sort / Move Files ===

# Loop through all files in folderFiles
for index in range(0, len(folderFiles)):

    # Get the extension from extensionList
    currentExtension = extensionList[index]

    # Lookup folder in extensionMap
    currentCategory = extensionMap.get(currentExtension)

    # Use "Other" if extension not found
    if currentCategory == None:

        # Create full folder paths
        sourcePath = os.path.join(folderPath, folderFiles[index])
        destinationPath = os.path.join(folderPath, "Other", folderFiles[index])

        # Move file into the correct folder while excepting errors
        try:
            shutil.move(sourcePath, destinationPath)
        except FileExistsError:
            log.write("File already exists in folder... \n")
            continue
        except PermissionError:
            log.write("Missing permissions to move file... \n")
            continue

    else: # IF CURRENT CATEGORY IS NOT NONE

        # Create full folder paths
        sourcePath = os.path.join(folderPath, folderFiles[index])
        destinationPath = os.path.join(folderPath, currentCategory, folderFiles[index])

        # Move file into the correct folder while excepting errors
        try:
            shutil.move(sourcePath, destinationPath)
        except FileExistsError:
            log.write("File already exists in folder... \n")
            continue
        except PermissionError:
            log.write("Missing permissions to move file... \n")
            continue

# === Milestone 6 - Log ===
log.write("Finished process. \n")
log.close()