class Port():

    def __init__(self):
        self.port_number = None
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback
