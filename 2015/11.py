"""
--- Day 11: Corporate Policy ---
https://adventofcode.com/2015/day/11
"""

from utils import *

args = parse_args(year=2015, day=11)
password = get_input(args.filename, year=2015, day=11)

alphabet = "abcdefghijklmnopqrstuvwxyz"


def next_password(password: str) -> str:
    last = password[-1]
    if last == "z":
        return next_password(password[:-1]) + "a"
    new = password[:-1] + chr(ord(last) + 1)
    if "i" in new or "o" in new or "l" in new:
        return next_password(new)
    return new


def valid_password(password: str) -> bool:
    if not any("".join(seq) in password for seq in windows(alphabet, 3)):
        return False
    if "i" in password or "o" in password or "l" in password:
        return False
    count = 0
    for c in alphabet:
        count += password.count(c + c)
    return count >= 2


while not valid_password(password):
    password = next_password(password)
p1 = password
print(p1)

password = next_password(password)
while not valid_password(password):
    password = next_password(password)
p2 = password
print(p2)

if args.test:
    args.tester(p1, p2)
