from utils import *

args = parse_args(year=2024, day=14)
raw = get_input(args["filename"], year=2024, day=14)

robots = [tuple(nums(line))[::-1] for line in raw.splitlines()]
R, C = 103, 101

robots_100 = []
for vr, vc, pr, pc in robots:
    robots_100.append(((pc + 100 * vc) % C, (pr + 100 * vr) % R))

q1 = sum([1 for c, r in robots_100 if c < C // 2 and r < R // 2])
q2 = sum([1 for c, r in robots_100 if c < C // 2 and r > R // 2])
q3 = sum([1 for c, r in robots_100 if c > C // 2 and r < R // 2])
q4 = sum([1 for c, r in robots_100 if c > C // 2 and r > R // 2])

p1 = q1 * q2 * q3 * q4
print(p1)

p2 = 0
while True:
    grid = [["." for _ in range(C)] for _ in range(R)]
    for _, _, r, c in robots:
        grid[r][c] = "#"
    tree = 0
    for row in grid:
        if "#####" in "".join(row):
            tree += 1
    if tree > 10:
        break
    robots = [(vr, vc, (pr + vr) % R, (pc + vc) % C) for vr, vc, pr, pc in robots]
    p2 += 1
print(p2)

assert p1 == 222208000
assert p2 == 7623
