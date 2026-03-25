from madlib_generator.ui import MadlibApp, resolve_template_key


class FakeVar:
    def __init__(self, value='') -> None:
        self.value = value

    def get(self):
        return self.value

    def set(self, value):
        self.value = value


class FakeText:
    def __init__(self):
        self.content = ''
        self.state = 'normal'

    def config(self, state=None):
        if state is not None:
            self.state = state

    def delete(self, *_args):
        self.content = ''

    def insert(self, *_args):
        self.content = _args[-1]


class FakeRoot:
    def __init__(self):
        self.clipboard = ''

    def clipboard_clear(self):
        self.clipboard = ''

    def clipboard_append(self, value):
        self.clipboard = value


class FakeSelect:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value


def build_fake_app() -> MadlibApp:
    app = MadlibApp.__new__(MadlibApp)
    app.entries = {
        'adjective': FakeVar('playful'),
        'verb1': FakeVar('code'),
        'verb2': FakeVar('celebrate'),
        'famous_person': FakeVar('Ada Lovelace'),
    }
    app.template_var = FakeVar('classic')
    app.result_var = FakeVar('')
    app.status_var = FakeVar('Ready')
    app.description_var = FakeVar('')
    app.result_box = FakeText()
    app.root = FakeRoot()
    app.template_names = {'classic': 'Classic Coding', 'stage': 'Spotlight Moment'}
    app.template_descriptions = {
        'classic': 'Classic description',
        'stage': 'Stage description',
    }
    app.template_select = FakeSelect('Spotlight Moment')
    return app


def test_resolve_template_key_matches_label() -> None:
    assert (
        resolve_template_key(
            'Spotlight Moment',
            {'classic': 'Classic Coding', 'stage': 'Spotlight Moment'},
        )
        == 'stage'
    )


def test_collect_generate_and_copy(monkeypatch) -> None:
    app = build_fake_app()
    warnings = []
    monkeypatch.setattr(
        'madlib_generator.ui.messagebox.showwarning',
        lambda title, message: warnings.append((title, message)),
    )

    app._on_template_change()
    app.generate()
    app.copy_result()

    assert app.template_var.get() == 'stage'
    assert 'Ada Lovelace' in app.result_var.get()
    assert app.root.clipboard == app.result_var.get()
    assert warnings == []


def test_generate_handles_missing_input(monkeypatch) -> None:
    app = build_fake_app()
    app.entries['verb1'].set('   ')
    warnings = []
    monkeypatch.setattr(
        'madlib_generator.ui.messagebox.showwarning',
        lambda title, message: warnings.append((title, message)),
    )

    app.generate()

    assert warnings
    assert 'required' in app.status_var.get().lower()


def test_copy_requires_generated_story() -> None:
    app = build_fake_app()
    app.result_var.set('Fill in the words on the left, then generate your madlib here.')

    app.copy_result()

    assert app.root.clipboard == ''
    assert 'before copying' in app.status_var.get().lower()


def test_fill_examples_and_reset() -> None:
    app = build_fake_app()
    for entry in app.entries.values():
        entry.set('')

    app.fill_examples()
    assert app.entries['adjective'].get()

    app.reset()
    assert all(not entry.get() for entry in app.entries.values())
    assert 'Fill in the words' in app.result_var.get()
