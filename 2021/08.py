"""
--- Day 8: Seven Segment Search ---
https://adventofcode.com/2021/day/8
"""

from utils import *

args = parse_args(year=2021, day=8)
raw = get_input(args.filename, year=2021, day=8)

lines = [line.split() for line in raw.splitlines()]

p1 = 0
p2 = 0

for line in lines:
    numbers, value = line[:10], line[-4:]

    one = set(next(number for number in numbers if len(number) == 2))
    four = set(next(number for number in numbers if len(number) == 4))

    result = ""
    for number in value:
        if len(number) in [2, 3, 4, 7]:
            p1 += 1

        if len(number) == 2:
            result += "1"
        elif len(number) == 3:
            result += "7"
        elif len(number) == 4:
            result += "4"
        elif len(number) == 5:  # 2, 3, 5
            if len(one & set(number)) == 2:
                result += "3"
            elif len(four & set(number)) == 2:
                result += "2"
            else:
                result += "5"
        elif len(number) == 6:  # 0, 6, 9
            if len(four & set(number)) == 4:
                result += "9"
            elif len(one & set(number)) == 2:
                result += "0"
            else:
                result += "6"
        elif len(number) == 7:
            result += "8"

    p2 += int(result)

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
