# Introduction

- [x] Add notes to file.  

- [x] Print notes of files.
- [x] Print Noted files in the given directory
- [x] Search noted files with given keyword.
- [ ] Export data of noted files.
- [ ] Add relationships between files.
- [ ] Print Relationships about a given file.

# Requirements

python>=3.6

# Installation
```
git clone https://github.com/wapping/FileNote.git
cd FileNote
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m build
pip install dist/FileNote-0.0.1-py3-none-any.whl
```

Check if you have successfully install this tool, just enter `fnote` on the console.

# How to use

1. Add note to a file

`fnote -a file note`

like this

`fnote -a /Users/me/file.txt 'my file'`

2. Print the note of a file

`fnote -pf file`

like this

`fnote -pf -k /Users/me/file.txt`