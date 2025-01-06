"""
--- Day 24: It Hangs in the Balance ---
https://adventofcode.com/2015/day/24

The solution here reuses the same logic from day 17 of this year. We first start by realising that for each
compartment to have the same weight, they must each weigh `total-weight / num-of-presents`. Now we have a target
weight, and the list of weights, we can reuse the liquid container problem from day 17 which had us find ways of
using containers to reach the target.

We have the same problem here, but now are only really concerned with the presents in the compartment Santa is in.
The other compartments will have some irrelevant combination of presents that sum to our target, but we do not
need that information.

To search all ways of taking presents to reach our target weight is somewhat slow, but by using a global minimum
number of presents we have already found, we can quit early on the combinations that are already worse that our
best. This cuts it down from ~6 => <1 seconds. Next we just need to keep track of the best quantum entanglement
every time we see our current minimum number of presents.
"""

from collections import defaultdict
from utils import *

args = parse_args(year=2015, day=24)
raw = get_input(args.filename, year=2015, day=24)

weights = list(nums(raw))


def present_entanglement(target: int, total: int = 0, taken: int = 0, i: int = 0,
                         quantum: int = 1, entanglement: dict = defaultdict(lambda: float("inf"))) -> int:
    global smallest
    if total > target or taken > smallest:
        return entanglement[smallest]
    if i == len(weights):
        if total == target and taken <= smallest:
            smallest = min(smallest, taken)
            entanglement[taken] = min(entanglement[taken], quantum)
        return entanglement[smallest]
    present_entanglement(target, total + weights[i], taken + 1, i + 1, quantum * weights[i], entanglement)
    present_entanglement(target, total, taken, i + 1, quantum, entanglement)
    return entanglement[smallest]


smallest = float("inf")
p1 = present_entanglement(sum(weights) // 3)
print(p1)

# assumption is we should be able to use even less presents than with 3 compartments
p2 = present_entanglement(sum(weights) // 4)
print(p2)

if args.test:
    args.tester(p1, p2)
