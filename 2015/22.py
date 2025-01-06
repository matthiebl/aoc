"""
--- Day 22: Wizard Simulator 20XX ---
https://adventofcode.com/2015/day/22

This problem is rather simple when you use the right search method. The problem can be simplified down to a kind of
graph traversal, where the cost of moving between nodes (or game states) is the mana cost. Thus, if we use a
priority queue (we will use a heap), we can always try the lowest cost path first until we reach a win state.
"""

from utils import *

args = parse_args(year=2015, day=22)
raw = get_input(args.filename, year=2015, day=22)

health, damage = nums(raw)


def min_cost_to_win(hardmode=False):
    from heapq import heappush, heappop

    visited = set()
    heap = [(0, 50, health, 500, 0, 0, 0, True)]
    while heap:
        nxt = heappop(heap)
        if nxt in visited:
            continue
        visited.add(nxt)
        spent, hp, ehp, mana, shield, poison, recharge, player_turn = nxt

        if player_turn and hardmode:
            hp -= 1
            if hp <= 0:
                continue

        armour = 0
        if poison:
            ehp -= 3
            poison -= 1
        if shield:
            armour = 7
            shield -= 1
        if recharge:
            mana += 101
            recharge -= 1
        if ehp <= 0:
            return spent

        if player_turn:
            if mana >= 53:
                if ehp - 4 <= 0:
                    return spent + 53
                heappush(heap, (spent + 53, hp, ehp - 4, mana - 53, shield, poison, recharge, not player_turn))
            # drain
            if mana >= 73:
                if ehp - 2 <= 0:
                    return spent + 73
                heappush(heap, (spent + 73, hp + 2, ehp - 2, mana - 73, shield, poison, recharge, not player_turn))
            # shield
            if mana >= 113 and shield == 0:
                heappush(heap, (spent + 113, hp, ehp, mana - 113, 6, poison, recharge, not player_turn))
            # poison
            if mana >= 173 and poison <= 1:
                heappush(heap, (spent + 173, hp, ehp, mana - 173, shield, 6, recharge, not player_turn))
            # recharge
            if mana >= 229 and recharge <= 1:
                heappush(heap, (spent + 229, hp, ehp, mana - 229, shield, poison, 5, not player_turn))
        else:
            hp -= max(damage - armour, 1)
            if hp > 0:
                heappush(heap, (spent, hp, ehp, mana, shield, poison, recharge, not player_turn))


p1 = min_cost_to_win()
print(p1)
p2 = min_cost_to_win(hardmode=True)
print(p2)

if args.test:
    args.tester(p1, p2)
