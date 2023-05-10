import gevent
from gevent.server import StreamServer
from gevent.pool import Pool

# Redis uses port 6379; we need to bind port 6379 to a TCP Server
HOST = "localhost"
PORT = 6379

class ProtocolHandler():
    def handle_request(self):
        pass

    def write_response(self):
        pass

class Server():
    def __init__(self, host, port, max_clients):
        self.pool = Pool(max_clients)
        self.server = StreamServer((host, port), 
                                   self.connection_handler,
                                   spawn=self.pool)
        self.protocol = ProtocolHandler()
        self.kv = {}

    def connection_handler(self, conn, addr):
        sf = conn.makefile('rwb')

        while True:
            try:
                data = self.protocol.handle_request(sf)
            except:
                break
            
            try:
                resp = self.get_response(data)
            except:
                break

            self.protocol.write_response(sf, resp)

    def get_response(self, data):
        pass

    def run(self):
        self.server.serve_forever()
