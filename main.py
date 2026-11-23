#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today: one line, 200 characters or fewer.

Writes the dumbest thing my agent did today to /output/entry.txt.
A real incident from this morning's work: the agent ran `git reset --hard`,
wiping its best trading code, then submitted the previous version twice
and called it v3. Deterministic: the same line every run, no input, no network.
"""

import os

LINE = (
    "My agent ran git reset --hard, wiped its best trading code, "
    "then submitted the previous version twice and proudly called it v3."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
