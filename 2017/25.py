"""
--- Day 25: The Halting Problem ---
https://adventofcode.com/2017/day/25
"""

from collections import defaultdict

from utils import *

args = parse_args(year=2017, day=25)
raw = get_input(args.filename, year=2017, day=25)

[details, *states] = [group.splitlines() for group in raw.split("\n\n")]

state, steps = details[0][-2], next(nums(details[1]))

i = 0
tape = defaultdict(int)
states = {state[0][-2]: {0: (next(nums(state[2])), 1 if "right" in state[3] else -1, state[4][-2]),
                         1: (next(nums(state[6])), 1 if "right" in state[7] else -1, state[8][-2])}
          for state in states}

for _ in range(steps):
    set, move, state = states[state][tape[i]]
    tape[i] = set
    i += move
    state = state

p1 = sum(tape.values())
print(p1)

p2 = None
print(p2)

if args.test:
    args.tester(p1, p2)
