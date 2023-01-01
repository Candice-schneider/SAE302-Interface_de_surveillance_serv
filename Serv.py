import socket
import psutil
import sys


def serveur():
    msg = ""
    conn = None
    server_socket = None
    while msg != "kill":
        msg = ""
        server_socket = socket.socket()
        """ options qui permet de réutiliser l'adresse et le port rapidement"""

        # l'adresse 0.0.0.0 permet d'écouter toutes les IP de la machine, localhost, locale comme publique
        server_socket.bind(("0.0.0.0", 50000))

        server_socket.listen(1)
        print('Serveur en attente de connexion')
        while msg != "kill" and msg != "reset":
            msg = ""
            try:
                conn, addr = server_socket.accept()
                print(addr)
            except ConnectionError:
                print("erreur de connection")
                break
            else:
                while msg != "kill" and msg != "reset" and msg != "disconnect":
                    msg = conn.recv(1024).decode()
                    print("Received from client: ", msg)
                    # Commandes du serveur
                    if msg == "cpu":
                        msg = 'cpu : ' + str(psutil.cpu_percent())
                    elif msg == "os":
                        msg = 'os : ' + str(sys.platform)
                    elif msg == "memory":
                        msg = 'memory : ' + str(psutil.virtual_memory().total)
                    elif msg == "ram":
                        msg = 'ram : ' + str(psutil.disk_usage('/'))
                    elif msg == "ip":
                        msg = 'ip : ' + socket.gethostbyname(socket.gethostname())
                    elif msg == "name":
                        msg = 'name : ' + socket.gethostname()
                    elif msg == "python":
                        msg = 'python : ' + str(sys.version)
                    elif msg != "kill" and msg != "reset" and msg != "disconnect":
                        msg = "Commande inconnue"
                    conn.send(msg.encode())
                conn.close()
        print("Connection closed")
        server_socket.close()
        print("Server closed")


if __name__ == '__main__':
    serveur()
