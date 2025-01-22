import random
from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
# Définition des dimensions de la fenêtre et de sa position sur l'écran
root.geometry("500x500+500+100")
# Définition du titre de la fenêtre
root.title("Jeu de simulation de dé")

# Fonction afin de lancer le bouton "lancer le dé"
def play():

    number = 0
    # Récupère les images dans la liste, il prend une image aléatoirement et l'affiche
    choice_image = random.choice(list_images)
    # Chargement aléatoire d'une image depuis Choice image qui est relié à list_images
    image1 = ImageTk.PhotoImage(Image.open(choice_image))
    # Met à jour l'image affichée dans le label
    label_image.configure(image=image1)
    label_image.image = image1

    if choice_image == "images/de1.png":
        number = 1
    elif choice_image == "images/de2.png":
        number = 2
    elif choice_image == "images/de3.png":
        number = 3
    elif choice_image == "images/de4.png":
        number = 4
    elif choice_image == "images/de5.png":
        number = 5
    else:
        number = 6

    if number != int(choice_number.get()):
        label_result.config(text="Vous avez perdu")
    else:
        label_result.config(text="Vous avez gagné")



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

# Afficher les boutons pour lancer le dé
button_play = Button(root, text="Lancer le dé", fg = "blue", font=("Arial", 14, "bold"), width=15, height=3, command=play)
button_play.grid(row=4, column=1, padx= 20, pady=20)

# Afficher le bouton pour quitter la fenêtre
button_leave = Button(root, text="Quitter", fg = "red", font=("Arial", 14, "bold"), width=15, height=3, command=root.quit)
button_leave.grid(row=4, column=2, padx= 20, pady=20)

# Afficher le résultat à la fin de la partie
label_result = Label(root, text="", pady=20, fg="red", font=("Arial", 14, "bold"))
label_result.grid(row=5, column=1, columnspan=2)

root.mainloop()