def test():
    pass

if __name__ == "__main__":
    test()

else:
    import sys, os



def command_list(command=""):
    if not command:
        return ["clear", "exit", "help", "nano"]

def clear():
    os.system("clear")

def exit():
    exit()

def help(command):
    return "Available commands:\n" + "\n".join(command_list(command))

def nano(args, Arduino):
    args = args[5:]
    
    if args[:9] == "write_all":
        Arduino.write_all()
    
    elif args[:5] == "write":
        Arduino.write()
        