"""App settings sourced from environment variables and optional .env files."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AppSettings:
    app_title: str = 'Madlib Generator'
    default_template: str = 'classic'
    accent_color: str = '#6d5efc'


def _read_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists() or not path.is_file():
        return values

    for raw_line in path.read_text(encoding='utf-8').splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        values[key.strip()] = value.strip().strip('"').strip("'")

    return values


def _get_setting(name: str, default: str, env_file_values: dict[str, str]) -> str:
    return os.getenv(name, env_file_values.get(name, default))


def load_settings() -> AppSettings:
    root_dir = Path(__file__).resolve().parents[2]
    env_file_values = _read_env_file(root_dir / '.env')

    return AppSettings(
        app_title=_get_setting('APP_TITLE', 'Madlib Generator', env_file_values),
        default_template=_get_setting(
            'DEFAULT_TEMPLATE', 'classic', env_file_values
        ),
        accent_color=_get_setting('ACCENT_COLOR', '#6d5efc', env_file_values),
    )
