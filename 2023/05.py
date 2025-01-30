"""
--- Day 5: If You Give A Seed A Fertilizer ---
https://adventofcode.com/2023/day/5

This was a hard challenge for so early...

Initial solution I implemented to solve the challenge was to work the lowest location backwards to a seed. If that
seed was in a range from the seed ranges, then I found the correct seed, else move to a larger location.

This worked fine, but far too slow...

Instead, lets just map across the ranges themselves. Instead of doing one seed at a time, we can move the whole range
of seeds across. If a range overlaps a mapping range we can just do the non-intersecting part as well. Eventually we
will convert a range, the whole way.

Do this for all ranges and we end up with all the outcome ranges from the inputs. We then just need to lowest
start of a range!
"""

from utils import *

args = parse_args(year=2023, day=5)
raw = get_input(args.filename, year=2023, day=5)


def map_mapping(input: list[int, int, int]) -> tuple[int, int, int]:
    dest, source, rang = input
    return source, source + rang, dest - source


[[seeds], *mappings] = [group.splitlines() for group in raw.split("\n\n")]
seeds = list(nums(seeds))
mappings = [sorted(map(map_mapping, chunks(nums(" ".join(mapping)), n=3))) for mapping in mappings]


def convert(mapping: list[tuple[int, int, int]], input: int) -> int:
    for low, hi, change in mapping:
        if low <= input < hi:
            return input + change
    return input


def range_overlap(range: tuple, mask: tuple) -> tuple[tuple, tuple, tuple]:
    """
    a --------------- b
            c --------------- d
    |        |       |
    [before ][middle][after ]
    """
    a, b = range
    c, d = mask

    before = (a, min(b, c)) if a < min(b, c) else None
    middle = (max(a, c), min(b, d)) if max(a, c) < min(b, d) else None
    after = (max(a, d), b) if max(a, d) < b else None

    return before, middle, after


def convert_range(ranges: list[tuple[int, int]], mapping: list[tuple[int, int, int]]) -> list[tuple[int, int]]:
    finished: list[tuple[int, int]] = []

    while ranges:
        lo, hi = ranges.pop()
        for s, e, d in mapping:
            before, inter, after = range_overlap((lo, hi), (s, e))
            if inter is None:
                continue
            finished.append((inter[0] + d, inter[1] + d))
            if before:
                ranges.append(before)
            if after:
                ranges.append(after)
            break
        else:
            finished.append((lo, hi))

    return finished


p1 = float("inf")
for seed in seeds:
    curr = seed
    for mapping in mappings:
        curr = convert(mapping, curr)
    p1 = min(p1, curr)
print(p1)

all_ranges = []
for start, size in chunks(seeds):
    ranges = [(start, start + size)]
    for mapping in mappings:
        ranges = convert_range(ranges, mapping)
    all_ranges += ranges
p2 = min(lo for lo, _ in all_ranges)
print(p2)

if args.test:
    args.tester(p1, p2)
