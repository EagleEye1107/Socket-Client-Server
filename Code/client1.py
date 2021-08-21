#!/usr/bin/env python3

import socket

adresseIP = "127.0.0.1"
port = 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((adresseIP, port))

print("Connecté au serveur")
print("\nTapez FIN pour terminer la conversation. ")

req = ""

while req.upper() != "FIN":
    req = input("> ")

    if req !='':
        client.send(req.encode("utf-8"))

        trouve = client.recv(255).decode("utf-8")

        if trouve == 'T':
            file = client.recv(9999999)
            file_name = 'dataClient1/%s' %req
            with open(file_name, 'wb') as _file:
                _file.write(file)
            print("Fichier bien reçu !")
        else:
            print("Erreur, Aucun fichier trouvé avec ce nom, réessayez !")
    else:
        print("Erreur, Aucun nom entré, réessayez !")

print("\nConnexion fermée")
client.close()
