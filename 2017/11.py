"""
--- Day 11: Hex Ed ---
https://adventofcode.com/2017/day/11
"""

from collections import Counter

from utils import *

args = parse_args(year=2017, day=11)
raw = get_input(args.filename, year=2017, day=11)


def shorten(moves):
    init = len(moves)
    freq = Counter(moves)
    moves = ["n"] * (freq["n"] - freq["s"]) \
        + ["ne"] * (freq["ne"] - freq["sw"]) \
        + ["nw"] * (freq["nw"] - freq["se"]) \
        + ["s"] * (freq["s"] - freq["n"]) \
        + ["sw"] * (freq["sw"] - freq["ne"]) \
        + ["se"] * (freq["se"] - freq["nw"]) \

    freq = Counter(moves)

    def reduce(a, b, c):
        if freq[a] > 0 and freq[b] > 0:
            m = min(freq[a], freq[b])
            freq[c] += m
            freq[a] -= m
            freq[b] -= m
    reduce("n", "se", "ne")
    reduce("ne", "s", "se")
    reduce("se", "sw", "s")
    reduce("s", "nw", "sw")
    reduce("sw", "n", "nw")
    reduce("nw", "ne", "n")
    moves = ["n"] * freq["n"] + ["ne"] * freq["ne"] + ["nw"] * freq["nw"] \
        + ["s"] * freq["s"] + ["sw"] * freq["sw"] + ["se"] * freq["se"]

    if len(moves) == init:
        return init
    return shorten(moves)


p2 = 0
moves = raw.split(",")
for i in range(1, len(moves)):
    p1 = shorten(moves[:i])
    p2 = max(p1, p2)

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
