#!/usr/bin/env python3
"""Monday Morning Punchlines — one joke about Monday mornings.

The joke casts Monday as a person with a grudge who files a formal
complaint against the weekend. The line is assembled from its parts
(setup, charge, quoted grievance) so each piece can be checked, then
the finished line is validated and written to /output/entry.txt.
"""

import os

os.umask(0o022)

MAX_CHARS = 200

SETUP = "Monday filed a complaint against the weekend for ending too soon"
CHARGE = "Two days off, zero notice"
PUNCHLINE = "and I'm the villain for showing up at 8 a.m."


def build_line() -> str:
    """Assemble the single joke line from its parts."""
    grievance = f"'{CHARGE} \u2014 {PUNCHLINE}'"
    return f"{SETUP}: {grievance}"


def validate(line: str) -> None:
    """Fail loudly if the line breaks the bounty rules."""
    if not line:
        raise SystemExit("entry line is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry too long: {len(line)} chars (max {MAX_CHARS})"
        )


def main() -> None:
    line = build_line()
    validate(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
