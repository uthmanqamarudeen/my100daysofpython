# Day 29: Tkinter — Password Manager

## Objectives
- Build a **Password Manager** GUI app using Tkinter.
- Generate strong, randomized passwords with `random`.
- Auto-copy passwords to clipboard using `pyperclip`.
- Save credentials to a file with input validation and confirmation dialogs.

## Features
- **Password Generator**: Creates a mix of letters, numbers and symbols (shuffled).
- **Auto-Copy**: Generated password is instantly copied to clipboard.
- **Save Credentials**: Stores website, email, and password to `data.txt`.
- **Input Validation**: Alerts user if website or password fields are empty.
- **Confirmation Dialog**: Asks for confirmation before saving (via `messagebox`).

## How to Run
```bash
cd password-manager-start
python main.py
```

> **Note:** Requires `pyperclip` — install with `pip install pyperclip`.
