# Day 6: Reeborg's World

## Objectives
- Master `while` loops and functions.
- Learn to define custom functions (e.g., `turn_right()`).
- Solve algorithmic challenges (Hurdles, Maze) in the Reeborg's World environment.

## Content
- **`reeborgs_solution.py`**: My generic solution that solves multiple Reeborg's World challenges, including **Hurdle 1-4** and **Maze**.
- **`tests/`**: Contains custom world configurations provided in the course resources to test the solution's robustness.

## My Learnings
- **Generalizing Solutions**: Writing a single algorithm (using `while` loops and conditional checks like `right_is_clear()`) that adapts to different world configurations rather than hard-coding a path for just one.
- **Robust Testing**: Verifying the solution against various custom worlds (found in the `tests` folder) to ensuring it handles edge cases correctly.

## Notes
The code in this folder is designed to run in the online Reeborg environment, as it depends on built-in functions like `move()` and `turn_left()`.
