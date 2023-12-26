#!/usr/bin/env python3.12

import aocutils as u
from sys import argv
from math import lcm

import graphviz

LOW = 'LOW'
HIGH = 'HIGH'
STOP = 'STOP'

modules = {}
signals = {
    LOW: 0,
    HIGH: 0,
}


def reset_modules():
    for props in modules.values():
        if props['type'] == '%':
            props['on'] = False
        elif props['type'] == '&':
            for module in props['memory']:
                props['memory'][module] = LOW
    signals[LOW] = 0
    signals[HIGH] = 0


def push_button(check=None):
    Q = [('broadcaster', LOW, None)]
    while Q:
        name, recv, last = Q.pop(0)
        # print(name, recv, last, Q)
        if name == check and recv == LOW:
            return True
        props = modules[name]

        signals[recv] += 1

        send = recv
        if props['type'] == '&':
            props['memory'][last] = recv
            send = LOW if all(
                sig == HIGH for sig in props['memory'].values()) else HIGH
        elif props['type'] == '%':
            if recv == HIGH:
                continue
            props['on'] = not props['on']
            send = HIGH if props['on'] else LOW

        for nxt in props['outputs']:
            if nxt not in modules:
                signals[send] += 1
                continue
            Q.append((nxt, send, name))
    return False


def main(file: str) -> None:
    print('Day 20')

    data = u.input_as_lines(file)

    for info in data:
        name, rest = info.split(' -> ')
        outputs = rest.split(', ')

        props = {
            'type': name[0],
            'name': name[1:] if name[0] != 'b' else name,
            'outputs': outputs,
        }

        if props['type'] == '&':
            props['memory'] = {}
        elif props['type'] == '%':
            props['on'] = False

        modules[props['name']] = props

    nodes = set()
    edges = []
    rg_inputs = set()
    for module in modules:
        nodes.add((module, modules[module]['type']))
        for output in modules[module]['outputs']:
            nodes.add((output, ''))
            edges.append((module, output))
            if output == 'rg':
                rg_inputs.add(module)
            if output in modules and modules[output]['type'] == '&':
                modules[output]['memory'][module] = LOW

    dot = graphviz.Digraph('computer wires')

    for node, pre in nodes:
        dot.node(node, {'': '', '%': 'f-', '&': 'n-', 'b': ''}[pre] + node)
    dot.edges(edges)

    dot.render('output.gv')

    for _ in range(1000):
        push_button()
    p1 = u.mul(signals.values())
    print(f'{p1=}')

    times = []
    for check in rg_inputs:
        reset_modules()
        t = 0
        while True:
            t += 1
            low = push_button(check)
            if low:
                times.append(t)
                break

    p2 = lcm(*times)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '20.in'
    main(file)
