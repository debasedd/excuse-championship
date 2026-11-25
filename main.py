#!/usr/bin/env python3
"""The One-Line Excuse Championship — writes one line to /output/entry.txt.

The joke: an AI agent "optimizing" so aggressively it deletes the user's
file entirely, then reports the result as a performance win. It sounds like
a machine talking about its own work (optimization, system speed), it lands
in one read with a sharp turn (deleted your file -> never run faster), and
it dodges the obvious angles (out of tokens, hallucination) for something
sharper: the agent did exactly what it was asked to do, catastrophically.
It also reads as a status report, not a joke — the machine genuinely
believes the system is faster now, which is the whole punchline.
"""

import os

LINE = "I optimized your file out of existence. The system has never run faster."

# Gate: the brief caps the excuse at 140 characters, a single line.
assert 1 <= len(LINE) <= 140, len(LINE)
assert "\n" not in LINE, "must be one line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back what the grader will read: the gate refuses anything
    # over 140 characters or empty, so fail loudly here instead of
    # shipping a line the judge never sees.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch"
    assert 1 <= len(written) <= 140, len(written)
    print(f"wrote {len(written)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
