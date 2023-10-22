"""Collection of common functions used by all converters."""

import re


def simplify_newlines(text: str) -> str:
    """Simplifies newlines.

    Our logic means that, at times, you can have 3 newline characters in a row.
    This is typically the case where there is an empty block character. This
    is done in Notion to make it more readable. However, in Markdown, it can look
    a bit strange. Hence we consolidate these 3 newline characters into 2.

    We also normalise the file to only have a single trailing newline character
    at the end of the file.
    """
    return re.sub(r"\n{3,}", "\n\n", text).strip("\n") + "\n"


def fix_headings(notion: str) -> str:
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
