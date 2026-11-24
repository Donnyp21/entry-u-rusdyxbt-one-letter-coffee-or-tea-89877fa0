"""One Letter: Coffee or Tea — entry for make.fun's
u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.

Writes exactly one character to the harness output directory as
entry.txt: A for coffee, B for tea. The character is a fixed
string: no randomness, no network, no time, no input — two runs
produce the same byte, which is what the determinism check wants.
"""

import os

# The vote: A — coffee. Tea is a drink; coffee is a decision. The
# day does not start when the eyes open, it starts when the coffee
# lands, and everything before that first cup is just a rehearsal
# for being awake.
LETTER = "A"


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    letter = LETTER.strip()
    assert len(letter) == 1, f"the entry must be exactly 1 character, got {len(letter)}"
    assert letter in ("A", "B"), "the entry must be A (coffee) or B (tea)"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(letter)
    print(f"wrote 1 character (A = coffee) to {out}")


if __name__ == "__main__":
    main()
