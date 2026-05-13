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

---

## Technologies Used

- Python
- OS Module
- Shutil Module

---

## Project Structure

```bash
Python-Automation-Script/
│
├── main.py
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
