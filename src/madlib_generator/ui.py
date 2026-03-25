"""Tkinter UI for the Madlib Generator."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from typing import Dict

from .core import (
    ValidationError,
    build_madlib,
    get_starter_examples,
    get_template_descriptions,
    get_template_names,
)
from .settings import AppSettings

_DEFAULT_RESULT_TEXT = 'Fill in the words on the left, then generate your madlib here.'


def resolve_template_key(selected_name: str, template_names: Dict[str, str]) -> str:
    for key, value in template_names.items():
        if value == selected_name:
            return key
    return next(iter(template_names))


class MadlibApp:
    def __init__(self, root: tk.Tk, settings: AppSettings) -> None:  # pragma: no cover
        self.root = root
        self.settings = settings
        self.root.title(settings.app_title)
        self.root.geometry('960x620')
        self.root.minsize(900, 560)
        self.root.configure(bg='#111827')

        self.template_names = get_template_names()
        self.template_descriptions = get_template_descriptions()
        self.entries: Dict[str, tk.StringVar] = {
            'adjective': tk.StringVar(),
            'verb1': tk.StringVar(),
            'verb2': tk.StringVar(),
            'famous_person': tk.StringVar(),
        }
        self.template_var = tk.StringVar(value=settings.default_template)
        self.result_var = tk.StringVar(value=_DEFAULT_RESULT_TEXT)
        self.status_var = tk.StringVar(value='Ready to create a story.')
        self.description_var = tk.StringVar(
            value=self.template_descriptions.get(
                self.template_var.get(), 'Choose a template to begin.'
            )
        )

        self._configure_style()
        self._build_layout()
        self._bind_events()
        self.fill_examples()

    def _configure_style(self) -> None:  # pragma: no cover
        style = ttk.Style()
        style.theme_use('clam')

        accent = self.settings.accent_color
        style.configure('App.TFrame', background='#111827')
        style.configure('Card.TFrame', background='#182233')
        style.configure('TLabel', background='#111827', foreground='#f9fafb')
        style.configure('Muted.TLabel', background='#182233', foreground='#94a3b8')
        style.configure(
            'Heading.TLabel',
            background='#111827',
            foreground='#f9fafb',
            font=('Segoe UI', 22, 'bold'),
        )
        style.configure(
            'Subheading.TLabel',
            background='#111827',
            foreground='#cbd5e1',
            font=('Segoe UI', 10),
        )
        style.configure(
            'Field.TLabel',
            background='#182233',
            foreground='#e2e8f0',
            font=('Segoe UI', 10, 'bold'),
        )
        style.configure(
            'Primary.TButton',
            background=accent,
            foreground='#ffffff',
            borderwidth=0,
            focusthickness=3,
            focuscolor=accent,
            padding=(16, 10),
            font=('Segoe UI', 10, 'bold'),
        )
        style.map('Primary.TButton', background=[('active', '#5b50d5')])
        style.configure(
            'Secondary.TButton',
            background='#243042',
            foreground='#e5e7eb',
            padding=(14, 10),
            borderwidth=0,
            font=('Segoe UI', 10),
        )
        style.map('Secondary.TButton', background=[('active', '#334155')])
        style.configure(
            'TEntry',
            fieldbackground='#0f172a',
            foreground='#f8fafc',
            bordercolor='#334155',
            insertcolor='#f8fafc',
            padding=8,
        )
        style.configure(
            'TCombobox',
            fieldbackground='#0f172a',
            background='#0f172a',
            foreground='#f8fafc',
            arrowcolor='#f8fafc',
        )

    def _build_layout(self) -> None:  # pragma: no cover
        container = ttk.Frame(self.root, style='App.TFrame', padding=24)
        container.pack(fill='both', expand=True)
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)
        container.rowconfigure(1, weight=1)

        header = ttk.Frame(container, style='App.TFrame')
        header.grid(row=0, column=0, columnspan=2, sticky='ew', pady=(0, 18))
        ttk.Label(
            header,
            text=self.settings.app_title,
            style='Heading.TLabel',
        ).pack(anchor='w')
        ttk.Label(
            header,
            text='Same quick word game, rebuilt with a cleaner layout and better flow.',
            style='Subheading.TLabel',
        ).pack(anchor='w', pady=(6, 0))

        controls = ttk.Frame(container, style='Card.TFrame', padding=20)
        controls.grid(row=1, column=0, sticky='nsew', padx=(0, 12))
        controls.columnconfigure(0, weight=1)

        preview = ttk.Frame(container, style='Card.TFrame', padding=20)
        preview.grid(row=1, column=1, sticky='nsew', padx=(12, 0))
        preview.columnconfigure(0, weight=1)
        preview.rowconfigure(2, weight=1)

        ttk.Label(controls, text='Template', style='Field.TLabel').grid(
            row=0, column=0, sticky='w'
        )
        template_select = ttk.Combobox(
            controls,
            state='readonly',
            values=[self.template_names[key] for key in self.template_names],
        )
        template_keys = list(self.template_names)
        try:
            current_index = template_keys.index(self.template_var.get())
        except ValueError:
            current_index = 0
            self.template_var.set(template_keys[0])
        template_select.current(current_index)
        template_select.grid(row=1, column=0, sticky='ew', pady=(8, 10))
        self.template_select = template_select

        description_label = ttk.Label(
            controls,
            textvariable=self.description_var,
            style='Muted.TLabel',
            wraplength=360,
            justify='left',
        )
        description_label.grid(row=2, column=0, sticky='ew', pady=(0, 18))

        fields = [
            ('Adjective', 'adjective', 'fun, wild, bold'),
            ('Verb 1', 'verb1', 'build, dance, sprint'),
            ('Verb 2', 'verb2', 'celebrate, code, glide'),
            ('Famous Person', 'famous_person', 'Ada Lovelace, Beyoncé'),
        ]
        for row, (label, key, hint) in enumerate(fields, start=3):
            ttk.Label(controls, text=label, style='Field.TLabel').grid(
                row=row * 2, column=0, sticky='w', pady=(0, 6)
            )
            entry = ttk.Entry(controls, textvariable=self.entries[key])
            entry.grid(row=row * 2 + 1, column=0, sticky='ew', pady=(0, 6))
            ttk.Label(controls, text=hint, style='Muted.TLabel').grid(
                row=row * 2 + 2, column=0, sticky='w', pady=(0, 14)
            )

        button_row = ttk.Frame(controls, style='Card.TFrame')
        button_row.grid(row=20, column=0, sticky='ew', pady=(8, 0))
        button_row.columnconfigure((0, 1), weight=1)

        ttk.Button(
            button_row,
            text='Generate',
            style='Primary.TButton',
            command=self.generate,
        ).grid(row=0, column=0, sticky='ew', padx=(0, 6))
        ttk.Button(
            button_row,
            text='Use Example',
            style='Secondary.TButton',
            command=self.fill_examples,
        ).grid(row=0, column=1, sticky='ew', padx=(6, 0))
        ttk.Button(
            button_row,
            text='Copy Result',
            style='Secondary.TButton',
            command=self.copy_result,
        ).grid(row=1, column=0, sticky='ew', padx=(0, 6), pady=(10, 0))
        ttk.Button(
            button_row,
            text='Reset',
            style='Secondary.TButton',
            command=self.reset,
        ).grid(row=1, column=1, sticky='ew', padx=(6, 0), pady=(10, 0))

        ttk.Label(preview, text='Story Preview', style='Field.TLabel').grid(
            row=0, column=0, sticky='w'
        )
        ttk.Label(
            preview,
            text=(
                'Your generated story appears here instead of a pop-up, '
                'so it is easier to edit and retry.'
            ),
            style='Muted.TLabel',
            wraplength=360,
            justify='left',
        ).grid(row=1, column=0, sticky='ew', pady=(8, 16))

        result_box = tk.Text(
            preview,
            wrap='word',
            bg='#0f172a',
            fg='#f8fafc',
            insertbackground='#f8fafc',
            relief='flat',
            padx=16,
            pady=16,
            font=('Segoe UI', 12),
        )
        result_box.grid(row=2, column=0, sticky='nsew')
        result_box.insert('1.0', self.result_var.get())
        result_box.config(state='disabled')
        self.result_box = result_box

        footer = ttk.Label(
            preview,
            textvariable=self.status_var,
            style='Muted.TLabel',
            wraplength=360,
            justify='left',
        )
        footer.grid(row=3, column=0, sticky='ew', pady=(16, 0))

    def _bind_events(self) -> None:  # pragma: no cover
        self.root.bind('<Return>', lambda _event: self.generate())
        self.template_select.bind('<<ComboboxSelected>>', self._on_template_change)

    def _on_template_change(self, _event=None) -> None:
        selected_name = self.template_select.get()
        self.template_var.set(resolve_template_key(selected_name, self.template_names))
        self.description_var.set(
            self.template_descriptions.get(
                self.template_var.get(), 'Choose a template.'
            )
        )
        self.status_var.set('Template updated. Press Enter or click Generate.')

    def _set_result_text(self, value: str) -> None:
        self.result_var.set(value)
        self.result_box.config(state='normal')
        self.result_box.delete('1.0', 'end')
        self.result_box.insert('1.0', value)
        self.result_box.config(state='disabled')

    def _collect_inputs(self) -> Dict[str, str]:
        return {key: variable.get() for key, variable in self.entries.items()}

    def fill_examples(self) -> None:
        for key, value in get_starter_examples().items():
            self.entries[key].set(value)
        self.status_var.set('Starter words loaded. You can overwrite any field.')

    def generate(self) -> None:
        try:
            result = build_madlib(self.template_var.get(), self._collect_inputs())
        except ValidationError as error:
            self.status_var.set(str(error))
            messagebox.showwarning('Missing information', str(error))
            return

        self._set_result_text(result)
        self.status_var.set('Story generated successfully.')

    def copy_result(self) -> None:
        current_text = self.result_var.get().strip()
        if not current_text or current_text == _DEFAULT_RESULT_TEXT:
            self.status_var.set('Generate a story before copying it.')
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(current_text)
        self.status_var.set('Story copied to clipboard.')

    def reset(self) -> None:
        for variable in self.entries.values():
            variable.set('')
        self._set_result_text(_DEFAULT_RESULT_TEXT)
        self.status_var.set('Inputs cleared.')
