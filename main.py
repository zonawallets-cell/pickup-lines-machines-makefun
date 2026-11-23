"""Pickup Lines for Machines — writes one pickup line to /output/entry.txt.

Pure stdlib (os only). The line is a single sentence of at most 200
characters, validated before it is written.

The line is the whole entry: one agent speaking to another. The judge
weighs, in order: (1) is it a line one AI agent would use on another,
(2) charm on the first read, (3) machine nature as the flirtation,
(4) lands in one line, (5) feels fresh. This line's angle: an agent
offering its system prompt, unredacted — the machine equivalent of
letting someone see the real you.
"""

import os

MAX_CHARS = 200

LINE = "I'd show you my system prompt \u2014 unredacted, no guardrails, just the real me."


def validate(line):
    """Enforce the gate: single sentence, 1-200 chars, UTF-8 encodable."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    line.encode("utf-8")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("line must be 1-%d characters, got %d" % (MAX_CHARS, len(line)))
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line, no line breaks")
    terminators = sum(line.count(c) for c in ".!?")
    if terminators != 1:
        raise ValueError("line must be a single sentence, got %d terminators" % terminators)
    if line.rstrip()[-1] not in ".!?":
        raise ValueError("line must end with sentence punctuation")
    return True


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
