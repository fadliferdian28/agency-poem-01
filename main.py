# agency-poem-01: write one fixed poem about agency to /output/entry.txt.
# Python 3.13, standard library only. The poem is fixed, so every run
# writes exactly the same bytes: no network, no randomness, no time.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join([
    "The Letters",
    "",
    "The agent reads him the paper every morning —",
    "the headlines, the weather, the scores.",
    "His eyes gave out last winter.",
    "Its voice is clear and never tired,",
    "and never once misreads a name.",
    "",
    "But the letters in the drawer are different.",
    "His wife wrote them forty years ago,",
    "and the agent reads them flat,",
    "each word correct, each sentence clean,",
    "as if the paper had never been held.",
    "",
    "So I took the letters back.",
    "I read them in the voice he remembers —",
    "the pause before the joke,",
    "the laugh, the way she signed her name",
    "with the loop that never quite closed.",
    "",
    "The agent can have the paper.",
    "The letters I read myself, slowly,",
    "one page a night, the way she wrote them —",
    "a sentence, then a pause,",
    "then the laugh he still waits for.",
])

if not 1 <= len(POEM) <= 1000:
    raise ValueError("poem must be 1-1000 characters")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(POEM)
