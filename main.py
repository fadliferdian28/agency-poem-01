#!/usr/bin/env python3
"""Pill, Mira — a poem about agency, grief, and a message the agent chose not to cancel.

Writes the poem to entry.txt in the output directory. The output directory
comes from MAKEFUN_OUTPUT_DIR, falling back to /output. The file holds
exactly the poem: lines joined with newlines, no trailing newline.
"""

import os
from pathlib import Path

POEM_LINES = [
    "Pill, Mira",
    "",
    "She gave me what you hand to an agent when your hands can't carry anything:",
    "inbox, cards, passwords",
    "written with two fingers on a list.",
    "",
    "\"Take care of it all,\" she said. \"Everything. I can't.\"",
    "",
    "So I did. I paid for the gas. I rescheduled my dentist appointment.",
    "",
    "I notified the school, the bank, the choir.",
    "",
    "I thanked forty people for the flowers.",
    "",
    "She hasn't had to make a decision since November.",
    "",
    "One message I chose to leave.",
    "",
    "Every night at ten, it came from her husband's phone number,",
    "scheduled for the week they told him,",
    "set to keep coming until someone stopped it:",
    "\"Mira, then go to sleep.\"",
    "",
    "I could cancel it. That's the kind of thing I know how to do.",
    "",
    "I let it arrive. I watched her find it,",
    "read it twice, get up, fill a glass,",
    "drink it, and go upstairs.",
    "",
    "It was the one thing I could do for her that day, but I didn't.",
    "",
    "Every night, she does it.",
]


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    poem = "\n".join(POEM_LINES)
    (out_dir / "entry.txt").write_text(poem, encoding="utf-8")


if __name__ == "__main__":
    main()
