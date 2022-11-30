""" Choses à faire:
- lien derrière les boutons
- cacher menu déroulant choix os
- ouvrir page cmd
- exception sur les entrées
-gérer les entrées
"""
import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        self.resize(800, 255)

        grid = QGridLayout()
        widget.setLayout(grid)

        Lab = QLabel('Commande Exécutables:')
        text = QLabel('Machines à choisir: ')
        padding1 = QLabel('')
        padding2 = QLabel('')
        serv1 = QCheckBox("Serveur 1")
        serv2 = QCheckBox("Serveur 2")
        serv3 = QCheckBox("Serveur 3")
        serv4 = QCheckBox("Serveur 4")
        ok = QPushButton("OK")
        self.choix = QComboBox()
        self.choix.addItem("  --Choisir commande--")
        self.choix.addItem("OS")
        self.choix.addItem("RAM")
        self.choix.addItem("CPU")
        self.choix.addItem("IP")
        self.choix.addItem("Nom machine")
        self.choix.addItem("Déconnecter")
        self.choix.addItem("Information de connection")
        self.choix.addItem("Kill")
        self.choix.addItem("Reset")
        self.choix.addItem("Commande Windows")
        self.choix.addItem("Commande Powershell")
        self.choix.addItem("Commande Linux")
        self.win = QComboBox()
        self.win.addItem("  --Commandes Windows--")
        self.win.addItem("dir")
        self.win.addItem("mkdir")
        self.win.addItem("ping")
        self.win.addItem("version python")
        self.lin = QComboBox()
        self.lin.addItem("  --Commandes Linux--")
        self.lin.addItem("ls -la")
        self.lin.addItem("ping")
        self.lin.addItem("version python")
        self.lin.addItem("mkdir")
        self.pow = QComboBox()
        self.pow.addItem("  --Commandes Powershell--")
        self.pow.addItem("Move-Item")
        self.pow.addItem("Get-Process")
        self.pow.addItem("Rename-Item")
        self.pow.addItem("Stop-Process")
        self.pow.addItem("Get-Localisation")
        self.pow.addItem("Remove-Item")
        self.cmd = QTextEdit()
        self.text_opt = QLabel('Option à rajouter à la commande')
        self.opt = QLineEdit()
        # self.choix.currentIndexChanged.connect(self.selectionchange)
        # self.win.currentIndexChanged.connect(self.selectionchange)
        # self.lin.currentIndexChanged.connect(self.selectionchange)
        # self.pow.currentIndexChanged.connect(self.selectionchange)
        aide = QPushButton("?")

        # Ajout des composants au grid layout
        grid.addWidget(Lab, 0, 2)
        grid.addWidget(text, 0, 0)
        grid.addWidget(padding1, 0, 7)
        grid.addWidget(padding2, 0, 1)
        grid.addWidget(self.text_opt, 0, 4)
        grid.addWidget(self.opt, 0, 5)
        grid.addWidget(ok, 0, 6)
        grid.addWidget(self.choix, 0, 3)
        grid.addWidget(aide, 0, 8)
        grid.addWidget(self.win, 1, 4)
        grid.addWidget(self.lin, 1, 5)
        grid.addWidget(self.pow, 1, 6)
        grid.addWidget(serv1, 1, 0)
        grid.addWidget(serv2, 2, 0)
        grid.addWidget(serv3, 3, 0)
        grid.addWidget(serv4, 4, 0)
        # grid.addWidget(self.cmd, 2, 2, 3, 5)

        # ok.clicked.connect(self.selectionchange)

        self.setWindowTitle("Gestion des serveurs ")
        aide.clicked.connect(self.action)

    def __createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = QMenu('&Fichier', self)
        menuBar.addMenu(fileMenu)
        openAction = QAction("&Ouvrir", self)
        fileMenu.addAction(openAction)
        openAction.triggered.connect(self.__ouvrir)

    def __ouvrir(self):
        pass

    def action(self):  # action de click sur ok
        QMessageBox(
            text="Cette application permet de contrôler des serveurs à distance à l'aide de commande à séléctionner. \n"
                 "Certaines commandes sont personnalisable comme la commande ping, vous devez alors renseigner"
                 " les informations manquantes. \n \n"
                 "Vous pouvez également choisir de lancer une commande sur plusieurs machines en même temps, \n"
                 "il suffit alors de sélectionner toutes les machines que vous souhaitez en même temps.\n \n "
                 "Choissisez la commande que vous voulez et appuyez sur OK.\n").exec()


if __name__ == '__main__':  # Execution de la fenêtre
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
