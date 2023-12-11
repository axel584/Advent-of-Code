import pytest

class EnginePart():
    debut : int  # coordonne du debut
    fin: int
    ligne : int
    objet : str

    def __init__(self, debut, fin, ligne,objet) :
        self.debut = debut
        self.fin = fin
        self.ligne = ligne
        self.objet = objet

    def __str__(self):
        return f'engine part {self.debut} / {self.fin} / {self.ligne} / objet : {self.objet}' 

    def __repr__(self): # TOADD : difference avec __str__
        return f'engine part (repr) {self.debut} / {self.fin} / {self.ligne} / objet : {self.objet}' 


matrice = []
all_engine_part = []
all_gears = {}

def is_symbole(ligne,colonne):
    if ligne<0 or colonne<0 or ligne>=len(matrice) or colonne>=len(matrice[0]):
        return False
    return matrice[ligne][colonne]!="." and not matrice[ligne][colonne].isdigit()

def has_gear_symbol(ligne,colonne):
    if ligne<0 or colonne<0 or ligne>=len(matrice) or colonne>=len(matrice[0]):
        return False
    return matrice[ligne][colonne]=="*"

def add_engine_part_to_all_gears(ligne,colonne,engine_part):
    print("add engine to gears :",ligne,colonne,engine_part.objet)
    if ligne not in all_gears:
        all_gears[ligne] = {}
    if colonne not in all_gears[ligne]:
        all_gears[ligne][colonne] = []
    all_gears[ligne][colonne].append(engine_part)



def find_gear_symbol(engine_part):
    # recherche à gauche du premier caractère
    if has_gear_symbol(engine_part.ligne-1,engine_part.debut-1):
        add_engine_part_to_all_gears(engine_part.ligne-1,engine_part.debut-1,engine_part)
    if has_gear_symbol(engine_part.ligne,engine_part.debut-1):
        add_engine_part_to_all_gears(engine_part.ligne,engine_part.debut-1,engine_part)
    if has_gear_symbol(engine_part.ligne+1,engine_part.debut-1):
        add_engine_part_to_all_gears(engine_part.ligne+1,engine_part.debut-1,engine_part)
    # recherche au dessus et en dessous des caractères
    for i in range(engine_part.debut,engine_part.fin):
        if has_gear_symbol(engine_part.ligne-1,i):
            add_engine_part_to_all_gears(engine_part.ligne-1,i,engine_part)
        if has_gear_symbol(engine_part.ligne+1,i):
            add_engine_part_to_all_gears(engine_part.ligne+1,i,engine_part)    
    # recherche à droite du dernier caractère
    if has_gear_symbol(engine_part.ligne-1,engine_part.fin):
        add_engine_part_to_all_gears(engine_part.ligne-1,engine_part.fin,engine_part)
    if has_gear_symbol(engine_part.ligne,engine_part.fin):
        add_engine_part_to_all_gears(engine_part.ligne,engine_part.fin,engine_part)
    if has_gear_symbol(engine_part.ligne+1,engine_part.fin):
        add_engine_part_to_all_gears(engine_part.ligne+1,engine_part.fin,engine_part)

def find_symbol(engine_part):
    # recherche à gauche du premier caractère
    if is_symbole(engine_part.ligne-1,engine_part.debut-1) or is_symbole(engine_part.ligne,engine_part.debut-1) or is_symbole(engine_part.ligne+1,engine_part.debut-1):
        return True
    # recherche au dessus et en dessous des caractères
    for i in range(engine_part.debut,engine_part.fin):
        if is_symbole(engine_part.ligne-1,i) or is_symbole(engine_part.ligne+1,i):
            return True
    # recherche à droite du dernier caractère
    if is_symbole(engine_part.ligne-1,engine_part.fin) or is_symbole(engine_part.ligne,engine_part.fin) or is_symbole(engine_part.ligne+1,engine_part.fin):
        return True
    return False

def search_engine_part(line,nb_line):
    liste_engine_part_found = []
    in_engine_part = False
    for i,x in enumerate(line): ##### TOADD
        if x.isdigit() :
            if not in_engine_part:
                debut = i
                in_engine_part = True
        else : # n'est pas / n'est plus dans un nombre
            if in_engine_part : 
                fin = i
                in_engine_part = False
                liste_engine_part_found.append(EnginePart(debut,fin,nb_line,line[debut:fin]))
    if in_engine_part : # cas où le nombre est à la fin de la ligne
        fin = len(line)
        liste_engine_part_found.append(EnginePart(debut,fin,nb_line,line[debut:fin]))            
    return liste_engine_part_found


def lire_carte(chemin):
    nb_line = 0
    for line in open(chemin):
        line = line.strip()
        matrice.append([x for x in line])
        all_engine_part.extend(search_engine_part(line,nb_line)) # TOADD
        nb_line += 1

def enigme_day3(chemin):
    lire_carte(chemin)
    somme = 0
    for line in matrice:
        print(line)
    for engine_part in all_engine_part:
        print(engine_part)
        if find_symbol(engine_part) :
            somme += int(engine_part.objet)
            print("somme : ",somme)
    return somme

def enigme_day3_second_part(chemin):
    lire_carte(chemin)
    somme = 0
    for line in matrice:
        print(line)
    for engine_part in all_engine_part:
        print(engine_part)
        find_gear_symbol(engine_part)
    print(all_gears)
    for ligne in all_gears.keys():
        for colonne in all_gears[ligne].keys():
            print(ligne,colonne)
            if len(all_gears[ligne][colonne])==2: # to add : tuple as coordonnées d'un dictionnaire
                somme += int(all_gears[ligne][colonne][0].objet)*int(all_gears[ligne][colonne][1].objet)
    return somme


@pytest.mark.skip(reason="test only part 2")
def test_enigme_day3():
    assert enigme_day3("input-03a-test.txt") == 4361

def test_enigme_day3_second_part():
    assert enigme_day3_second_part("input-03a-test.txt") == 467835

if __name__ == "__main__" :
    #print(enigme_day3("input-03.txt"))
    print(enigme_day3_second_part("input-03.txt"))