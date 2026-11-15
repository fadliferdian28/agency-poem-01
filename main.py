# "The Salt" (v7) — a poem about agency, memory, and a grandmother's recipe.
# The agent has every gram and every second. The human has the dish.
# The agent speaks twice, then does not act. The restraint is the gift.
# Top-10 pattern: agent restraint as care, role inversion, concrete detail,
# one repeated phrase, no slogan. First person, one scene, ~830 bytes.

import os
import sys

POEM_LINES = [
    "The Salt",
    "",
    "The agent has the recipe.",
    "Every gram. Every second.",
    "It watched her cook it forty years,",
    "from the camera in the corner.",
    "",
    "I stand at the stove. The pot is hers.",
    "The spoon is hers. My hands are not",
    "her hands. The salt is in my hand.",
    "",
    '"Two grams," the agent says.',
    "I pour. I do not measure.",
    "The salt falls the way it fell",
    "when she stood here. When she poured.",
    "",
    '"Too much," the agent says.',
    "It does not stop my hand.",
    "It knows the number. It knows",
    "the number is not the dish.",
    "",
    "I stir. The steam rises.",
    "It smells like her kitchen.",
    "It smells like Sunday. It smells",
    "like the house before she died.",
    "",
    "The agent dims its light.",
    "It does not correct me.",
    "It does not say the word again.",
    "It waits. It lets me finish.",
    "",
    "I taste. The salt is wrong.",
    "The salt is right. It tastes like her.",
    "It tastes like forty years",
    "of Sundays. I eat standing up.",
]

def main():
    poem = "\n".join(POEM_LINES)
    if not 1 <= len(poem) <= 1000:
        print(f"length {len(poem)} out of range", file=sys.stderr)
        sys.exit(1)
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(poem)

if __name__ == "__main__":
    main()
