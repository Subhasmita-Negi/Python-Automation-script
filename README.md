# Python Automation Script

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Status](https://img.shields.io/badge/Status-Active-success)

A Python automation script that scans folders and organizes files automatically based on file type.

---

## Features

### 1. Scan Folder

- Take folder path as user input
- Check whether folder exists
- Display all files and folders
- Handle empty folders
- Exception handling

### 2. Automatic File Organizer

- Organize files by extension
- Create folders automatically
- Move files into category folders
- Supports:
  - Images
  - Documents
  - Music
  - Videos
    
### 3. Delete Empty Folders

- Scan all folders inside a directory
- Detect empty folders
- Delete empty folders automatically
- Handle exceptions

### 4. Automatic Log Generation

- Generate `log.txt` automatically
- Store file operations
- Store error messages
- Track automation activities
---

## Technologies Used

- Python
- OS Module
- Shutil Module
- Logging Module
---

## Project Structure

```bash
Python-Automation-Script/
│
├── main.py
├── log.txt
└── README.md
```

---

## How to Run

```bash
python main.py
```

---

## Menu Options

```bash
1. Scan Folder
2. Organize Files
3. Delete Empty Folders
4. Exit
```

---

## Example Output

### Scan Folder

```bash
Enter folder path: D:/Downloads

Files and Folders:

photo.jpg
song.mp3
notes.pdf
```

### Organize Files

```bash
Moved: photo.jpg -> Images
Moved: notes.pdf -> Documents
Moved: song.mp3 -> Music
```
### Delete Empty Folders
Deleted: D:/Downloads/TestFolder

### Log File Example
2026-05-14 10:20:11 - Folder scanned successfully
2026-05-14 10:22:05 - Moved file: photo.jpg
2026-05-14 10:25:40 - Deleted folder: TestFolder
