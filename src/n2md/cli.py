"""Defines the main execution routines for the n2md CLI."""

from pathlib import Path

import typer

from n2md import converters

cli = typer.Typer()


@cli.command()
def main(infile: Path, outfile: Path):
    """Converts Notion export to pure Markdown."""
    notion = infile.read_text()
    markdown = converters.markdown.convert(notion)
    outfile.write_text(markdown)
