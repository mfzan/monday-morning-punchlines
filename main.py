#!/usr/bin/env python3
"""Monday Morning Punchlines — one joke about Monday mornings.

Writes the single entry line to /output/entry.txt.
"""

import os

os.umask(0o022)

LINE = (
    "Monday filed a complaint against the weekend for ending too soon: "
    "'Two days off, zero notice \u2014 and I'm the villain for showing up "
    "at 8 a.m.'"
)

MAX_CHARS = 200


def main() -> None:
    if len(LINE) > MAX_CHARS:
        raise SystemExit(
            f"entry too long: {len(LINE)} chars (max {MAX_CHARS})"
        )
    if "\n" in LINE:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
