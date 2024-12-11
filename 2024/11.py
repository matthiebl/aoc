from utils import *

args = parse_args(year=2024, day=11)
raw = get_input(args["filename"], year=2024, day=11)

stones = list(nums(raw))


@memoize()
def split_stones_count(stone: int, time: int):
    if time == 0:
        return 1
    if stone == 0:
        return split_stones_count(1, time - 1)
    stone_str = str(stone)
    stone_str_len = len(stone_str)
    if stone_str_len % 2 == 0:
        return split_stones_count(int(stone_str[:stone_str_len // 2]), time - 1) + split_stones_count(int(stone_str[stone_str_len // 2:]), time - 1)
    return split_stones_count(stone * 2024, time - 1)


p1 = sum(split_stones_count(stone, 25) for stone in stones)
print(p1)

p2 = sum(split_stones_count(stone, 75) for stone in stones)
print(p2)
