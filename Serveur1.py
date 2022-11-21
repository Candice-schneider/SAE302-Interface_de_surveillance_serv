import socket

server_socket = socket.socket()
server_socket.bind(("localhost", 5001))
server_socket.listen(1)

"""data = conn.recv(1024).decode()"""

while True:
    conn, address = server_socket.accept()
    reply = ""  # Envoyé
    data = ""  # Reçu
    while reply != "exit" and reply != "bye" and data != "exit" and data != "bye":
        data = conn.recv(1024).decode()
        print(data)
        reply = input("serveur -->")
        conn.send(reply.encode())

    conn.close()
    rep = input("continuer(y/n)")
    if rep == "n":
        break
server_socket.close()
