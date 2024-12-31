"""
--- Day 15: ... ---
https://adventofcode.com/2023/day/15
"""

from collections import defaultdict
from utils import *

args = parse_args(year=2023, day=15)
raw = get_input(args.filename, year=2023, day=15)

strings = raw.split(",")


def hash_string(string: str) -> int:
    hash_value = 0
    for c in string:
        hash_value = ((hash_value + ord(c)) * 17) % 256
    return hash_value


p1 = sum(map(hash_string, strings))
print(p1)

boxes = defaultdict(list)
focus = {}
for string in strings:
    index = string.index("=") if "=" in string else string.index("-")
    label = string[:index]
    label_hash = hash_string(label)
    if string[index] == "-":
        boxes[label_hash] = [lbl for lbl in boxes[label_hash] if lbl != label]
    else:
        focus[label] = int(string[index + 1:])
        if label not in boxes[label_hash]:
            boxes[label_hash].append(label)

p2 = 0
for box, labels in boxes.items():
    p2 += (box + 1) * sum((i + 1) * focus[label] for i, label in enumerate(labels))
print(p2)

if args.test:
    args.tester(p1, p2)
