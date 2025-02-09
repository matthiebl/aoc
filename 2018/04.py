"""
--- Day 4: Repose Record ---
https://adventofcode.com/2018/day/4
"""

from collections import defaultdict

from utils import *

args = parse_args(year=2018, day=4)
raw = get_input(args.filename, year=2018, day=4)

logs = sorted(raw.splitlines())

sleep = defaultdict(lambda: defaultdict(int))

for log in logs:
    n = list(nums(log))[-1]
    if "Guard" in log:
        guard = n
    elif "falls asleep" in log:
        asleep = n
    else:
        for t in range(asleep, n):
            sleep[guard][t] += 1

_, guard = sorted(((sum(times.values()), guard) for guard, times in sleep.items()), reverse=True)[0]
_, t = sorted(((n, t) for t, n in sleep[guard].items()), reverse=True)[0]
p1 = guard * t
print(p1)

_, guard, t = sorted(((n, guard, t) for guard, times in sleep.items() for t, n in times.items()), reverse=True)[0]
p2 = guard * t
print(p2)

if args.test:
    args.tester(p1, p2)
