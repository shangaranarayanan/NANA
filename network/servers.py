import socket

s=socket.socket()
s.bind(('localhost',12345))
s.listen(5)
print("Server is running...")

while True:
   c,abbr=s.accept()
   print("Got connection from", abbr)
   sm=input("Message to client:")
   c.send(sm.encode())
   cm=c.recv(1024).decode()
   print("Message from client:",cm)
   c.close()
