from collections import defaultdict, deque
from copy import deepcopy


class Interpreter:

    def __init__(self, instructions: list = [], queue: list = [], registers: dict = {}, regtype=int, **init_registers: dict):
        self.instructions = deepcopy(instructions)
        self.length = len(self.instructions)
        self.ip = 0

        # initialise registers - supports both a dictionary and kwargs as initialisers
        self.registers = defaultdict(regtype)
        self.registers.update(registers)
        self.registers.update(init_registers)

        self.input = deque(queue)
        self.output = deque([])

        self.halt = False
        self.complete = False

    def parse_instructions(self, raw: str):
        """
        Parses a raw version of the instructions into a useable version.

        Must set `self.instructions` and `self.length` attributes.
        """
        self.instructions = [line.split() for line in raw.splitlines()]
        self.length = len(self.instructions)
        return self

    def value(self, x: str):
        if x[0] in "-+" or x.isnumeric():
            return int(x)
        return self.registers[x]

    def run(self):
        """
        Runs the program. Ends execution if program finished naturally or `self.halt` is set to `True`.

        `self.complete` will be set to `True` if the program finished naturally.
        """
        self.halt = False
        while 0 <= self.ip < self.length and not self.halt:
            [op, *args] = self.instructions[self.ip]
            jmp = getattr(self, f"_{op}")(*args)
            self.ip += 1 if jmp is None else jmp
        self.complete = not self.halt
        return self

    # --- Operations ---
    # All operations are methods in the format `_{name}`
    # Should return the change to the instruction pointer or None for +1

    def _set(self, x, y): self.registers[x] = self.value(y)
    def _cpy(self, x, y): self.registers[y] = self.value(x)
    def _inp(self, x): self.registers[x] = self.input.popleft()
    def _add(self, x, y): self.registers[x] += self.value(y)
    def _sub(self, x, y): self.registers[x] -= self.value(y)
    def _mul(self, x, y): self.registers[x] *= self.value(y)
    def _div(self, x, y): self.registers[x] //= self.value(y)
    def _mod(self, x, y): self.registers[x] %= self.value(y)
    def _inc(self, x): self.registers[x] += 1
    def _dec(self, x): self.registers[x] -= 1
    def _hlf(self, x): self.registers[x] //= 2
    def _dbl(self, x): self.registers[x] *= 2
    def _tpl(self, x): self.registers[x] *= 3

    def _jmp(self, x): return self.value(x)
    def _jnz(self, x, y): return self.value(y) if self.value(x) != 0 else 1
    def _jez(self, x, y): return self.value(y) if self.value(x) == 0 else 1
    def _jgz(self, x, y): return self.value(y) if self.value(x) > 0 else 1
    def _jlz(self, x, y): return self.value(y) if self.value(x) < 0 else 1

    def _snd(self, x): self.output.append(self.value(x))

    def _rcv(self, x):
        if len(self.input) == 0:
            self.halt = True
            return 0
        self.registers[x] = self.input.popleft()

    # --- Other ---

    def __repr__(self):
        return f"{type(self).__name__}(registers={self.registers})"
