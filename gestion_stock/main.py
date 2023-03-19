import tkinter 
from tkinter import *
import mysql.connector

# connection à la base de donnée mysql
connexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12Abcdef@",
    database = "boutique"
)
if connexion.is_connected:
    print("succefull")
else:
    print("failled")


# création de fenetre
root = tkinter.Tk()
root.title("gestion de stock")
root.geometry("720x720")
root.config(bg="yellow",)

# créer un menu
menubar = Menu(root)
# créer un sous-menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New" )
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_command(label="Quit!", command=root.quit)

#afficher le menu
root.config(menu=menubar)


#creer un gframe
table = tkinter.Frame(root)
table.pack(pady=10)

id_label = tkinter.Label(table, text="ID", width=10,bg="red", anchor=W)
id_label.grid(row=0, column=0)
nom_label = tkinter.Label(table, text="Nom", width=20,bg="red", anchor=W)
nom_label.grid(row=0, column=1)
description_label = tkinter.Label(table, text="Description", width=30,bg="red", anchor=W)
description_label.grid(row=0, column=2)
prix_label = tkinter.Label(table, text="Prix", width=10,bg="red", anchor=W)
prix_label.grid(row=0, column=3)
quantite_label = tkinter.Label(table, text="Quantité", width=10,bg="red", anchor=W)
quantite_label.grid(row=0, column=4)
categorie_label = tkinter.Label(table, text="Catégorie", width=20,bg="red", anchor=W)
categorie_label.grid(row=0, column=5)

# la liste de produits
#liste_produits = tkinter.Listbox(root, bg="red", width=90, height=20)

# recuperation des donnée de la table produit
#cursor = connexion.cursor()
#sql = "SELECT * FROM produit"
#cursor.execute(sql)
#produit = cursor.fetchall()

#for i, row in enumerate(produit):
#    id_label = tkinter.Label(table, text=row[0], width=10,bg="blue", anchor=W)
#    id_label.grid(row=i+1, column=0)
#    nom_label = tkinter.Label(table, text=row[1], width=20,bg="blue", anchor=W)
#    nom_label.grid(row=i+1, column=1)
#    description_label = tkinter.Label(table, text=row[2], width=30,bg="blue", anchor=W)
 #   description_label.grid(row=i+1, column=2)
 #   prix_label = tkinter.Label(table, text=row[3], width=10,bg="blue", anchor=W)
 #   prix_label.grid(row=i+1, column=3)
 #   quantite_label = tkinter.Label(table, text=row[4], width=10,bg="blue", anchor=W)
 #   quantite_label.grid(row=i+1, column=4)
 #   categorie_label = tkinter.Label(table, text=row[5], width=20,bg="blue", anchor=W)
 #   categorie_label.grid(row=i+1, column=5)

cursor = connexion.cursor()
# fonction pour mettre à jour les données du tableau
def charger_produits():
    
    sql = "SELECT * FROM produit"
    cursor.execute(sql)
    produit = cursor.fetchall()

    for i, row in enumerate(produit):
        id_label = tkinter.Label(table, text=row[0], width=10,bg="blue", anchor=W)
        id_label.grid(row=i+1, column=0)
        nom_label = tkinter.Label(table, text=row[1], width=20,bg="blue", anchor=W)
        nom_label.grid(row=i+1, column=1)
        description_label = tkinter.Label(table, text=row[2], width=30,bg="blue", anchor=W)
        description_label.grid(row=i+1, column=2)
        prix_label = tkinter.Label(table, text=row[3], width=10,bg="blue", anchor=W)
        prix_label.grid(row=i+1, column=3)
        quantite_label = tkinter.Label(table, text=row[4], width=10,bg="blue", anchor=W)
        quantite_label.grid(row=i+1, column=4)
        categorie_label = tkinter.Label(table, text=row[5], width=20,bg="blue", anchor=W)
        categorie_label.grid(row=i+1, column=5)

# bouton pour charger les produits
charger_btn = tkinter.Button(root, text="Charger les produits", command=charger_produits)
charger_btn.pack()



# ajouter des ou un nouveau produits
nom = Label(root, text="Nom : ")
nom.place(x=0, y=300)
champ_nom = Entry(root)
champ_nom.place(x=80, y=300)

description = Label(root, text="description : ")
description.place(x=0, y=330)
champ_description = Entry(root)
champ_description.place(x=80, y=330) 

prix = Label(root, text="prix : ")
prix.place(x=0, y=360)
champ_prix = Entry(root)
champ_prix.place(x=80, y=360)

quantite = Label(root, text="quantité : ")
quantite.place(x=0, y=390)
champ_quantite = Entry(root)
champ_quantite.place(x=80, y=390)

id_categorie = Label(root, text="id_categorie : ")
id_categorie.place(x=0, y=420)
champ_id_categorie = Entry(root)
champ_id_categorie.place(x=80, y=420)


def ajoute_produits():
    nom = champ_nom.get()
    description = champ_description.get()
    prix = champ_prix.get()
    quantité = champ_quantite.get()
    id_categorie = champ_id_categorie.get()
    
    cursor = connexion.cursor()
    sql = "INSERT INTO produit (nom, description, prix, quantité, id_categorie) VALUES (%s, %s, %s, %s, %s)"
    val = (nom, description, prix, quantité, id_categorie)
    cursor.execute(sql, val)
    connexion.commit()
    print(cursor.rowcount, "animal ajouté.")

    cursor.close()
    connexion.close()

def efacer_valeur():
    champ_nom.delete(0, END)
    champ_description.delete(0, END)
    champ_prix.delete(0, END)
    champ_quantite.delete(0, END)
    champ_id_categorie.delete(0, END)

bouton_ajouter = Button(root, text="ajouter", command=ajoute_produits)
bouton_ajouter.place(x=35, y=460)
bouton_effacer = Button(root, text="effacer", command=efacer_valeur)
bouton_effacer.place(x=100, y=460)


# supprimer les produits
def supprimer_produit():
    id = champ_ID.get()
    sql = "DELETE FROM produit WHERE id=%s"
    val = [id]
    cursor.execute(sql, val)

    connexion.commit()
    print(cursor.rowcount, "produit supprimé.")   

id_produit = Label(root, text="ID :")
id_produit.place(x=500, y=300)
champ_ID = Entry(root)
champ_ID.place(x=530, y=300)
bouton_supprimer = Button(root, text="supprimer", command=supprimer_produit)
bouton_supprimer.place(x=540, y=340)


#  modifier les produits 
def modifier_produit():
    id = champ_ID_modifier.get()
    nom = champ_nom_modifier.get()
    description = champ_description_modifier.get()
    prix = champ_prix_modifier.get()
    quantité = champ_quantité_modifier.get()
    id_categorie = champ_id_categorie_modifier.get()
    sql = "UPDATE produit SET nom=%s, description=%s, prix=%s, quantité=%s, id_categorie=%s WHERE id=%s"
    val= (nom, description, prix, quantité, id_categorie, id)
    cursor.execute(sql, val)

    connexion.commit()
    print(cursor.rowcount, "produit modifier.")

id_produit = Label(root, text="id :")
id_produit.place(x=450, y=500)
champ_ID_modifier = Entry(root)
champ_ID_modifier.place(x=530, y=500)

nom_produit = Label(root, text="nom :")
nom_produit.place(x=450, y=530)
champ_nom_modifier = Entry(root)
champ_nom_modifier.place(x=530, y=530)

description_produit = Label(root, text="description :")
description_produit.place(x=450, y=560)
champ_description_modifier = Entry(root)
champ_description_modifier.place(x=530, y=560)

prix_produit = Label(root, text="prix :")
prix_produit.place(x=450, y=590)
champ_prix_modifier = Entry(root)
champ_prix_modifier.place(x=530, y=590)

quantité_produit = Label(root, text="quantité :")
quantité_produit.place(x=450, y=620)
champ_quantité_modifier = Entry(root)
champ_quantité_modifier.place(x=530, y=620)

id_categorie_produit = Label(root, text="id_categorie :")
id_categorie_produit.place(x=450, y=650)
champ_id_categorie_modifier = Entry(root)
champ_id_categorie_modifier.place(x=530, y=650)

bouton_modifier = Button(root, text="modifier", command=modifier_produit)
bouton_modifier.place(x=530, y=680)





root.mainloop()
