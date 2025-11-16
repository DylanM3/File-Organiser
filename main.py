# PYTHON FILE ORGANISER
# ====== ==== =========

# === Milestone 1 – Basic Setup ===

# Import modules
import os
import shutil

# Define variables

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
# Prompt user for folder path
# Validate path exists (FileNotFoundError)
# Validate permissions (PermissionError)
# List all files (ignore directories)

# === Milestone 3 – Split Files into Name + Extension ===
# For each file:
#   Split base name and extension
#   Normalize extension (.lower())
#   Append to files, name, extension lists

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