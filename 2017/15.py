"""
--- Day 15: Dueling Generators ---
https://adventofcode.com/2017/day/15
"""

from utils import *

args = parse_args(year=2017, day=15)
raw = get_input(args.filename, year=2017, day=15)

gen_a, gen_b = nums(raw)
p1 = 0
for _ in range(40_000_000):
    gen_a = (16807 * gen_a) % 2147483647
    gen_b = (48271 * gen_b) % 2147483647
    if bin(gen_a)[-16:] == bin(gen_b)[-16:]:
        p1 += 1
print(p1)

gen_a, gen_b = nums(raw)
p2 = 0
for _ in range(5_000_000):
    gen_a = (16807 * gen_a) % 2147483647
    while gen_a % 4 != 0:
        gen_a = (16807 * gen_a) % 2147483647
    gen_b = (48271 * gen_b) % 2147483647
    while gen_b % 8 != 0:
        gen_b = (48271 * gen_b) % 2147483647
    if bin(gen_a)[-16:] == bin(gen_b)[-16:]:
        p2 += 1
print(p2)

if args.test:
    args.tester(p1, p2)
