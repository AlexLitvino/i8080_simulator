from register import Register
from utilities import get_bit


class Accumulator(Register):
    pass

# TODO: Should it be moved to constant file?
flags_bits = {
    'S': 7,
    'Z': 6,
    'A': 4,
    'P': 2,
    'C': 0
}


class StatusRegister():
    """
    Flag register (F) bits:

    7 	6 	5 	4 	3 	2 	1 	0
    S 	Z 	0 	A 	0 	P 	1 	C

    S - Sign Flag
    Z - Zero Flag
    0 - Not used, always zero
    A - also called AC, Auxiliary Carry Flag
    0 - Not used, always zero
    P - Parity Flag
    1 - Not used, always one
    C - Carry Flag
    """

    def __init__(self):
        self.value = 0b00000010

    def set_flag(self, flag_name):
        mask = (1<<flags_bits[flag_name])
        self.value = self.value | mask

    def clear_flag(self, flag_name):
        n= flags_bits[flag_name]
        mask = ((pow(2, 7 - n) - 1) << (7- n)) | (pow(2, n) - 1)
        self.value = self.value & mask

    def get_flag(self, flag_name):
        return get_bit(self.value, flags_bits[flag_name])

    def is_flag_set(self, flag_name):
        if self.get_flag(flag_name) == 1:
            return True
        else:
            return False

    def is_flag_cleared(self, flag_name):
        if self.get_flag(flag_name) == 0:
            return True
        else:
            return False


class StackPointer():
    pass


class ProgramCounter():
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

if __name__ == '__main__':
    pass
