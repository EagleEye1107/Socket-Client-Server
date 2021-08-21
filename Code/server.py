#!/usr/bin/env python3

import os
import socket
import threading
from tkinter import *
from tkinter import Tk

threadsClients = []



def instanceServeur (client, infosClient):
    adresseIP = infosClient[0]
    port = str(infosClient[1])
    print("Instance de serveur prêt pour " + adresseIP + ":" + port)

    message = ""
    while message.upper() != "FIN":
        message = client.recv(255).decode("utf-8")
        if message.upper() != "FIN":
            print("Le client " + adresseIP + ":" + port + " demande le fichier : dataServer/%s" %message)
            print("   Vérification de la présence du fichier ...")
            e = os.path.exists('dataServer/%s' %message)
            if e:
                client.send("T".encode("utf-8"))
                r = 'dataServer/%s' %message
                print("   Ouverture du fichier :", r, "...")
                fp = open(r, 'rb')
                client.send(fp.read())
                print("   Fichier envoyé")
            else:
                client.send("F".encode())
                print("   Fichier introuvable.")
        else:
            print("Message reçu du client "+ adresseIP + ":" + port + " : " + message)

    print("Connexion fermée avec " + adresseIP + ":" + port)
    client.close()


'''
def instanceServeur (client, infosClient):
    adresseIP = infosClient[0]
    port = str(infosClient[1])

    #serverTK.tk.call('wm', 'iconphoto', serverTK._w, PhotoImage(file='dataServer/img/server.png'))

    label = Label(serverTK, text="Instance de serveur prêt pour " + adresseIP + ":" + port)
    label.pack()
    print("Instance de serveur prêt pour " + adresseIP + ":" + port)

    message = ""
    while message.upper() != "FIN":
        message = client.recv(255).decode("utf-8")
        if message.upper() != "FIN":

            label1 = Label(serverTK, text="Le client " + adresseIP + ":" + port + " demande le fichier : dataServer/%s" %message)
            label1.pack()

            label2 = Label(serverTK, text="   Vérification de la présence du fichier ...")
            label2.pack()

            e = os.path.exists('dataServer/%s' %message)
            if e:
                client.send("T".encode("utf-8"))
                r = 'dataServer/%s' %message

                label3 = Label(serverTK, text="   Ouverture du fichier :" +r+ "...")
                label3.pack()

                fp = open(r, 'rb')
                client.send(fp.read())

                label4 = Label(serverTK, text="   Fichier envoyé")
                label4.pack()
            else:
                client.send("F".encode())

                label5 = Label(serverTK, text="   Fichier introuvable.")
                label5.pack()
        else:
            label6 = Label(serverTK, text="Message reçu du client "+ adresseIP + ":" + port + " : " + message)
            label6.pack()

    label7 = Label(serverTK, text="Connexion fermée avec " + adresseIP + ":" + port)
    label7.pack()
    print("Connexion fermée avec " + adresseIP + ":" + port)

    client.close()
'''

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('', 50000))
serveur.listen(5)

serverTK: Tk = Tk()
serverTK.geometry("1000x800")
serverTK.title("Server")



while True:
    (client, (ip, port)) = serveur.accept()

    threadsClients.append(threading.Thread(None, instanceServeur, None, (client, (ip, port)), {}))
    threadsClients[-1].start()

serveur.close()