from misc_registers import Accumulator, ProgramCounter, StackPointer, StatusRegister
from register import Register


class RegisterFile():

    def __init__(self):

        # TODO: None parameters, should be avoided?
        self.A = Accumulator("A", None, None)#accumulator
        self.F = StatusRegister()

        self.PC = ProgramCounter()
        self.SP = StackPointer()

        self.B = Register("B", self.A, self.F)
        self.C = Register("C", self.A, self.F)
        self.D = Register("D", self.A, self.F)
        self.E = Register("E", self.A, self.F)
        self.H = Register("H", self.A, self.F)
        self.L = Register("L", self.A, self.F)
        self.register = []
