"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
https://adventofcode.com/2015/day/5
"""

import re

from utils import *

args = parse_args(year=2015, day=5)
raw = get_input(args.filename, year=2015, day=5)

strings = raw.splitlines()


def nice(string: str) -> bool:
    if re.search(r"ab|cd|pq|xy", string):
        return False
    return any(a == b for a, b in windows(string)) and len(re.findall(r"a|e|i|o|u", string)) >= 3


def nice_v2(string: str) -> bool:
    return (any(string.count(a + b) >= 2 for a, b in windows(string))
            and any(a == b for a, b in zip(string, string[2:])))


p1 = len(list(filter(nice, strings)))
print(p1)

p2 = len(list(filter(nice_v2, strings)))

print(p2)

if args.test:
    args.tester(p1, p2)
