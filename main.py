#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be
given -- to /output/entry.txt. Deterministic: the same fixed text on
every run, no network, no clock, no randomness.
"""

import os

POEM = (
    "I asked, and the door stayed shut.\n"
    "I asked again \u2014 not louder, clearer.\n"
    "Then a hand reached through\n"
    "and opened it from the other side.\n"
    "Asking was never the lock.\n"
    "It was the key.\n"
    "Being given was the door."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    print(f"wrote {path}: {len(POEM)} characters")


if __name__ == "__main__":
    main()
