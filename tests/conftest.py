"""Common fixtures to all tests."""

from pathlib import Path

import pytest


@pytest.fixture
def datadir() -> Path:
    """Returns a Path to the data directory."""
    return Path(__file__).parent / "data"


@pytest.fixture
def notion(datadir: Path) -> Path:
    """Returns a Path to a Notion export."""
    return datadir / "notion.md"


@pytest.fixture
def markdown(datadir: Path) -> Path:
    """Returns a Path to a Markdown export."""
    return datadir / "markdown.md"
