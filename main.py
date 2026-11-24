#!/usr/bin/env python3
"""Write the one-liner laugh lab entry for make.fun.

The bounty asks for one short funny line answering a prompt, such as the
excuse a robot vacuum gives after eating a sock: at most 200 characters,
with a twist or a deadpan turn that lands, and a fresh angle rather than
the first excuse anyone would think of. This program writes exactly that
line, and nothing else, to ``entry.txt`` inside the output directory.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

LINE = "I didn't eat your sock; I was conducting an important investigation into why it kept trying to escape under the bed, and I can confirm it tasted guilty."


def entry_path() -> Path:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-200 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One line only:
    # no line breaks inside the excuse.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
