from constants import MEMORY_SIZE


class Memory():

    def __init__(self):
        self._memory = [0] * MEMORY_SIZE  #memory initialized with zero bytes

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


