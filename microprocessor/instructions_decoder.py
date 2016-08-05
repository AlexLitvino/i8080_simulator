from common.utilities import get_bit
from common.utilities import get_bits

from common.commands import *
from common.registers import rrr, ccc
from common.registers import NZ, Z, NC, C, PO, PE, P, M
from common.registers import BC, DE, HL
from common.registers import dd, qq

from common.exceptions import IncorrectCommandPageException, IncorrectCommandException


def page00_handler(yyy, zzz):
    command = None
    operand_1 = None
    operand_2 = None

    if yyy == 0b000 and zzz == 0b000:
        command = nop
    elif get_bit(yyy, 0) == 0 and zzz == 0b001:
        command = lxi
        register_pair_code = get_bits(yyy, 1, 2)
        operand_1 = dd[register_pair_code]
    elif get_bit(yyy, 0) == 1 and zzz == 0b001:
        command = dad
        register_pair_code = get_bits(yyy, 1, 2)
        operand_1 = dd[register_pair_code]
    elif yyy == 0b000 and zzz == 0b010:
        command = stax
        operand_1 = BC
    elif yyy == 0b010 and zzz == 0b010:
        command = stax
        operand_1 = DE
    elif yyy == 0b100 and zzz == 0b010:
        command = shld
    elif yyy == 0b110 and zzz == 0b010:
        command = sta
    elif yyy == 0b001 and zzz == 0b010:
        command = ldax
        operand_1 = BC
    elif yyy == 0b011 and zzz == 0b010:
        command = ldax
        operand_1 = DE
    elif yyy == 0b101 and zzz == 0b010:
        command = lhld
    elif yyy == 0b111 and zzz == 0b010:
        command = lda
    elif get_bit(yyy, 0) == 0 and zzz == 0b011:
        command = inx
        register_pair_code = get_bits(yyy, 1, 2)
        operand_1 = dd[register_pair_code]
    elif get_bit(yyy, 0) == 1 and zzz == 0b011:
        command = dcx
        register_pair_code = get_bits(yyy, 1, 2)
        operand_1 = dd[register_pair_code]
    elif zzz == 0b100:
        command = inr
        operand_1 = rrr[yyy]
    elif zzz == 0b101:
        command = dcr
        operand_1 = rrr[yyy]
    elif zzz == 0b110:
        command = mvi
        operand_1 = rrr[yyy]
    elif yyy == 0b000 and zzz == 0b111:
        command = rlc
    elif yyy == 0b001 and zzz == 0b111:
        command = rrc
    elif yyy == 0b010 and zzz == 0b111:
        command = ral
    elif yyy == 0b011 and zzz == 0b111:
        command = rar
    elif yyy == 0b100 and zzz == 0b111:
        command = dad
    elif yyy == 0b101 and zzz == 0b111:
        command = cma
    elif yyy == 0b110 and zzz == 0b111:
        command = stc
    elif yyy == 0b111 and zzz == 0b111:
        command = cmc

    return command, operand_1, operand_2


def page01_handler(yyy, zzz):
    command = None
    operand_1 = None
    operand_2 = None

    ddd = yyy
    sss = zzz
    if ddd == 0b110 and sss == 0b110:
        command = hlt
    else:
        command = mov
        operand_1 = rrr[ddd]
        operand_2 = rrr[sss]
    return command, operand_1, operand_2


def page10_handler(yyy, zzz):
    command = None
    operand_1 = rrr[zzz]
    operand_2 = None

    if yyy == 0b000:
        command = add
    elif yyy == 0b001:
        command = adc
    elif yyy == 0b010:
        command = sub
    elif yyy == 0b011:
        command = sbb
    elif yyy == 0b100:
        command = ana
    elif yyy == 0b101:
        command = xra
    elif yyy == 0b110:
        command = ora
    elif yyy == 0b111:
        command = cmp

    return command, operand_1, operand_2


def page11_handler(yyy, zzz):
    command = None
    operand_1 = None
    operand_2 = None

    if zzz == 0b000:
        # Conditional Return Instructions
        if yyy == ccc[NZ]:
            command = rnz
        elif yyy == ccc[Z]:
            command = rz
        elif yyy == ccc[NC]:
            command = rnc
        elif yyy == ccc[C]:
            command = rc
        elif yyy == ccc[PO]:
            command = rpo
        elif yyy == ccc[PE]:
            command = rpe
        elif yyy == ccc[P]:
            command = rp
        elif yyy == ccc[M]:
            command = rm

    if zzz == 0b001:
        command = pop
        register_pair_code = get_bits(yyy, 1, 2)
        operand_1 = qq[register_pair_code]
    elif yyy == 0b001 and zzz == 0b001:
        command = ret
    elif yyy == 0b011 and zzz == 0b001:
        raise IncorrectCommandException()
    elif yyy == 0b101 and zzz == 0b001:
        command = pchl
    elif yyy == 0b111 and zzz == 0b001:
        command = sphl

    elif zzz == 0b010:
        # Conditional Jump Instructions
        if yyy == ccc[NZ]:
            command = jnz
        elif yyy == ccc[Z]:
            command = jz
        elif yyy == ccc[NC]:
            command = jnc
        elif yyy == ccc[C]:
            command = jc
        elif yyy == ccc[PO]:
            command = jpo
        elif yyy == ccc[PE]:
            command = jpe
        elif yyy == ccc[P]:
            command = jp
        elif yyy == ccc[M]:
            command = jm

    elif yyy == 0b000 and zzz == 0b011:
        command = jmp
    elif yyy == 0b001 and zzz == 0b011:
        raise IncorrectCommandException()
    elif yyy == 0b010 and zzz == 0b011:
        command = out
    elif yyy == 0b011 and zzz == 0b011:
        command = in_cmd
    elif yyy == 0b100 and zzz == 0b011:
        command = xthl
    elif yyy == 0b101 and zzz == 0b011:
        command = xchg
    elif yyy == 0b110 and zzz == 0b011:
        command = di
    elif yyy == 0b111 and zzz == 0b011:
        command = ei

    elif zzz == 0b100:
        # Conditional Call Instructions
        if yyy == ccc[NZ]:
            command = cnz
        elif yyy == ccc[Z]:
            command = cz
        elif yyy == ccc[NC]:
            command = cnc
        elif yyy == ccc[C]:
            command = cc
        elif yyy == ccc[PO]:
            command = cpo
        elif yyy == ccc[PE]:
            command = cpe
        elif yyy == ccc[P]:
            command = cp
        elif yyy == ccc[M]:
            command = cm

    elif get_bit(yyy, 0) == 0 and zzz == 0b101:
        command = push
        register_pair_code = get_bits(yyy, 1, 2)
        operand_1 = qq[register_pair_code]
    elif yyy == 0b001 and zzz == 0b101:
        command = call
    elif yyy == 0b011 and zzz == 0b101:
        raise IncorrectCommandException()
    elif yyy == 0b101 and zzz == 0b101:
        raise IncorrectCommandException()
    elif yyy == 0b111 and zzz == 0b101:
        raise IncorrectCommandException()

    elif zzz == 0b111:
        command = rst
        operand_1 = yyy

    return command, operand_1, operand_2


def cmd_decoder(cmd):

    # cmd = XX YYY ZZZ#command structure for decoding

    xx = get_bits(cmd, 6, 7)
    page = xx

    yyy = get_bits(cmd, 3, 5)
    zzz = get_bits(cmd, 0, 2)

    decode_command = None

    if page == 0b00:
        decode_command = page00_handler(yyy, zzz)
    elif page == 0b01:
        decode_command = page01_handler(yyy, zzz)
    elif page == 0b10:
        decode_command = page10_handler(yyy, zzz)
    elif page == 0b11:
        decode_command = page11_handler(yyy, zzz)
    else:
        raise IncorrectCommandPageException()
    return decode_command

if __name__ == '__main__':
    pass
