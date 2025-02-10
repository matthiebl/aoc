"""
--- Day 5: Alchemical Reduction ---
https://adventofcode.com/2018/day/5
"""

from utils import *

args = parse_args(year=2018, day=5)
polymer = get_input(args.filename, year=2018, day=5).strip()
# polymer = "dabAcCaCBAcCcaDA"


def react(polymer):
    stack = []
    for c in polymer:
        if not stack or c.swapcase() != stack[-1]:
            stack.append(c)
        else:
            stack.pop()
    return "".join(stack)


reacted_polymer = react(polymer)
p1 = len(reacted_polymer)
print(p1)

p2 = p1
for c in "qwertyuiopasdfghjklzxcvbnm":
    p2 = min(p2, len(react(reacted_polymer.replace(c, "").replace(c.upper(), ""))))
print(p2)

if args.test:
    args.tester(p1, p2)
