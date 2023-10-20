"""Defines the conversion algorithm."""

import re

###################
## Main Function ##
###################


def convert(notion: str) -> str:
    """Converts Notion export to pure Markdown."""
    return notion  # TODO


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
