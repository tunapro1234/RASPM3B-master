import raspm3b.gui.main as graphical
import raspm3b.tui.main as console
from raspm3b.lib import firmpy

mod = "console"

def main(mode=mod):
    def func():
        return firmpy.Arduino(port="/dev/ttyUSB0", s_pins=[3, 4, 5], invert=True)

    if mode.startswith("c"):
        console.main(func)
    
    elif mode.startswith("g"):
        graphical.main(func)
    