class Intcode:
    opcodes = {1: "add", 2: "mul", 99: "halt"}

    def __init__(self, program: list[int]):
        self.memory = program
        self.ip = 0
        self.halted = False

    def run(self):
        while not self.halted:
            opcode = self.next()
            op_fn = getattr(self, f"opcode_{self.opcodes.get(opcode, 'error')}")
            op_fn(code=opcode)

    def next(self) -> int:
        """Get the next int from memory and push the instruction pointer."""
        n = self.memory[self.ip]
        self.ip += 1
        return n

    def get(self, i: int) -> int:
        return self.memory[i]

    def opcode_add(self, **kwargs):
        i, j, k = self.next(), self.next(), self.next()
        self.memory[k] = self.get(i) + self.get(j)

    def opcode_mul(self, **kwargs):
        i, j, k = self.next(), self.next(), self.next()
        self.memory[k] = self.get(i) * self.get(j)

    def opcode_halt(self, **kwargs):
        self.halted = True

    def opcode_error(self, **kwargs):
        raise ValueError(f"Opcode does not exist: {kwargs['code']}")
