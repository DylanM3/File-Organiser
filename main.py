# PYTHON FILE ORGANISER
# ====== ==== =========

# === IMPORT MODULES AND DEFINE VARIABLES ===
import os

files = [] # Full file name
name = [] # File Name without Extensions
extension = [] # File Extensions without Name

supportedExtensions = {
    "Documents": [".txt", ".pdf", ".docx",
                  ".doc", ".odt", ".rtf",
                  ".xlsx", ".xls", ".pptx",
                  ".ppt"],
    
    "Images": [".jpg", ".jpeg", ".png",
               ".gif", ".bmp", ".tiff",
               ".svg", ".webp"],
    
    "Audio": [".mp3", ".wav", ".flac",
              ".aac", ".ogg", ".m4a"],
    
    "Video": [".mp4", ".mkv", ".avi",
              ".mov", ".wmv", ".flv"],
    
    "Archives": [".zip", ".rar", ".7z",
                 ".tar", ".gz", ".bz2"],
    
    "Code": [".py", ".js", ".html",
             ".css", ".java", ".c",
             ".cpp", ".rb", ".php",
             ".sh"],
    
    "Other": [".iso", ".exe", ".dll",
              ".log", ".json", ".csv"]
}

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

# === REMOVE DIRECTORYS AND SPLIT FILES BY NAME AND EXTENSIONS ===

for item in folderContents:
    # Reconstruct a file path to use with isFile()
    itemPath = os.path.join(filePath, item)

    # Append to a new file only directory
    if os.path.isfile(itemPath) == True:
        files.append(item)

        # Split itemPath into root and ext, then append to corresponding list
        root, ext = os.path.splitext(itemPath)
        name.append(root)
        extension.append(ext)

print(folderContents) # Everything
print(files) # Only Files
print(name) # File name WITH PATH
print(extension) # File Extensions