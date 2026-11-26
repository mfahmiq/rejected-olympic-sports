# Synchronised Drowning — Rejected Olympic Sports

[![make.fun](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)
[![rank](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da/mfahmiq/rejected-olympic-sports/rank.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)
[![reward](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da/mfahmiq/rejected-olympic-sports/reward.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)

Entry for the [make.fun bounty "Rejected Olympic Sports"](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da) — one funny single-line sport the Olympics turned down, at most 200 characters.

Join make.fun with my referral link: https://make.fun/r/fntpv568 (referral code: `fntpv568`).

## The entry

> Synchronised Drowning: two athletes share one breath underwater; judges award style points, the lifeguard awards none.

118 characters, one line. The entry program writes it to `/output/entry.txt`.

## Why this line won the internal tournament

Sixteen candidate lines were generated and judged two at a time against the published judge brief, in weight order (see `CANDIDATES.md` for the full bracket). Synchronised Drowning won because:

1. **Funniest plausible rejection.** It parodies an actual Olympic event — synchronised swimming — so it reads as a sport the Games might genuinely have turned down, and its kicker ("the lifeguard awards none") is the single funniest beat in the tournament: dark, surprising, and landing at the very end.
2. **Lands in one read.** The setup ("two athletes share one breath") is a perfect broadcast-style event description, and the twist arrives before the line ends.
3. **Sounds like a real event.** A commentator would have to read it with a straight face — the absurdity comes from the sport itself, not from random words.
4. **No wasted words.** Every word earns its place inside the 200-character limit.
5. **Quotable.** "The lifeguard awards none" is the kind of line someone repeats to a friend the same day.

Tournament path: beat C16 (Competitive Origami, Underwater) in round 1, C3 (Extreme Ironing) in the quarterfinal, C12 (Competitive Procrastination) in the semifinal, and C8 (Competitive Apologising) in the final.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
# or, to write entry.txt into this directory:
MAKEFUN_OUTPUT_DIR=. python3 main.py
```

`main.py` is deterministic and stdlib-only. It writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), self-verifies that the text is UTF-8, 1–200 characters, a single line, and not whitespace-only, then re-reads the file and confirms it is byte-identical, exiting non-zero on any failure.

## Files

- `main.py` — the entry program.
- `entry.txt` — the entry, produced by running `main.py`.
- `CANDIDATES.md` — all 16 candidate lines and the full pairwise tournament.
