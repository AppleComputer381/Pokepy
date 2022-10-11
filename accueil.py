from tkinter import*
import tkinter
import tkinter as tk
from tkinter import filedialog
import tkinter.font as font
from PIL import Image, ImageTk
from ajouter_pokemon import*
from affichage_pokedex import*
from affichage_pokemon import*
from pokedex import*

##Creation de la fenetre
fenetre = Tk()
fenetre.title("Pokedex")
fenetre.geometry('640x480')
fenetre.attributes('-fullscreen', True)
fenetre.bind('<Escape>',lambda e: fenetre.destroy())


##Importation des images


image1 = Image.open("pokemon.png")
resize_image = image1.resize((320, 118))
img1 = ImageTk.PhotoImage(resize_image)


image2= Image.open("image_fond.png")
resize_image = image2.resize((1194,606))
img2 = ImageTk.PhotoImage(resize_image) 


image3= Image.open("pokepy.png")
resize_image = image3.resize((1112,170))
img3 = ImageTk.PhotoImage(resize_image)





#création du label de l'image redimensionner

label1 = Label(image=img1)
label1.image1 = img1
label1.pack()

label2 = Label(image=img2)
label2.image = img2
label2.pack()

label3 = Label(image=img3)
label3.image = img3
label3.pack()




##creation des widgets
Button(fenetre, text="Afficher le Pokedex", command = pokedex).place(relx=0.5, rely=0.5, anchor=CENTER, width=164)


def clique_entry(evenement):
    if entry.get() == 'Rechercher un Pokemon':
       entry.delete(0, "end") 
       entry.insert(0, '') 

def getEntry():
    res = entry.get()
    filename = open_csv("pokemon_copie_2.csv")
    filename = valide(filename)
    aff_pokemon(res, filename)


entry = tk.Entry(fenetre, bd=1)
entry.insert(0, 'Rechercher un Pokemon')
entry.bind('<FocusIn>', clique_entry)
entry.place(relx=0.5, rely=0.54, anchor=CENTER, width=164)

btn = fenetre.bind('<Return>',lambda e: getEntry())






#Création d'une bar de menu
def onOpen():
    print(filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))


"""

menubar = tk.Menu(fenetre)

filemenu = tk.Menu(menubar, tearoff=0)#tearoff=0 desactive les pointillés qui permettent de creer un menu a part
optionmenu = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label="Exit", command = fenetre.destroy)
menubar.add_cascade(label="Menu", menu = optionmenu)

optionmenu.add_command(label="Importer un pokedex",command=onOpen)#A utiliser surement pour importer un pokedex
optionmenu.add_command(label="Ajouter un pokemon", command=ajouter_pokemon)


fenetre.config(menu=menubar)

"""


fenetre.mainloop()

