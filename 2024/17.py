"""
--- Day 17: Chronospatial Computer ---
https://adventofcode.com/2024/day/17
"""

from utils import *

args = parse_args(year=2024, day=17)
numbers = list(nums(get_input(args.filename, year=2024, day=17)))
A = numbers[0]
code = numbers[3:]


def run(A: int, B: int = 0, C: int = 0):
    output = []
    ip = 0
    while ip < len(code) - 1:
        opcode, operand = code[ip], code[ip + 1]
        comb = A if operand == 4 else B if operand == 5 else C if operand == 6 else operand

        A = A >> comb if opcode == 0 else A
        B = B ^ operand if opcode == 1 else comb % 8 if opcode == 2 else B ^ C if opcode == 4 else A >> comb if opcode == 6 else B
        C = A >> comb if opcode == 7 else C
        output += [str(comb % 8)] if opcode == 5 else []
        ip = operand if opcode == 3 and A != 0 else ip + 2

    return output


p1 = ",".join(run(A))
print(p1)


def reverse_engineer(i, start):
    if i == -1:
        return int(start, 8)
    total = [reverse_engineer(i - 1, start + n) for n in "01234567" if run(int(start + n, 8))[0] == str(code[i])]
    return min(total) if total else float("inf")


p2 = reverse_engineer(len(code) - 1, "0o")
print(p2)

if args.test:
    args.tester(p1, p2)
