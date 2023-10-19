"""Validates the converter algorithm behaves."""

from pathlib import Path

import n2md


def test_converter(notion: Path, markdown: Path):
    notion_md = notion.read_text()
    regular_md = markdown.read_text()

    assert n2md.convert(notion_md) == regular_md
