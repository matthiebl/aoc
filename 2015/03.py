"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
https://adventofcode.com/2015/day/3
"""

from utils import *

args = parse_args(year=2015, day=3)
moves = get_input(args.filename, year=2015, day=3)

D = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}

r, c = 0, 0
gifted = set([(r, c)])
for move in moves:
    dr, dc = D[move]
    r, c = r + dr, c + dc
    gifted.add((r, c))

p1 = len(gifted)
print(p1)

r1, c1 = 0, 0
r2, c2 = 0, 0
gifted = set([(r1, c1)])
for move1, move2 in chunks(moves):
    dr, dc = D[move1]
    r1, c1 = r1 + dr, c1 + dc
    gifted.add((r1, c1))
    dr, dc = D[move2]
    r2, c2 = r2 + dr, c2 + dc
    gifted.add((r2, c2))

p2 = len(gifted)
print(p2)

if args.test:
    args.tester(p1, p2)
