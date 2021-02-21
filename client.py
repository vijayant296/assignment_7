# Using socket and cryptography.
import socket
from cryptography.fernet import Fernet

# Using the key generated by server for connection.
file = open("key.key",'rb')
key2 = file.read()
file.close()

# Make connection with server.
sock = socket.socket()
host = socket.gethostname()
port = 1212
sock.connect((host,port))
sock.send(b"Hello from client.")

print("--------Receiving Data---------")
while True:
    try:
        # Receiving encrypted data from server and decrypting.
        data = sock.recv(1024)
        f2 = Fernet(key2)
        decrypted = f2.decrypt(data)
        original = decrypted.decode()
        print(f"Data = {original}")
        with open("received_data.txt", "a") as file:
            file.write(original)
        if not data:
            break
    except:
        break

# Closing the connection once data has been received.
print("Got the file")
sock.close()
print("Connection is closed")