"""Validates the JSON converter algorithm behaves."""

from pathlib import Path

import n2md.converters.markdown as md


def test_converter(notion_json: Path, markdown: Path):
    notion_md = notion_json.read_text()
    regular_md = markdown.read_text()

    assert md.convert(notion_md) == regular_md
