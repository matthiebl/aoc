"""
--- Day 19: Go With The Flow ---
https://adventofcode.com/2018/day/19
"""

from utils import *

args = parse_args(year=2018, day=19)
raw = get_input(args.filename, year=2018, day=19)


class Device(Interpreter):
    def parse_instructions(self, raw: str):
        lines = raw.splitlines()
        self.ip = next(nums(lines.pop(0)))
        self.instructions = [[line.split()[0], *nums(line)] for line in lines]
        self.length = len(self.instructions)
        return self

    def instruction(self):
        return self.instructions[self.registers[self.ip]]

    def running(self):
        return 0 <= self.registers[self.ip] < self.length and not self.halt

    def pre_op(self, op, *args):
        if op == "seti" and args[0] == 0 and args[2] == self.ip:
            self.halt = True

    def post_op(self, jmp):
        self.registers[self.ip] += jmp

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


n1 = max(Device().parse_instructions(raw).run().registers.values())
p1 = sum(i for i in range(1, n1 // 2 + 1) if n1 % i == 0) + n1
print(p1)

n2 = max(Device(registers={0: 1}).parse_instructions(raw).run().registers.values())
p2 = sum(i for i in range(1, n2 // 2 + 1) if n2 % i == 0) + n2
print(p2)

if args.test:
    args.tester(p1, p2)
