"""Madlib templates and starter examples."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class MadlibTemplate:
    key: str
    name: str
    description: str
    pattern: str


TEMPLATES: List[MadlibTemplate] = [
    MadlibTemplate(
        key='classic',
        name='Classic Coding',
        description='A polished version of the original programming-themed madlib.',
        pattern=(
            'Computer programming is so {adjective}! It makes me excited all the '
            'time because I love to {verb1}. Stay hydrated and {verb2} like you '
            'are {famous_person}!'
        ),
    ),
    MadlibTemplate(
        key='adventure',
        name='Adventure Quest',
        description='A playful fantasy-style story for more expressive results.',
        pattern=(
            'On a wildly {adjective} journey, I had to {verb1} before sunset. '
            'Then I remembered the advice of {famous_person}: always {verb2} '
            'when the mission gets strange.'
        ),
    ),
    MadlibTemplate(
        key='stage',
        name='Spotlight Moment',
        description='A stage-and-performance version for more dramatic outputs.',
        pattern=(
            'The crowd went {adjective} the second I started to {verb1}. Even '
            '{famous_person} would be impressed if they saw me {verb2} '
            'under the lights.'
        ),
    ),
]


STARTER_EXAMPLES: Dict[str, str] = {
    'adjective': 'brilliant',
    'verb1': 'prototype',
    'verb2': 'celebrate',
    'famous_person': 'Ada Lovelace',
}
