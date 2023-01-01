from PyQt5.QtWidgets import *
from Cli import Client
import sys, socket, threading


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.__host = 'localhost'
        self.__port = 50000
        self.__sock = socket.socket()
        self.__thread = None
        self.__createMenuBar()

        widget = QWidget()
        self.setCentralWidget(widget)
        self.setWindowTitle('testing')

        grid = QGridLayout()
        widget.setLayout(grid)

        connect = QPushButton('connexion')
        grid.addWidget(connect, 0, 0)
        connect.clicked.connect(self.__conect)

        cmd = QComboBox()
        cmd.addItem('os')
        cmd.addItem('ram')
        cmd.addItem('memory')
        cmd.addItem('version')
        cmd.addItem('ip')
        grid.addWidget(cmd, 1, 0)
        text = cmd.currentText()
        cmd.currentIndexChanged.connect(self.__dialogue)

        self.text = text


    def __conect(self) -> int:
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

    def __dialogue(self):
        msg = self.text
        self.__thread = threading.Thread(target=self.__reception, args=[self.__sock, ])
        self.__thread.start()
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = self.__envoi()
        self.__thread.join()
        self.__sock.close()

    def __reception(conn):
        msg = ""
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = conn.recv(1024).decode()
            print(msg)

    def __envoi(self):
        msg = self.text
        try:
            self.__sock.send(msg.encode())
        except BrokenPipeError:
            print("erreur, socket fermée")
        return msg

    def __cmd(self):

        msg = 'os : ' + str(sys.platform)
        self.__sock.send(msg.encode())
        return msg

    def __createMenuBar(self):  # création d'une barre de menu avec des options
        menuBar = self.menuBar()
        fileMenu = QMenu('&CSV', self)  # 1er menu déroulant
        fileMenu1 = QMenu('&Aide', self)  # 2ème menu déroulant
        # Si j'y arrive, ajouter une option qui permet d'exporter un graphique sur l'utilisation du cpu
        menuBar.addMenu(fileMenu)
        menuBar.addMenu(fileMenu1)
        openAction = QAction("&Importer", self)
        openAction1 = QAction("&Exporter", self)
        aideAction = QAction("&Information sur l'application", self)
        aideAction1 = QAction("&Choix machine ", self)
        aideAction2 = QAction("&Commande à exécuter", self)
        aideAction3 = QAction("&Fenêtre CMD", self)
        aideAction4 = QAction("&import/export CSV", self)
        fileMenu.addAction(openAction)
        fileMenu.addAction(openAction1)
        fileMenu1.addAction(aideAction)
        fileMenu1.addAction(aideAction1)
        fileMenu1.addAction(aideAction2)
        fileMenu1.addAction(aideAction3)
        fileMenu1.addAction(aideAction4)

        openAction1.triggered.connect(self.__ouvrir1)
        aideAction.triggered.connect(self.action)
        aideAction1.triggered.connect(self.action1)
        aideAction2.triggered.connect(self.action2)
        aideAction3.triggered.connect(self.action3)
        aideAction4.triggered.connect(self.action4)
        openAction.triggered.connect(self.__explorateur)

    def __ouvrir(self):
        pass

    def __ouvrir1(self):
        pass

    @staticmethod
    def action():  # action de click sur information dur l'application
        QMessageBox(
            text="Cette application permet de contrôler des serveurs à distance à l'aide de commande que vous pouvez "
                 "séléctionner ou à renseigner. \nOn peut ensuite voir le résultat de la commande choisi dans "
                 "l'encadrement au centre de la page. \n \n"
                 "Les machines qui peuvent être utilisée doivent être importée à l'aide d'un fichier csv contenant "
                 "les adresses ip et le port de chaque machines. \n\n"
                 "Vous pouvez trouvez des informations supplémentaires sur chaqu'un des modules dans l'onglet au nom "
                 "du module. \n\n\n"
                 "Si vous avez des questions qui n'ont pas été répondus dans les différentes aides, vous pouvez "
                 "écrire au développeur: \n"
                 "Candice Schneider\n - discord: schneider_candice#8647 \n - mail: candice.schneider@uha.fr\n").exec()

    @staticmethod
    def action1():  # action de clique sur Machines à choisir
        QMessageBox(text="Une fois que la/les machine(s) ont été importées d'un fichier csv (voir la documentation "
                         "'importation/exportation CSV'), vous pouvez choisir la/les machine(s) où vous exécuter une "
                         "commande. \n \n \n"
                         "             ************ Attention ************* \n"
                         "Lorsque vous choisissez plusieurs machines  et une commande propre à un système "
                         "d'exploitation en même temps, vous avez un risque d'avoir une erreur si le système "
                         "d'exploitation est different entre les machines sélectionnées. ").exec()

    @staticmethod
    def action2():
        QMessageBox(
            text="Dans le menu déroulant 'Commande exécutables', vous pouvez choisir une commande générique, "
                 "une commande powershell ou une commande propre à un système d'exploitation.\n"
                 "Un nouveau menu déroulant va s' ouvrir dans le cas où vous choisissez l' une des deux dernières "
                 "options.\nVous aurez également la possibilité d' entrer une commande non présente dans le menu en "
                 "choisissant 'Autre commande', un champ va apparaitre où vous pourrez écrire votre commande.\n \n "
                 "            ************ Attention *************\n"
                 "Une commande propre à un système d'exploitation ne peut pas être exécutée sur une machine n'ayant "
                 "pas ce système d'exploitation.").exec()

    @staticmethod
    def action3():
        QMessageBox(
            text="dddddddddddddddddddddddddddddactiondddddddddddddddddd"
        ).exec()

    @staticmethod
    def action4():
        QMessageBox(
            text="L'importation et l'exportation de CSV est possible.\n Cette option est possible dans l'onglet"
                 " 'CSV'.\n\nLe CSV importé doit comporter les informations de connexion au/aux serveur(s)"
                 " dont vous voulez prendre la mains."

        ).exec()

    def __explorateur(self):
        self.fich.open()
        print(self.fich.selectedFiles())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
