from utilities import get_bit
from utilities import get_bits

from registers import rrr

#cmd = XX YYY ZZZ


def page00_handler():
    pass


def page01_handler(yyy, zzz):
    command = None
    operand_1 = None
    operand_2 = None

    ddd = yyy
    sss = zzz
    if ddd == 0b110 and sss == 0b110:
        command = "HLT"
    else:
        command = "MOV"
        operand_1 = rrr[ddd]
        operand_2 = rrr[sss]
    return command, operand_1, operand_2


def page10_handler():
    pass


def page11_handler():
    pass


def cmd_decoder(cmd):
    xx = get_bits(cmd, 6, 7)
    page = xx

    yyy = get_bits(cmd, 3, 5)
    zzz = get_bits(cmd, 0, 2)

    if page == 0b00:
        page00_handler()
    elif page == 0b01:
        page01_handler(yyy, zzz)
    elif page == 0b10:
        page10_handler()
    elif page == 0b11:
        page11_handler()
    else:
        raise Exception("Incorrect command page.")
