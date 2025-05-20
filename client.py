import socket
import threading
from encryption import EncryptionManager
from config import SERVER_HOST, SERVER_PORT

name = input("Enter your name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_HOST, SERVER_PORT))
client.send(name.encode())

encryption = EncryptionManager()
symmetric_key = encryption.generate_symmetric_key()
cipher = encryption.get_cipher(symmetric_key)

def receive_messages():
    while True:
        try:
            message = client.recv(4096).decode()
            print(message)
        except:
            print("[ERROR] Disconnected from server.")
            break

def send_messages():
    while True:
        msg = input()
        encrypted_msg = cipher.encrypt(msg.encode())
        client.send(encrypted_msg)

recv_thread = threading.Thread(target=receive_messages)
recv_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
