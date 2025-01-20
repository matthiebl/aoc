"""
--- Day 21: Scrambled Letters and Hash ---
https://adventofcode.com/2016/day/21
"""

from itertools import permutations

import numpy as np

from utils import *

args = parse_args(year=2016, day=21)
raw = get_input(args.filename, year=2016, day=21)

instructions = raw.splitlines()


def scramble(password: str, instructions: list[str] = instructions) -> str:
    password = list(password)
    for instruction in instructions:
        if instruction.startswith("swap position"):
            i, j = nums(instruction)
            password[i], password[j] = password[j], password[i]
        elif instruction.startswith("swap letter"):
            _, _, a, _, _, b = instruction.split()
            mapping = {a: b, b: a}
            password = np.vectorize(lambda x: mapping[x] if x in mapping else x)(password).tolist()
        elif instruction.startswith("rotate based"):
            a = instruction.split()[-1]
            i = password.index(a)
            if i >= 4:
                i += 1
            password = np.roll(password, i + 1).tolist()
        elif instruction.startswith("rotate"):
            (i,) = nums(instruction)
            password = np.roll(password, i * (-1 if "left" in instruction else 1)).tolist()
        elif instruction.startswith("reverse"):
            i, j = sorted(nums(instruction))
            password = password[:i] + password[i:j + 1][::-1] + password[j + 1:]
        elif instruction.startswith("move"):
            i, j = nums(instruction)
            a = password.pop(i)
            password.insert(j + (0 if j <= i else 0), a)
    return "".join(password)


p1 = scramble("abcdefgh")
print(p1)

for a in permutations("abcdefgh"):
    if scramble(a) == "fbgdceah":
        p2 = "".join(a)
        break
print(p2)

if args.test:
    args.tester(p1, p2)
