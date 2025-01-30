"""
--- Day 20: Pulse Propagation ---
https://adventofcode.com/2023/day/20
"""

from collections import deque
from enum import Enum
from math import lcm

from utils import *

args = parse_args(year=2023, day=20)
raw = get_input(args.filename, year=2023, day=20)


class Pulse(Enum):
    LOW = 0
    HIGH = 1
    STOP = 2


modules = {}
for info in raw.splitlines():
    name, rest = info.split(" -> ")

    props = {
        "type": name[0],
        "name": name[1:] if name[0] != "b" else name,
        "outputs": rest.split(", "),
    }

    if "rx" in props["outputs"]:
        rx_input = props["name"]
    if props["type"] == "&":
        props["memory"] = {}
    elif props["type"] == "%":
        props["on"] = False

    modules[props["name"]] = props

rx_input_inputs = set()
for module in modules:
    for output in modules[module]["outputs"]:
        if output == rx_input:
            rx_input_inputs.add(module)
        if output in modules and modules[output]["type"] == "&":
            modules[output]["memory"][module] = Pulse.LOW

signals = {
    Pulse.LOW: 0,
    Pulse.HIGH: 0,
}


def reset_modules():
    for props in modules.values():
        if props["type"] == "%":
            props["on"] = False
        elif props["type"] == "&":
            props["memory"] = {module: Pulse.LOW for module in props["memory"]}
    signals[Pulse.LOW] = 0
    signals[Pulse.HIGH] = 0


def push_button(check=None):
    queue = deque([("broadcaster", Pulse.LOW, None)])
    while queue:
        name, recv, last = queue.popleft()
        if name == check and recv == Pulse.LOW:
            return True
        props = modules[name]
        signals[recv] += 1

        send = recv
        if props["type"] == "&":
            props["memory"][last] = recv
            send = Pulse.LOW if all(sig == Pulse.HIGH for sig in props["memory"].values()) else Pulse.HIGH
        elif props["type"] == "%":
            if recv == Pulse.HIGH:
                continue
            props["on"] = not props["on"]
            send = Pulse.HIGH if props["on"] else Pulse.LOW

        for nxt in props["outputs"]:
            if nxt not in modules:
                signals[send] += 1
                continue
            queue.append((nxt, send, name))
    return False


for _ in range(1000):
    push_button()
p1 = mul(signals.values())
print(p1)

times = []
for input in rx_input_inputs:
    reset_modules()
    for t in range(10**9):
        if push_button(input):
            times.append(t + 1)
            break

p2 = lcm(*times)
print(p2)

if args.test:
    args.tester(p1, p2)
