"""
--- Day 16: Dragon Checksum ---
https://adventofcode.com/2016/day/16
"""

from utils import *

args = parse_args(year=2016, day=16)
initial = get_input(args.filename, year=2016, day=16)


def dragon_checksum(length: int):
    disk = initial
    while len(disk) < length:
        b = "".join("1" if x == "0" else "0" for x in disk[::-1])
        disk = disk + "0" + b

    checksum = disk[:length]
    while len(checksum) % 2 == 0:
        checksum = "".join("1" if x == y else "0" for x, y in chunks(checksum))
    return checksum


p1 = dragon_checksum(length=272)
print(p1)

p2 = dragon_checksum(length=35651584)
print(p2)

if args.test:
    args.tester(p1, p2)
