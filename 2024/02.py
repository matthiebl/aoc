"""
--- Day 2: Red-Nosed Reports ---
https://adventofcode.com/2024/day/2
"""

from utils import *

args = parse_args(year=2024, day=2)
raw = get_input(args.filename, year=2024, day=2)

reports = [list(nums(line)) for line in raw.splitlines()]


def report_is_safe(report: list[int]) -> bool:
    diffs = [report[i] - report[i+1] for i in range(len(report) - 1)]
    return all(1 <= abs(x) <= 3 for x in diffs) and (all(x < 0 for x in diffs) or all(x > 0 for x in diffs))


p1 = 0
p2 = 0
for report in reports:
    if report_is_safe(report):
        p1 += 1
    # Remove number one by one and check
    for i in range(len(report)):
        if report_is_safe(report[:i] + report[i+1:]):
            p2 += 1
            break
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
