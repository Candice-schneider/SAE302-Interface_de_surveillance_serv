import socket
import threading
import sys


class Client(threading.Thread):

    host = 'localhost'
    port = 50000

    def __init__(self, host, port):
        super().__init__()
        self.__host = host
        self.__port = port
        self.__sock = socket.socket()
        self.__thread = None

    # fonction de connection.
    def connect(self) -> int:
        try:
            self.__sock.connect((self.__host, self.__port))
        except ConnectionRefusedError:
            print("serveur non lancé ou mauvaise information")
            return -1
        except ConnectionError:
            print("erreur de connection")
            return -1
        else:
            print("connexion réalisée")
            return 0

    """ 
        fonction qui gère le dialogue
        -> lance une thread pour la partie reception 
        -> lance une boucle pour la partie emission. arrêt si kill, reset ou disconnect
    """

    def dialogue(self):
        msg = ""
        self.__thread = threading.Thread(target=self.__reception, args=[self.__sock, ])
        self.__thread.start()
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = self.__envoi()
        self.__thread.join()
        self.__sock.close()

    # méthode d'envoi d'un message au travers la socket. Le résultat de cette methode est le message envoyé.
    def __envoi(self):
        msg = input("client: ")
        try:
            self.__sock.send(msg.encode())
        except BrokenPipeError:
            print("erreur, socket fermée")
        return msg

    """
      thread reception, la connection étant passée en argument
    """

    @staticmethod
    def __reception(conn):
        msg = ""
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = conn.recv(1024).decode()
            print(msg)


if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) < 3:
        client = Client("127.0.0.1", 50000)
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        # création de l'objet client qui est aussi un thread
        client = Client(host, port)
        # démarrage de la thread client
    client.start()
    client.join()

    # en dehors du if
    client.connect()
    client.dialogue()
