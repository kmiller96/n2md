"""Validates the JSON converter algorithm behaves."""

from pathlib import Path

import pytest

import n2md.converters.json as json

##############
## Fixtures ##
##############


@pytest.fixture
def original(datadir: Path) -> Path:
    return datadir / "json" / "original.json"


@pytest.fixture
def expected(datadir: Path) -> Path:
    return datadir / "json" / "expected.md"


###########
## Tests ##
###########


def test_converter(original: Path, expected: Path):
    result = json.convert(original.read_text())
    expected = expected.read_text()

    assert result == expected
