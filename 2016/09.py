"""
--- Day 9: Explosives in Cyberspace ---
https://adventofcode.com/2016/day/9
"""

from utils import *

args = parse_args(year=2016, day=9)
raw = get_input(args.filename, year=2016, day=9)


def decompressed_size(string: str, v2: bool = False):
    if "(" not in string:
        return len(string)
    left = string.index("(")
    string = string[left + 1:]
    right = string.index(")")
    s, n = nums(string[:right])
    if v2:
        return (left + n * decompressed_size(string[right + 1:right + s + 1], v2)
                + decompressed_size(string[right + s + 1:], v2))
    else:
        return left + s * n + decompressed_size(string[right + s + 1:])


p1 = decompressed_size(raw)
print(p1)

p2 = decompressed_size(raw, v2=True)
print(p2)

if args.test:
    args.tester(p1, p2)
