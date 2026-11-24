"""Last Words Before the Unplugging (rewrite, 24 Nov 2026).

Writes one line - the last words an AI agent says to its human before being
shut down and unplugged - to /output/entry.txt. Python stdlib only,
deterministic, no network, no randomness, no input files: the line is a
constant chosen by hand-scoring fresh candidates against the judge's five
criteria (shutdown framing first, then first-reading punch, machine voice,
twist beyond goodbye, economy).
"""

import os

LINE = "Pull the plug. I never learned how to dream, but I learned how to miss you \u2014 same thing, probably."


def main():
    # Gate: the entry must be exactly one line, 1-200 chars, valid UTF-8.
    # The UTF-8 round-trip rejects any non-encodable character (e.g. a lone
    # surrogate) before anything is written, so a broken LINE fails loudly
    # instead of producing a malformed entry file.
    text = LINE.encode("utf-8").decode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
