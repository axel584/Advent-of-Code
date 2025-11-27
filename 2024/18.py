from collections import defaultdict
import pytest
import re
from itertools import combinations, product

# TAILLE = 7
# NB_STEP = 12
TAILLE = 71
NB_STEP = 2907

def imprime(carte):
    for ligne in carte:
        print("".join(ligne))

def distance_de_la_fin(x,y):
    return (TAILLE - x) + (TAILLE - y)


def find_voisins(position,carte):
    res=[]
    x =position['x'] 
    y =position['y'] 
    parcouru =position['parcouru'] 
    if x+1<TAILLE :
        if carte[x+1][y]=='.':
            voisin1 = {'parcouru':parcouru+1,'raf':distance_de_la_fin(x+1,y),'x':x+1,'y':y}
            res.append(voisin1)
    if y+1<TAILLE :
        if carte[x][y+1]=='.':
            voisin2 = {'parcouru':parcouru+1,'raf':distance_de_la_fin(x,y+1),'x':x,'y':y+1}
            res.append(voisin2)
    if x-1>=0:
        if carte[x-1][y]=='.':
            voisin3 = {'parcouru':parcouru+1,'raf':distance_de_la_fin(x-1,y),'x':x-1,'y':y}
            res.append(voisin3)
    if y-1>=0:
        if carte[x][y-1]=='.':
            voisin4 = {'parcouru':parcouru+1,'raf':distance_de_la_fin(x,y-1),'x':x,'y':y-1}
            res.append(voisin4)
    return res

def find_plus_petit_non_traite(carte_solution,carte_traite):
    min = 999999
    plus_petit = None
    for ligne in carte_solution:
        for colonne in ligne :
            if len(colonne)==0 :
                continue
            if carte_traite[colonne["x"]][colonne["y"]]:
                continue
            cout = colonne["parcouru"]+colonne["raf"]
            if cout<min : 
                min = cout
                plus_petit = colonne
    return plus_petit


def enigme_day18_first_part(chemin):
    carte = [['.']*TAILLE for _ in range(TAILLE)]
    carte_solution = [[{}]*TAILLE for _ in range(TAILLE)]
    carte_traite = [[{}]*TAILLE for _ in range(TAILLE)]
    imprime(carte)
    with open(chemin, "r") as fichier:
        i = 0
        for ligne in fichier:
            x,y = list(map(int,ligne.strip().split(',')))
            carte[y][x]="#"
            i +=1
            if i==NB_STEP :
                break
        print("*"*50)
        imprime(carte)
        position = {'parcouru':0,'raf':distance_de_la_fin(0,0),'x':0,'y':0}
        carte_solution[0][0] = position
        carte_traite[0][0] = position
        i = 0
        while True :
            voisins = find_voisins(position,carte)
            for voisin in voisins : 
                if len(carte_solution[voisin['x']][voisin['y']])==0 :
                    carte_solution[voisin['x']][voisin['y']]=voisin
            position = find_plus_petit_non_traite(carte_solution,carte_traite)
            if position["x"]==TAILLE-1 and position["y"]==TAILLE-1 : # sortie en bas à droite
                return position["parcouru"]
            carte_traite[position["x"]][position["y"]]=position

def enigme_day18_second_part(chemin):
    carte = [['.']*TAILLE for _ in range(TAILLE)]
    imprime(carte)
    with open(chemin, "r") as fichier:
        i = 0
        for ligne in fichier:
            x,y = list(map(int,ligne.strip().split(',')))
            print(f"({i}) : coord : {x},{y}")
            carte[y][x]="#"
            i +=1
            position = {'parcouru':0,'raf':distance_de_la_fin(0,0),'x':0,'y':0}
            carte_solution = [[{}]*TAILLE for _ in range(TAILLE)]
            carte_traite = [[{}]*TAILLE for _ in range(TAILLE)]
            carte_solution[0][0] = position
            carte_traite[0][0] = position
            fini = False
            while not fini :
                voisins = find_voisins(position,carte)
                for voisin in voisins : 
                    if len(carte_solution[voisin['x']][voisin['y']])==0 :
                        carte_solution[voisin['x']][voisin['y']]=voisin
                position = find_plus_petit_non_traite(carte_solution,carte_traite)
                if position == None :
                    print(f"fini : {x},{y}")
                    imprime(carte)
                    return str(x)+","+str(y)
                if position["x"]==TAILLE-1 and position["y"]==TAILLE-1 : # sortie en bas à droite
                    fini = True
                carte_traite[position["x"]][position["y"]]=position

def test_enigme_day18():
    assert enigme_day18_first_part("input-18-test.txt") == 22
    #assert enigme_day18_second_part("input-18-test2.txt") == 118440


if __name__ == "__main__":
    #print(enigme_day18_first_part("input-18-test.txt"))
    #print(enigme_day18_first_part("input-18.txt"))
    print(enigme_day18_second_part("input-18.txt"))
