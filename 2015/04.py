"""
--- Day 4: The Ideal Stocking Stuffer ---
https://adventofcode.com/2015/day/4
"""

from _md5 import md5
from utils import *

args = parse_args(year=2015, day=4)
key = get_input(args.filename, year=2015, day=4)

p1 = 0
p2 = 0
i = 1
while not (p1 and p2):
    hash = md5(f"{key}{i}".encode()).hexdigest()
    if not p1 and hash.startswith("00000"):
        p1 = i
    if not p2 and hash.startswith("000000"):
        p2 = i
    i += 1
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
