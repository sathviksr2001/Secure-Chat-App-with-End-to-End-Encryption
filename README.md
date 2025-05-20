# 💬 Secure Chat App (EC2-Deployed)

A **real-time, encrypted chat application** built using Python sockets and hosted on an **AWS EC2 instance** for global access. The app supports multiple clients and features a basic GUI using Tkinter.

---

## 🚀 Features

- 🔒 End-to-end encryption (symmetric AES)
- 🌐 Internet-based communication (EC2 hosted server)
- 👥 Multi-client chat support using threading
- 🖥️ Simple GUI interface using Tkinter
- ⚙️ Custom IP/port configuration
- 🧱 Modular design (easy to extend)
- 📡 Deployable and accessible globally
- 🔧 Easy to modify for educational or demo purposes

---

## 📁 Project Structure

```
secure-chat-app/
├── client.py          # Client-side logic
├── server.py          # Server-side logic (run this on AWS EC2)
├── config.py          # IP and port settings
├── encryption.py      # AES encryption/decryption functions
├── gui_client.py      # Tkinter-based GUI for client
├── requirements.txt   # Required Python packages
└── README.md
```

---

## 🛠 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/secure-chat-app.git
cd secure-chat-app
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure IP and Port
Edit `config.py`:
```python
SERVER_HOST = 'your-ec2-public-ip'
SERVER_PORT = 65432
```

### 4. Launch the Server (on EC2)
```bash
python3 server.py
```

### 5. Launch the Client (from any remote system)
```bash
python3 gui_client.py
```

---

## 🌐 Deploying Server on AWS EC2

1. Launch an EC2 Ubuntu Instance  
2. Allow port `65432` and `22` in the security group  
3. SSH into the instance:  
```bash
ssh -i "your-key.pem" ubuntu@<your-ec2-ip>
```
4. Upload and run `server.py` on EC2  
5. Use your EC2 IP in `config.py` on clients  

---

## 🔐 Security Notes

- Uses AES symmetric encryption (key is currently hardcoded/shared)  
- For real-world use, implement:  
  - Public key exchange (RSA)  
  - User authentication system  
  - Encrypted key storage or TLS  
- Keep your EC2 instance secure (use SSH keys, close unused ports)  

---

## 🧠 Learning Outcomes

- Understanding Python socket programming  
- Basics of symmetric encryption with PyCryptodome  
- Multi-threaded network programming  
- GUI development with Tkinter  
- Cloud deployment using AWS EC2  

---

## ✨ Future Improvements

- Add login/sign-up authentication system  
- Use RSA for secure key exchange  
- Host a web-based client version  
- Persistent chat logs (using database)  
- Notification and sound support  

---

## 👏 Acknowledgments

Built with Python, sockets, Tkinter, and love 💙. Deployed globally using AWS EC2.

---

## 🌟 Star This Project

If you like this project, please consider giving it a ⭐ on GitHub to support the developer.

---

## 📸 Screenshots

> Coming Soon — add screenshots of your GUI and terminal views!

---

## 🔗 Connect with Me

- GitHub: [@your-username](https://github.com/your-username)  
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-linkedin)  
- Portfolio: [your-website.com](https://your-website.com)
