import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from encryption import EncryptionManager
from config import SERVER_HOST, SERVER_PORT

class ChatClientGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Secure Chat App")

        self.encryption = EncryptionManager()
        self.symmetric_key = self.encryption.generate_symmetric_key()
        self.cipher = self.encryption.get_cipher(self.symmetric_key)

        self.setup_ui()
        self.connect_to_server()

    def setup_ui(self):
        self.chat_label = tk.Label(self.root, text="Secure Chat Window", font=("Arial", 14))
        self.chat_label.pack(pady=5)

        self.text_area = scrolledtext.ScrolledText(self.root, state='disabled', width=50, height=20)
        self.text_area.pack(padx=10, pady=5)

        self.entry_field = tk.Entry(self.root, width=40)
        self.entry_field.pack(side=tk.LEFT, padx=(10, 5), pady=10)

        self.send_button = tk.Button(self.root, text="Send", width=10, command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=(5, 10))

    def connect_to_server(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect((SERVER_HOST, SERVER_PORT))
            self.name = tk.simpledialog.askstring("Username", "Enter your name:")
            self.client.send(self.name.encode())
            threading.Thread(target=self.receive_messages).start()
        except:
            messagebox.showerror("Connection Error", "Failed to connect to server.")
            self.root.destroy()

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(4096).decode()
                self.text_area.config(state='normal')
                self.text_area.insert(tk.END, message + "\n")
                self.text_area.yview(tk.END)
                self.text_area.config(state='disabled')
            except:
                messagebox.showwarning("Connection Lost", "Disconnected from server.")
                break

    def send_message(self):
        message = self.entry_field.get()
        if message:
            encrypted_msg = self.cipher.encrypt(message.encode())
            try:
                self.client.send(encrypted_msg)
                self.entry_field.delete(0, tk.END)
            except:
                messagebox.showerror("Send Error", "Failed to send message.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClientGUI(root)
    root.mainloop()

