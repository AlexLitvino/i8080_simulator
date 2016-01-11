class Register():

    def __init__(self, name, accumulator, flags):
        self.name = name
        self.value = 0
        self.flags = flags

    def normalization(self):
        if 0 <= self.value <= 255:
            pass
        else:
            self.value = self.value % 256

    def add(self, summand):
        self.value = self.value + summand
        #register flags update
        self.normalization()
