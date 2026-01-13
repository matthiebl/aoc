from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Any


class Intcode:
    @dataclass
    class Opcode:
        name: str
        nargs: int

    OPCODES = {
        1: Opcode(name="add", nargs=4),
        2: Opcode(name="mul", nargs=4),
        3: Opcode(name="input", nargs=2),
        4: Opcode(name="output", nargs=1),
        5: Opcode(name="jit", nargs=2),
        6: Opcode(name="jif", nargs=2),
        7: Opcode(name="lt", nargs=4),
        8: Opcode(name="eq", nargs=4),
        9: Opcode(name="rb_off", nargs=1),
        99: Opcode(name="halt", nargs=0),
    }

    def __init__(self, program: list[int], replace: dict[int, int] = {}, queue: list[Any] = []):
        self.memory = defaultdict(int)
        for idx, val in enumerate(program):
            self.memory[idx] = val
        for idx, val in replace.items():
            self.memory[idx] = val
        self.pointer = 0
        self.relative_base = 0

        self.halted = False

        self.input: deque[Any] = deque(queue)
        self.output: deque[Any] = deque()

    def running(self) -> bool:
        return not self.halted

    def run(self) -> None:
        while self.running():
            opcode, op_fn, modes = self._get_opcode()
            op_fn(modes=modes, code=opcode)

    def _get(self, mode: int = 0, address_mode: bool = False) -> int:
        """
        Return the mode dependent value of the next value in memory.

        If `mode == 0` (position mode), then the value at memory is returned.

        If `mode == 1` (immediate mode), then the value itself is returned.

        If `mode == 2` (relative mode), then the relative base plus the value is returned.
        """
        val = self.memory[self.pointer]
        self.pointer += 1

        if mode == 2:
            addr = self.relative_base + val
            return addr if address_mode else self.memory[addr]
        if mode == 1 or address_mode:
            return val
        if mode == 0:
            return self.memory[val]

        raise ValueError(f"Intcode._get mode cannot be {mode}")

    def _get_opcode(self) -> tuple[int, Any, list[int]]:
        raw = self._get(mode=1)
        opcode = raw % 100

        modes = list(map(int, str(raw // 100)))[::-1]
        modes += [0] * (self.OPCODES[opcode].nargs - len(modes))

        op_fn = getattr(self, f"_op_{self.OPCODES[opcode].name}")

        return opcode, op_fn, modes

    # --- Opcode Operations ---
    # All opcode operations are methods in the format `_op_{name}`

    def _op_add(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        y = self._get(modes[1])
        addr = self._get(modes[2], True)
        self.memory[addr] = x + y

    def _op_mul(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        y = self._get(modes[1])
        addr = self._get(modes[2], True)
        self.memory[addr] = x * y

    def _op_input(self, modes: list[int], **kwargs: Any) -> None:
        x = self.input.popleft()
        addr = self._get(modes[0], True)
        self.memory[addr] = x

    def _op_output(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        self.output.append(x)

    def _op_jit(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        y = self._get(modes[1])
        if x:
            self.pointer = y

    def _op_jif(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        y = self._get(modes[1])
        if not x:
            self.pointer = y

    def _op_lt(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        y = self._get(modes[1])
        addr = self._get(modes[2], True)
        self.memory[addr] = int(x < y)

    def _op_eq(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        y = self._get(modes[1])
        addr = self._get(modes[2], True)
        self.memory[addr] = int(x == y)

    def _op_rb_off(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        self.relative_base += x

    def _op_halt(self, **kwargs: Any) -> None:
        self.halted = True

    def _op_error(self, **kwargs: Any) -> None:
        raise ValueError(f"Opcode does not exist: {kwargs['code']}")
