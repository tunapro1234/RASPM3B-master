from time import time, sleep
import pyfirmata, sys, os

class Arduino(pyfirmata.Arduino):
    def __init__(self, port, s_pins):
        # pyfirmata.Arduino.__init__(port)
        super().__init__(port)
        self.s_pins = s_pins
        self.port = port

        for index, s_pin in enumerate(s_pins):
            self.s_pins[index] = [int(s_pin), self.get_pin("d:" + str(s_pin) + ":o")]
    
    def write_(self, pin, state):
        try:
            pin_index = [i for i in range(len(self.s_pins)) if self.s_pins[i][0] == int(pin)]
            if len(pin_index) == 1:
                pin_index = pin_index[0]
                if state.isdigit() or type(state) == int:
                    self.s_pins[pin_index][1].write(int(state))
                elif state.startswith("c"):
                    self.s_pins[pin_index][1].write(1 - int(self.s_pins[pin_index][1].read()))
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