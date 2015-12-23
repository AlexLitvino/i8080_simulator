def main():
    pass

if __name__ == '__main__':
    main()


prg = """
.ORG 8000
LOAD A, 3
LOAD B, 5
ADD B
OUT 40
"""

print(prg)
#prg_lines = prg.split('\n')
prg_lines = prg.split('\n')[1: -1]#
print(prg_lines)

asm = []

#cmd_template = {label:, line:, command:, op1:, op2:, comment:}

class Memory():
    raise NotImplemented

class Processor():

    def __init__(self):
        pass
        #PC - programm counter
        #SP - stack pointer


#Commands
'''
ADD
SUB
RET
INC
DEC



'''




memory = [1,2,3,3,5,6,7,8]
a = 0
start = 0

addr = start

cmds = {
1:"add",
2:"sub",
3:"out"
}

def add():
    global a
    global addr
    a = memory[addr + 1] + memory[addr + 2]
    addr += 2
    print(a)

def sub():
    a = memory[addr + 1] - memory[addr + 2]
    addr += 2

def out():
    global addr
    print("IN CMD == 3")
    print(a)
    addr += 1


def unknown():
    global addr
    print("Unknown command")
    addr += 1

i = 1
while i < 10 and i < len(memory):
    globals()[cmds.get(cmd, "unknown")]()



    '''
    if cmd == 1:
        a = memory[addr + 1] + memory[addr + 2]
        addr += 2
        print(a)
    elif cmd == 2:
        a = memory[addr + 1] - memory[addr + 2]
        addr += 2
    elif cmd == 3:
        print("IN CMD == 3")
        print(a)
        addr += 1
    else:
        print("Unknown command")
        addr += 1
    '''



    print("addr::" + str(addr))

    i += 1
    #print(i)
#print(globals())

