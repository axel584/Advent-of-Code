import pytest
import re

DIRECTION = {
    'N':[-1,0],
    'NE':[-1,1],
    'E':[0,1],
    'SE':[1,1],
    'S':[1,0],
    'SO':[1,-1],
    'O':[0,-1],
    'NO':[-1,-1],
}

DIRECTION_DIAG = {
    'NE':[-1,1],
    'SE':[1,1],
    'SO':[1,-1],
    'NO':[-1,-1],
}

def imprime_tableau(tableau):
    for ligne in tableau:
        print("|".join(ligne))

def recherche(pattern,tab,l,c,direction,display=False):
    for i in range(len(pattern)):
        coord_ligne = l+(i*DIRECTION[direction][0])
        coord_colonne = c+(i*DIRECTION[direction][1])
        if coord_ligne<0 or coord_colonne<0 :
            return False
        try :
            case = tab[coord_ligne][coord_colonne]
        except IndexError:
            return False
        if display:
            print(i,l+(i*DIRECTION[direction][0]),c+(i*DIRECTION[direction][1]),case,pattern[i])
            #print(tab[l+(i*DIRECTION[direction][0])])
        if case!=pattern[i]:
            return False
    return True

def enigme_day04_first_part(chemin):
    tab = []
    somme = 0
    with open(chemin,'r') as fichier :
        for ligne in fichier:
            tab.append(list(ligne.strip()))
        #imprime_tableau(tab)
        for num_ligne,ligne in enumerate(tab):
            for num_colonne,case in enumerate(ligne):
                for direction in DIRECTION:
                    #print(case,num_ligne,num_colonne,direction)
                    if recherche("XMAS",tab,num_ligne,num_colonne,direction):
                        #print("*"*50)
                        #print(somme,num_ligne,num_colonne,direction)
                        recherche("XMAS",tab,num_ligne,num_colonne,direction,True)
                        somme += 1
    return somme


def enigme_day04_second_part(chemin):
    tab = []
    somme = 0
    coordonnee_a = []
    with open(chemin,'r') as fichier :
        for ligne in fichier:
            tab.append(list(ligne.strip()))
        for num_ligne,ligne in enumerate(tab):
            for num_colonne,case in enumerate(ligne):
                for direction in DIRECTION_DIAG:
                    if recherche("MAS",tab,num_ligne,num_colonne,direction):
                        recherche("MAS",tab,num_ligne,num_colonne,direction,True)
                        position_a = str(num_ligne+DIRECTION[direction][0])+"-"+str(num_colonne+DIRECTION[direction][1])
                        print(position_a)
                        if position_a in coordonnee_a :
                            somme += 1
                        else :
                            coordonnee_a.append(position_a)
    return somme

def test_enigme_day04_first_part():
    assert enigme_day04_first_part("input-04-test.txt")==18

def test_enigme_day04_second_part():
    assert enigme_day04_second_part("input-04-test.txt")==9

if __name__ == "__main__" :
    #print(enigme_day04_first_part("input-04.txt"))
    print(enigme_day04_second_part("input-04.txt"))