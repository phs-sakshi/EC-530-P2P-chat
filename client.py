import socket
import threading

# Set up server
HOST = ''  # Host IP address
PORT = 5000  # Port to listen on
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

# Set up list of clients
clients = []

def broadcast(msg, sender):
    """
    Broadcast a message to all connected clients

    :param msg: Message to broadcast
    :param sender: Client that sent the message
    """
    for client in clients:
        if client != sender:
            try:
                client.send(msg.encode())
            except:
                # Remove disconnected client
                clients.remove(client)

def handle_client(client):
    """
    Handle a client connection

    :param client: Client socket object
    """
    while True:
        try:
            msg = client.recv(1024).decode()
            broadcast(msg, client)
        except:
            # Remove disconnected client
            clients.remove(client)
            client.close()
            break

def accept_clients():
    """
    Accept incoming client connections
    """
    while True:
        client, addr = server.accept()
        clients.append(client)
        print(f'Connected to {addr}')

        # Start thread to handle client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == '__main__':
    # Start accepting clients
    print('Waiting for connections...')
    accept_clients()