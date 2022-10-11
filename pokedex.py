import csv
import os
from PIL import Image


def open_csv(path):
    dico=[] #c'est une liste
    csv.register_dialect('myDialect', delimiter=',', quotechar='|')
    with open(path) as myFile:
            reader = csv.DictReader(myFile, dialect='myDialect')
            for row in reader:
                dico.append(row)
    return dico


def valide(dico):
    result = {}
    typ= []
    for element in dico:
        typ.append(element['Type 1'])
        typ.append(element['Type 2'])
        result[element["Name"]] = element
        result[element["Name"]]["Type"] = typ
        del result[element["Name"]]["Type 1"],result[element["Name"]]["Type 2"], result[element["Name"]]["Name"]
        typ= []

    return result


def research(pokedex, pokemon):
    try:
        assert type(pokedex) is dict, "Renseigner un dictionnaire  dans pokedex (la fonction valide peut vous aider a l'optenir"
        
    except:
        pokedex = valide(pokedex)
        
    if pokemon in pokedex:
        return True
    return False
                

		
        
def fusion(pokedex1, pokedex2):
    x = pokedex2
    y = pokedex1
    try:
        assert type(pokedex1) == dict
    except AssertionError:
        pokedex1 = valide(pokedex1)
        
    try:
        assert type(pokedex2) == dict
    except AssertionError:
        pokedex2 = valide(pokedex2)

    if len(pokedex1) > len(pokedex2):
        x = pokedex1
        y = pokedex2
    for key in y.keys():
        if key in x:
            continue
        else:
            x[key] = y[key]
    return x


def save_csv(dico):
    result =  []
    temp = {}
    for key in dico.keys():
        temp["Nom"] = key
        for value in dico[key].keys():
            temp[value] = dico[key][value]
        result.append(temp)
        temp = {}


    champs=['Nom','HP','Attaque','Defense', 'Vitesse', 'Type']
    with open('pokedexfinal.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, dialect="myDialect",fieldnames = champs) #le fichier objet csvfile est converti en DictWriter objet.
    #avec les champs en argument.
        writer.writeheader()
        writer.writerows(result)




def research_element(pokedex, specificite):
    #assert type(pokedex) == dict, "merci d'utiliser la fonction valide avant de reutiliser cette commande"
    if specificite == "Type":
        pass

    spe = 0
    pokemon = ""
    for key in pokedex.keys():
        if int(pokedex[key][specificite]) > spe:
            spe = int(pokedex[key][specificite])
            pokemon = key

            continue
        elif int(pokedex[key][specificite]) == spe:
            pokemon += key
            
            continue
            
    return pokemon

def recup_images():
    a = open_csv("pokemon.csv")
    a = valide(a)
    for key in a.keys():
        key = key.lower()
        os.system(f"wget https://img.pokemondb.net/artwork/large/{key}.jpg")


def convertir_img():
    a = open_csv("pokemon.csv")
    a = valide(a)
    for key in a.keys():
        try:
            key = key.lower()
            im = Image.open(f'{key}.jpg')
            im.save(f'images/{key}.png')
        except:
            continue
    print("ok")

def resize_img():
    a = open_csv("pokemon.csv")
    a = valide(a)
    for key in a.keys():

        try:
            key = key.lower()
            foo = Image.open(f"png/{key}.png")
            width, height = foo.size
            width, height = 90, 90
            width, height = int(round(width)), int(round(height))
            imResize = foo.resize((width, height), Image.ANTIALIAS)
            imResize.save(f'ico/{key}.png', imResize.format)
        except:
            continue
    print("ok")

#etape 1 : open_csv
#etape 2 :valide
#etape 3 fusion
#etape 4 : save


    
