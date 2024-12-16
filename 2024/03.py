"""
--- Day 3: Mull It Over ---
https://adventofcode.com/2024/day/3
"""

import re
from utils import *

args = parse_args(year=2024, day=3)
raw = get_input(args.filename, year=2024, day=3)

line = "".join(raw.splitlines())

p1 = 0
enabled = True
parts = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
for part in parts:
    i = part.index(',')
    p1 += int(part[4:i]) * int(part[i+1:-1])
print(p1)

p2 = 0
parts_2 = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)
for part in parts_2:
    if part == 'do()':
        enabled = True
    elif part == 'don\'t()':
        enabled = False
    elif enabled:
        i = part.index(',')
        p2 += int(part[4:i]) * int(part[i+1:-1])
print(p2)

if args.test:
    args.tester(p1, p2)
