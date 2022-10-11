from tkinter import*
import tkinter
import tkinter as tk
from tkinter import filedialog
import tkinter.font as font
from PIL import Image, ImageTk
from ajouter_pokemon import*


def getEntry():
    res = myEntry.get()
    print(res)

    myEntry = tk.Entry(gui, width=40)
    myEntry.pack(pady=20)
    btn = tk.Button(gui, height=1, width=10, text="Lire", command=getEntry)
    btn.pack()

def ajouter_pokemon():
    
    pokemon = Tk()
    pokemon.title("Nouveau Pokemon")
    pokemon.geometry('640x480')
    pokemon.bind('<Escape>',lambda e: pokemon.destroy())
    pokemon.resizable(width=False, height=False)
 
    image4 = Image.open("creer.png")
    resize_image = image4.resize((550, 118))
    resize_image.save(f'creer.png', resize_image.format)
 
    img = PhotoImage(master = pokemon, file = "creer.png")
    Label(pokemon, image = img, anchor=CENTER).pack()

   
    pokemon_new = {}
    nom = Label(pokemon, text = 'Quel est le nom de votre Pokemon ?')
    nom.pack()

    
    
    entry = tk.Entry(pokemon, bd=1)
    entry.pack()  
    
    
    typ = Label(pokemon, text = 'Quel est le type de votre Pokemon ?')
    typ.pack()
    
    entry = tk.Entry(pokemon, bd=1)
    entry.pack()

    
    hp = Label(pokemon, text = "Combien d' HP a votre pokemon? ?")
    hp.pack()
    
    entry = tk.Entry(pokemon, bd=1)
    entry.pack()

    
    attack = Label(pokemon, text = "Combien a votre pokemon en attaque ?")
    attack.pack()
    
    entry = tk.Entry(pokemon, bd=1)
    entry.pack()

    
    defense = Label(pokemon, text = 'Combien a votre pokemon en défense ?')
    defense.pack()
    
    entry = tk.Entry(pokemon, bd=1)
    entry.pack()  
    
	
    pokemon_new[nom] = { "Type 1":typ, "Type 2":"","Total":"", "HP":hp, "Attack": attack, "Defense": defense, "Sp. Atk":"", "Sp. Def":"", "Sp. Def":"", "Speed":"",
"Generation":"Special!", "Legendary":True}
    a = open_csv("pokemon_copie_2.csv")
    a = valide(a)
    a[nom]=pokemon_new[nom]
    save_csv(a)

    pokemon.mainloop()


