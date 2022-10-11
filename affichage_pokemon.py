from tkinter import *
from tkinter import filedialog
from pokedex import *
from tkinter import ttk

def aff_pokemon(name,filename):

	"""
	Affiche le pokemon qui a ete cliquer sur la page pokedex
	"""

	#creer une fenetre pour afficher le pokemon et la parametre
	pokemon = Tk()
	pokemon.title(name)
	pokemon.geometry('640x480')
	pokemon.grid_columnconfigure((0,1,2), minsize=15, weight=1) #permet de tout centrer
	pokemon.attributes('-fullscreen', True)
	pokemon.bind('<Escape>',lambda e: pokemon.destroy())

	#affiche le nom
	Label(pokemon, text= name, font = ("Arial",20), anchor=CENTER, width=140).grid(row=0,column=0,columnspan = 3)
	file = f"png/{name}.png"
	img = PhotoImage(master = pokemon, file = file)
	Label(pokemon, image = img, anchor=CENTER).grid(row=4,column=0,columnspan = 3)
	#permet de creer des jauges pour les differents paramettre
	spe = {"HP": 320, "Attack":190, "Defense": 230, "Sp. Atk": 194, "Sp. Def": 230}
	gauge = {"HP": 320, "Attack":190, "Defense": 230, "Sp. Atk": 194, "Sp. Def": 230}

	a = ""
	l = 60
	r = 0
	bar = [1, 2, 3, 4, 5]
	co = 0
	values = filename[name]

	#une boulce pour creer u
	for value in values.keys():
		if value in gauge.keys():
			cal = int(spe[value])*10
			c = round(int(values[value])*1000/cal)
			Label(pokemon, text=f"{value}:", font=("Arial", 15)).grid(row = l, column= 0, sticky= "e")
			Label(pokemon, text=f"{values[value]}", font=("Arial", 15)).grid(row = l, column= 2, sticky= "w")			
			bar[co] = ttk.Progressbar(pokemon, orient = HORIZONTAL, 
	              length = 1000, mode = 'determinate') 
			bar[co]['value'] = c
			bar[co].grid(row=l, column=1, sticky="w")
			pokemon.update_idletasks()
			l +=1
			co +=1
		if value == "Generation" or value == "Type" or value == "Legendary":
			if value == "Type":
				if values[value][1] == "":
					a +=f", {value}: {values[value][0]}"
				else:
					a +=f", {value}: {values[value][0]} & {values[value][1]}"
			else:
				a += f", {value}:{values[value]}"

		Label(pokemon, text=a, font=("Arial", 15)).grid(row = l, column= 1)

	
	pokemon.mainloop()

		
		
