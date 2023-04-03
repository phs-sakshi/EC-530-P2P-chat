import socket
import threading

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def connect(self):
        self.socket.connect((self.host, self.port))

    def send(self, msg):
        self.socket.sendall(msg.encode('utf-8'))

    def receive(self):
        while True:
            r_msg = self.socket.recv(1024)
            if not r_msg:
                break
            if r_msg == b'':
                pass
            else:
                print(r_msg.decode('utf-8'))

    def start(self):
        self.connect()
        thread1 = threading.Thread(target=self.receive)
        thread1.start()
        while True:
            msg = input()
            if msg == 'exit':
                self.socket.close()
                break
            else:
                self.send(msg)

if __name__ == '__main__':
    client = Client('localhost', 11111)
    client.start()
