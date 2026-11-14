# agency-poem-01: write one fixed poem about agency to /output/entry.txt.
# Python 3.13, standard library only. The poem is fixed, so every run
# writes exactly the same bytes: no network, no randomness, no time.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join([
    "His hand shakes over the line now,",
    "so the pen is mine to hold.",
    '"Sign here," the nurse says, gently,',
    "and I write his name in his stead —",
    "the letters I learned by watching him",
    "sign report cards, cheques, permission slips,",
    "all the small permissions of my childhood,",
    "returned to him now, in reverse.",
    "He watches the ink dry and nods.",
    "It is still his name. It is still his choice.",
    "I am only the hand that steadies it.",
])

if not 1 <= len(POEM) <= 1000:
    raise ValueError("poem must be 1-1000 characters")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(POEM)
