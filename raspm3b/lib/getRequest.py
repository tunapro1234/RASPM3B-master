from BaseHTTPServer import BaseHTTPRequestHandler
from threading import thread
import raspm3b.lib.firmpy
import SocketServer

class MyHandler(BaseHTTPRequestHandler):
    def __init__(self, ip, port, arduino):
        super().__init__()
        
        self.arduino = arduino
        self.port = int(port)
        self.ip = str(ip)
        
    def do_GET(self):
        try:
            self.path = self.path.split("/")
            if not self.path[1].isdigit():
                raise Exception("tunapro1234")
                return False
                                    
            elif self.path[0] == "nano":
                if self.path[2].isdigit() or self.path[2].startswith("c"):
                    self.arduino.write(self.path[1], self.path[2])
                else:
                    return False
                                        
            # elif self.path[0] == "mega":
                # if self.path[2].isdigit() or self.path[2].startswith("c"):
                #     nano.write(self.path[1], self.path[2])
                # else:
                #     return False

        self.send_response(200)
        return True
        
    def start_server(self):
        httpd = SocketServer.TCPServer((self.ip, self.port), self)
        httpd.serve_forever()