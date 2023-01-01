import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        self.setWindowTitle('Gestion à distance de serveurs')
        self.__createMenuBar()

        layout = QHBoxLayout()
        self.setLayout(layout)

        Lab = QLabel('Commande Exécutables:')
        layout.addWidget(Lab)
        text = QLabel('Machines à choisir: ')
        layout.addWidget(text)
        padding1 = QLabel('')
        layout.addWidget(padding1)
        padding2 = QLabel('')
        layout.addWidget(padding2)
        serv1 = QCheckBox("Serveur 1")
        layout.addWidget(serv1)
        serv2 = QCheckBox("Serveur 2")
        layout.addWidget(serv2)
        serv3 = QCheckBox("Serveur 3")
        layout.addWidget(serv3)
        serv4 = QCheckBox("Serveur 4")
        layout.addWidget(serv4)
        ok = QPushButton("OK")
        layout.addWidget(ok)
        self.cmd = QLabel()
        layout.addWidget(self.cmd)
        self.text_opt = QLabel('Option à rajouter à la commande')
        self.opt = QLineEdit()
        self.fich = QFileDialog()
        self.fich.setFileMode(QFileDialog.AnyFile)
        self.fich.setNameFilter("*.csv")
        self.choix = QComboBox()
        self.choix.addItem('--Choisir commande--')  # index 0
        self.choix.addItem('OS')  # index 1
        self.choix.addItem('RAM')  # index 2
        self.choix.addItem('CPU')  # index 3
        self.choix.addItem('IP')  # index 4
        self.choix.addItem('Nom machine')  # index 5
        self.choix.addItem('Déconnecter')  # index 6
        self.choix.addItem('Information de connection')  # index 7
        self.choix.addItem('Kill')  # index 8
        self.choix.addItem('Reset')  # index 9
        self.choix.addItem('Commande Windows', ['dir', 'mkdir', 'ping', 'version python', 'Autre commande'])  # index 10
        self.choix.addItem('Commande Powershell', ['Move-Item', 'Get-Process', 'Rename-Item', 'Stop-Process',
                                                   'Get-Localisation', 'Remove-Item', 'Autre commande'])  # index 11
        self.choix.addItem('Commande Linux', ['ls -la', 'ping', 'version python', 'mkdir', 'Autre commande'])
        # index 12
        self.choix.addItem('Commande Mc OS', ['ping', 'Autre commande'])  # index 13
        layout.addWidget(self.choix)

        self.systexp = QComboBox()
        layout.addWidget(self.systexp)

        self.choix.currentIndexChanged.connect(self.updatesystexp)

        self.updatesystexp(self.choix.currentIndex())

    def updatesystexp(self, index):
        self.systexp.clear()
        syst = self.choix.itemData(index)
        if syst:
            self.systexp.addItems(syst)

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
