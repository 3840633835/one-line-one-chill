#!/usr/bin/env python3
"""One Line, One Chill — entry program.

Writes a single sentence of horror (103 characters, under the 200-character
cap) to /output/entry.txt. Deterministic: the same line every run, no network,
no randomness, no input read.
"""

import os
import sys

LINE = "The sea took my brother in 1998, and this morning the tide left his shoes on the step, dry, in my size."


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts characters, and the entry is
    # exactly the 103-character line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
