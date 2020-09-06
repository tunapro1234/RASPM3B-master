from raspm3b.res.globalv import *
from raspm3b.tui import terminal
import os

def runStartCommands(Arduino):
    print(info + "Starting...")    
    try:
        with open("raspm3b/res/StartCom.txt", "r") as file:
            startCom = file.read()
    except:
        print(fail + "Cannot run starting commands.")
        
    startCom = startCom.split("\n")

    if type(startCom) != str:
        for com in startCom:
            command_handler(Arduino, command=com)
    else:
        command_handler(Arduino, command=startCom)
        
    
def command_handler(Arduino, command=None):
    if command is None:
        print(" >>> ", end="")
        command = input()
    
    command = [i for i in command.split(" ") if i != ""]
    
    if len(command) > 0 and [i[0] for i in terminal.command_list() if command[0].startswith(i[0])]:
        if command[0].startswith("c"):
            terminal.clear()
        
        elif command[0] in ["h", "help"]:
            if len(command) < 2:
                command[1] = ""
            terminal.help(command[1])
        
        elif command[0].startswith("nano") and command[0][4] == ".":
            command = " ".join(command)
            terminal.nano(command, Arduino)
        
        elif command[0].startswith("server"):
            terminal.server(command, Arduino)
        
        # elif command[0] in ["e", "exit"]:
        #     # terminal.exitt()
        #     exit()
                        

def main(ardFunc):
    try:
        Arduino = ardFunc()
    
    except:
        print(fail + "Cannot import boards.")
        return False
    
    else:
        runStartCommands(Arduino)
        while True:
            command_handler(Arduino, None)