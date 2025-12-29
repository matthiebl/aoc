from collections import deque
from typing import Any


class Intcode:
    opcodes = {
        1: "add",
        2: "mul",
        3: "input",
        4: "output",
        5: "jit",
        6: "jif",
        7: "lt",
        8: "eq",
        99: "halt",
    }

    def __init__(self, program: list[int]):
        self.memory = program
        self.ip = 0
        self.halted = False
        self.input: deque[Any] = deque()
        self.output: deque[Any] = deque()

    def run(self) -> None:
        while not self.halted:
            opcode, modes = self.get_opcode()
            op_fn = getattr(self, f"opcode_{self.opcodes.get(opcode, 'error')}")
            op_fn(modes=modes, code=opcode)

    def next(self) -> int:
        """Get the next int from memory and push the instruction pointer."""
        n = self.memory[self.ip]
        self.ip += 1
        return n

    def add_input(self, any: Any) -> None:
        self.input.append(any)

    def take_output(self) -> Any:
        return self.output.popleft()

    def get(self, i: int, mode: int = 0) -> int:
        if mode == 1:
            return i
        return self.memory[i]

    def get_opcode(self) -> tuple[int, list[int]]:
        raw = self.next()
        opcode = raw % 100
        modes = list(map(int, str(raw // 100)))[::-1]
        return opcode, modes + [0] * 10

    def opcode_add(self, **kwargs: Any) -> None:
        modes: list[int] = kwargs["modes"]
        i, j, addr = self.next(), self.next(), self.next()
        self.memory[addr] = self.get(i, modes[0]) + self.get(j, modes[1])

    def opcode_mul(self, **kwargs: Any) -> None:
        modes: list[int] = kwargs["modes"]
        i, j, addr = self.next(), self.next(), self.next()
        self.memory[addr] = self.get(i, modes[0]) * self.get(j, modes[1])

    def opcode_input(self, **kwargs: Any) -> None:
        i, addr = self.input.popleft(), self.next()
        self.memory[addr] = i

    def opcode_output(self, **kwargs: Any) -> None:
        modes: list[int] = kwargs["modes"]
        i = self.next()
        self.output.append(self.get(i, modes[0]))

    def opcode_jit(self, **kwargs: Any) -> None:
        modes: list[int] = kwargs["modes"]
        i, j = self.next(), self.next()
        if self.get(i, modes[0]):
            self.ip = self.get(j, modes[1])

    def opcode_jif(self, **kwargs: Any) -> None:
        modes: list[int] = kwargs["modes"]
        i, j = self.next(), self.next()
        if not self.get(i, modes[0]):
            self.ip = self.get(j, modes[1])

    def opcode_lt(self, **kwargs: Any) -> None:
        modes: list[int] = kwargs["modes"]
        i, j, addr = self.next(), self.next(), self.next()
        self.memory[addr] = 1 if self.get(i, modes[0]) < self.get(j, modes[1]) else 0

    def opcode_eq(self, **kwargs: Any) -> None:
        modes: list[int] = kwargs["modes"]
        i, j, addr = self.next(), self.next(), self.next()
        self.memory[addr] = 1 if self.get(i, modes[0]) == self.get(j, modes[1]) else 0

    def opcode_halt(self, **kwargs: Any) -> None:
        self.halted = True

    def opcode_error(self, **kwargs: Any) -> None:
        raise ValueError(f"Opcode does not exist: {kwargs['code']}")
