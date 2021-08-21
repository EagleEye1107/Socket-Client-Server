'''
#!/usr/bin/env python3

import socket

adresseIP = "127.0.0.1"
port = 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((adresseIP, port))

print("Connecté au serveur")
print("\nTapez FIN pour terminer la conversation. ")
print("Entrez le nom du fichier que vous voulez télécharger !")

req = ""

while req.upper() != "FIN":
    req = input("> ")

    if req !='':
        client.send(req.encode("utf-8"))

        trouve = client.recv(255).decode("utf-8")

        if trouve == 'T':
            file = client.recv(9999999)
            file_name = 'dataClient/%s' %req
            with open(file_name, 'wb') as _file:
                _file.write(file)
            print("Fichier bien reçu !")
        else:
            print("Erreur, Aucun fichier trouvé avec ce nom, réessayez !")
    else:
        print("Erreur, Aucun nom entré, réessayez !")

print("\nConnexion fermée")
client.close()
'''

# coding: utf-8

import time
import socket
from threading import Timer
from tkinter import *
from tkinter.messagebox import *

#address and port
hote = "127.0.0.1"
port = 50000

#socket config
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((hote, port))


#téléchargement
def getFile():
    req = myEntry.get()
    if req != '':
        myEntry.delete(0, END)
        if req.upper() == "FIN":
            client.send(req.encode())
            label = Label(frame, text="Connexion fermée avec le serveur.")
            label.pack()
            #label.after(5000, lambda: label.destroy())
            #print("\nConnexion fermée")
            client.close()
        else:
            file_name = req
            client.send(file_name.encode())
            trouve = client.recv(255).decode("utf-8")
            if trouve == 'T':
                file_name = 'dataClient/%s' % (file_name,)
                r = client.recv(9999999)
                with open(file_name, 'wb') as _file:
                    _file.write(r)
                label = Label(frame, text="Le fichier a été correctement copié dans : %s" % file_name)
                label.pack()
                label.after(5000, lambda: label.destroy())
            elif trouve == 'F':
                showwarning('Error', 'Aucun fichier trouvé avec ce nom, réessayez !')
    else:
        showwarning('Error', 'Aucun nom entré, réessayez !')


#gui

#design
clientTk = Tk()
clientTk.minsize(500, 200)
clientTk.maxsize(500,200)
clientTk.title("Client")
clientTk.tk.call('wm', 'iconphoto', clientTk._w, PhotoImage(file='dataClient/img/client.png'))
#client.config(background='code couleur')

#frame
frame = Frame(clientTk)

#label
label = Label(frame, text="Entrez le nom du fichier demandé")
label1 = Label(frame, text="Tapez FIN pour terminer la conversation.")

#entrée
valeur = StringVar()
myEntry = Entry(frame, textvariable=valeur, width=30)

#button
btn1 = Button(frame, height=1, width=10, text="Télécharger", command=getFile)

#affichage
label.pack()
label1.pack()
myEntry.pack(pady=10)
btn1.pack(pady=10)
frame.pack(expand=YES)
clientTk.mainloop()