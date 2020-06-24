from time import time, sleep
import pyfirmata, sys, os

class Arduino(pyfirmata.Arduino):
    def __init__(self, port, s_pins):
        pyfirmata.Arduino.__init__(port)
        self.s_pins = s_pins
        self.port = port

        for index, s_pin in enumerate(s_pins):
            self.s_pins[index] = [int(s_pin), self.get_pin("d:" + int(s_pin) + ":o")]
    
    def write_(self, pin, state):
        pin_index = [i for i in range(len(self.s_pins)) if self.s_pins[i][0] == int(pin)]
        if pin_index:
            if state.isdigit():
                self.s_pins[pin_index][1].write(state)
            elif state.startswith("c"):
                self.s_pins[pin_index][1].write(1 - self.s_pins[pin_index][1].read())

def test():
    pass


if __name__ == "__main__":
    test()