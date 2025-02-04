"""
--- Day 23: Coprocessor Conflagration ---
https://adventofcode.com/2017/day/23
"""

from sympy import isprime

from utils import *

args = parse_args(year=2017, day=23)
raw = get_input(args.filename, year=2017, day=23)


class Coprocessor(Interpreter):
    invoked = 0

    def _mul(self, x, y):
        self.invoked += 1
        return super()._mul(x, y)


p1 = Coprocessor().parse_instructions(raw).run().invoked
print(p1)

lower = 100000 + next(nums(raw)) * 100
upper = lower + 17000 + 1
p2 = sum(not isprime(n) for n in range(lower, upper, 17))
print(p2)

if args.test:
    args.tester(p1, p2)
