# registers
A = "A"
F = "F"
B = "B"
C = "C"
D = "D"
E = "E"
H = "H"
L = "L"
M = "M"  # reference to memory - memory cell with address saved in HL register pair

# register pairs
BC = "BC"
DE = "DE"
HL = "HL"
SP = "SP"
AF = "AF"

# conditions used in jump
NZ = "NZ"
Z = "Z"
NC = "NC"
C = "C"  # TODO: the same as register C, should be changed
PO = "PO"
PE = "PE"
P = "P"
M = "M"  # TODO: the same as reference to memory, should be changed

rrr = {
    0b000: B,
    0b001: C,
    0b010: D,
    0b011: E,
    0b100: H,
    0b101: L,
    0b110: M,  # reference to memory - memory cell with address saved in HL register pair
    0b111: A
}

dd = {
    0b00: BC,
    0b01: DE,
    0b10: HL,
    0b11: SP
}

qq = {
    BC: 0b00,
    DE: 0b01,
    HL: 0b10,
    AF: 0b11
}

ccc = {
    NZ: 0b000,
    Z: 0b001,
    NC: 0b010,
    C: 0b011,
    PO: 0b100,
    PE: 0b101,
    P: 0b110,
    M: 0b111
}
