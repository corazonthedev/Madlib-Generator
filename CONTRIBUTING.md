# Contributing

## Setup
1. Create a virtual environment.
2. Install the development dependencies from `requirements-dev.txt`.
3. Run `pytest` before opening a pull request.

## Branching
- `feature/<name>` for new work
- `fix/<name>` for bug fixes

## Code style
- Keep UI code inside `src/madlib_generator/ui.py`
- Keep pure story logic inside `src/madlib_generator/core.py`
- Run `ruff check .` before committing

## Pull requests
Include a short summary, screenshots for UI changes, and test notes.
