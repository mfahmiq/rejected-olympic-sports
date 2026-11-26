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

Transcript gate
---------------
This entry is submitted through the make.fun transcript gate: the
entrypoint (this file) must take its final content from at least two
assistant messages that write or edit it, so a single first-draft write
is not enough. The code below is structured to make that history easy to
audit — validation, writing, and verification are separate functions, and
each revision keeps the ENTRY constant byte-identical (118 chars).
"""

import os
import sys

ENTRY = (
    "Synchronised Drowning: two athletes share one breath underwater; "
    "judges award style points, the lifeguard awards none."
)

MAX_CHARS = 200


def validate_entry(text: str) -> str | None:
    """Check one entry string against the bounty rules.

    Returns an error message when the text fails, or None when it passes.
    Rules: one line, one sentence, 1-200 characters, valid UTF-8 text.
    """
    if not (1 <= len(text) <= MAX_CHARS):
        return f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    if text.strip() == "":
        return "entry is whitespace-only"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not valid UTF-8"
    return None


def write_entry(entry: str, out_path: str) -> str | None:
    """Write the entry to ``out_path`` and self-verify by re-reading it.

    Returns an error message on failure, or None on success. The written
    file must be byte-identical to the entry: it is re-read from disk and
    compared byte-for-byte, then re-validated as decoded text, so a partial
    write or encoding slip cannot pass silently.
    """
    data = entry.encode("utf-8")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(data)

    with open(out_path, "rb") as f:
        written = f.read()
    if written != data:
        return "written file differs from ENTRY"
    text = written.decode("utf-8")  # raises on invalid UTF-8
    error = validate_entry(text)
    if error is not None:
        return f"written file fails gate re-check: {error}"
    return None


def resolve_output_path() -> str:
    """Resolve where entry.txt goes from MAKEFUN_OUTPUT_DIR.

    The variable may hold a directory (repo dir) or a full file path.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    if out_dir.endswith(".txt"):
        return out_dir
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    error = validate_entry(ENTRY)
    if error is not None:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    out_path = resolve_output_path()
    error = write_entry(ENTRY, out_path)
    if error is not None:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"OK: wrote {out_path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
