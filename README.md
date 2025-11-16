# 📁 Python File Organiser

A lightweight Python script that automatically sorts files from a folder into categorized subfolders based on file extensions. Perfect for keeping messy directories organized with a single command.

---

## Features

- Automatically detects file types and moves them into category folders.
- Supports Documents, Images, Audio, Video, Archives, Code, and more.
- Unknown file types are sorted into an `Other` folder.
- If no folder path is provided, it sorts the current directory.
- Generates a `log.txt` file with details of the sorting process.

---

## Supported Extensions

**Documents:** `.txt`, `.pdf`, `.docx`, `.doc`, `.xls`, `.xlsx`, `.ppt`, `.pptx`  
**Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`  
**Audio:** `.mp3`, `.wav`, `.flac`, `.aac`  
**Video:** `.mp4`, `.mkv`, `.avi`, `.mov`  
**Archives:** `.zip`, `.rar`, `.7z`, `.tar`, `.gz`  
**Code:** `.py`, `.js`, `.html`, `.css`, `.java`, `.c`, `.cpp`, `.rb`, `.php`, `.sh`  

*You can expand this list by modifying the `extensionMap` dictionary in the script.*

---

## Usage

### **Run in Terminal**
```bash
$ cd Folder/To/Organise
$ py main.py
Leave blank to default to current folder / directory
Folder Path: 
```
