"""
--- Day 23: Opening the Turing Lock ---
https://adventofcode.com/2015/day/23
"""

from utils import *

args = parse_args(year=2015, day=23)
instructions = get_input(args.filename, year=2015, day=23)


class TuringLock(Interpreter):
    def parse_instructions(self, raw: str):
        for line in raw.splitlines():
            [op, *args] = line.split()
            if op in ["jie", "jio"]:
                self.instructions.append([op, args[0][:-1], args[1]])
            else:
                self.instructions.append([op, *args])
        self.length = len(self.instructions)
        return self

    def _jie(self, x, y): return self.value(y) if self.value(x) % 2 == 0 else 1
    def _jio(self, x, y): return self.value(y) if self.value(x) == 1 else 1


p1 = TuringLock().parse_instructions(instructions).run().value("b")
print(p1)

p2 = TuringLock(a=1).parse_instructions(instructions).run().value("b")
print(p2)

if args.test:
    args.tester(p1, p2)
