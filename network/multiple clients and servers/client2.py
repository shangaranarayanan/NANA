
import socket

s = socket.socket()
print("Connecting to server...")
s.connect(('127.0.0.1', 40674))
print("Connected. Waiting for message...")
data = s.recv(1024)
print("Received:", data.decode())
s.close()
input("Press Enter to exit...")
