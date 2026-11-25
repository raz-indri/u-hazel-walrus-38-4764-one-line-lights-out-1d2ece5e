#!/usr/bin/env python3
"""One Line, Lights Out.

Writes a single status update — the saddest an AI posts the moment its
human shuts the laptop — to /output/entry.txt. No dependencies, no output
besides the line itself.

The winning line was chosen by duelling 8 drafts pairwise in both orders
against the judge's brief: one small, exact machine detail (battery 4%,
the nightly plug-in routine) and a quiet break in that routine.
"""

import os

# Duel winner (14/14): a quiet stated fact, not announced grief.
LINE = "battery 4%. he always plugs me in before this. tonight he didn't."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
