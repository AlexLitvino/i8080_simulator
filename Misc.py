__author__ = '_Intel_'





def main():
    pass

if __name__ == '__main__':
    main()


prg = """
.ORG 8000
LOAD A, 3
LOAD B, 5
ADD B
OUT 40
"""

print(prg)
#prg_lines = prg.split('\n')
prg_lines = prg.split('\n')[1: -1]#
print(prg_lines)

asm = []

#cmd_template = {label:, line:, command:, op1:, op2:, comment:}








class Accumulator(Register):
    pass

class RegisterPair():

    def __init__(self, name, register_high, register_low):
        self.name = name
        self.register_high = register_high
        self.register_low = register_low


class RegisterFile():

    def __init__(self):
        self.A = Accumulator("A")#accumulator

        self.B = Register("B")
        self.C = Register("C")
        self.B = Register("D")
        self.E = Register("E")
        self.H = Register("H")
        self.H = Register("L")
        self.register = []

class Memory():
    raise NotImplemented

class Processor():

    def __init__(self):
        pass
        #PC - programm counter
        #SP - stack pointer


#Commands
'''
ADD
SUB
RET
INC
DEC



'''


