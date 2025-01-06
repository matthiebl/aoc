"""
--- Day 10: Balance Bots ---
https://adventofcode.com/2016/day/10
"""

from collections import defaultdict
from re import search
from utils import *

args = parse_args(year=2016, day=10)
raw = get_input(args.filename, year=2016, day=10)

instructions = raw.splitlines()

bots = defaultdict(list)
rules = {}
for instruction in instructions:
    if instruction.startswith("value"):
        value, bot = nums(instruction)
        bots[bot].append(value)
    else:
        bot, target_low, lt, target_high, ht = search(
            r"^.* (\d+) .*(bot|output) (\d+) .*(bot|output) (\d+)$", instruction).groups()
        rules[int(bot)] = (target_low, int(lt), target_high, int(ht))

p1 = 0
output = defaultdict(list)
while True:
    choices = [bot for bot in bots if len(bots[bot]) == 2]
    if not choices:
        break
    bot = choices[0]
    target_low, lt, target_high, ht = rules[bot]
    low, high = sorted(bots[bot])
    if (low, high) == (17, 61):
        p1 = bot
    (bots if target_low == "bot" else output)[lt].append(low)
    (bots if target_high == "bot" else output)[ht].append(high)
    bots[bot] = []

print(p1)

p2 = mul([n for [n] in [output[b] for b in [0, 1, 2]]])
print(p2)

if args.test:
    args.tester(p1, p2)
