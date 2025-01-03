"""
--- Day 15: ... ---
https://adventofcode.com/2015/day/15
"""

from utils import *

args = parse_args(year=2015, day=15)
raw = get_input(args.filename, year=2015, day=15)

ingredients = list(map(list, map(nums, raw.splitlines())))

p1 = 0
p2 = 0

for teaspoons in nums_sum_to(100, n=len(ingredients)):
    properties = [
        sum(teaspoons[ingredient] * ingredients[ingredient][prop] for ingredient in range(len(ingredients)))
        for prop in range(len(ingredients[0]))
    ]
    if any(p <= 0 for p in properties[:-1]):
        continue
    score = mul(properties[:-1])
    p1 = max(p1, score)
    if properties[-1] == 500:
        p2 = max(p2, score)

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
