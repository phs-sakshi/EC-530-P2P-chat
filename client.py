import socket
import threading

# Set up client
HOST = '127.0.0.3'  # Local server IP address
PORT = 5001  # Port to connect to
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    """
    Receive messages from server and print them
    """
    while True:
        try:
            msg = client.recv(1024).decode()
            print(msg)
        except:
            # Server has disconnected
            client.close()
            break

def send_messages():
    """
    Send messages to server
    """
    while True:
        try:
            msg = input()
            client.send(msg.encode())
        except:
            # Server has disconnected
            client.close()
            break

if __name__ == '__main__':
    # Start threads to receive and send messages
    thread_receive = threading.Thread(target=receive_messages)
    thread_receive.start()

    thread_send = threading.Thread(target=send_messages)
    thread_send.start()
