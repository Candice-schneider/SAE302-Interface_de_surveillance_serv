import socket

message = ""  # Envoyé
data = " "  # Reçu

client_socket = socket.socket()
client_socket.connect(("localhost", 5001))
"""client_socket.send(message.encode())
data = client_socket.recv(1024).decode()"""

while message != "exit" and message != "bye" and data != "exit" and data != "bye":
    message = input("-->")
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print(data)

client_socket.close()
