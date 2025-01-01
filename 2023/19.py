"""
--- Day 19: Aplenty ---
https://adventofcode.com/2023/day/19

The solution here for part 2 is rather simple in the end. We just keep track of how a full range [1, 4000], is moved
between workflows based on the comparison.
"""

from utils import *

args = parse_args(year=2023, day=19)
raw = get_input(args.filename, year=2023, day=19)

instructions, parts = [group.splitlines() for group in raw.split("\n\n")]

workflows = {}
for instruction in instructions:
    name, rules = instruction[:-1].split("{")
    rules = rules.split(",")
    workflows[name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(":")
        key, cmp = comparison[0], comparison[1]
        n = int(comparison[2:])
        workflows[name][0].append((key, cmp, n, target))


def is_accepted(part: dict, workflow: str = "in"):
    if workflow in "AR":
        return workflow == "A"
    rules, fallback = workflows[workflow]
    for key, cmp, n, target in rules:
        if (int.__lt__ if cmp == "<" else int.__gt__)(part[key], n):
            return is_accepted(part, target)
    return is_accepted(part, fallback)


def count_accepted(ranges: dict[str, tuple], workflow: str = "in"):
    if workflow == "R" or any(b - a <= 0 for a, b in ranges.values()):
        return 0
    if workflow == "A":
        return mul(b - a for a, b in ranges.values())

    total = 0
    rules, fallback = workflows[workflow]
    for key, cmp, n, target in rules:
        lo, hi = ranges[key]
        if cmp == "<":
            modified = {k: ((l, n) if k == key else (l, h)) for k, (l, h) in ranges.items()}
            total += count_accepted(modified, target)
            ranges[key] = (n, hi)
        else:
            modified = {k: ((n + 1, h) if k == key else (l, h)) for k, (l, h) in ranges.items()}
            total += count_accepted(modified, target)
            ranges[key] = (lo, n + 1)
    return total + count_accepted(ranges, fallback)


p1 = 0
for part in parts:
    x, m, a, s = list(nums(part))
    if is_accepted({"x": x, "m": m, "a": a, "s": s}):
        p1 += x + m + a + s
print(p1)

p2 = count_accepted({"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)})
print(p2)

if args.test:
    args.tester(p1, p2)
