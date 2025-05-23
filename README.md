# Extension Crawler Tool

A simple, interactive command-line tool written in Python that allows users to list files by extension within a specified directory.

This utility helps you quickly find and display files based on their extension (e.g. `.txt`, `.jpg`, `.nk`), making it useful for basic file management, cleanup tasks, or quick inspection of project folders.

---

## Features

- Prompt-based interface (no arguments needed)
- Validates the directory path input
- Filters and lists files by user-specified extension
- Displays total number of matching files
- Logs search results with timestamps

---

## Usage

Run the script in a terminal or command prompt:

```bash
python file_finder.py
You will be prompted to enter:

A directory path and A file extension (.py, .txt)

Example output:

Enter directory path: /Users/username/projects
Enter file extension (.py):

1. main.py
2. utils.py
3. config.py

The tool will also log the number of files found using the Python logging module.
```

## Requirements

- Python 3.6 or higher

No external libraries needed (uses only Python standard library)

## License

This project is provided as is, without warranty of any kind. Use at your own risk.

## Author

Developed by Erik Elizalde
