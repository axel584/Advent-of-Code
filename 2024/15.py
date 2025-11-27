from collections import defaultdict
import pytest
import re
from itertools import combinations, product

DIRECTION = {
    '^':(-1,0),
    'v':(1,0),
    '>':(0,1),
    '<':(0,-1),
}

TAILLE_LARGEUR = 0
TAILLE_HAUTEUR = 0
carte = []
robot = (0,0)

def imprime():
    global robot,carte
    print("ROBOT",robot)
    for ligne in carte:
        print("".join(ligne))

def deplace(direction):
    global robot,carte
    position_robot = robot
    pile = []
    pile.append(position_robot)
    while carte[position_robot[0]][position_robot[1]]!="#":
        position_robot = (position_robot[0]+direction[0],position_robot[1]+direction[1])
        if carte[position_robot[0]][position_robot[1]]=='.' : # si on trouve un espace libre, on depile
            while len(pile)>0 :
                element = pile.pop()
                carte[position_robot[0]][position_robot[1]] = carte[element[0]][element[1]]
                position_robot = element
            carte[robot[0]][robot[1]]="."
            robot=(robot[0]+direction[0],robot[1]+direction[1]) # il a trouve un espace, il se deplace dans la direction d'une case
            return
        pile.append(position_robot)
    return


def enigme_day15_first_part(chemin):
    global robot, carte
    with open(chemin, "r") as fichier:
        premiere_partie = True
        for num_ligne,ligne in enumerate(fichier):
            if ligne.strip()=="" :
                premiere_partie = False
                #imprime()
            if premiere_partie :
                carte.append(list(ligne.strip()))
                for num_colonne,c in enumerate(ligne.strip()):
                    if c=='@':
                        robot = (num_ligne,num_colonne)
            else : 
                for direction in ligne.strip():
                    deplace(DIRECTION[direction])
                    #imprime()
    somme = 0
    for num_ligne,ligne in enumerate(carte):
        for num_colonne,colonne in enumerate(ligne):
            if colonne=="O":
                somme += (num_ligne *100) + num_colonne
    return somme



def test_enigme_day15():
    #assert enigme_day15_first_part("input-15-mini.txt") == 2028
    assert enigme_day15_first_part("input-15-test.txt") == 10092
    #assert enigme_day15_second_part("input-15-test2.txt") == 12


if __name__ == "__main__":
    print(enigme_day15_first_part("input-15.txt"))
    #print(enigme_day15_second_part("input-15.txt"))
