# Day 26: List Comprehension & Dictionary Comprehension

## Objectives
- Master **List Comprehension** (creating lists in one line).
- Learn **Dictionary Comprehension** (creating dicts in one line).
- Apply comprehensions to real-world projects.
- Refactor code to be more "Pythonic" and concise.

## Key Concepts

**List Comprehension:**
```python
new_list = [item for item in old_list if condition]
```

**Dictionary Comprehension:**
```python
new_dict = {key:value for (key, value) in old_dict.items() if condition}
```

## Projects

### NATO Alphabet Converter
- Converts words into the NATO phonetic alphabet.
- Uses **dict comprehension** to create alphabet lookup.
- Uses **list comprehension** to generate phonetic output.
- Example: "HELLO" → ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']

### Day 25 Refactor
- Updated US States Game to use list comprehend (cleaner code!).
- Replaced loop with: `[state for state in states_list if state not in correct_guesses]`

## How to Run
```bash
cd NATO-alphabet
python main.py
```
