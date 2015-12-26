

def get_bit(value, index):
    return value & (1 << index)

def get_bits(value, start_index, end_index):
    mask = 2 ** (end_index - start_index + 1) - 1
    print("mask::" + "{0:b}".format(mask))

    mask = mask << start_index
    print("mask::" + "{0:b}".format(mask))


    temp = value & mask
    print("temp::" + "{0:b}".format(temp))

    ret_val = temp >> start_index
    print("ret_val::" + "{0:b}".format(ret_val))

    #print("mask::" + "{0:b}".format(mask))#shift to right
    #print("mask::" + "{0:b}".format(value & mask >> start_index))
    return 0


a = 0b101
print("{0:b}".format(a))

#get_bit(a, 4)
get_bits(a, 1, 8)