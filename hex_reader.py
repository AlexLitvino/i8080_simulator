import re
from constants import MEMORY_SIZE


def populate_memory(file_path):
    memory = [0] * MEMORY_SIZE

    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith(';'):
                if line.endswith('\n'):
                    line = line[:-1]# Last line of file doesn't contain 'n' so it shouldn't be cut off
                if line != '':
                    splitted_line = re.split(r"[ ;\t]", line)
                    splitted_line = [item for item in splitted_line if item not in ['']]
                    addr = int(splitted_line[0], 16)
                    value = int(splitted_line[1], 16)
                    memory[addr] = value
    return memory

if __name__ == "__main__":
    file_name = "hello.hex"
    m = populate_memory(file_name)


