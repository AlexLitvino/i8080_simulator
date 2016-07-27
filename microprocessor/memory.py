from common.constants import MEMORY_SIZE
from common.utilities import hex_formatter


class Memory:

    def __init__(self):
        self._memory = [0] * MEMORY_SIZE  # memory initialized with zero bytes

    def __getitem__(self, key):
        if 0 <= key <= MEMORY_SIZE - 1:
            return self._memory[key]
        else:
            raise Exception

    def __setitem__(self, key, value):
        if 0 <= key <= MEMORY_SIZE - 1:
            self._memory[key] = value
        else:
            raise Exception

    def dump(self, start_address=0, end_address=16):
        """
        Prints memory content along with addresses from start_address to end_address (including boundaries)
        :param start_address: starting address to print memory content; 0 by default
        :param end_address: ending address to print memory content; 16 by default
        :return: None
        """
        for address in range(start_address, end_address + 1):
            print("M[" + hex_formatter(address) + "]:" + hex_formatter(self._memory[address]))
