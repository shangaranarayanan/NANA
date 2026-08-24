import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 40674))
server.listen(2)

print("Server started...")
print("Waiting for clients...")

while True:
    client, address = server.accept()
    print("Client connected:", address)

    message = "Hello from server!"
    client.send(message.encode())

    client.close()
