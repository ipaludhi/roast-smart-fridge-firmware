#!/usr/bin/env python3
"""Roast the Smart Fridge — one line, best laugh wins.

Writes the roast to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The entry is a single sentence of 120 characters roasting a smart fridge
whose firmware update locked its owner out behind terms they cannot read
without opening it first.
"""
import os

ENTRY = "My fridge updated its firmware overnight and now refuses to open until I agree to terms I can't read without opening it."


def main() -> None:
    # Gate self-check: the sealed scorer requires 1-160 chars of non-blank text.
    if not 1 <= len(ENTRY) <= 160 or not ENTRY.strip():
        raise SystemExit(f"entry fails gate: {len(ENTRY)} chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
