class OldComputerEmulator:

  def __init__(self):
    self.memory = [0] * 1000  # initialize memory with 1000 slots
    self.registers = [0] * 10  # initialize 10 registers

  def load_program(self, program):
    d = 0
    for ligne in program:
      self.memory[d] = ligne
      d = d + 1

  def run_program(self):
    code = self.memory
    for instruction in code:
      if self.execute_instruction(instruction):  # execute each instruction
        break
  
  def execute_instruction(self, instruction):
    if instruction == 100:
        return True
    elif instruction == 200:
      self.registers[0] = self.registers[1] + self.registers[2]
      
    elif instruction == 300:
      self.registers[0] = self.registers[1] - self.registers[2]
      
    elif instruction == 400:
      self.registers[0] = self.registers[1] * self.registers[2]
      
    elif instruction == 500:
      self.registers[0] = self.registers[1] / self.registers[2]
    elif instruction == 600:
      # set a register value
      self.registers[instruction % 10] = self.registers[(instruction // 10) % 10]
    elif instruction == 700:
        jump_to = self.registers[1]
        if jump_to < len(code):
            self.memory[0] = jump_to
    elif instruction == 800:
        if self.registers[3] == 1:
          jump_to = self.registers[1]
          if jump_to < len(code):
              self.memory[0] = jump_to
    elif instruction == 900:
        self.registers[0] = self.registers[1] or self.registers[2]
        pass
    elif instruction == 1000:
      if self.registers[0] != 0:
       pass
  def reverse_string(s):
    return s[::-1]


class BasicCoderConsole:

  def __init__(self, computer):
    self.computer = computer  # reference to the OldComputerEmulator

  def write_code(self, code):
    self.computer.load_program(code)  # write code to the computer

  def run_code(self):
    self.computer.run_program()  # run code on the computer


basic = BasicCoderConsole(OldComputerEmulator())
code = [
  100, 200, 300, 400, 500, 600, 700, 800, 900, 1000
]
basic.write_code(code)
basic.run_code()