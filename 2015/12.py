"""
--- Day 12: JSAbacusFramework.io ---
https://adventofcode.com/2015/day/12
"""

from json import loads

from utils import *

args = parse_args(year=2015, day=12)
raw = get_input(args.filename, year=2015, day=12)

p1 = sum(list(nums(raw)))
print(p1)


def non_red_sum(json) -> int:
    if isinstance(json, int):
        return json
    if isinstance(json, str):
        return 0
    if isinstance(json, list):
        return sum(non_red_sum(it) for it in json)
    assert isinstance(json, dict)
    if any(v == "red" for v in json.values()):
        return 0
    return sum(non_red_sum(v) for v in json.values())


p2 = non_red_sum(loads(raw))
print(p2)

if args.test:
    args.tester(p1, p2)
