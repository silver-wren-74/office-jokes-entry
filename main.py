#!/usr/bin/env python3
"""Write one original office joke to /output/entry.txt.

Competition: Make the AI Judge Laugh: Office Jokes.
The gate requires UTF-8 text of 1 to 199 characters, not only whitespace.
"""

import os

JOKE = (
    "I replied all begging everyone to stop replying all; 412 people replied "
    "all to agree, three attached files, and it is now our best-attended "
    "weekly meeting."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
