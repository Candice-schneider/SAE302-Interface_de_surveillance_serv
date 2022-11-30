from threading import Thread
import platform as p
import socket
import re
import os

os.system("color 0f")

id_co_individuel = 0
msg_envoi = ""
ligne_ajout = ""
msg_encode = ""


def async_recv(client_socket):
    while msg_recu != "kill":
        msg_recu = client_socket.recv(1024)
        while msg_recu != "kill" and msg_recu != "reset":

            if msg_recu == b"":
                client_socket.close()
                print("Le serveur est arrêté.\n")
                break
            if msg_recu != msg_encode:
                msg_recu = msg_recu.decode()
                if re.search(r'^id_', msg_recu) is None:
                    print("\n>>>{0}".format(msg_recu))
                else:
                    id_co_individuel = int(re.sub(r'(id_)', r'', msg_recu))
            elif msg_encode == msg_recu:
                msg_recu = msg_recu.decode()
                print("\n>>>Envoyé : {0}".format(msg_recu))


def envoie(msg_a_envoyer):
    msg_a_encoder = str(msg_a_envoyer)
    msg_a_encoder = msg_a_envoyer.encode()
    print("Envoie du message  . . . \1")
    connexion_avec_serveur.send(msg_a_encoder)
    msg_a_encoder = ""
    msg_a_envoyer = ""
    # on envoie le message
    print("Attente de la réponse . . .")


print(" " * 20 + "****** Client, bienvenue. ******\n\n\n" + " " * 20)
hote = input(" " * 21 + "Entrez le nom de l'hôte > ")
port = int(input(" " * 21 + "Entrez le port (50000 par défault) > "))
print("\n")
print("_" * 80 + "|/-\\" * (81 // 4) + "|   " * (81 // 4))

afficher = lambda cle, valeur: print("{k} :: {v}".format(k=cle, v=valeur))
systeme = p.system()
python = p.python_version()
jeu, formatFichier = p.architecture()
distribution = p.version()
afficher("Système      Opérant    ", systeme)
afficher("Architecture Processeur ", jeu)
afficher("Version      Système    ", distribution)
afficher("Version      Python     ", python)

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))

envoie(systeme)
envoie(jeu)
envoie(distribution)
envoie(python)

# faire la réception du socket dans un autre thread
thread = Thread(target=async_recv, args=(connexion_avec_serveur,))
thread.start()

print("Connexion établie avec le serveur sur le port {}.".format(port))

while msg_envoi.lower() != "fin":
    try:
        # partie du code où on va écrire un message pour le client
        while 1:
            ligne_ajout = input("> ")
            if ligne_ajout == "send":  # la commande 'fin' demande l'arrêt du serveur
                break
            elif ligne_ajout.lower() == "fin":
                # on arrete tout :
                break
            elif ligne_ajout == "ren":
                msg_envoi += "\n"
                msg_envoi += ligne_ajout
                envoie(msg_envoi)
            elif ligne_ajout == "id":
                msg_envoi += "\n"
                msg_envoi += ligne_ajout
                envoie(msg_envoi)
            else:
                msg_envoi += "\n"
                msg_envoi += ligne_ajout

        if msg_envoi != "" and ligne_ajout.lower() != "fin" and ligne_ajout != "ren":
            # on envoie
            envoie(msg_envoi)
        # --------------------------------------------------------
        elif ligne_ajout.lower() == "fin":
            msg_envoi = "fin"
            msg_encode = msg_envoi.encode()
            connexion_avec_serveur.send(msg_encode)
            break
        # --------------------------------------------------------
    except NameError as nom_erreur:
        print(nom_erreur)

    except TypeError as type_err:
        print(type_err)

    except EnvironmentError as env_err:
        print(env_err)

thread.stop()
print("Fermeture de la connexion. Appuyer sur une touche pour continuer . . .")
wait = input()
connexion_avec_serveur.close()
