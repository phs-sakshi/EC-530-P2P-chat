import socket
import threading

class Server:
    def __init__(self, port):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        self.socket.bind(('', self.port))
        self.socket.listen()
        (conn, addr) = self.socket.accept()
        thread1 = threading.Thread(target=self.connect, args=(conn,))
        thread1.start()
        while True:
            msg = input().replace('b', '')
            if msg == 'exit':
                conn.close()
                self.socket.close()
                break
            else:
                conn.sendall(msg.encode())

    def connect(self, conn):
        while True:
            received = conn.recv(1024)
            if received == b'':
                pass
            else:
                print(received)

if __name__ == '__main__':
    server = Server(11111)
    server.start()
