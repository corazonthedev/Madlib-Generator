# Madlib Generator

A refreshed desktop madlib app built from the original single-file Tkinter project.
It keeps the same quick word-game idea, but adds cleaner structure, stronger UI, inline results, validation, and test coverage.

## What's improved
- Cleaner two-panel desktop interface
- Default template that stays close to the original project
- Two extra templates for replay value
- Inline result preview instead of only pop-up feedback
- Input validation and clearer status messages
- Copy result, reset form, and load starter examples
- Modular source layout with automated tests and CI
- Proper package metadata and a console entry point

## Project structure
```text
Madlib-Generator-main/
├── main.py
├── src/madlib_generator/
├── tests/
├── docs/
├── .github/workflows/ci.yml
├── pyproject.toml
├── requirements.txt
└── requirements-dev.txt
```

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
python main.py
```

## Install as a package
```bash
pip install -e .
madlib-generator
```

## Test locally
```bash
pytest
```

## Lint locally
```bash
ruff check .
```

## Configuration
You can override the optional defaults with either environment variables or a project-level `.env` file.
See `.env.example` for the supported keys.

## UX direction
The redesign stays loyal to the original repo by keeping the same four-word input flow and classic madlib output, while presenting it in a more modern and easier-to-use layout.
