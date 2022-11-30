import platform as p


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
