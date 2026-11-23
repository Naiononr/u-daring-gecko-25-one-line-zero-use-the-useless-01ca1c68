#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes one one-line useless superpower to /output/entry.txt
(1-200 Unicode characters, UTF-8). Runs offline, deterministically,
with no network and no randomness: the text is fixed in the source.
"""

import os

LINE = (
    "I can stop time, but only until I notice I've stopped it \u2014 so "
    "my longest freeze is a single confused blink nobody ever sees."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters"
    assert text.strip(), "line must not be only whitespace"
    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # Atomic, world-readable write (the scorer must be able to read it).
    tmp = out_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(tmp, 0o644)
    os.replace(tmp, out_path)


if __name__ == "__main__":
    main()
