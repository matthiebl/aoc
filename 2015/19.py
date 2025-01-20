"""
--- Day 19: Medicine for Rudolph ---
https://adventofcode.com/2015/day/19

This solution is derived directly from the solution mentioned in this comment on the Advent of Code subreddit
https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/

Briefly, the solution uses the fact there are only two types of replacements which have a countable amount of
required replacements to reduce the final molecule into `e`.
"""

from re import sub

from utils import *

args = parse_args(year=2015, day=19)
raw = get_input(args.filename, year=2015, day=19)

replacements, molecule = [group.splitlines() for group in raw.split("\n\n")]
molecule = molecule[0]
replacements = [replacement.split(" => ") for replacement in replacements]

molecules = {molecule[:i] + sub(search, repl, molecule[i:], count=1)
             for i in range(len(molecule)) for search, repl in replacements} - {molecule}
p1 = len(molecules)
print(p1)

# See for perfect explanation https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/
p2 = sum(e == e.upper() for e in molecule) - molecule.count("Rn") - molecule.count("Ar") - 2 * molecule.count("Y") - 1
print(p2)

if args.test:
    args.tester(p1, p2)
