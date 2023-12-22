#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


class Mod:
    def __init__(self, kind, name, outputs) -> None:
        self.kind = kind
        self.name = name
        self.outputs: list[str] = outputs

    def process(self, signal: int, name: str):
        pass

    def __repr__(self) -> str:
        return f'<{self.kind}:{self.name}, out={self.outputs}>'


class Broad(Mod):
    def __init__(self, name, outputs) -> None:
        super().__init__('broadcaster', name, outputs)

    def process(self, signal: int, name: str):
        return signal


class Flip(Mod):
    def __init__(self, name, outputs) -> None:
        self.on = False
        super().__init__('flip-flop', name, outputs)

    def process(self, signal: int, name: str):
        if signal == 1:
            return -1
        self.on = not self.on
        return 1 if self.on else 0

    def __repr__(self) -> str:
        return f'<{self.kind}:{self.name}, out={self.outputs}, status={"on" if self.on else "off"}>'


class Conj(Mod):
    def __init__(self, name, outputs) -> None:
        self.mem = u.defaultdict(int)
        super().__init__('conjunction', name, outputs)

    def process(self, signal: int, name: str):
        self.mem[name] = signal
        if all(sig == 1 for sig in self.mem.values()):
            return 0
        return 1

    def __repr__(self) -> str:
        return f'<{self.kind}:{self.name}, out={self.outputs}, mem={self.mem}>'


def push_button(modules, t):
    low = 0
    high = 0
    Q = [('', modules['broadcaster'], 0)]

    while Q:
        prev, module, signal = Q.pop(0)
        module: Mod = module

        if signal == 0:
            low += 1
        else:
            high += 1

        output = module.process(signal, prev)
        if output == -1:
            continue

        for mod in module.outputs:
            if mod not in modules:
                if output == 0:
                    if mod == 'rx':
                        return 0, 0, True
                    low += 1
                else:
                    high += 1
                continue
            Q.append((module.name, modules[mod], output))
    return low, high, False


def main(file: str) -> None:
    print('Day 20')

    data = u.input_as_lines(file)
    modules = {}
    conj = []
    for line in data:
        [[name], outputs] = u.double_sep(line, ' -> ', ', ')
        if name[0] == '%':
            modules[name[1:]] = Flip(name[1:], outputs)
        elif name[0] == '&':
            modules[name[1:]] = Conj(name[1:], outputs)
            conj.append(name[1:])
        else:
            modules[name] = Broad(name, outputs)

    for mod in modules:
        for con in conj:
            if con in modules[mod].outputs:
                modules[con].mem[mod] = 0
    # for mod in modules:
    #     print(mod, modules[mod])

    low = 0
    high = 0
    t = 0
    while True:
        if t == 1000:
            p1 = low * high
            print(f'{p1=}')
        a, b, out = push_button(modules, t)
        if out:
            p2 = t
            print(f'{p2=}')
            break
        low += a
        high += b
        t += 1
        if t % 1000 == 0:
            print(t)


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '20.in'
    main(file)
