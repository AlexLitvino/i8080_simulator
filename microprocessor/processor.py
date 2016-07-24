import sys
sys.path.append("./../common")

from microprocessor.memory import Memory
from microprocessor.register import Register
from microprocessor.instructions_decoder import cmd_decoder
from microprocessor.misc_registers import *
from microprocessor.port import Port
from hex_reader import populate_memory
from common.constants import _IN, _OUT
from common.utilities import get_bit, hex_formatter


class Processor:
    _MAX_LOOP = 30

    def __init__(self, file_name):
        self.file_name = file_name
        self.memory = Memory()
        #self.register_file = RegisterFile()
        # set PC to 0

        # TODO: None parameters, should be avoided?
        self.A = Accumulator("A", None, None)  # accumulator
        self.F = StatusRegister()

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
            self.dump()
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

            self.dump()
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

    ####################################################################################################################
    # Methods to update flags
    ####################################################################################################################
    def _update_S_flag(self, value):
        if get_bit(value, 7) == 1:
            self.F.set_flag('S')
        else:
            self.F.clear_flag('S')

    def _update_Z_flag(self, value):
        if value == 0:
            self.F.set_flag('Z')
        else:
            self.F.clear_flag('Z')

    def _update_A_flag(self, value):
        raise NotImplementedError("Updating A flag is not implemented yet.")
        '''
        if condition:
            self.F.set_flag('A')
        else:
            self.F.clear_flag('A')
        '''

    def _update_P_flag(self, value):
        binary_string = bin(value)
        unit_number = binary_string.count('1')
        if unit_number % 2 == 0:
            self.F.set_flag('P')
        else:
            self.F.clear_flag('P')

    def _update_C_flag(self, value):
        raise NotImplementedError("Updating C flag is not implemented yet.")
        '''
        if condition:
            self.F.set_flag('C')
        else:
            self.F.clear_flag('C')
        '''

    '''
    S - Sign Flag
    Z - Zero Flag
    0 - Not used, always zero
    A - also called AC, Auxiliary Carry Flag
    0 - Not used, always zero
    P - Parity Flag
    1 - Not used, always one
    C - Carry Flag
    '''
    ####################################################################################################################
    # Command handlers section
    ####################################################################################################################

    def _cmd_mvi_handler(self, operand1, operand2):
        print("In MVI")
        destination = operand1
        print(destination)
        r = self.__getattribute__(destination)
        self.PC.inc()
        r.value = self.memory[self.PC.value]
        self.PC.inc()
        pass

    def _cmd_lxi_handler(self, operand1, operand2):
        print("In LXI")
        rp = operand1
        self.PC.inc()
        lb = self.memory[self.PC.value]
        self.__getattribute__(rp[1]).value = lb
        self.PC.inc()
        hb = self.memory[self.PC.value]
        self.__getattribute__(rp[0]).value = hb
        self.PC.inc()

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

    def _cmd_out_handler(self, operand1, operand2):
        print("In OUT")
        self.PC.inc()
        port_number = self.memory[self.PC.value]
        print("Output to port #" + str(port_number) + " value " + str(self.A.value))
        with open("output.txt", 'a') as f:
            f.write(str(chr(self.A.value)) + " ")
        self.PC.inc()
        pass

    def _cmd_inx_handler(self, operand1, operand2):
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

    def _cmd_dcr_handler(self, operand1, operand2):
        print("In DCR")
        r = operand1
        reg = self.__getattribute__(r)
        reg.value -= 1
        #TODO: change flags
        self.PC.inc()
        # TODO: ZSPA flags should be set
        self._update_Z_flag(reg.value)
        self._update_S_flag(reg.value)
        self._update_P_flag(reg.value)
        #self._update_A_flag(reg.value)#TODO: uncomment when _update_A_flag will be implemented
        pass

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

    def _cmd_hlt_handler(self, operand1, operand2):
        print("In HLT")
        self.PC.inc()
        self._halt_flag = True
        pass

if __name__ == '__main__':
    file_name = "./../program_samples/hello.hex"

    processor = Processor(file_name)

    # port configuration
    processor.get_port(255, "IN").set_callback(print)
    processor.get_port(255, "IN").set_value(15)
    processor.get_port(255, "OUT").get_value()

    processor.load()
    processor.run()
