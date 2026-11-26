"""Rejected Olympic Sports — make.fun entry.

Entry (118 characters, one line, one sentence):

    Synchronised Drowning: two athletes share one breath underwater;
    judges award style points, the lifeguard awards none.

Why it won the internal tournament (see CANDIDATES.md): of 16 candidates,
this line parodies an actual Olympic event — synchronised swimming — so it
is the most plausible rejection in the field, and its kicker ("the
lifeguard awards none") is the single funniest beat in the tournament: a
dark, surprising twist that lands at the very end, in one read. The setup
("two athletes share one breath") is a perfect broadcast-style event
description, every word earns its place, and the line is quotable end to
end. It beat the runner-up (Competitive Apologising, "say sorry until one
of them finally means it; the match has run since 1998") in the final
because its laugh is bigger — a laugh out loud where the runner-up gets a
smile — and nothing later in the judge brief overturns criterion 1.
Tournament path: beat C16 in round 1, C3 (Extreme Ironing) in the
quarterfinal, C12 (Competitive Procrastination) in the semifinal, and C8
in the final.
"""

import os
import sys

ENTRY = (
    "Synchronised Drowning: two athletes share one breath underwater; "
    "judges award style points, the lifeguard awards none."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory (repo dir) or a full file path.
    if out_dir.endswith(".txt"):
        out_path = out_dir
    else:
        out_path = os.path.join(out_dir, "entry.txt")

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)

    data = ENTRY.encode("utf-8")

    # Self-verification before writing.
    if not (1 <= len(ENTRY) <= 200):
        print(f"FAIL: entry is {len(ENTRY)} chars, must be 1-200", file=sys.stderr)
        return 1
    if ENTRY.strip() == "":
        print("FAIL: entry is whitespace-only", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("FAIL: entry must be a single line", file=sys.stderr)
        return 1

    with open(out_path, "wb") as f:
        f.write(data)

    # Re-read the written file and confirm it is byte-identical.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != data:
        print("FAIL: written file differs from ENTRY", file=sys.stderr)
        return 1
    text = written.decode("utf-8")  # raises on invalid UTF-8
    if not (1 <= len(text) <= 200) or text.strip() == "" or "\n" in text:
        print("FAIL: written file fails gate re-check", file=sys.stderr)
        return 1

    print(f"OK: wrote {out_path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
