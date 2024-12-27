"""
--- Day 1: Trebuchet?! ---
https://adventofcode.com/2023/day/1
"""

import re
from utils import *

args = parse_args(year=2023, day=1)
raw = get_input(args.filename, year=2023, day=1)

lines = raw.splitlines()
pattern = r"zero|one|two|three|four|five|six|seven|eight|nine"
value = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

p1 = 0
p2 = 0

for line in lines:
    first = None
    for last in re.findall(r"\d", line):
        first = last if first is None else first
    p1 += int(first + last)

    first = re.findall(pattern + r"|\d", line)[0]
    last = re.findall(pattern[::-1] + r"|\d", line[::-1])[0][::-1]
    p2 += (value.index(first) if first in value else int(first)) * \
        10 + (value.index(last) if last in value else int(last))

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
