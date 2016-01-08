from utilities import get_bit
from utilities import get_bits

#cmd = XX YYY ZZZ
cmd = 20
print(bin(cmd))

#registers
A = "A"
F = "F"
B = "B"
C = "C"
D = "D"
E = "E"
H = "H"
L = "L"

#register pairs
BC = "BC"
DE = "DE"
HL = "HL"
SP = "SP"
AF = "AF"

#condition used in jump
NZ = "NZ"
Z = "Z"
NC = "NC"
C = "C"
PO = "PO"
PE = "PE"
P = "P"
M = "M"

'''
rrr = {
    B: 0b000,
    C: 0b001,
    D: 0b010,
    E: 0b011,
    H: 0b100,
    L: 0b101,
    #F: 0b110,#not used, flag register excluded
    A: 0b111
}
'''
rrr = {
    0b000: B,
    0b001: C,
    0b010: D,
    0b011: E,
    0b100: H,
    0b101: L,
    #0b110: F,#not used, flag register excluded
    0b111: A
}


dd = {
    BC: 0b00,
    DE: 0b01,
    HL: 0b10,
    SP: 0b11
}

qq = {
    BC: 0b00,
    DE: 0b01,
    HL: 0b10,
    AF: 0b11
}

ccc = {
    NZ: 0b000,
    Z:  0b001,
    NC: 0b010,
    C:  0b011,
    PO: 0b100,
    PE: 0b101,
    P:  0b110,
    M:  0b111
}

xx = get_bits(cmd, 6, 7)
page = xx

yyy = get_bits(cmd, 3, 5)
zzz = get_bits(cmd, 0, 2)
print(xx)
print(yyy)
print(zzz)


command = None
operand_1 = None
operand_2 = None


def page00_handler():
    pass

def page01_handler():
    ddd = yyy
    sss = zzz
    if ddd == 0b110 and sss == 0b110:
        command = "HALT"
    else:
        command = "MOV"
        operand_1 = rrr[ddd]
        operand_2 = rrr[sss]
    return (command, operand_1, operand_2)


def page10_handler():
    pass

def page11_handler():
    pass


if page == 0b00:
    page00_handler()
elif page == 0b01:
    page01_handler()
elif page == 0b10:
    page10_handler()
elif page == 0b11:
    page11_handler()
else:
    raise Exception("Incorrect command page.")


def cmd_decoder(cmd):
    pass







