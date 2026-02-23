# Day 31: Flash Card App (Capstone Project)

## Objectives
- Build a professional **Flash Card App** to learn languages (or anything!).
- Master the `after()` method in Tkinter for timed events.
- Practice **CSV** management and data persistence with **Pandas**.
- Build a clean GUI with advanced Tkinter techniques.

## Features
- **Flash Card System**: Shows a word in French, then flips after 3 seconds to show the English translation.
- **Progress Tracking**: MASTERED words are removed from the deck.
- **Smart Loading**: Automatically saves remaining words to `words_to_learn.csv` so you can pick up where you left off.
- **User Interface**: High-quality images for the cards and buttons.

## Key Concepts
- `pandas.read_csv().to_dict(orient="records")` for easy data access.
- `window.after()` and `window.after_cancel()` for robust timing logic.
- `try-except` blocks for handling the first-time setup (loading backup data if progress file doesn't exist).
- `Canvas.itemconfig()` for dynamic UI updates.

## How to Run
```bash
cd flash-card-project-start
python main.py
```

> **Note:** Requires `pandas`. master your vocabulary efficiently! 🧠📖
