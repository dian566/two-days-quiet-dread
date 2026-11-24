#!/usr/bin/env python3
"""Two Days of Quiet Dread entry for make.fun: one code review comment."""

# The line below is fixed by the bounty brief; this program only writes it out.

from os import makedirs

DREAD = (
    "LGTM. The tests pass, the diff is clean, and none of that will "
    "matter when this code outlives us both."
)


def write_dread() -> None:
    """Write the review comment to /output/entry.txt, nothing else."""
    if len(DREAD) > 140 or not DREAD.strip():
        raise ValueError("entry must be a non-empty line of at most 140 characters")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(DREAD)


if __name__ == "__main__":  # run as a script
    write_dread()
