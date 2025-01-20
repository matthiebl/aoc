"""
--- Day 5: How About a Nice Game of Chess? ---
https://adventofcode.com/2016/day/5
"""

from _md5 import md5

from utils import *

args = parse_args(year=2016, day=5)
seed = get_input(args.filename, year=2016, day=5)

i = 1
p1 = ""
p2 = list("........")
while len(p1) < 8 or p2.count(".") > 0:
    hash = md5(f"{seed}{i}".encode()).hexdigest()
    if hash.startswith("00000"):
        if len(p1) < 8:
            p1 += hash[5]
        if hash[5] in "01234567" and p2[int(hash[5])] == ".":
            p2[int(hash[5])] = hash[6]
    i += 1
p2 = "".join(p2)

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
