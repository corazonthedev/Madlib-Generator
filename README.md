<div align="center">

# Madlib Generator

**A polished desktop Mad Libs app built with Python and Tkinter.**  
It stays faithful to the original repo’s simple word-game idea, then upgrades the experience with a cleaner UI, modular architecture, automated tests, and production-style project structure.

<p>
  <img src="https://img.shields.io/badge/Python-3.11%2B-blue.svg" alt="Python 3.11+" />
  <img src="https://img.shields.io/badge/UI-Tkinter-6f42c1.svg" alt="Tkinter UI" />
  <img src="https://img.shields.io/badge/Code%20Style-Ruff-black.svg" alt="Ruff" />
  <img src="https://img.shields.io/badge/Tests-Pytest-0A9EDC.svg" alt="Pytest" />
  <img src="https://img.shields.io/badge/Coverage-97%25-brightgreen.svg" alt="97% coverage" />
</p>

</div>

---

## Overview

This project began as a lightweight single-file Tkinter app. The current version keeps the same fast, playful Mad Libs workflow, but turns it into a more complete desktop application with:

- a cleaner and more modern layout
- multiple reusable story templates
- inline result preview
- better validation and feedback states
- modular, testable source code
- packaging, linting, and automated quality checks

The goal was simple: **keep the original spirit, improve everything around the experience.**

## Why this version is better

### Better UX
- Two-panel desktop layout instead of a cramped single-window flow
- Clearer input labels and feedback states
- Inline story preview instead of relying only on pop-ups
- One-click actions for generate, copy, reset, and starter examples
- Template switching for replay value without changing the core idea

### Better engineering
- Logic, UI, settings, and templates are separated into dedicated modules
- High test coverage with focused unit tests
- Linting and packaging support
- Cleaner project structure for future feature work

## Features

- **Classic input flow**: adjective, two verbs, and a famous person
- **Multiple templates**: classic, adventure, and stage-style story modes
- **Starter examples**: instantly fill the form to demo the app
- **Copy-to-clipboard**: copy generated stories in one click
- **Reset support**: quickly clear and restart
- **Configurable settings**: customize title, accent color, and default template
- **Package-ready**: run as a script or install as a local package

## Tech stack

- **Language:** Python 3.11+
- **UI:** Tkinter / ttk
- **Testing:** Pytest
- **Linting:** Ruff
- **Packaging:** setuptools + `pyproject.toml`

## Project structure

```text
Madlib-Generator-main/
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   └── ADR.md
├── src/
│   └── madlib_generator/
│       ├── __init__.py
│       ├── app.py
│       ├── core.py
│       ├── settings.py
│       ├── templates.py
│       └── ui.py
├── tests/
│   ├── conftest.py
│   ├── test_core.py
│   ├── test_settings_and_app.py
│   └── test_ui_logic.py
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── README.md
├── main.py
├── pyproject.toml
├── requirements-dev.txt
└── requirements.txt
```

## Getting started

### 1) Clone the repository

```bash
git clone https://github.com/corazonthedev/Madlib-Generator.git
cd Madlib-Generator
```

### 2) Create and activate a virtual environment

**macOS / Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

For normal usage:

```bash
pip install -r requirements.txt
```

For development:

```bash
pip install -r requirements-dev.txt
```

### 4) Run the app

```bash
python main.py
```

## Install as a package

You can also install the app in editable mode and use the console entry point.

```bash
pip install -e .
madlib-generator
```

## Configuration

The app supports optional overrides through environment variables or a project-level `.env` file.

Use `.env.example` as a reference.

| Variable | Description | Default |
|---|---|---|
| `APP_TITLE` | Window and app title | `Madlib Generator` |
| `DEFAULT_TEMPLATE` | Default template key loaded on startup | `classic` |
| `ACCENT_COLOR` | Main accent color used by the UI | `#6d5efc` |

Example:

```env
APP_TITLE=My Madlib Generator
DEFAULT_TEMPLATE=adventure
ACCENT_COLOR=#8b5cf6
```

## Development

### Run tests

```bash
pytest
```

### Run linting

```bash
ruff check .
```

### Compile-check the codebase

```bash
python -m compileall -q .
```

## Quality status

The current version has already been hardened beyond the original prototype:

- modularized application structure
- automated tests for core logic, settings, and UI behavior
- high coverage threshold configured in `pyproject.toml`
- cleaner packaging and local install support
- headless-friendly validation for desktop app behavior

## Design direction

This redesign intentionally stays close to the identity of the original project.

Instead of turning it into a completely different product, it improves the same idea in a more polished way:

- same fast “fill a few words and generate a story” concept
- same playful programming-inspired roots
- cleaner visual hierarchy
- more app-like interaction model
- easier future expansion

## Roadmap ideas

Potential next improvements:

- save generated stories to file
- add theme switching (light/dark)
- ship screenshots or a small demo GIF in the README
- add more story packs and user-defined templates
- package standalone desktop builds for Windows/macOS

## Contributing

Contributions, cleanup, and improvements are welcome.

If you want to extend the project, start here:

1. fork the repository
2. create a feature branch
3. make your changes
4. run tests and linting
5. open a pull request

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for project notes.

## License

No license file is currently included in this repository.
If you want the project to be openly reusable, add a `LICENSE` file before public reuse or redistribution.
