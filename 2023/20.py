#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

LOW = 'LOW'
HIGH = 'HIGH'
STOP = 'STOP'

modules = {}
signals = {
    LOW: 0,
    HIGH: 0,
}


def push_button():
    Q = [('broadcaster', LOW, None)]
    while Q:
        name, recv, last = Q.pop(0)
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

    for module in modules:
        for output in modules[module]['outputs']:
            if output in modules and modules[output]['type'] == '&':
                modules[output]['memory'][module] = LOW

    for t in range(1000):
        push_button()
    p1 = u.mul(signals.values())
    print(f'{p1=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '20.in'
    main(file)
