"""
--- Day 13: Claw Contraption ---
https://adventofcode.com/2024/day/13

I was not expecting to require sympy this early...

I'm sure there are some other ways to calculate this, and some more maths I could try,
but sympy was an easy out here. It's a quick and easy solution not really requiring
much work.

We are practically given the equations in the question:
```
a * xa + b * xb - xp = 0
a * ya + b * yb - yp = 0
```
"""
from sympy import symbols, Eq, solve, Integer
from utils import *

args = parse_args(year=2024, day=13)
raw = get_input(args.filename, year=2024, day=13)

machines = chunks(nums(raw), 6)

p1 = 0
p2 = 0
for [xa, ya, xb, yb, xp, yp] in machines:
    a, b = symbols("a b")
    eq1 = Eq(a * xa + b * xb - xp, 0)
    eq2 = Eq(a * ya + b * yb - yp, 0)
    r = solve((eq1, eq2), (a, b))
    if isinstance(r[a], Integer) and isinstance(r[b], Integer):
        p1 += r[a] * 3 + r[b]

    xp += 10000000000000
    yp += 10000000000000
    eq1 = Eq(a * xa + b * xb - xp, 0)
    eq2 = Eq(a * ya + b * yb - yp, 0)
    r = solve((eq1, eq2), (a, b))
    if isinstance(r[a], Integer) and isinstance(r[b], Integer):
        p2 += r[a] * 3 + r[b]

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
