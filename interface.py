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
        self.__createMenuBar()

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
        self.choix.addItem("Commande Mac Os")
        self.win = QComboBox()
        self.win.addItem("  --Commandes Windows--")
        self.win.addItem("dir")
        self.win.addItem("mkdir")
        self.win.addItem("ping")
        self.win.addItem("version python")
        self.win.addItem("Autre commande")
        self.lin = QComboBox()
        self.lin.addItem("  --Commandes Linux--")
        self.lin.addItem("ls -la")
        self.lin.addItem("ping")
        self.lin.addItem("version python")
        self.lin.addItem("mkdir")
        self.lin.addItem("Autre commande")
        self.pow = QComboBox()
        self.pow.addItem("  --Commandes Powershell--")
        self.pow.addItem("Move-Item")
        self.pow.addItem("Get-Process")
        self.pow.addItem("Rename-Item")
        self.pow.addItem("Stop-Process")
        self.pow.addItem("Get-Localisation")
        self.pow.addItem("Remove-Item")
        self.pow.addItem("Autre commande")
        self.mac = QComboBox()
        self.mac.addItem("  --Commandes Mac Os--")
        self.mac.addItem("Autre commande")
        self.cmd = QLabel()
        self.text_opt = QLabel('Option à rajouter à la commande')
        self.opt = QLineEdit()
        # self.choix.currentIndexChanged.connect(self.selectionchange)
        # self.win.currentIndexChanged.connect(self.selectionchange)
        # self.lin.currentIndexChanged.connect(self.selectionchange)
        # self.pow.currentIndexChanged.connect(self.selectionchange)
        self.fich = QFileDialog()
        self.fich.setFileMode(QFileDialog.AnyFile)
        self.fich.setNameFilter("*.csv")

        # Ajout des composants au grid layout
        grid.addWidget(Lab, 0, 2)
        grid.addWidget(text, 0, 0)
        grid.addWidget(padding1, 0, 7)
        grid.addWidget(padding2, 0, 1)
        grid.addWidget(self.text_opt, 0, 4)
        grid.addWidget(self.opt, 0, 5)
        grid.addWidget(ok, 0, 6)
        grid.addWidget(self.choix, 0, 3)
        grid.addWidget(self.win, 1, 4)
        grid.addWidget(self.lin, 1, 5)
        grid.addWidget(self.pow, 1, 6)
        grid.addWidget(serv1, 1, 0)
        grid.addWidget(serv2, 2, 0)
        grid.addWidget(serv3, 3, 0)
        grid.addWidget(serv4, 4, 0)
        grid.addWidget(self.cmd, 2, 2, 3, 5)

        # ok.clicked.connect(self.selectionchange)

        self.setWindowTitle("Gestion des serveurs ")

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
            text="ddddddddddddddddddddddddddddddddddddddddddddddd"
        ).exec()

    @staticmethod
    def action3():
        QMessageBox(
            text="ddddddddddddddddddddddddddddddddddddddddddddddd"
        ).exec()

    @staticmethod
    def action4():
        QMessageBox(
            text="ddddddddddddddddddddddddddddddddddddddddddddddd"
        ).exec()

    def __explorateur(self):
        self.fich.open()
        print(self.fich.selectedFiles())


if __name__ == '__main__':  # Execution de la fenêtre
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
