"""
--- Day 9: Disk Fragmenter ---
https://adventofcode.com/2024/day/9
"""

from utils import *

args = parse_args(year=2024, day=9)
file = get_input(args.filename, year=2024, day=9)


# Part 1
disk = []
fid = 0
for i, size in enumerate(file):
    size = int(size)
    if i % 2 == 0:
        disk += [fid] * size
        fid += 1
    else:
        disk += [-1] * size

blanks = [i for i, fid in enumerate(disk) if fid == -1]
for i in blanks:
    while disk[-1] == -1:
        disk.pop()
    if len(disk) <= i:
        break
    disk[i] = disk.pop()
p1 = sum(i * fid for i, fid in enumerate(disk) if fid > 0)
print(p1)


# Part 2
files = {}
blanks = []
fid = 0
pos = 0
for i, size in enumerate(file):
    size = int(size)
    if i % 2 == 0:
        files[fid] = (pos, size)
        fid += 1
    elif size > 0:
        blanks.append((pos, size))
    pos += size

while fid > 0:
    fid -= 1
    (pos, size) = files[fid]
    for i, (start, length) in enumerate(blanks):
        if start >= pos:
            break
        if length >= size:
            files[fid] = (start, size)
            if size == length:
                blanks.pop(i)
            else:
                blanks[i] = (start + size, length - size)
            break

p2 = 0
for fid, (pos, size) in files.items():
    for x in range(pos, pos + size):
        p2 += x * fid
print(p2)

if args.test:
    args.tester(p1, p2)
