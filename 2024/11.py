from utils import *

args = parse_args(year=2024, day=11)
raw = get_input(args["filename"], year=2024, day=11)

stones = list(nums(raw))


@memoize()
def split_stones_count(stone: int, time: int):
    if time == 0:
        return 1
    stone_str = str(stone)
    stone_str_len = len(stone_str)
    total = 0
    if stone == 0:
        total += split_stones_count(1, time - 1)
    elif stone_str_len % 2 == 0:
        total += split_stones_count(int(stone_str[:stone_str_len // 2]), time - 1)
        total += split_stones_count(int(stone_str[stone_str_len // 2:]), time - 1)
    else:
        total += split_stones_count(stone * 2024, time - 1)
    return total


p1 = sum(split_stones_count(s, 25) for s in stones)
print(p1)

p2 = sum(split_stones_count(s, 75) for s in stones)
print(p2)
