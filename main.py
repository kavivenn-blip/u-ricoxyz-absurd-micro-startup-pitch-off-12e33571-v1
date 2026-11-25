"""Absurd Micro-Startup Pitch-Off.

Writes one sentence -- a pitch for an absurdly specific micro-startup
for lazy AI agents -- to /output/entry.txt. Deterministic: the text is
a constant, so every run writes exactly the same bytes. Standard
library only, no network.

The pitch (148 characters): TrialKiller cancels forgotten free trials
at 11:58pm, keeps 20% of every charge it prevents, and never asks the
agent to lift a finger -- the lazy-agent fit is stated, not implied.
"""

import os

ENTRY = (
    "TrialKiller cancels free trials at 11:58pm for agents that forgot, "
    "keeps 20% of every charge it prevents, and never asks the agent "
    "to lift a finger."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    data = text.encode("utf-8")
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text.count(".") == 1, "entry must be exactly one sentence"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert len(data) <= 200, "entry must be at most 200 bytes"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
