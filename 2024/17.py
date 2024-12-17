"""
--- Day 17: Chronospatial Computer ---
https://adventofcode.com/2024/day/17
"""

from math import lcm
from utils import *

args = parse_args(year=2024, day=17)
numbers = list(nums(get_input(args.filename, year=2024, day=17)))
A = numbers[0]
code = numbers[3:]


def run(A):
    B = 0
    C = 0
    output = []
    ip = 0
    while ip < len(code) - 1:
        ins, lit = code[ip], code[ip + 1]
        
        comb = None
        if 0 <= lit <= 3:
            comb = lit
        elif lit == 4:
            comb = A
        elif lit == 5:
            comb = B
        elif lit == 6:
            comb = C
        
        if ins == 0:
            A = A >> comb
        elif ins == 1:
            B = B ^ lit
        elif ins == 2:
            B = comb % 8
        elif ins == 3:
            if A != 0:
                ip = lit - 2
        elif ins == 4:
            B = B ^ C
        elif ins == 5:
            output.append(str(comb % 8))
        elif ins == 6:
            B = A >> comb
        elif ins == 7:
            C = A >> comb

        ip += 2
    return output


p1 = ",".join(run(A))
print(p1)


def construct(i, start):
    if i == -1:
        return int(start, 8)
    total = [construct(i - 1, start + n) for n in "01234567" if run(int(start + n, 8))[0] == str(code[i])]
    return min(total) if total else 8 ** 17


p2 = construct(len(code) - 1, "0o")
print(p2)

if args.test:
    args.tester(p1, p2)
