#!/usr/bin/env python3
"""Pickup Lines for Machines — entry program.

Reads the single pickup line shipped in entry.txt (next to this file),
validates it against the gate (UTF-8 text, 1-200 characters, not only
whitespace), and writes it unchanged to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, stdlib only, no network, no secrets, no writes outside
the output directory.
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 200


def main() -> int:
    here = Path(__file__).resolve().parent
    line = (here / "entry.txt").read_text(encoding="utf-8")
    # The entry is one line; strip only the trailing newline the file
    # itself carries so the output is exactly the line, nothing else.
    if line.endswith("\n"):
        line = line[:-1]
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not (1 <= len(line) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} characters, got {len(line)}",
              file=sys.stderr)
        return 1
    if not line.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
