import socket

s = socket.socket()
s.bind(('127.0.0.1', 40664))
s.listen(1)
print("Socket is listening...")

c, addr = s.accept()
print("Got connection from", addr)
c.send(b'Thank you for connecting')
c.close()
s.close() 

