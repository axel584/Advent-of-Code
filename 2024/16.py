from collections import defaultdict
import pytest
import re
from itertools import combinations, product

DIRECTION = {'N':(-1,0),'E':(0,1),'S':(1,0),'O':(0,-1)}

def imprime(carte,carte_traite=None):
    if carte_traite!=None :
        for element in carte_traite:
            carte[element["l"]][element["c"]]='X'
    for ligne in carte:
        print("".join(ligne))

def mahnattan(l,c,end):
    return abs(l-end[0])+abs(c-end[1])

def voisin_dans_carte(voisin,carte):
    for element in carte : 
        if element["l"]==voisin["l"] and element["c"]==voisin["c"]:
            return True
    return False

def find_plus_petit_non_traite(carte_solution,carte_traite):
    coord_traite = []
    for element in carte_traite:
        coord_traite.append(str(element["l"])+"-"+str(element["c"]))
    min = None
    min_value = 999999
    for element in carte_solution:
        if element["cout"]+element["raf"]<min_value and str(element["l"])+"-"+str(element["c"]) not in coord_traite:
            min = element
            min_value = element["cout"]+element["raf"]
    return min


def find_voisins(position,carte,end):
    res=[]
    l =position['l'] 
    c =position['c'] 
    cout =position['cout']
    sens_position = position["sens"]
    if carte[l+DIRECTION[sens_position][0]][c+DIRECTION[sens_position][1]]=='.' or carte[l+DIRECTION[sens_position][0]][c+DIRECTION[sens_position][1]]=='E':
        res.append({'cout':cout+1,'raf':mahnattan(l+DIRECTION[sens_position][0],c+DIRECTION[sens_position][1],end),'sens':position["sens"],'l':l+DIRECTION[sens_position][0],'c':c+DIRECTION[sens_position][1]})
    directions = list(DIRECTION.keys())
    sens_droite = directions[(directions.index(sens_position)+1)%4]
    if carte[l+DIRECTION[sens_droite][0]][c+DIRECTION[sens_droite][1]]=='.' or carte[l+DIRECTION[sens_droite][0]][c+DIRECTION[sens_droite][1]]=='E':
        res.append({'cout':cout+1001,'raf':mahnattan(l+DIRECTION[sens_droite][0],c+DIRECTION[sens_droite][1],end),'sens':sens_droite,'l':l+DIRECTION[sens_droite][0],'c':c+DIRECTION[sens_droite][1]})
    sens_gauche = directions[(directions.index(sens_position)+3)%4]    
    if carte[l+DIRECTION[sens_gauche][0]][c+DIRECTION[sens_gauche][1]]=='.' or carte[l+DIRECTION[sens_gauche][0]][c+DIRECTION[sens_gauche][1]]=='E':
        res.append({'cout':cout+1001,'raf':mahnattan(l+DIRECTION[sens_gauche][0],c+DIRECTION[sens_gauche][1],end),'sens':sens_gauche,'l':l+DIRECTION[sens_gauche][0],'c':c+DIRECTION[sens_gauche][1]})
    return res

def enigme_day16_first_part(chemin):
    carte = []
    start = (0,0)
    end = (0,0)
    with open(chemin, "r") as fichier:
        premiere_partie = True
        for num_ligne,ligne in enumerate(fichier):
            carte.append(list(ligne.strip()))
            for num_colonne,c in enumerate(ligne.strip()):
                if c=='S':
                    start = (num_ligne,num_colonne)
                if c=='E':
                    end = (num_ligne,num_colonne)
    position = {'l':start[0],'c':start[1],'sens':'E','cout':0,'raf':mahnattan(start[0],start[1],end)}
    #print(position)
    #print(start,end)
    imprime(carte)
    fini = False
    carte_solution = []
    carte_traite = []
    while not fini :
        voisins = find_voisins(position,carte,end)
        #print(voisins)
        for voisin in voisins : 
            if not voisin_dans_carte(voisin,carte_solution):
                carte_solution.append(voisin)
        position = find_plus_petit_non_traite(carte_solution,carte_traite)
        if position == None :
            imprime(carte,carte_traite)
        if position["l"]==end[0] and position["c"]==end[1] : # sortie
            fini = True
        carte_traite.append(position)
    return position["cout"]



def test_enigme_day16():
    assert enigme_day16_first_part("input-16-test.txt") == 7036
    #assert enigme_day16_second_part("input-16-test2.txt") == 12


if __name__ == "__main__":
    print(enigme_day16_first_part("input-16.txt"))
    #print(enigme_day16_second_part("input-16.txt"))
