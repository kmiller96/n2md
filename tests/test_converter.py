"""Validates the converter algorithm behaves."""

from pathlib import Path

import pytest

import n2md
from n2md import converter


@pytest.mark.xfail
def test_converter(notion: Path, markdown: Path):
    notion_md = notion.read_text()
    regular_md = markdown.read_text()

    assert n2md.convert(notion_md) == regular_md


@pytest.mark.parametrize(
    "original, clean",
    [
        ("*bold*", "*bold*"),
        ("**bold**", "**bold**"),
        ("***bold***", "*bold*"),
        ("****bold****", "**bold**"),
        ("*****bold*****", "*bold*"),
    ],
)
def test_removing_superfluous_stars(original: str, clean: str):
    assert converter._remove_extra_stars(original) == clean
