from raspm3b.res.globalv import *
import sys, os


def command_list(command=""):
    if not command:
        return ["clear", "exit", "help", "nano", "server"]

def clear():
    os.system("clear")

def exit():
    exit()

def help(command):
    return "Available commands:\n" + "\n".join(command_list(command))

def nano(args, Arduino):
    args = [i for i in args[5:].split("(").split(",").split(")").split(" ") if i != ""]
    
    if args[0] == "write_all" and len(args) == 2:
        Arduino.write_all(args[1])
    
    elif args[0] == "write" and len(args) == 3:
        Arduino.write_(args[1], args[2])

# server start komutunu filan ekle
        
        
def test():
    pass

if __name__ == "__main__":
    test()
