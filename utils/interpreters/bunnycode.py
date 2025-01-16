
class BunnyCode:
    def __init__(self, instructions: list[str], a: int = 0, b: int = 0, c: int = 0, d: int = 0):
        self.instructions = [i.split() for i in instructions]
        self.length = len(instructions)
        self.registers = {"a": a, "b": b, "c": c, "d": d}
        self.ip = 0

    def run(self):
        while self.ip < self.length:
            (instruction, *parts) = self.instructions[self.ip]
            if instruction == "inc":
                if self._is_addition():
                    continue
                [x] = parts
                if x in self.registers:
                    self.registers[x] += 1
            elif instruction == "dec":
                [x] = parts
                if x in self.registers:
                    self.registers[x] -= 1
            elif instruction == "cpy":
                x, y = parts
                if y in self.registers:
                    self.registers[y] = self.registers[x] if x in self.registers else int(x)
            elif instruction == "jnz":
                x, y = parts
                if (self.registers[x] if x in self.registers else int(x)) != 0:
                    self.ip += self.registers[y] if y in self.registers else int(y)
                    continue
            elif instruction == "tgl":
                [x] = parts
                target = self.ip + self.registers[x] if x in self.registers else int(x)
                if 0 <= target < self.length:
                    if len(self.instructions[target]) == 2:
                        self.instructions[target][0] = "dec" if self.instructions[target][0] == "inc" else "inc"
                    else:
                        self.instructions[target][0] = "cpy" if self.instructions[target][0] == "jnz" else "jnz"
            self.ip += 1
        return self.registers["a"]

    def _is_addition(self) -> bool:
        if self.ip > self.length - 3:
            return False
        instructions = self.instructions[self.ip:self.ip+3]
        if [i[0] for i in instructions] != ["inc", "dec", "jnz"] or instructions[2][-1] != "-2" or instructions[1][1] != instructions[2][1]:
            return False
        x = instructions[0][1]
        y = instructions[1][1]
        if x not in self.registers or y not in self.registers:
            return False
        self.registers[x] += self.registers[y]
        self.registers[y] = 0
        self.ip += 3
        return True
