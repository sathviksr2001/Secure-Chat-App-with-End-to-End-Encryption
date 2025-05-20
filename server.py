import socket
import threading
from config import SERVER_HOST, SERVER_PORT

clients = []
client_names = []

def handle_client(client_socket, addr):
    name = client_socket.recv(1024).decode()
    client_names.append(name)
    print(f"[NEW CONNECTION] {name} connected from {addr}")
    broadcast(f"{name} has joined the chat!", client_socket)

    while True:
        try:
            message = client_socket.recv(4096)
            if not message:
                break
            broadcast(f"{name}: {message.decode()}", client_socket)
        except:
            break

    client_socket.close()
    clients.remove(client_socket)
    client_names.remove(name)
    broadcast(f"{name} has left the chat.", None)

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_HOST, SERVER_PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
