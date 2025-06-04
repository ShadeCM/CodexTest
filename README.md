# CodexTest

## Duplicate File Detection

This repository includes `check_duplicates.py`, a small utility that scans for
duplicate files based on their contents.

### Usage on Windows

Run the script from the command prompt or PowerShell:

```powershell
python check_duplicates.py
```

By default it scans your Windows Desktop directory (e.g.
`C:\Users\<username>\Desktop`). Pass a directory path if you want to search a
different location:

```powershell
python check_duplicates.py "D:\Some\Folder"
```
