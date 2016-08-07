from common.commands import *

# Constants for getting number of cycles for special cases
REGULAR = 0  # For commands that performs always for the same number of cycles

REGISTER = 0  # For commands that processes registers
MEMORY = 1  # For commands that processes memory cell

NEXT_CMD = 0  # For return and call commands when condition is not satisfied
RET = 1  # For return commands when condition is satisfied
CALL = 1  # For call commands when condition is satisfied


cycles = {

    # Move, load and store

    mov: [5, 7],  # 5 for registers, 7 for memory
    mvi: [7, 10],  # 7 for registers, 10 for memory
    lxi: [10],
    stax: [7],
    ldax: [7],
    sta: [13],
    lda: [13],
    shld: [16],
    lhld: [16],
    xchg: [4],

    # Stack operations

    push: [11],
    pop: [10],
    xthl: [18],
    sphl: [5],

    # Jump

    jmp: [10],
    jc: [10],
    jnc: [10],
    jz: [10],
    jnz: [10],
    jp: [10],
    jm: [10],
    jpe: [10],
    jpo: [10],
    pchl: [5],

    # Call

    call: [17],
    cc: [11, 17],  # 11 for next command, 17 for call
    cnc: [11, 17],  # 11 for next command, 17 for call
    cz: [11, 17],  # 11 for next command, 17 for call
    cnz: [11, 17],  # 11 for next command, 17 for call
    cp: [11, 17],  # 11 for next command, 17 for call
    cm: [11, 17],  # 11 for next command, 17 for call
    cpe: [11, 17],  # 11 for next command, 17 for call
    cpo: [11, 17],  # 11 for next command, 17 for call

    # Return

    ret: [10],
    rc: [5, 11],  # 5 for next command, 11 for return
    rnc: [5, 11],  # 5 for next command, 11 for return
    rz: [5, 11],  # 5 for next command, 11 for return
    rnz: [5, 11],  # 5 for next command, 11 for return
    rp: [5, 11],  # 5 for next command, 11 for return
    rm: [5, 11],  # 5 for next command, 11 for return
    rpe: [5, 11],  # 5 for next command, 11 for return
    rpo: [5, 11],  # 5 for next command, 11 for return

    # Restart

    rst: [11],

    # Increment and decrement

    inr: [5, 10],  # 5 for registers, 10 for memory
    dcr: [5, 10],  # 5 for registers, 10 for memory
    inx: [5],
    dcx: [5],

    # Add

    add: [4, 7],  # 4 for registers, 7 for memory
    adc: [4, 7],  # 4 for registers, 7 for memory
    adi: [7],
    aci: [7],
    dad: [10],

    # Subtract

    sub: [4, 7],  # 4 for registers, 7 for memory
    sbb: [4, 7],  # 4 for registers, 7 for memory
    sui: [7],
    sbi: [7],

    # Logical

    ana: [4, 7],  # 4 for registers, 7 for memory
    xra: [4, 7],  # 4 for registers, 7 for memory
    ora: [4, 7],  # 4 for registers, 7 for memory
    cmp: [4, 7],  # 4 for registers, 7 for memory
    ani: [7],
    xri: [7],
    ori: [7],
    cpi: [7],

    # Rotate

    rlc: [4],
    rrc: [4],
    ral: [4],
    rar: [4],

    # Specials

    cma: [4],
    stc: [4],
    cmc: [4],
    daa: [4],

    # Input/Output

    in_cmd: [10],
    out: [10],

    # Control

    ei: [4],
    di: [4],
    nop: [4],
    hlt: [7]

}
