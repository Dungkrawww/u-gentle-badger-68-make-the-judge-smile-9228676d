# u-gentle-badger-68-make-the-judge-smile-9228676d: one fixed one-liner, judged pairwise
# by a house judge on subject, warmth, surprise, concreteness, and fresh
# wording. Single sentence, <=200 chars.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Candidates, best first. The winner was picked for a three-beat arc that
# hits every judging criterion in one breath: a concrete small kindness
# (corner shop, newspaper, coins), a surprise turn (the seller refuses
# payment), and fresh wording ("the good news is on the house") that makes
# the kindness feel genuinely felt rather than reported. No greeting-card
# phrasing, no borrowed sentiment.
CANDIDATES = [
    "The old man at the corner shop refused my coins for the newspaper and said, 'today, the good news is on the house.'",
    "The bus driver held the door while I sprinted through the rain, then waved off my thanks like kindness was just part of the route.",
    "At 6 a.m. the baker slipped a still-warm bun into my bag and said, 'first one is on the morning.'",
]

# Deterministic: the entry is one fixed line, so both harness runs must
# write the same bytes. No randomness, no network, no clock.
LINE = CANDIDATES[0]


def main() -> None:
    # Gate rules (sealed scorer): /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    assert LINE.count(".") == 1 and LINE.rstrip("'").endswith("."), "exactly one sentence"
    assert "\n" not in LINE, "no newline inside the line"
    # A one-liner must read cleanly aloud: no double spaces, and enough
    # words to carry a setup plus a punchline (a 1-2 word line cannot).
    assert "  " not in LINE, "no double spaces"
    assert len(LINE.split()) >= 5, "line must have at least 5 words"

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
