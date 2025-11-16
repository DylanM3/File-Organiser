# PYTHON FILE ORGANISER
# ====== ==== =========

# === Milestone 1 – Basic Setup ===

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

# === Milestone 2 – Get Folder Contents ===

while True:
    # Prompt user for folder path
    folderPath = input("Folder Path: ")
    
    try:
        # Get folder contents
        folderContents = os.listdir(folderPath)
        break
        # Validate path exists (FileNotFoundError)
    except FileNotFoundError:
        print("Please confirm folder exists...")
        # Validate permissions (PermissionError)
    except PermissionError:
        print("Please confirm you have privileges to access this folder...")

# List all files (ignore directories)
for item in folderContents:
    # Reconstruct file path for use with isfile()
    itemPath = os.path.join(folderPath, item)

    # If item is a file than append to file only list
    if os.path.isfile(itemPath):
        folderFiles.append(item)

# === Milestone 3 – Split Files into Name + Extension ===

# For each file:
for file in folderFiles:

    # Split base name and extension
    baseName, extension = os.path.splitext(file)

    # Normalize extension with .lower()
    extension = extension.lower()

    # Append to name and extension lists
    nameList.append(baseName)
    extensionList.append(extension)

print(folderFiles)
print(nameList)
print(extensionList)

# === Milestone 4 – Create Folders Using extensionMap ===
# Build a set of unique extensions
# Loop through the set:
#   Lookup folder in extensionMap
#   Create folder if it doesn’t exist (os.mkdir or os.makedirs)

# === Milestone 5 – Sort / Move Files ===
# Loop through all files
# Lookup folder using normalized extension (extensionMap)
# Construct source and destination paths
# Move file with shutil.move
# Handle exceptions (file exists, permission errors)

# === Milestone 6 – Optional Improvements ===
# Handle multi-dot extensions (.tar.gz) if needed
# Skip hidden/system files (.DS_Store, Thumbs.db)
# Print a summary of files moved per folder
# Add user-friendly messages for progress