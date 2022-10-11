from tkinter import *
from pokedex import *
from affichage_pokemon import *


def pokedex():

    """
    Foncrion appeler par la page d'accueil, pour afficher le pokedex a partir d'un csv
    """



    #Ouverture d'une fenetre pour choisir son fichier csv pour generer l'affichage du pokedex
    filename = filedialog.askopenfilename(initialdir = "/", 
        title = "Select a File", 
        filetypes = (("", 
            "*.csv"), ("all files", "*.*")))

    #creation de la fenetre du pokedex
    pokedex = Tk()
    height = pokedex.winfo_height()
    pokedex.title("Pokedex")
    pokedex.attributes('-fullscreen', True)
    pokedex.bind('<Escape>',lambda e: pokedex.destroy())

    
    def listing_animaux(nom):
        config = configparser.ConfigParser()
        config.read(f"save/{nom}/liste_animaux.conf")
        animaux = {}
        for element in config.sections():
            if element != nom:
                animaux[element] = config[element]["photo"]
        return animaux
        
    #traitement du CSV voir le fichier pokedex.py pour comprendre open_csv() & valide()
    filename = listing_animaux("POulet")
    filename = valide(filename)

    #creation d'une frame et d'un canvas pour avoir une scrollbar et afficher tout les pokemons
    frame_container=Frame(pokedex)
    canvas_container=Canvas(frame_container, height=1080, width=1900)
    frame2=Frame(canvas_container)
    myscrollbar=Scrollbar(frame_container,orient="vertical",command=canvas_container.yview)
    canvas_container.create_window((0,0),window=frame2,anchor='nw')


    def find_key(v): 
        """
        fonction qui permet de rechercher une clef en fonction d'une valeur
        """
        for k, val in keys_images.items(): 
            if v == val: 
                return k 
        return "Clé n'existe pas"


    def pokem(img):
        """
        Fonction qui va donner le nom du pokemon en l'ayant trouver avec find_key() a la fonction qui permet d'afficher le pokemon et ces 
        specifications
        """
        img = find_key(img)
        print(img)
        aff_pokemon(img, filename)
        

    #affichage des differents boutons de pokemons
    button = [] #creer une liste d'images pour les boutons

    keys_images = {} #associe le nom de l'image donner a tkinter au pokemon

    #permet de remplir la liste button et keys_images, le try except permet de contourner les quelques images manquantes
    for key in filename.keys():
        try:
            file = f"ico/{key}.png"
            key2 = PhotoImage(master = pokedex, file = file) #ouverture de l'image dans tkinter

            #ajout dans la liste et le dico decrit ci-dessus
            keys_images[key] = key2
            button.append(key2)

        except:
            continue
    l = 0
    c = 0

    casebutton = {} #permet d'associer un numero a chaque bouton (plus simple pour la suite)
    Buttonpok = {} #permet d'associer un numero a chaque image (identique a celui du bouton)

    #genere les differents numero par apport au nombre de boutons
    for i in range(len(button)):
        casebutton[i] = button[i]

    #creer les boutons
    for a in casebutton.keys():
        
        #permet de mettre en forme avec une grille de 14 colonnes pour un bon affichage et d'une infinité de ligne en fonction du nombre de pokemon present
        if c == 15:
                c = 0
                l += 1
        

        Buttonpok[a] = Button(frame2, image = casebutton[a], width = 90, padx = 0, command = lambda img=casebutton[a]: pokem(img))
        Buttonpok[a].grid(row=l, column=c, columnspan=1,padx=5,pady=5)
            
        c += 1

    
    frame2.update() # met a jour la frame pour tout afficher
    canvas_container.configure(yscrollcommand=myscrollbar.set, scrollregion="0 0 0 %s" % frame2.winfo_height())#met a jour le canvas pour afficher la scrollbar

    #mets tout en forme pour la presentation
    canvas_container.pack(side=LEFT)
    myscrollbar.pack(side=RIGHT, fill = Y)

    frame_container.pack()
    pokedex.mainloop()


