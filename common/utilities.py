def get_bit(value, index):
    """
    Returns bit in position index from byte value
    :param value: integer positive value
    :param index: number of target bit in byte, most-significant bit is considered on the left and has number 0.
    :return: bit in position index from byte value
    """
    return (value & (1 << index)) >> index


def get_bits(value, start_index, end_index):
    """
    Returns a set of bit in position from start_index till end_index indexes(inclusively) from byte value
    :param value: integer positive value
    :param start_index: the number of the first bit which will be included to result;
    most-significant bit is considered on the left and has number 0.
    :param end_index: the number of the last bit which will be included to result,
    end_index should be greater than start_index; most-significant bit is considered on the left and has number 0.
    :return: set of bit in position from start_index till end_index indexes(inclusively) from byte value
    """
    mask = 2 ** (end_index - start_index + 1) - 1
    mask = mask << start_index
    return (value & mask) >> start_index


def hex_formatter(decimal_number, is_capitalized=False):
    """
    Returns decimal number converted to hex string with prefix '0x' and leading zero if number less than 16
    :param decimal_number: number to convert to hex
    :param is_capitalized: True, if hex string should be uppercased. False by default
    :return: decimal number converted to hex string
    """
    hex_string = ""
    if 0 <= decimal_number < 16:
        hex_string = str(hex(decimal_number))
        hex_string = hex_string[0:2] + "0" + hex_string[2]
    elif decimal_number >= 16:
        hex_string = str(hex(decimal_number))
    else:
        raise NotImplemented()
    if is_capitalized:
        hex_string = hex_string[0:2] + hex_string[2:].upper()
    return hex_string

if __name__ == '__main__':
    pass
