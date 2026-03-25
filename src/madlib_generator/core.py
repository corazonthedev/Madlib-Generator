"""Core madlib logic."""

from __future__ import annotations

from typing import Dict

from .templates import STARTER_EXAMPLES, TEMPLATES

_FIELD_ORDER = ('adjective', 'verb1', 'verb2', 'famous_person')
_TEMPLATE_MAP = {template.key: template for template in TEMPLATES}


class ValidationError(ValueError):
    """Raised when required input values are missing."""


def normalize_value(value: str) -> str:
    return ' '.join(value.strip().split())


def validate_inputs(inputs: Dict[str, str]) -> Dict[str, str]:
    cleaned: Dict[str, str] = {}

    for field in _FIELD_ORDER:
        raw_value = inputs.get(field, '')
        cleaned_value = normalize_value(raw_value)
        if not cleaned_value:
            label = field.replace('_', ' ').title()
            raise ValidationError(f'{label} is required.')
        cleaned[field] = cleaned_value

    return cleaned


def build_madlib(template_key: str, inputs: Dict[str, str]) -> str:
    if template_key not in _TEMPLATE_MAP:
        raise KeyError(f'Unknown template: {template_key}')

    cleaned_inputs = validate_inputs(inputs)
    template = _TEMPLATE_MAP[template_key]
    return template.pattern.format(**cleaned_inputs)


def get_template_names() -> Dict[str, str]:
    return {template.key: template.name for template in TEMPLATES}


def get_template_descriptions() -> Dict[str, str]:
    return {template.key: template.description for template in TEMPLATES}


def get_starter_examples() -> Dict[str, str]:
    return dict(STARTER_EXAMPLES)
