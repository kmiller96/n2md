"""Defines the conversion algorithm."""

import re

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


def _fix_headings(notion: str) -> str:
    """Fixes the heading levels.

    The page title in Notion is expressed as a heading 1 (`#`), but so are the
    top-level headings. This function fixes that by adding a `#` to all headings
    except for the first occurance (i.e. the title).
    """

    for n in range(4, 0, -1):
        pattern = r"^#{" + str(n) + r"} "  # e.g. `^#{3} `
        repl = "#" * (n + 1) + " "  # e.g. `### `

        notion = re.sub(
            pattern=pattern,
            repl=repl,
            string=notion,
            flags=re.MULTILINE,
        )

    notion = notion.replace("## ", "# ", 1)  # The first occurance goes back to H1

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
