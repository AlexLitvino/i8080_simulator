from constants import _IN, _OUT


class Port():

    def __init__(self, port_number, direction):
        self.port_number = None
        self.direction = direction
        self.callback = None
        self._value = 0

    #get method should be accessed for out ports, and set - for in ports
    def get_value(self):
        if self.direction == _OUT:
            return self._value
        else:
            raise AttributeError("")#Should be possibility to read data from in port?

    def set_value(self, value):
        if self.direction == _IN:
            self._value = value
        else:
            raise AttributeError("Data could not be written to out port.")

    def set_callback(self, callback):
        self.callback = callback
