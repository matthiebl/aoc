"""
--- Day 13: Knights of the Dinner Table ---
https://adventofcode.com/2015/day/13
"""

from collections import defaultdict
from itertools import permutations
from utils import *

args = parse_args(year=2015, day=13)
raw = get_input(args.filename, year=2015, day=13)

desires = [line[:-1].split() for line in raw.splitlines()]

people = defaultdict(lambda: defaultdict(int))
for [name, _, change, amt, *_, next_to] in desires:
    people[name][next_to] = int(amt) * (-1 if change == "lose" else 1)


def best_seating_score(names) -> int:
    best = 0
    for arrangement in permutations(names):
        score = people[arrangement[0]][arrangement[-1]] + people[arrangement[-1]][arrangement[0]]
        for n1, n2 in windows(arrangement):
            score += people[n1][n2] + people[n2][n1]
        best = max(score, best)
    return best


p1 = best_seating_score(people)
print(p1)

p2 = best_seating_score(set(people) | {"Me"})
print(p2)

if args.test:
    args.tester(p1, p2)
