English | [简体中文](./README_cn.md) 

# Introduction

This is a tool for managing file notes through the command line and has the following functions.

- [x] Add notes to files (folders).
- [x]  files with notes.
- [x] View files with added notes in the given directory.
- [x] Search for files with notes based on the given keyword.
- [x] Add relationships to files.
- [x] View files related to a file.
- [ ] Export all file notes data.

One limitation of this tool is that after a file is moved or renamed, it cannot be associated with its note.

# Installation

1. Install python 

   Install python with a version greater than or equal to 3.6.

2. Download and install this tool

   2.1 Download the repository

    ```
    git clone https://github.com/wapping/FileNote.git
    cd FileNote
    ```

   2.2 Choose one of the following methods

    - Install from package

   ```
   pip install dist/FileNote-0.0.1-py3-none-any.whl
   ```

    - Compile and install from source code

   ```
   python3 -m pip install --upgrade pip
   python3 -m pip install --upgrade build
   python3 -m build
   pip install dist/FileNote-0.0.1-py3-none-any.whl
   ```
3. Test


Check if you have successfully install this tool, just enter `fnote` in the terminal.

# Quick start

1. Add a note to a file

`fnote -a /path/to/your/file note`

`/path/to/your/file`：The path of the file you want to note, which can be a relative path.

`note`：You note.

2. View the note of a file
`fnote -pf -k keyword`

`keyword`：The keyword,  can be a keyword of a file path or a note.