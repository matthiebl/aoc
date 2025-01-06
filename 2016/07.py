"""
--- Day 7: Internet Protocol Version 7 ---
https://adventofcode.com/2016/day/7
"""

from utils import *

args = parse_args(year=2016, day=7)
raw = get_input(args.filename, year=2016, day=7)

ips = raw.splitlines()
alphabet = "abcdefghijklmnopqrstuvwxyz"


def has_abba(string):
    for a, b, c, d in windows(string, n=4):
        if a == b:
            continue
        if a + b == d + c:
            return True
    return False


def has_aba_bab(super, hyper):
    for a, b, c in windows(super, n=3):
        if a == b:
            continue
        if a == c and b + a + b in hyper:
            return True


p1 = 0
p2 = 0

for ip in ips:
    supernet = ""
    hypernet = ""
    for i, (j, k) in enumerate(windows([-1, *[i for i, c in enumerate(ip) if c in "[]"], len(ip)])):
        supernet += ip[j + 1:k] if i % 2 == 0 else "_"
        hypernet += ip[j + 1:k] if i % 2 == 1 else "_"
    if has_abba(supernet) and not has_abba(hypernet):
        p1 += 1
    if has_aba_bab(supernet, hypernet):
        p2 += 1

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
