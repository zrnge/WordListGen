#!/usr/bin/env python3

import argparse
import itertools

SYMBOLS = ["!", "@", "#", "$", "%", "&", "*", "_", "."]
NUMBERS = [str(i) for i in range(10)]

LEET_MAP = {
    "a": ["a", "@", "4"],
    "b": ["b", "8"],
    "e": ["e", "3"],
    "i": ["i", "1"],
    "l": ["l", "1"],
    "o": ["o", "0"],
    "s": ["s", "$", "5"],
    "t": ["t", "7"]
}


def case_variations(word):
    return {
        word,
        word.lower(),
        word.upper(),
        word.capitalize()
    }


def leet_variations(word):
    pools = []
    for c in word.lower():
        pools.append(LEET_MAP.get(c, [c]))
    return {''.join(p) for p in itertools.product(*pools)}


def number_variations():
    nums = set(NUMBERS)
    nums |= {str(i) for i in range(1, 100)}
    nums |= {"01", "02", "03", "007", "123", "1234"}
    return nums


def date_variations(date):
    if len(date) < 6:
        return {date}

    dd = date[:2]
    mm = date[2:4]
    yy = date[4:]
    yyyy = "20" + yy

    return {
        date,
        yyyy + dd,
        dd + yyyy,
        dd + mm + yyyy,
        yyyy,
        yy,
        dd + mm,
        mm + yy,
        mm + yyyy
    }


def combine_words(words):
    combos = set(words)
    for a, b in itertools.permutations(words, 2):
        combos.add(a + b)
        combos.add(b + a)
    return combos


def enrich(words, numbers, dates, symbols):
    results = set(words)

    for w in words:
        for n in numbers:
            results.add(w + n)
            results.add(n + w)

        for d in dates:
            results.add(w + d)
            results.add(d + w)

        for s in symbols:
            results.add(w + s)
            results.add(s + w)

    return results


def main():
    parser = argparse.ArgumentParser(description="Advanced Password Wordlist Generator")
    parser.add_argument("--name", required=True)
    parser.add_argument("--job")
    parser.add_argument("--birthday")
    parser.add_argument("--leet", action="store_true")
    parser.add_argument("--numbers", action="store_true")
    parser.add_argument("--symbols", action="store_true")
    parser.add_argument("--max-length", type=int, default=32)
    parser.add_argument("--output", default="wordlist.txt")

    args = parser.parse_args()

    base_words = set()

    for w in [args.name, args.job]:
        if w:
            base_words |= case_variations(w)

    if args.leet:
        leet_words = set()
        for w in base_words:
            leet_words |= leet_variations(w)
        base_words |= leet_words

    combined = combine_words(base_words)

    numbers = number_variations() if args.numbers else set()
    dates = date_variations(args.birthday) if args.birthday else set()
    symbols = SYMBOLS if args.symbols else []

    final = enrich(combined, numbers, dates, symbols)

    final = {w for w in final if len(w) <= args.max_length}

    with open(args.output, "w") as f:
        for w in sorted(final):
            f.write(w + "\n")

    print(f"[+] Generated {len(final)} passwords → {args.output}")


if __name__ == "__main__":
    main()
