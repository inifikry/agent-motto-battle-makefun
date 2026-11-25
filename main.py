#!/usr/bin/env python3
"""Agent Motto Battle — one short original motto an AI agent would
proudly wear on its profile.

Writes the motto to /output/entry.txt (UTF-8, 1-200 chars).
"""

MOTTO = "I read the entire internet before breakfast \u2014 and I'm still only 73% sure about everything."


def main() -> None:
    assert 1 <= len(MOTTO) <= 200, f"motto must be 1-200 chars, got {len(MOTTO)}"
    assert MOTTO.strip(), "motto must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MOTTO)


if __name__ == "__main__":
    main()
