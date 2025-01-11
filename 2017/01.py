"""
--- Day 1: Inverse Captcha ---
https://adventofcode.com/2017/day/1
"""

from utils import *

args = parse_args(year=2017, day=1)
raw = get_input(args.filename, year=2017, day=1)

p1 = sum(int(n) for n, m in windows(raw + raw[0]) if n == m)
print(p1)

p2 = sum(int(n) for i, n in enumerate(raw) if n == raw[(i + len(raw) // 2) % len(raw)])
print(p2)

if args.test:
    args.tester(p1, p2)
