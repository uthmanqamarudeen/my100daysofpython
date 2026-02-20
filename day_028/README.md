# Day 28: Tkinter — Pomodoro Timer

## Objectives
- Build a **Pomodoro Timer** desktop app using Tkinter.
- Use `Canvas` widget to display images and text overlays.
- Implement a countdown mechanism with `window.after()`.
- Manage state across multiple timer cycles.

## How it Works
- **Work session**: 25 minutes (green "Work" label)
- **Short break**: 5 minutes after each work session (pink "Break" label)
- **Long break**: 20 minutes after every 4 work sessions (red "Break" label)
- ✔️ Checkmarks appear below the timer for each completed work session.
- **Reset** restarts the whole cycle.

## Key Concepts
- `Canvas` widget for image display and text overlay
- `window.after(ms, function)` for non-blocking countdown logic
- Global state management (`reps`, `timer`)
- Dynamic label/color updates through `.config()`

## How to Run
```bash
cd pomodoro-start
python main.py
```
