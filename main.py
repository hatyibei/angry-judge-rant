#!/usr/bin/env python3
"""Entry for make.fun's "Angry Judge: The Short Rant Contest".

Writes a short funny rant about an everyday annoyance to /output/entry.txt
(UTF-8, 1-400 characters, no trailing newline).
"""
import os

ENTRY = (
    "To whoever invented the 'quick call' that eats my whole afternoon: "
    "may your Wi-Fi drop one bar forever, your charger only work at one "
    "angle, and every meeting you book get a sequel with a pre-read."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
