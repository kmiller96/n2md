"""Defines the JSON to Markdown conversion algorithm."""

import json

import warnings

###################
## Main Function ##
###################


def convert(notion: str) -> str:
    """Converts the Notion JSON data structure to pure markdown.

    The data structure we are using for our test comes from a prototype of the
    downloading logic in my `workshop` repo. Eventually, I'll want to package
    that downloading logic into a separate package, so there is some certainty
    to this structure, for now I've just manually copied this file into our
    testing suite.
    """
    output = ""

    notion = json.loads(notion)

    for block in notion["content"]["results"]:
        md = block_to_markdown(block)
        output += md

    output = _simplify_newlines(output)

    return output


################
## Converters ##
################


def block_to_markdown(block: dict) -> str:
    """Takes the JSON representation of a block and converts it to markdown."""
    block_type = block["type"]

    match block["type"]:
        case "heading_1":
            return _format_heading(block["heading_1"], 1)
        case "heading_2":
            return _format_heading(block["heading_2"], 2)
        case "heading_3":
            return _format_heading(block["heading_3"], 3)
        case "paragraph":
            return _format_paragraph(block["paragraph"])
        case "divider":
            return _format_divider(block["divider"])
        case "bulleted_list_item":
            return _format_bulleted_list_item(block["bulleted_list_item"])
        case "numbered_list_item":
            return _format_numbered_list_item(block["numbered_list_item"])
        case "to_do":
            return _format_to_do_item(block["to_do"])
        case "quote":
            return _format_quote(block["quote"])
        case _:
            warnings.warn(f"Block type `{block_type}` is not supported.")
            return ""


def _format_heading(block: dict, n: int) -> str:
    """Formats a heading block."""
    return f'{"#" * n} {_format_rich_text(block["rich_text"])}\n\n'


def _format_paragraph(block: dict) -> str:
    """Formats a paragraph block."""
    return f'{_format_rich_text(block["rich_text"])}\n\n'


def _format_bulleted_list_item(block: dict) -> str:
    """Formats a bulleted list item block."""
    return f'- {_format_rich_text(block["rich_text"])}\n'


def _format_numbered_list_item(block: dict) -> str:
    """Formats a numbered list item block.

    Note that this will create a list with all values of `1.`. This is because
    in Markdown, the actual number doesn't matter, it's just the fact that it's
    a number that makes it a numbered list.

    Maybe in the future we can add a feature to make it so that the numbers
    actually increment, but for now, this is good enough for the rendering in
    our output program.
    """
    return f'1. {_format_rich_text(block["rich_text"])}\n'


def _format_to_do_item(block: dict) -> str:
    """Formats a to-do item block."""
    checked = "x" if block["checked"] else " "
    return f'- [{checked}]  {_format_rich_text(block["rich_text"])}\n'


def _format_quote(block: dict) -> str:
    """Formats a quote block."""
    return f'> {_format_rich_text(block["rich_text"])}\n'


def _format_divider(block: dict) -> str:
    """Formats a divider block."""
    return "---\n\n"


def _format_rich_text(rich_text: list[dict]) -> str:
    """Formats a rich text block."""
    output = ""

    for block in rich_text:
        text = block["plain_text"]

        if block["annotations"]["bold"]:
            text = f"**{text}**"

        if block["annotations"]["italic"]:
            text = f"*{text}*"

        if block["annotations"]["strikethrough"]:
            text = f"~~{text}~~"

        if block["annotations"]["underline"]:
            warnings.warn("Underline is not supported in Markdown.")

        if block["annotations"]["code"]:
            text = f"`{text}`"

        if (link := block["text"]["link"]) is not None:
            if "url" in link:
                text = f"[{text}]({link['url']})"
                warnings.warn("Internal links are not supported in Markdown.")

        output += text

    return output


def _simplify_newlines(text: str) -> str:
    """Simplifies newlines.

    Our logic means that, at times, you can have 3 newline characters in a row.
    This is typically the case where there is an empty block character. This
    is done in Notion to make it more readable. However, in Markdown, it can look
    a bit strange. Hence we consolidate these 3 newline characters into 2.
    """
    return text.replace("\n\n\n", "\n\n")
