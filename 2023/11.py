
from itertools import combinations


map = []
galaxies = []

class Case:

    ligne : int
    colonne : int
    value : str

    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f'[{self.ligne}/{self.colonne}] {self.value}'

    def __repr__(self):
        return f'{self.value}'

def is_colonne_vide(indice_colonne):
    for indice_ligne in range(len(map)):
        if map[indice_ligne][indice_colonne].value=="#":
            return False
    return True

def augmente_colonne(indice_colonne):
    for indice_ligne in range(len(map)):
        map[indice_ligne].insert(indice_colonne,Case('M')) # M for million !

def is_ligne_vide(indice_ligne):
    for indice_colonne in range(len(map[0])):
        if map[indice_ligne][indice_colonne].value=="#":
            return False
    return True

def augmente_ligne(indice_ligne):
    nouvelle_ligne = []
    for _ in range(len(map[0])):
        nouvelle_ligne.append(Case('M')) # M for million
    map.insert(indice_ligne,nouvelle_ligne)

def distance(galaxie1,galaxie2):
    #print(galaxie1.ligne,galaxie1.colonne,galaxie2.ligne,galaxie2.colonne)
    return abs(galaxie2.ligne-galaxie1.ligne)+abs(galaxie2.colonne-galaxie1.colonne)

def enigme_day11(chemin):
    with open(chemin,'r') as fichier :
        for ligne in fichier :
            ligne_case = []
            for colonne in ligne.strip():
                ligne_case.append(Case(colonne.strip()))
            map.append(ligne_case)
    # affiche map:
    # for ligne in map:
    #     print(''.join([case.value for case in ligne]))        
    # augmente les colonnes si colonne vide
    has_increase = False
    for indice_colonne,colonne in enumerate(map[0]):
        if has_increase:
            has_increase=False
            continue
        if is_colonne_vide(indice_colonne):
            print("colonne vide",indice_colonne)
            has_increase=True
            augmente_colonne(indice_colonne)
    # affiche map:
    #print("apres gestion colonne")
    # for ligne in map:
    #     print(''.join([case.value for case in ligne]))            
    # augmente les lignes
    has_increase = False
    for indice_ligne,ligne in enumerate(map):
        if has_increase:
            has_increase=False
            continue
        if is_ligne_vide(indice_ligne):
            has_increase=True
            augmente_ligne(indice_ligne)
    # ajoute les compteurs        
    for indice_ligne,ligne in enumerate(map):
        for indice_colonne,colonne in enumerate(ligne):
            colonne.ligne = indice_ligne
            colonne.colonne = indice_colonne
            if colonne.value=="#":
                galaxies.append(colonne)
    #print(galaxies)   
    # liste les combinaisons possibles de galaxies
    comb = combinations(galaxies, 2)   
    somme = 0       
    for i in list(comb):
        somme += distance(i[0],i[1])
    # affiche map:
    # for ligne in map:
    #     print(''.join([case.value for case in ligne]))
    return somme

def test_enigme_day11():
    assert enigme_day11("input-11a-test.txt") == 374


if __name__ == "__main__" :
    print(enigme_day11("input-11.txt"))