"""
--- Day 16: Chronal Classification ---
https://adventofcode.com/2018/day/16
"""

from utils import *

args = parse_args(year=2018, day=16)
raw = get_input(args.filename, year=2018, day=16)

[*samples, _, program] = [group.splitlines() for group in raw.split("\n\n")]

opcodes = {i: {"addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori",
               "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"} for i in range(16)}

p1 = 0
for sample in samples:
    possible = set()
    before, cmd, after = chunks(nums("".join(sample)), n=4)
    op, a, b, c = cmd
    if after[c] == before[a] + before[b]:
        possible.add("addr")
    if after[c] == before[a] + b:
        possible.add("addi")
    if after[c] == before[a] * before[b]:
        possible.add("mulr")
    if after[c] == before[a] * b:
        possible.add("muli")
    if after[c] == before[a] & before[b]:
        possible.add("banr")
    if after[c] == before[a] & b:
        possible.add("bani")
    if after[c] == before[a] | before[b]:
        possible.add("borr")
    if after[c] == before[a] | b:
        possible.add("bori")
    if after[c] == before[a]:
        possible.add("setr")
    if after[c] == a:
        possible.add("seti")
    if after[c] == (1 if a > before[b] else 0):
        possible.add("gtir")
    if after[c] == (1 if before[a] > b else 0):
        possible.add("gtri")
    if after[c] == (1 if before[a] > before[b] else 0):
        possible.add("gtrr")
    if after[c] == (1 if a == before[b] else 0):
        possible.add("eqir")
    if after[c] == (1 if before[a] == b else 0):
        possible.add("eqri")
    if after[c] == (1 if before[a] == before[b] else 0):
        possible.add("eqrr")

    if len(possible) >= 3:
        p1 += 1
    opcodes[op] &= possible

print(p1)

confirmed = set(next(iter(v)) for v in opcodes.values() if len(v) == 1)
while len(confirmed) != 16:
    opcodes = {op: v if len(v) == 1 else v - confirmed for op, v in opcodes.items()}
    confirmed = set(next(iter(v)) for v in opcodes.values() if len(v) == 1)
opcodes = {op: next(iter(v)) for op, v in opcodes.items()}


class Device(Interpreter):
    def parse_instructions(self, raw):
        self.instructions = [(opcodes[op], a, b, c) for op, a, b, c in chunks(nums(" ".join(raw)), n=4)]
        self.length = len(self.instructions)
        return self

    def _addr(self, a, b, c): self.registers[c] = self.registers[a] + self.registers[b]
    def _addi(self, a, b, c): self.registers[c] = self.registers[a] + b
    def _mulr(self, a, b, c): self.registers[c] = self.registers[a] * self.registers[b]
    def _muli(self, a, b, c): self.registers[c] = self.registers[a] * b
    def _banr(self, a, b, c): self.registers[c] = self.registers[a] & self.registers[b]
    def _bani(self, a, b, c): self.registers[c] = self.registers[a] & b
    def _borr(self, a, b, c): self.registers[c] = self.registers[a] | self.registers[b]
    def _bori(self, a, b, c): self.registers[c] = self.registers[a] | b
    def _setr(self, a, b, c): self.registers[c] = self.registers[a]
    def _seti(self, a, b, c): self.registers[c] = a
    def _gtir(self, a, b, c): self.registers[c] = 1 if a > self.registers[b] else 0
    def _gtri(self, a, b, c): self.registers[c] = 1 if self.registers[a] > b else 0
    def _gtrr(self, a, b, c): self.registers[c] = 1 if self.registers[a] > self.registers[b] else 0
    def _eqir(self, a, b, c): self.registers[c] = 1 if a == self.registers[b] else 0
    def _eqri(self, a, b, c): self.registers[c] = 1 if self.registers[a] == b else 0
    def _eqrr(self, a, b, c): self.registers[c] = 1 if self.registers[a] == self.registers[b] else 0


p2 = Device().parse_instructions(program).run().registers[0]
print(p2)

if args.test:
    args.tester(p1, p2)
