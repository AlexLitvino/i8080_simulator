from misc_registers import Accumulator
from register import Register


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