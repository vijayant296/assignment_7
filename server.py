# importing cryptography
from cryptography.fernet import Fernet
import socket

ONE_CONNECTION_ONLY = True

# Sending data using file
filename = 'file.txt'

# Defining port , host and socket details.
port = 1212
sock = socket.socket()
host = socket.gethostname()
sock.bind((host, port))
sock.listen(10)

# Generating key for encryption.
key1 = Fernet.generate_key()
file = open("key.key", 'rb+')
file.write(key1)
key = file.read()
file.close()

print("-----------Server started---------")

while True:
    # Accepting connection from the client.
    conn, addr = sock.accept()
    print(f"Accepted connection from {addr}")
    data = conn.recv(1024)
    print(f"Server received {data}")
    with open(filename, 'r') as file:
        # Opening data file to encrypt and send the data.
        data = file.read(1024)
        while data:
            encoded = data.encode()
            f = Fernet(key1)
            encrypted = f.encrypt(encoded)
            conn.send(encrypted)
            print(f"Sent {encrypted!r}")
            data = file.read(1024)
    print("File sent complete")
    conn.close()
    if ONE_CONNECTION_ONLY:
        break

# Closing the connection
sock.shutdown(1)
sock.close()
