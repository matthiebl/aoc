from utils import *

args = parse_args(year=2024, day=1)
raw = get_input(args["filename"], year=2024, day=1)

pairs = list(chunks(nums(raw)))
left = sorted(x for x, _ in pairs)
right = sorted(y for _, y in pairs)

p1 = sum(abs(x - y) for x, y in zip(left, right))
print(p1)

p2 = sum(x * right.count(x) for x in left)
print(p2)
