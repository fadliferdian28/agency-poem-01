#!/usr/bin/env python3
"""Two Sugars (v6.2) — a poem about agency, memory, and a husband's tea.

Writes the poem to entry.txt in the output directory. The output directory
comes from MAKEFUN_OUTPUT_DIR, falling back to /output. The file holds
exactly the poem: lines joined with newlines, no trailing newline.
"""

import os
from pathlib import Path

POEM_LINES = [
    "Two Sugars",
    "",
    "I help her sit up.",
    "The screen lights up beside her bed.",
    '"This is your husband. Married forty-three years."',
    "She looks at me. She looks at the screen.",
    "Her eyes move past us both.",
    "",
    "It shows her face at twenty. 'This is you,'",
    "it says. She looks at the girl. She shakes her head.",
    "She folds her hands. She waits for it to stop.",
    "",
    "I sit beside her. The agent dims its screen.",
    "It waits in the corner,",
    "its screen dark. I take her hand.",
    "Her hand is cold. I warm it between mine.",
    "",
    "I make her tea. I have made it",
    "for forty-three years. Two sugars, three stirs,",
    "too hot, in the chipped cup she always chose.",
    "The agent measures the water,",
    "the temperature, the leaves.",
    "The kettle is warm in my hand.",
    "",
    "I put the cup in her hands. She holds it",
    "the way she always held it, both hands round,",
    "and breathes the steam.",
    "Her fingers find the chip. She looks up.",
    "Her eyes find mine.",
    "Then she looks down. She drinks the tea.",
]


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    poem = "\n".join(POEM_LINES)
    if not 1 <= len(poem) <= 1000:
        raise ValueError("poem must be 1-1000 characters")
    (out_dir / "entry.txt").write_text(poem, encoding="utf-8")


if __name__ == "__main__":
    main()
