import platform as p
import os
from PyQt5.QtWidgets import *


self.__filename = QFileDialog()
self.__filename.setFileMode(QFileDialog.AnyFile)
self.__filename.setNameFilter("*.csv")
self.__filename.getOpenFileName() #ouvre le menu pour choisir le fichier
self.__filename.selectedFiles()

def info():
    # afficher = lambda cle, valeur: print("{k} :: {v}".format(k=cle, v=valeur))
    systeme = p.system()
    python = p.python_version()
    jeu, formatFichier = p.architecture()
    distribution = p.version()
    print("Système      Opérant    ", systeme)
    print("Architecture Processeur ", jeu)
    print("Version      Système    ", distribution)
    print("Version      Python     ", python)

