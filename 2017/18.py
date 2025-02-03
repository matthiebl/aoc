"""
--- Day 18: Duet ---
https://adventofcode.com/2017/day/18
"""

from utils import *

args = parse_args(year=2017, day=18)
instructions = get_input(args.filename, year=2017, day=18)


class Solo(Interpreter):
    def _rcv(self, x):
        if self.value(x) != 0:
            return self.length


class Duet(Interpreter):
    def _snd(self, x):
        super()._snd(x)
        self.sent = 1 + (0 if not hasattr(self, "sent") else self.sent)


p1 = Solo().parse_instructions(instructions).run().output[-1]
print(p1)

prog1 = Duet().parse_instructions(instructions)
prog2 = Duet(p=1).parse_instructions(instructions)
prog1.input = prog2.output
prog2.input = prog1.output
while not (prog1.halt and not prog1.input):
    prog1.run()
    prog2.run()
p2 = prog2.sent
print(p2)

if args.test:
    args.tester(p1, p2)
