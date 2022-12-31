import socket


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
                    # msg = input('Enter a message to send: ')
                    """ 
                    le serveur va ici récupère les commandes du client et lui renvoyer. Dans la suite de la SAÉ, 
                    le serveur fait pareil mais en renvoyant le résultat des commandes demandées par le client.
                    """
                    conn.send(msg.encode())
                conn.close()
        print("Connection closed")
        server_socket.close()
        print("Server closed")


# Coder les commande ici

if __name__ == '__main__':
    serveur()
