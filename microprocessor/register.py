from common.utilities import get_bit


class Register:

    def __init__(self, name, accumulator, status_register):
        self.name = name
        self.value = 0
        self.A = accumulator
        self.F = status_register

    def normalization(self):
        if 0 <= self.value <= 255:
            pass
        else:
            self.value = self.value % 256


    ####################################################################################################################
    # Methods for processing register commands
    ####################################################################################################################

    def add(self, summand):
        self.value = self.value + summand
        # register flags update
        self.normalization()

    def adi(self):
        raise NotImplementedError("ADI is not implemented yet.")

    def adc(self):
        raise NotImplementedError("ADC is not implemented yet.")

    def aci(self):
        raise NotImplementedError("ACI is not implemented yet.")

    def sub(self):
        raise NotImplementedError("SUB is not implemented yet.")

    def sui(self):
        raise NotImplementedError("SUI is not implemented yet.")

    def sbb(self):
        raise NotImplementedError("SBB is not implemented yet.")

    def sbi(self):
        raise NotImplementedError("SBI is not implemented yet.")

    def inr(self):
        self.value += 1
        # register flags update
        self._update_P_flag()
        self._update_S_flag()
        self._update_Z_flag()
        self._update_A_flag()
        self.normalization()

    def dcr(self):
        self.value -= 1
        # register flags update
        self._update_P_flag()
        self._update_S_flag()
        self._update_Z_flag()
        self._update_A_flag()
        self.normalization()

    def ana(self):
        raise NotImplementedError("ANA is not implemented yet.")

    def ani(self):
        raise NotImplementedError("ANI is not implemented yet.")

    def ora(self):
        raise NotImplementedError("ORI is not implemented yet.")

    def xra(self):
        raise NotImplementedError("XRA is not implemented yet.")

    def xri(self):
        raise NotImplementedError("XRI is not implemented yet.")

    # TODO: should CMP and CPI be implemented in Register?
    # def cmp(self):
    #     raise NotImplementedError("CMP is not implemented yet.")
    #
    # def cpi(self):
    #     raise NotImplementedError("CPI is not implemented yet.")

    # Rotate commands applied only to Accumulator
    # def rlc(self):
    #     raise NotImplementedError("RLC is not implemented yet.")
    #
    # def rrc(self):
    #     raise NotImplementedError("RRC is not implemented yet.")
    #
    # def ral(self):
    #     raise NotImplementedError("RAL is not implemented yet.")
    #
    # def rar(self):
    #     raise NotImplementedError("RAR is not implemented yet.")

    ####################################################################################################################
    # Methods to update flags
    ####################################################################################################################
    def _update_S_flag(self):
        if get_bit(self.value, 7) == 1:
            self.F.set_flag('S')
        else:
            self.F.clear_flag('S')

    def _update_Z_flag(self):
        if self.value == 0:
            self.F.set_flag('Z')
        else:
            self.F.clear_flag('Z')

    def _update_A_flag(self):
        # if condition:
        #     self.F.set_flag('A')
        # else:
        #     self.F.clear_flag('A')
        # raise NotImplementedError("Updating A flag is not implemented yet.")
        pass

    def _update_P_flag(self):
        binary_string = bin(self.value)
        unit_number = binary_string.count('1')
        if unit_number % 2 == 0:
            self.F.set_flag('P')
        else:
            self.F.clear_flag('P')

    def _update_C_flag(self):
        # if condition:
        #     self.F.set_flag('C')
        # else:
        #     self.F.clear_flag('C')
        # raise NotImplementedError("Updating C flag is not implemented yet.")
        pass
