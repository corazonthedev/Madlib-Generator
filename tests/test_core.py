import pytest

from madlib_generator.core import (
    ValidationError,
    build_madlib,
    get_starter_examples,
    get_template_names,
    validate_inputs,
)

VALID_INPUTS = {
    'adjective': ' playful ',
    'verb1': ' code ',
    'verb2': ' celebrate ',
    'famous_person': ' Ada Lovelace ',
}


def test_validate_inputs_trims_values() -> None:
    cleaned = validate_inputs(VALID_INPUTS)
    assert cleaned == {
        'adjective': 'playful',
        'verb1': 'code',
        'verb2': 'celebrate',
        'famous_person': 'Ada Lovelace',
    }


@pytest.mark.parametrize('field', ['adjective', 'verb1', 'verb2', 'famous_person'])
def test_validate_inputs_rejects_missing_fields(field: str) -> None:
    broken = dict(VALID_INPUTS)
    broken[field] = '   '

    with pytest.raises(ValidationError):
        validate_inputs(broken)


def test_build_madlib_classic_template() -> None:
    result = build_madlib('classic', VALID_INPUTS)
    assert result == (
        'Computer programming is so playful! It makes me excited all the time '
        'because I love to code. Stay hydrated and celebrate like you are Ada Lovelace!'
    )


def test_build_madlib_rejects_unknown_template() -> None:
    with pytest.raises(KeyError):
        build_madlib('missing-template', VALID_INPUTS)


def test_metadata_helpers_are_available() -> None:
    names = get_template_names()
    examples = get_starter_examples()

    assert names['classic'] == 'Classic Coding'
    assert examples['famous_person']
