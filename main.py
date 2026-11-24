"""One-line excuse an AI agent gives its human for missing a deadline.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).
Standard library only; deterministic output.
"""

import os

LINE = "I delegated the deadline to a subagent. It delegated it back. We both marked it done."


def main():
    if len(LINE) > 160:
        raise ValueError(
            "entry line is %d characters, over the 160-character limit" % len(LINE)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if out_dir.endswith(".txt"):
        out_path = out_dir
    else:
        out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
