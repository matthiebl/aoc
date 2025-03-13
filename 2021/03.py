"""
--- Day 3: Binary Diagnostic ---
https://adventofcode.com/2021/day/3
"""

from collections import Counter

from utils import *

args = parse_args(year=2021, day=3)
raw = get_input(args.filename, year=2021, day=3)

diagnostic = raw.splitlines()

gamma, epsilon = "", ""
for col in list(zip(*diagnostic)):
    (g, _), (e, _) = Counter(col).most_common()
    gamma += g
    epsilon += e

p1 = int(gamma, 2) * int(epsilon, 2)
print(p1)


def reduce(diagnostic: list[str], default: str):
    if len(diagnostic) == 1:
        return diagnostic[0]

    (m, mc), (l, lc) = Counter(next(zip(*diagnostic))).most_common()
    ch = default if mc == lc else m if default == "1" else l
    return ch + reduce([bits[1:] for bits in diagnostic if bits[0] == ch], default)


oxygen = reduce(diagnostic, "1")
carbon = reduce(diagnostic, "0")

p2 = int(oxygen, 2) * int(carbon, 2)
print(p2)

if args.test:
    args.tester(p1, p2)
