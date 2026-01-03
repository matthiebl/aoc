from collections import deque
from typing import Any


class Intcode:
    OPCODES = {
        1: {"name": "add", "nargs": 3},
        2: {"name": "mul", "nargs": 3},
        3: {"name": "input", "nargs": 1},
        4: {"name": "output", "nargs": 1},
        5: {"name": "jit", "nargs": 2},
        6: {"name": "jif", "nargs": 2},
        7: {"name": "lt", "nargs": 3},
        8: {"name": "eq", "nargs": 3},
        99: {"name": "halt", "nargs": 0},
    }

    def __init__(self, program: list[int], replace: dict[int, int] = {}, queue: list[Any] = []):
        self.memory = program
        for idx, val in replace.items():
            self.memory[idx] = val
        self.ip = 0

        self.halted = False

        self.input: deque[Any] = deque(queue)
        self.output: deque[Any] = deque()

    def running(self) -> bool:
        return not self.halted

    def run(self) -> None:
        while self.running():
            opcode, op_fn, modes = self._get_opcode()
            op_fn(modes=modes, code=opcode)

    def _get(self, mode: int = 0) -> int:
        """
        Return the mode dependent value of the next value in memory.

        If `mode == 0`, then the value at memory is returned.

        If `mode == 1`, then the value itself is returned.
        """
        val = self.memory[self.ip]
        self.ip += 1

        if mode == 0:
            return self.memory[val]
        if mode == 1:
            return val

        raise ValueError(f"Intcode._get mode cannot be {mode}")

    def _get_opcode(self) -> tuple[int, Any, list[int]]:
        raw = self._get(mode=1)
        opcode = raw % 100

        modes = list(map(int, str(raw // 100)))[::-1]
        extra_modes = self.OPCODES[opcode]["nargs"] - len(modes)
        modes += [0] * extra_modes

        op_fn = getattr(self, f"_op_{self.OPCODES[opcode]['name']}")

        return opcode, op_fn, modes

    # --- Opcode Operations ---
    # All opcode operations are methods in the format `_op_{name}`

    def _op_add(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        y = self._get(modes[1])
        addr = self._get(mode=1)
        self.memory[addr] = x + y

    def _op_mul(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        y = self._get(modes[1])
        addr = self._get(mode=1)
        self.memory[addr] = x * y

    def _op_input(self, **kwargs: Any) -> None:
        x = self.input.popleft()
        addr = self._get(mode=1)
        self.memory[addr] = x

    def _op_output(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        self.output.append(x)

    def _op_jit(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        y = self._get(modes[1])
        if x:
            self.ip = y

    def _op_jif(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        y = self._get(modes[1])
        if not x:
            self.ip = y

    def _op_lt(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        y = self._get(modes[1])
        addr = self._get(mode=1)
        self.memory[addr] = int(x < y)

    def _op_eq(self, modes: list[int], **kwargs: Any) -> None:
        x = self._get(modes[0])
        y = self._get(modes[1])
        addr = self._get(mode=1)
        self.memory[addr] = int(x == y)

    def _op_halt(self, **kwargs: Any) -> None:
        self.halted = True

    def _op_error(self, **kwargs: Any) -> None:
        raise ValueError(f"Opcode does not exist: {kwargs['code']}")
