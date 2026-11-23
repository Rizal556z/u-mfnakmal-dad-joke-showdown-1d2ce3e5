#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes a single original dad joke to /output/entry.txt.
Pure Python standard library, no network, no clock, no randomness:
two runs write byte-identical files.
"""

import os

JOKE = (
    "People ask how I afford three kids. Easy \u2014 I just keep raising "
    "them: the cost, the noise, and my blood pressure."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
