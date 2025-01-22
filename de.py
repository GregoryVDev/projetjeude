import random
from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
# Définition des dimensions de la fenêtre et de sa position sur l'écran
root.geometry("320x500+500+100")
# Définition du titre de la fenêtre
root.title("Jeu de simulation de dé")

def play():
    pass



# Création d'un label pour le texte d'instruction
label1 = Label(root, text="Choisir un numéro entre 1 et 6", pady=10, bg="blue", fg="white", font=("Arial", 14, "bold"))
# Positionnement du label dans une grille à la ligne 1 et colonnes 1-2
label1.grid(row=1, column=1, columnspan=2)

# Création d'une entrée pour que l'utilisateur puisse entrer un numéro
choice_number = Entry(root)
# Positionnement de l'entrée dans une grille à la ligne 2 et colonnes 1-2, avec un padding vertical
choice_number.grid(row=2, column=1, columnspan=2, pady=15)

# Liste des chemins vers les images des dés (une pour chaque face)

list_images = ["images/de1.png", "images/de2.png", "images/de3.png", "images/de4.png", "images/de5.png", "images/de6.png"]

# Chargement aléatoire d'une image depuis la liste
image_de = ImageTk.PhotoImage(Image.open(random.choice(list_images)))

# Création d'un label pour afficher l'image sélectionnée
label_image = Label(root, image=image_de)
# Lier l'image au label pour éviter qu'elle soit supprimée par le garbage collector
label_image.image = image_de
# Positionnement de l'image dans une grille à la ligne 3 et colonnes 1-2
label_image.grid(row=3, column=1, columnspan=2)

button_play = Button(root, text="Lancer le dé", fg = "blue", font=("Arial", 14, "bold"), width=15, height=3, command=play)
button_play.grid(row=4, column=1, padx= 20, pady=20)




root.mainloop()