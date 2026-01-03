from collections import defaultdict, deque
from copy import deepcopy
from typing import Any

from advent.utils.input_string import InputString


class Interpreter:
    def __init__(
        self,
        instructions: list[list[str]] = [],
        queue: list[int] = [],
        registers: dict[str, int] = {},
        **init_registers: int,
    ):
        self.instructions = deepcopy(instructions)
        self.length = len(self.instructions)
        self.ip = 0

        # initialise registers - supports both a dictionary and kwargs as initialisers
        self.registers: dict[str, int] = defaultdict(int)
        self.registers.update(registers)
        self.registers.update(init_registers)

        self.input = deque(queue)
        self.output: deque[int] = deque([])

        self.halted = False
        self.complete = False

    def parse_instructions(self, raw: InputString) -> "Interpreter":
        """
        Parses a raw version of the instructions into a useable version.

        Must set `self.instructions` and `self.length` attributes.
        """
        self.instructions = [line.split() for line in raw.lines()]
        self.length = len(self.instructions)
        return self

    def value(self, x: str) -> int:
        """
        Gets the value of `x`.

        If `x` is an integer, returns its value, otherwise the value in register `x`.
        """
        if x[0] in "-+" or x.isnumeric():
            return int(x)
        return self.registers[x]

    def instruction(self) -> list[str]:
        """
        Gets the current instruction to run.
        """
        return self.instructions[self.ip]

    def running(self) -> bool:
        return 0 <= self.ip < self.length and not self.halted

    def run(self) -> "Interpreter":
        """
        Runs the program.
        Ends execution if program finished naturally or `self.halted` is set to `True`.

        `self.complete` will be set to `True` if the program finished naturally.
        """
        self.halted = False
        while self.running():
            [op, *args] = self.instruction()
            self.pre_op(op, *args)
            res: int | None = self.operation(op)(*args)
            jmp = 1 if res is None else res
            self.post_op(jmp)
        self.complete = not self.halted
        return self

    def operation(self, op: str) -> Any:
        """
        Gets the current operation function to run.
        """
        return getattr(self, f"_op_{op}")

    def pre_op(self, op: str, *args: str) -> None:
        """
        Runs before the operation is executed.

        Takes the `op` that is about to execute, as well as its `args`.
        """
        pass

    def post_op(self, jmp: int) -> None:
        """
        Runs after the operation is executed.

        Takes the `jmp` length, and defaults to incrementing the instruction pointer by that length.
        """
        self.ip += jmp

    # --- Operations ---
    # All operations are methods in the format `_op_{name}`
    # Should return the change to the instruction pointer or None for +1

    def _op_set(self, x: str, y: str) -> None:
        self.registers[x] = self.value(y)

    def _op_cpy(self, x: str, y: str) -> None:
        self.registers[y] = self.value(x)

    def _op_inp(self, x: str) -> None:
        self.registers[x] = self.input.popleft()

    def _op_add(self, x: str, y: str) -> None:
        self.registers[x] += self.value(y)

    def _op_sub(self, x: str, y: str) -> None:
        self.registers[x] -= self.value(y)

    def _op_mul(self, x: str, y: str) -> None:
        self.registers[x] *= self.value(y)

    def _op_div(self, x: str, y: str) -> None:
        self.registers[x] //= self.value(y)

    def _op_mod(self, x: str, y: str) -> None:
        self.registers[x] %= self.value(y)

    def _op_inc(self, x: str) -> None:
        self.registers[x] += 1

    def _op_dec(self, x: str) -> None:
        self.registers[x] -= 1

    def _op_hlf(self, x: str) -> None:
        self.registers[x] //= 2

    def _op_dbl(self, x: str) -> None:
        self.registers[x] *= 2

    def _op_tpl(self, x: str) -> None:
        self.registers[x] *= 3

    def _op_jmp(self, x: str) -> int:
        return self.value(x)

    def _op_jnz(self, x: str, y: str) -> int:
        return self.value(y) if self.value(x) != 0 else 1

    def _op_jez(self, x: str, y: str) -> int:
        return self.value(y) if self.value(x) == 0 else 1

    def _op_jgz(self, x: str, y: str) -> int:
        return self.value(y) if self.value(x) > 0 else 1

    def _op_jlz(self, x: str, y: str) -> int:
        return self.value(y) if self.value(x) < 0 else 1

    def _op_snd(self, x: str) -> None:
        self.output.append(self.value(x))

    def _op_rcv(self, x: str) -> None:
        if len(self.input) == 0:
            self.halted = True
            return None
        self.registers[x] = self.input.popleft()

    # --- Other ---

    def __repr__(self) -> str:
        return f"{type(self).__name__}(registers={self.registers})"
