"""
--- Day 17: Chronospatial Computer ---
https://adventofcode.com/2024/day/17

It took me a while to work towards the solution for part 2 today.

The main difficulty I found was there were lots of ideas I had come up with to try. But I wasn't able to work any of
them out in my head or on paper well enough due to a lack of ability with mental XOR-ing. I worked out my program did
the following:

```
do:
    C = A >> (A % 8 ^ 2)
    B = (A % 8 ^ 2 ^ 3) ^ C
    print(B)
    A = A >> 3
while A
```

Eventually, I decided to pursue creating the input register in reverse. The basis of this idea is under the
following assumptions:

1. `A` is only ever right shifted by 3, exactly once per loop
2. `B` and `C` are reinitialised every loop

With these assumptions, we can be confident in working backwards, since after printing the final digit, `A` must be set
to 0 to end the loop. Then the final digit will be printed based on the 3 most significant bits. We just need to check
8 numbers to find if they output the last digit. Then based on any input that achieves the last digit, we try to get
the second last digit by appending the next less significant bits, and recursing to the final digit based on any
configuration that continues to print the previous digit one by one until we have the entire original code.
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
        combo = A if operand == 4 else B if operand == 5 else C if operand == 6 else operand

        # The raw instructions are just condensed here:
        A = A >> combo if opcode == 0 else A
        B = (B ^ operand if opcode == 1 else combo % 8 if opcode == 2 else
             B ^ C if opcode == 4 else A >> combo if opcode == 6 else B)
        C = A >> combo if opcode == 7 else C
        output += [str(combo % 8)] if opcode == 5 else []
        ip = operand if opcode == 3 and A != 0 else ip + 2

    return output


p1 = ",".join(run(A))
print(p1)


def reverse_engineer(i: int, good_a_start: str):
    """We are taking an octal string as `good_a_start` which is a known good prefix for the last `n - i` digits."""
    if i == -1:
        return int(good_a_start, 8)
    total = [reverse_engineer(i - 1, good_a_start + n) for n in "01234567"
             if run(int(good_a_start + n, 8))[0] == str(code[i])]
    return min(total) if total else float("inf")


p2 = reverse_engineer(len(code) - 1, "0o")
print(p2)

if args.test:
    args.tester(p1, p2)
