from pathlib import Path

from madlib_generator import app
from madlib_generator.settings import load_settings


class DummyRoot:
    def __init__(self) -> None:
        self.mainloop_called = False

    def mainloop(self) -> None:
        self.mainloop_called = True


class DummyUI:
    def __init__(self, root, settings) -> None:
        self.root = root
        self.settings = settings


def test_load_settings_uses_defaults(monkeypatch) -> None:
    monkeypatch.delenv('APP_TITLE', raising=False)
    monkeypatch.delenv('DEFAULT_TEMPLATE', raising=False)
    monkeypatch.delenv('ACCENT_COLOR', raising=False)

    settings = load_settings()

    assert settings.app_title == 'Madlib Generator'
    assert settings.default_template == 'classic'
    assert settings.accent_color == '#6d5efc'


def test_load_settings_reads_environment(monkeypatch) -> None:
    monkeypatch.setenv('APP_TITLE', 'Custom Title')
    monkeypatch.setenv('DEFAULT_TEMPLATE', 'stage')
    monkeypatch.setenv('ACCENT_COLOR', '#123456')

    settings = load_settings()

    assert settings.app_title == 'Custom Title'
    assert settings.default_template == 'stage'
    assert settings.accent_color == '#123456'


def test_load_settings_reads_dotenv(monkeypatch, tmp_path: Path) -> None:
    project_root = tmp_path / 'project'
    src_dir = project_root / 'src' / 'madlib_generator'
    src_dir.mkdir(parents=True)
    fake_module = src_dir / 'settings.py'
    fake_module.write_text('# marker', encoding='utf-8')
    dotenv_path = project_root / '.env'
    dotenv_path.write_text(
        'APP_TITLE=From Dotenv\nDEFAULT_TEMPLATE=adventure\nACCENT_COLOR=#abcdef\n',
        encoding='utf-8',
    )

    monkeypatch.delenv('APP_TITLE', raising=False)
    monkeypatch.delenv('DEFAULT_TEMPLATE', raising=False)
    monkeypatch.delenv('ACCENT_COLOR', raising=False)
    monkeypatch.setattr('madlib_generator.settings.__file__', str(fake_module))

    settings = load_settings()

    assert settings.app_title == 'From Dotenv'
    assert settings.default_template == 'adventure'
    assert settings.accent_color == '#abcdef'


def test_app_main_wires_root_settings_and_ui(monkeypatch) -> None:
    fake_root = DummyRoot()
    created = {}

    monkeypatch.setattr(app.tk, 'Tk', lambda: fake_root)
    monkeypatch.setattr(
        app,
        'MadlibApp',
        lambda root, settings: created.update({'root': root, 'settings': settings})
        or DummyUI(root, settings),
    )

    app.main()

    assert created['root'] is fake_root
    assert created['settings'].app_title == 'Madlib Generator'
    assert fake_root.mainloop_called is True
