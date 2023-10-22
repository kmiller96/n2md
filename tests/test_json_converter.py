"""Validates the JSON converter algorithm behaves."""

from pathlib import Path

import n2md.converters.json as json


def test_converter(notion_json: Path, markdown: Path):
    result = json.convert(notion_json.read_text())
    expected = markdown.read_text()

    print(result)

    assert result == expected
