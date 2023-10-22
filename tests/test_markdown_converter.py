"""Validates the converter algorithm behaves."""

from textwrap import dedent
from pathlib import Path

import pytest

import n2md.converters.markdown as md


def test_converter(notion_markdown: Path, markdown: Path):
    notion_md = notion_markdown.read_text()
    regular_md = markdown.read_text()

    assert md.convert(notion_md) == regular_md


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
    assert md._remove_extra_stars(original) == clean


def test_fixing_headings():
    original = dedent(
        """
        # Title

        # Heading 1
        ## Heading 2
        ### Heading 3
        """
    ).strip("\n")

    expected = dedent(
        """
        # Title

        ## Heading 1
        ### Heading 2
        #### Heading 3
        """
    ).strip("\n")

    assert md._fix_headings(original) == expected


def test_converting_callouts_to_quotes():
    original = dedent(
        """
        <aside>
        This is a callout.
        </aside>
        """
    ).strip("\n")

    expected = dedent(
        """
        > This is a callout.
        """
    ).strip("\n")

    assert md._convert_callouts_to_quotes(original) == expected


def test_converting_callouts_to_quotes_multiple_times():
    original = dedent(
        """
        <aside>
        This is a callout.
        </aside>
        <aside>
        This is another callout.
        </aside>
        """
    ).strip("\n")

    expected = dedent(
        """
        > This is a callout.
        > This is another callout.
        """
    ).strip("\n")

    assert md._convert_callouts_to_quotes(original) == expected
