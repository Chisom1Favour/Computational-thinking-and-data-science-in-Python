import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    @property
    def is_online(self):
        try:
            socket.create_connection((self.host, self.port), timeout=1)
            return True
        except OSError:
            return False

s = Server("google.com", 10)
if s.is_online:
    print("Up")