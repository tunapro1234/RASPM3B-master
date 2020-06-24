from raspm3b.res.globalv import *
from raspm3b.tui import terminal

def command_handler(Arduino):
    while True:
        print(" >>> ", end="")
        command = input().split(" ")
        
        if [i[0] for i in terminal.command_list() if command[0].startswith(i[0])]:
            if command[0].startswith("c"):
                terminal.clear()
            
            elif command[0] in ["help", "h"]:
                if len(command) < 2:
                    command[1] = ""
                terminal.help(command[1])
            
            elif command[0].startswith("nano") and command[0][4] == ".":
                command = " ".join(command)
                terminal.nano(command, Arduino)
            
            
            # komutların devamı gelcek 


def main(ardFunc):
    try:
        Arduino = ardFunc()
    
    except:
        print(fail + "CANNOT IMPORT BOARDS.")
        return False
    
    else:
        command_handler(Arduino)