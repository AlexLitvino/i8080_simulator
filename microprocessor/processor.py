from time import clock
import sys
sys.path.append("./../")
sys.path.append("./../common")
#sys.path.append("./../microprocessor")

from microprocessor.memory import Memory
from microprocessor.register import Register
from microprocessor.instructions_decoder import cmd_decoder
from microprocessor.misc_registers import *
from microprocessor.port import Port
from hex_reader import populate_memory
from common.constants import _IN, _OUT
from common.utilities import get_bit, hex_formatter
from common.command_cycles import cycles
from common.command_cycles import REGULAR, REGISTER, MEMORY, NEXT_CMD, RET, CALL
import common.commands as cmd


class Processor:
    _MAX_LOOP = 30

    def __init__(self, file_name):
        self.file_name = file_name
        self.memory = Memory()
        #self.register_file = RegisterFile()
        # set PC to 0

        # TODO: None parameters, should be avoided?
        self.F = StatusRegister()
        self.A = Accumulator("A", None, self.F)  # accumulator

        self.PC = ProgramCounter()
        self.SP = StackPointer()

        self.B = Register("B", self.A, self.F)
        self.C = Register("C", self.A, self.F)
        self.D = Register("D", self.A, self.F)
        self.E = Register("E", self.A, self.F)
        self.H = Register("H", self.A, self.F)
        self.L = Register("L", self.A, self.F)

        self.in_ports = {}
        self.out_ports = {}

        self.frequency = 1
        self._halt_flag = False

    def start(self):
        pass

    def load(self):
        self.memory._memory = populate_memory(self.file_name)
        self.memory.dump()

    def dump(self):
        print('*'*20)
        print("A:" + hex_formatter(self.A.value) + '\t' + "F:" + "UNKNOWN")  # TODO: should add bin formatter or special printing for F register
        print("B:" + hex_formatter(self.B.value) + '\t' + "C:" + hex_formatter(self.C.value))
        print("D:" + hex_formatter(self.D.value) + '\t' + "E:" + hex_formatter(self.E.value))
        print("H:" + hex_formatter(self.H.value) + '\t' + "L:" + hex_formatter(self.L.value))
        print("PC:" + hex_formatter(self.PC.value))
        print("SP:" + "UNKNOWN")
        print('*'*20)

    def start_from_address(self, start_address):
        self.PC.value = start_address

    def _perform_clock_cycles(self, cycles):
        pass

    def get_port(self, port_number, direction):
        port = None
        ports_list = {_IN: self.in_ports, _OUT: self.out_ports}.get(direction, None)
        if port_number in ports_list:
            port = ports_list[port_number]
        else:
            port = Port(port_number, direction)
            ports_list[port_number] = port
        return port

    COMMAND_DICT = {}  # TODO: Is it necessary variable?

    def run(self):
        iteration = 0
        while True:
            print("Iteration " + str(iteration) + " Start" + '*'*10)
            #self.dump()
            print("PC = " + str(self.PC.value))
            print("MEMORY = " + str(self.memory[self.PC.value]))
            cmd_tuple = cmd_decoder(self.memory[self.PC.value])
            print("cmd_tuple::" + str(cmd_tuple))
            cmd_name = cmd_tuple[0]
            operand1 = cmd_tuple[1]
            operand2 = cmd_tuple[2]
            print("cmd_name::" + str(cmd_name))
            print("operand1::" + str(operand1))
            print("operand2::" + str(operand2))
            self._get_command_handler(cmd_name)(operand1, operand2)

            #self.dump()
            print("Iteration " + str(iteration) + " End" + '*'*10)
            print()

            if self._halt_flag:
                break

            iteration += 1
            if iteration >= Processor._MAX_LOOP:
                break

    def _get_command_handler(self, cmd_name):
        print(cmd_name)
        command = self.__getattribute__("_cmd_" + cmd_name + "_handler")
        return command

    def _clock(self, number_of_cycles, correction):
        pass

    ####################################################################################################################
    # Command handlers section
    ####################################################################################################################

    # Move, load and store

    def _cmd_mov_handler(self, operand1, operand2):
        raise NotImplementedError("MOV not implemented yet.")

    def _cmd_mvi_handler(self, operand1, operand2):
        command_start_time = clock()
        print("In MVI")
        destination = operand1
        print(destination)
        r = self.__getattribute__(destination)
        self.PC.inc()
        r.value = self.memory[self.PC.value]
        self.PC.inc()
        command_end_time = clock()
        self._clock(cycles[cmd.mvi][REGISTER], command_end_time - command_start_time)

    def _cmd_lxi_handler(self, operand1, operand2):
        # TODO: It doesn't support LXI SP
        print("In LXI")
        rp = operand1
        self.PC.inc()
        lb = self.memory[self.PC.value]
        self.__getattribute__(rp[1]).value = lb
        self.PC.inc()
        hb = self.memory[self.PC.value]
        self.__getattribute__(rp[0]).value = hb
        self.PC.inc()

    def _cmd_stax_handler(self, operand1, operand2):
        raise NotImplementedError("STAX not implemented yet.")

    def _cmd_ldax_handler(self, operand1, operand2):
        print("In LDAX")
        # Load A from the memory  cell with address Loc(BC)
        rp = operand1
        rh = self.__getattribute__(rp[0])
        print("rh::" + str(rh.name))
        rl = self.__getattribute__(rp[1])
        print("rl::" + str(rl.name))
        memory_address = (rh.value << 8) + rl.value
        print("memory_address " + str(memory_address))

        self.A.value = self.memory[memory_address]
        print("A::" + str(self.A.value))
        self.PC.inc()
        pass

    def _cmd_sta_handler(self, operand1, operand2):
        raise NotImplementedError("STA not implemented yet.")

    def _cmd_lda_handler(self, operand1, operand2):
        raise NotImplementedError("LDA not implemented yet.")

    def _cmd_shld_handler(self, operand1, operand2):
        raise NotImplementedError("SHLD not implemented yet.")

    def _cmd_lhld_handler(self, operand1, operand2):
        raise NotImplementedError("LHLD not implemented yet.")

    def _cmd_xchg_handler(self, operand1, operand2):
        raise NotImplementedError("XCHG not implemented yet.")

    # Stack operations

    def _cmd_push_handler(self, operand1, operand2):
        raise NotImplementedError("PUSH not implemented yet.")

    def _cmd_pop_handler(self, operand1, operand2):
        raise NotImplementedError("POP not implemented yet.")

    def _cmd_xthl_handler(self, operand1, operand2):
        raise NotImplementedError("XTHL not implemented yet.")

    def _cmd_sphl_handler(self, operand1, operand2):
        raise NotImplementedError("SPHL not implemented yet.")

    # Jump

    def _cmd_jmp_handler(self, operand1, operand2):
        raise NotImplementedError("JMP not implemented yet.")

    def _cmd_jc_handler(self, operand1, operand2):
        raise NotImplementedError("JC not implemented yet.")

    def _cmd_jnc_handler(self, operand1, operand2):
        raise NotImplementedError("JNC not implemented yet.")

    def _cmd_jz_handler(self, operand1, operand2):
        raise NotImplementedError("JZ not implemented yet.")

    def _cmd_jnz_handler(self, operand1, operand2):
        print("In JNZ")
        # TODO:
        self.PC.inc()
        ml = self.memory[self.PC.value]
        self.PC.inc()
        mh = self.memory[self.PC.value]
        #self.PC.inc()
        address = (mh << 8) + ml
        if self.F.is_flag_cleared('Z'):
            self.PC.value = address
        else:
            self.PC.inc()
        pass

    def _cmd_jp_handler(self, operand1, operand2):
        raise NotImplementedError("JP not implemented yet.")

    def _cmd_jm_handler(self, operand1, operand2):
        raise NotImplementedError("JM not implemented yet.")

    def _cmd_jpe_handler(self, operand1, operand2):
        raise NotImplementedError("JPE not implemented yet.")

    def _cmd_jpo_handler(self, operand1, operand2):
        raise NotImplementedError("JPO not implemented yet.")

    def _cmd_pchl_handler(self, operand1, operand2):
        raise NotImplementedError("PCHL not implemented yet.")

    # Call

    def _cmd_call_handler(self, operand1, operand2):
        raise NotImplementedError("CALL not implemented yet.")

    def _cmd_cc_handler(self, operand1, operand2):
        raise NotImplementedError("CC not implemented yet.")

    def _cmd_cnc_handler(self, operand1, operand2):
        raise NotImplementedError("CNC not implemented yet.")

    def _cmd_cz_handler(self, operand1, operand2):
        raise NotImplementedError("CZ not implemented yet.")

    def _cmd_cnz_handler(self, operand1, operand2):
        raise NotImplementedError("CNZ not implemented yet.")

    def _cmd_cp_handler(self, operand1, operand2):
        raise NotImplementedError("CP not implemented yet.")

    def _cmd_cm_handler(self, operand1, operand2):
        raise NotImplementedError("CM not implemented yet.")

    def _cmd_cpe_handler(self, operand1, operand2):
        raise NotImplementedError("CPE not implemented yet.")

    def _cmd_cpo_handler(self, operand1, operand2):
        raise NotImplementedError("CPO not implemented yet.")

    # Return

    def _cmd_ret_handler(self, operand1, operand2):
        raise NotImplementedError("RET not implemented yet.")

    def _cmd_rc_handler(self, operand1, operand2):
        raise NotImplementedError("RC not implemented yet.")

    def _cmd_rnc_handler(self, operand1, operand2):
        raise NotImplementedError("RNC not implemented yet.")

    def _cmd_rz_handler(self, operand1, operand2):
        raise NotImplementedError("RZ not implemented yet.")

    def _cmd_rnz_handler(self, operand1, operand2):
        raise NotImplementedError("RNZ not implemented yet.")

    def _cmd_rp_handler(self, operand1, operand2):
        raise NotImplementedError("RP not implemented yet.")

    def _cmd_rm_handler(self, operand1, operand2):
        raise NotImplementedError("RM not implemented yet.")

    def _cmd_rpe_handler(self, operand1, operand2):
        raise NotImplementedError("RPE not implemented yet.")

    def _cmd_rpo_handler(self, operand1, operand2):
        raise NotImplementedError("RPO not implemented yet.")

    # Restart

    def _cmd_rst_handler(self, operand1, operand2):
        raise NotImplementedError("RST not implemented yet.")

    # Increment and decrement

    def _cmd_inr_handler(self, operand1, operand2):
        raise NotImplementedError("INR not implemented yet.")

    def _cmd_dcr_handler(self, operand1, operand2):
        print("In DCR")
        r = operand1
        reg = self.__getattribute__(r)
        reg.dcr()
        self.PC.inc()
        pass

    def _cmd_inx_handler(self, operand1, operand2):
        # TODO: It doesn't support INX SP
        print("In INX")
        rp = operand1
        rh = self.__getattribute__(rp[0])
        rl = self.__getattribute__(rp[1])
        rp_value = (rh.value << 8) + rl.value
        rp_value += 1
        rh.value = (rp_value & 0xFF00) >> 8
        rl.value = (rp_value & 0xFF)
        self.PC.inc()
        pass

    def _cmd_dcx_handler(self, operand1, operand2):
        # TODO: It doesn't support DCX SP
        raise NotImplementedError("DCX not implemented yet.")

    # Add

    def _cmd_add_handler(self, operand1, operand2):
        raise NotImplementedError("ADD not implemented yet.")

    def _cmd_adc_handler(self, operand1, operand2):
        raise NotImplementedError("ADC not implemented yet.")

    def _cmd_adi_handler(self, operand1, operand2):
        raise NotImplementedError("ADI not implemented yet.")

    def _cmd_aci_handler(self, operand1, operand2):
        raise NotImplementedError("ACI not implemented yet.")

    def _cmd_dad_handler(self, operand1, operand2):
        raise NotImplementedError("DAD not implemented yet.")

    # Subtract

    def _cmd_sub_handler(self, operand1, operand2):
        raise NotImplementedError("SUB not implemented yet.")

    def _cmd_sbb_handler(self, operand1, operand2):
        raise NotImplementedError("SBB not implemented yet.")

    def _cmd_sui_handler(self, operand1, operand2):
        raise NotImplementedError("SUI not implemented yet.")

    def _cmd_sbi_handler(self, operand1, operand2):
        raise NotImplementedError("SBI not implemented yet.")

    # Logical

    def _cmd_ana_handler(self, operand1, operand2):
        raise NotImplementedError("ANA not implemented yet.")

    def _cmd_xra_handler(self, operand1, operand2):
        raise NotImplementedError("XRA not implemented yet.")

    def _cmd_ora_handler(self, operand1, operand2):
        raise NotImplementedError("ORA not implemented yet.")

    def _cmd_cmp_handler(self, operand1, operand2):
        raise NotImplementedError("CMP not implemented yet.")

    def _cmd_ani_handler(self, operand1, operand2):
        raise NotImplementedError("ANI not implemented yet.")

    def _cmd_xri_handler(self, operand1, operand2):
        raise NotImplementedError("XRI not implemented yet.")

    def _cmd_ori_handler(self, operand1, operand2):
        raise NotImplementedError("ORI not implemented yet.")

    def _cmd_cpi_handler(self, operand1, operand2):
        raise NotImplementedError("CPI not implemented yet.")

    # Rotate

    def _cmd_rlc_handler(self, operand1, operand2):
        raise NotImplementedError("RLC not implemented yet.")

    def _cmd_rrc_handler(self, operand1, operand2):
        raise NotImplementedError("RRC not implemented yet.")

    def _cmd_ral_handler(self, operand1, operand2):
        raise NotImplementedError("RAL not implemented yet.")

    def _cmd_rar_handler(self, operand1, operand2):
        raise NotImplementedError("RAR not implemented yet.")

    # Specials

    def _cmd_cma_handler(self, operand1, operand2):
        raise NotImplementedError("CMA not implemented yet.")

    def _cmd_stc_handler(self, operand1, operand2):
        raise NotImplementedError("STC not implemented yet.")

    def _cmd_cmc_handler(self, operand1, operand2):
        raise NotImplementedError("CMC not implemented yet.")

    def _cmd_daa_handler(self, operand1, operand2):
        raise NotImplementedError("DAA not implemented yet.")

    # Input/Output

    # TODO: this could not work because command named in_cmd
    def _cmd_in_handler(self, operand1, operand2):
        raise NotImplementedError("IN not implemented yet.")

    def _cmd_out_handler(self, operand1, operand2):
        print("In OUT")
        self.PC.inc()
        port_number = self.memory[self.PC.value]
        print("Output to port #" + str(port_number) + " value " + str(self.A.value))
        with open("output.txt", 'a') as f:
            f.write(str(chr(self.A.value)) + " ")
        self.PC.inc()
        pass

    # Control

    def _cmd_ei_handler(self, operand1, operand2):
        raise NotImplementedError("EI not implemented yet.")

    def _cmd_di_handler(self, operand1, operand2):
        raise NotImplementedError("DI not implemented yet.")

    def _cmd_nop_handler(self, operand1, operand2):
        raise NotImplementedError("NOP not implemented yet.")

    def _cmd_hlt_handler(self, operand1, operand2):
        print("In HLT")
        self.PC.inc()
        self._halt_flag = True
        pass

    ####################################################################################################################
    # End of command handlers section
    ####################################################################################################################

if __name__ == '__main__':
    file_name = "./../program_samples/hello.hex"

    processor = Processor(file_name)

    # port configuration
    processor.get_port(255, "IN").set_callback(print)
    processor.get_port(255, "IN").set_value(15)
    processor.get_port(255, "OUT").get_value()

    processor.load()
    processor.run()
