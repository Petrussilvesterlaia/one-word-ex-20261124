"""One Word From Your Ex — entry program.

Writes exactly one word to /output/entry.txt: the word an ex would
use to describe their former partner. No dependencies, no network,
no files read outside this repo.
"""

import os

WORD = "placeholder"

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate_word(word):
    """Gate: exactly one word, 1-24 chars, not blank-only."""
    assert isinstance(word, str), "word must be a string"
    assert 1 <= len(word) <= 24, "word must be 1-24 characters"
    assert word.strip() != "", "word must not be blank"
    assert len(word.split()) == 1, "word must be exactly one word"
    assert word == word.lower(), "word must be lowercase"
    return word


def main():
    word = validate_word(WORD)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word + "\n")
    # Self-check: read back and verify what was actually written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == word + "\n", "read-back mismatch"
    assert validate_word(written.strip()) == word


if __name__ == "__main__":
    main()
