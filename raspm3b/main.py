# import raspm3b.gui.main as graphical
import raspm3b.tui.main as console
from raspm3b.lib import firmpy
import sys

mode = "console"

def main(mode=mode):
    def func():
        if sys.platform.startswith("win"): 
            return firmpy.Arduino(port="COM5", s_pins=[3, 4, 5, 13], invert=0)
        else:
            return firmpy.Arduino(port="/dev/ttyUSB0", s_pins=[3, 4, 5], invert=0)

    if mode.startswith("c"):
        console.main(func)
    
    # elif mode.startswith("g"):
    #     graphical.main(func)
    