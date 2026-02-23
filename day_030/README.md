# Day 30: Errors, Exceptions, and JSON Data

## Objectives
- Master **Error Handling** using `try`, `except`, `else`, and `finally`.
- Learn to `raise` custom exceptions.
- Work with **JSON** (JavaScript Object Notation) for complex data structures.
- Refactor existing projects to be more robust and feature-rich.

## Key Concepts

**Error Handling:**
```python
try:
    # Code that might cause an exception
except FileNotFoundError:
    # Code to run if exception happens
else:
    # Code to run if NO exception happens
finally:
    # Code that runs NO MATTER WHAT
```

**JSON Operations:**
- `json.dump()`: Write data to JSON.
- `json.load()`: Read data from JSON.
- `json.update()`: Update existing JSON data.

## Projects

### 1. Password Manager (Revised)
- **Search Functionality**: Users can now search for existing passwords by website name.
- **JSON Storage**: Switched from `.txt` to `.json` for structured, multi-key data storage.
- **Robustness**: Uses exception handling to manage missing data files or missing keys.

### 2. NATO Alphabet (Revised)
- Added error handling to handle non-alphabet characters (like numbers or symbols) without crashing.
- Loops back to ask for input if an error occurs.

## How to Run

**Revised Password Manager:**
```bash
cd password-manager-revised
python main.py
```

**Revised NATO Alphabet:**
```bash
cd NATO-alphabet-revised
python main.py
```
