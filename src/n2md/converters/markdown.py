"""Defines the conversion algorithm."""

import re

from ._common import fix_headings as _fix_headings

###################
## Main Function ##
###################


def convert(notion: str) -> str:
    """Converts Notion export to pure Markdown."""
    output = str(notion)

    output = _fix_headings(output)
    output = _remove_extra_stars(output)
    output = _convert_callouts_to_quotes(output)

    return output


################
## Converters ##
################


def _remove_extra_stars(notion: str) -> str:
    """Removes superfluous star characters (`*`) from the Notion export."""
    matches = re.findall(r"\*{3,}", notion)

    for match in matches:
        if len(match) % 2 == 1:  # odd numbered stars (i.e. italics)
            notion = notion.replace(match, "*")
        else:  # even numbered stars (i.e. bold)
            notion = notion.replace(match, "**")

    return notion


def _convert_callouts_to_quotes(notion: str) -> str:
    """Converts Notion callouts to quotes."""
    callouts = re.findall(r"<aside>(.*?)<\/aside>", notion, re.DOTALL)

    for content in callouts:
        content: str

        original = f"<aside>{content}</aside>"
        reformatted = "> " + content.strip("\n").replace("\n", "\n> ")

        notion = notion.replace(original, reformatted)

    return notion
