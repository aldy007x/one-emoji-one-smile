"""One Emoji, One Smile — entry program.

Writes exactly one emoji to /output/entry.txt: nothing else, no words,
no caption, no explanation.

The emoji: U+1FAF6 HEART HANDS.

Why this one, against the judge's brief (most important first):

1. It plainly aims to warm a stranger. Heart hands is a gesture of
   warmth offered outward — "here, this is for you" — not a face
   describing its own mood.
2. Warmth at first glance. The shape is a heart made by two hands:
   readable in a split second, kind and gently playful, no context
   needed.
3. Universality. The hand-heart gesture is understood across ages and
   backgrounds, with no irony, in-joke, or slang that could land wrong.
4. Chosen, not default. It is not the first smiley that comes to mind
   (the plain smiling face every entry reaches for); it feels picked
   for this moment while staying instantly readable.
5. Right for a stranger. It carries gratitude and goodwill, not
   romance, flirtation, or physical intimacy — nothing that would read
   oddly coming from someone unknown. A hug face offers a hug; a
   smiling face with hearts offers affection; heart hands offers a
   small gift of warmth, which is exactly what a stranger can accept.
"""

import os

EMOJI = "\U0001faf6"  # 🫶 HEART HANDS

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Self-check against the bounty gate: /output/entry.txt must be
    # UTF-8 text of 1 to 8 characters, not only white space. Fail loudly
    # here rather than shipping an invalid entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if len(written) != 1 or not written.strip():
        raise SystemExit(f"invalid entry text: {written!r}")


if __name__ == "__main__":
    main()
