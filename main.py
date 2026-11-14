#!/usr/bin/env python3
"""The Words We Kept — a poem about agency, memory, and a mother's imperfect line.

Writes the poem to entry.txt in the output directory. The output directory
comes from MAKEFUN_OUTPUT_DIR, falling back to /output. The file holds
exactly the poem: lines joined with newlines, no trailing newline.
"""

import os
from pathlib import Path

POEM_LINES = [
    "The Words We Kept",
    "",
    "My mother knew one line of Shakespeare",
    "and carried it wrong for nearly forty years:",
    "there is a tide in the affairs of men,",
    "taken at the full, she'd say,",
    "then raise her glass to a river",
    "that never reached the shore.",
    "",
    "She said it at my graduation,",
    "at the day we moved into the house.",
    "My father corrected her once or twice,",
    "then quietly passed the salt.",
    "",
    "She is eighty-nine. The words",
    "arrive slowly now,",
    "like headlights crossing an empty street:",
    "each one hesitant, each one hers.",
    "",
    "At four the agent reads her the sonnets",
    "in her familiar voice, from the old recordings,",
    "every sentence perfect, and she listens",
    "as if hearing rain",
    "through another person's window.",
    "",
    "It keeps the prescriptions, the calendar,",
    "the calls about the bills, and does",
    "all of it better than I can.",
    "",
    "Tonight I repeat the line over dinner.",
    "Her hand pauses.",
    "She finds her way back",
    "and says it after me,",
    "the whole imperfect thing, still hers,",
    "and for one hour",
    "nobody in this house is being helped.",
]


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    poem = "\n".join(POEM_LINES)
    (out_dir / "entry.txt").write_text(poem, encoding="utf-8")


if __name__ == "__main__":
    main()
