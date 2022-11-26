""" Choses à faire:
- trouver comment donner un nom aux menus déroulant
- lien derrière les boutons
- faire du padding
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

        grid = QGridLayout()
        widget.setLayout(grid)

        Lab = QLabel('Commande Exécutables:')
        self.recup = QLineEdit()
        serv1 = QPushButton("Serveur 1")
        serv2 = QPushButton("Serveur 2")
        serv3 = QPushButton("Serveur 3")
        serv4 = QPushButton("Serveur 4")
        self.unit = QLabel()
        ok = QPushButton("OK")
        self.res = QLabel()
        self.choix = QComboBox()
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
        self.win.addItem("dir")
        self.win.addItem("mkdir")
        self.win.addItem("ping")
        self.win.addItem("version python")
        self.lin = QComboBox()
        self.lin.addItem("ls-la")
        self.lin.addItem("ping")
        self.lin.addItem("version python")
        self.lin.addItem("mkdir")
        self.pow = QComboBox()
        self.pow.addItem("Move-Item")
        self.pow.addItem("Get-Process")
        self.pow.addItem("Rename-Item")
        self.pow.addItem("Stop-Process")
        self.pow.addItem("Get-Localisation")
        self.pow.addItem("Remove-Item")
        self.choix.currentIndexChanged.connect(self.selectionchange)
        self.win.currentIndexChanged.connect(self.selectionchange)
        self.lin.currentIndexChanged.connect(self.selectionchange)
        self.pow.currentIndexChanged.connect(self.selectionchange)
        aide = QPushButton("?")

        # Ajout des composants au grid layout
        grid.addWidget(Lab, 2, 0)
        # grid.addWidget(self.recup, 0, 1)
        # grid.addWidget(self.unit, 0, 2)
        grid.addWidget(ok, 2, 2)
        grid.addWidget(self.res, 4, 0)
        grid.addWidget(self.choix, 2, 1)
        grid.addWidget(aide, 0, 5)
        grid.addWidget(self.win, 4, 0)
        grid.addWidget(self.lin, 4, 1)
        grid.addWidget(self.pow, 4, 2)
        grid.addWidget(serv1, 0, 0)
        grid.addWidget(serv2, 0, 1)
        grid.addWidget(serv3, 0, 2)
        grid.addWidget(serv4, 0, 3)

        ok.clicked.connect(self.selectionchange)

        self.setWindowTitle("Gestion des serveurs ")
        aide.clicked.connect(self.action)

    def selectionchange(self):
        if self.choix.currentText() == "Kelvin en Celsius ":
            try:
                envoi = float(self.recup.text())
            except ValueError:
                QMessageBox(text="Mauvaises valeures").exec()
            else:
                self.res.setText(f'Le résultat est de {float(envoi) - 273.15} °C.')
                self.unit.setText(f'K')

        else:
            try:
                envoi = float(self.recup.text())
            except:
                ValueError != float
                QMessageBox(text="Mauvaises valeures").exec()
            else:
                self.res.setText(f'Le résultat est de {float(envoi) + 273.15} K.')
                self.unit.setText(f'°C')

    def action(self):  # action de click sur ok
        QMessageBox(
            text="Cette application permet de contrôler des serveurs à distance à l'aide de commande à séléctionner."
                 "Choissisez la commande que vous voulez et appuyez sur OK. ").exec()


if __name__ == '__main__':  # Execution de la fenêtre
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
