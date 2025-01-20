"""
--- Day 12: Leonardo's Monorail ---
https://adventofcode.com/2016/day/12
"""

from utils import *
from utils.interpreters.bunnycode import BunnyCode

args = parse_args(year=2016, day=12)
raw = get_input(args.filename, year=2016, day=12)

instructions = raw.splitlines()

p1 = BunnyCode(instructions).run()
print(p1)

p2 = BunnyCode(instructions, c=1).run()
print(p2)

if args.test:
    args.tester(p1, p2)
