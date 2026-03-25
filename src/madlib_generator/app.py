"""Application entrypoint."""

from __future__ import annotations

import tkinter as tk

from .settings import load_settings
from .ui import MadlibApp


def main() -> None:
    root = tk.Tk()
    settings = load_settings()
    MadlibApp(root=root, settings=settings)
    root.mainloop()
