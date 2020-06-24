# from http.server import ThreadingHTTPServer as HTTPServerCommand
from http.server import BaseHTTPRequestHandler 
from http.server import HTTPServer as HTTPServerCommand
from threading import Thread
# from raspm3b.res.globalv import *
import firmpy as firmpy
# import raspm3b.lib.firmpy
# from socketserver import TCPServer as HTTPServerCommand

fail = "[FAIL] "
info = "[INFO] "

arduinos = {}

class test:
    @staticmethod
    def write_(pin, state):
        print("write_ : " + str(pin) + " : " + str(state))

def func1(path):
    global arduinos
    print(arduinos)
    if path == "/favicon.ico":
        return 
    
    path = [i for i in path.split("/") if i != ""]
    
    try:
        arduinos[path[0]].write_(path[1], path[2])
        arduinos[path[0]].s_pins[0][1].write(1)     
        print(path)
    except:
        if len(path) >= 3:
            print(fail + "lib/firmpy write_ error")
            # print(path)
        else:
            print(fail + "lib/HTTPHandler func1 - path error: ")
            # print(path)
        return False
    else:
        return True
    
class HandlerPro(BaseHTTPRequestHandler):
    def do_GET(self):
        # print("GET REQUEST RECEIVED")
        func1(self.path)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()  
        
        html = "<html>"
        html +=     "<head>"
        html +=         "<title> RASPM </title>"
        html +=     "</head>"
        html +=     "<body>"
        
        html +=         "<br><a href=\"/nano/3/change\"\"><button> NANO 3 CHANGE </button></a>"
        html +=         "<a href=\"/nano/3/0\"\"><button> NANO 3 ON </button></a>"
        html +=         "<a href=\"/nano/3/1\"\"><button> NANO 3 OFF </button></a>"
        
        html +=         "<br><a href=\"/nano/4/change\"\"><button> NANO 4 CHANGE </button></a>"
        html +=         "<a href=\"/nano/4/0\"\"><button> NANO 4 ON </button></a>"
        html +=         "<a href=\"/nano/4/1\"\"><button> NANO 4 OFF </button></a>"
        
        html +=         "<br><a href=\"/nano/5/change\"\"><button> NANO 5 CHANGE </button></a>"
        html +=         "<a href=\"/nano/5/0\"\"><button> NANO 5 ON </button></a>"
        html +=         "<a href=\"/nano/5/1\"\"><button> NANO 5 OFF </button></a>"
        
        html +=     "</body>"
        html += "</html>"
        
        self.wfile.write(html.encode())
        

def test():
    global arduinos
    board0 = firmpy.Arduino("COM3", [3, 4, 5, 13])
    arduinos = {"nano" : board0}
    
    httpd = HTTPServerCommand(("localhost", 80), HandlerPro)
    print(info + "Started")
    httpd.serve_forever()
    print(info + "Ended")

if __name__ == "__main__":
    test()











