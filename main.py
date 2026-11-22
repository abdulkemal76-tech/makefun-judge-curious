"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a concrete mystery that
leaves a real gap, ending on an unanswered question.
"""

import os

TEXT = (
    "The museum's newest painting arrived with no artist, no title, "
    "and no record of who ordered it. "
    "It shows this room, tonight, with one person missing."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"entry is {len(TEXT)} chars"
    assert "\u2014" not in TEXT
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
