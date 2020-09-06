from time import time, sleep
import pyfirmata, sys, os

class Arduino(pyfirmata.Arduino):
    def __init__(self, port, s_pins, invert):
        # pyfirmata.Arduino.__init__(port)
        super().__init__(port)
        self.invert = invert
        self.s_pins = s_pins
        self.port = port
        
        it = pyfirmata.util.Iterator(self)
        sleep(1)
        it.start()

        for index, s_pin in enumerate(s_pins):
            new_pin = self.get_pin("d:" + str(s_pin) + ":o")
            new_pin.write(self.invert - 1)            
            self.s_pins[index] = [int(s_pin), new_pin]
    
    def write_(self, pin, state):
        try:
            pin_index = [i for i in range(len(self.s_pins)) if self.s_pins[i][0] == int(pin)]
            if len(pin_index) == 1:
                pin_index = pin_index[0]
                if type(state) == int or state.isdigit():
                    self.s_pins[pin_index][1].write(self.invert - int(state))
                elif state.startswith("c"):
                    read = self.s_pins[pin_index][1].read()
                    print("READ: " + str(read))
                    if 0 < read < 1:
                        self.s_pins[pin_index][1].write(1 - int(self.s_pins[pin_index][1].read()))
                    else:
                        self.write_(pin, 1)
                else:
                    raise Exception("ahahahah")
        except:
            return False
        else:
            return True

    def write_all(self, state):
        try:
            [self.write_(i[0], state) for i in self.s_pins]
        except:
            return False
        else:
            return True        
        
def test():
    pass


if __name__ == "__main__":
    test()