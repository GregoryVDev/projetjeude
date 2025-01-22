from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("320x500+500+100")
root.title("Jeu de simulation de dé")

label1 = Label(root, text="Choisir un numéro entre 1 et 6", pady=10, bg="blue", fg="white", font=("Arial", 14, "bold"))
label1.grid(row=1, column=1, columnspan=2)

choice_number = Entry(root)
choice_number.grid(row=2, column=1, columnspan=2, pady=15)



root.mainloop()