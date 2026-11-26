"""One-line joke entry for the make.fun bounty
"u-coral-404-one-line-big-laugh-328fb857" (One Line, Big Laugh).

Writes the entry line to /output/entry.txt.
Deterministic, no network, no randomness: running it twice
produces byte-identical output.
"""

ENTRY = "My smart fridge caught me sneaking ice cream at 2 a.m. and now it charges me rent for the freezer shelf."


def main():
    line = ENTRY
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
