"""
--- Day 4: Security Through Obscurity ---
https://adventofcode.com/2016/day/4
"""

from collections import Counter

from utils import *

args = parse_args(year=2016, day=4)
raw = get_input(args.filename, year=2016, day=4)

rooms = [line.split("-") for line in raw.splitlines()]
alphabet = "abcdefghijklmnopqrstuvwxyz"

p1 = 0
for [*name, details] in rooms:
    sector_id = next(nums(details))
    checksum = details[details.index("[") + 1:-1]
    freq = Counter("".join(name))
    freq = sorted((-freq[c], c) for c in freq)
    if all(c == l for c, (_, l) in zip(checksum, freq)):
        p1 += sector_id
    decrypted = " ".join("".join(alphabet[(alphabet.index(c) + sector_id) % 26] for c in word) for word in name)
    if "northpole" in decrypted:
        p2 = sector_id

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
