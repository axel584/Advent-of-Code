from collections import defaultdict
import pytest
import re
from itertools import combinations, product


def is_in(point,max_l,max_c):
    return point[0]>=0 and point[0]<=max_l and point[1]>=0 and point[1]<=max_c

def enigme_day08_first_part(chemin):
    somme = 0
    antennes = defaultdict(list)
    antinodes = []
    with open(chemin,'r') as fichier :
        for num_ligne,ligne in enumerate(fichier):
            for num_colonne,colonne in enumerate(ligne.strip()):
                if colonne!='.':
                    antennes[colonne].append((num_ligne,num_colonne))
                max_l = num_ligne
                max_c = num_colonne
        #print(antennes)
        for frequence,positions in antennes.items():
            #print(frequence,positions)
            for combinaison in combinations(positions,2):
                #print("combinaison :",combinaison)
                vecteur = (combinaison[1][0]-combinaison[0][0],combinaison[1][1]-combinaison[0][1])
                #print("vecteur",vecteur)
                antinode1 = (combinaison[1][0]+vecteur[0],combinaison[1][1]+vecteur[1])
                if is_in(antinode1,max_l=max_l,max_c=max_c) :
                    antinodes.append(str(antinode1[0])+"-"+str(antinode1[1]))
                #print("antinode 1 :",antinode1)
                antinode2 = (combinaison[0][0]-vecteur[0],combinaison[0][1]-vecteur[1])
                #print("antinode 2 :",antinode2)
                if is_in(antinode2,max_l=max_l,max_c=max_c) :
                    antinodes.append(str(antinode2[0])+"-"+str(antinode2[1]))
    return len(set(antinodes))

def enigme_day08_second_part(chemin):
    somme = 0
    antennes = defaultdict(list)
    antinodes = set()
    with open(chemin,'r') as fichier :
        for num_ligne,ligne in enumerate(fichier):
            for num_colonne,colonne in enumerate(ligne.strip()):
                if colonne!='.':
                    antennes[colonne].append((num_ligne,num_colonne))
                max_l = num_ligne
                max_c = num_colonne
        #print(antennes)
        for frequence,positions in antennes.items():
            print(frequence,positions)
            for combinaison in combinations(positions,2):
                #print("combinaison :",combinaison)
                vecteur = (combinaison[1][0]-combinaison[0][0],combinaison[1][1]-combinaison[0][1])
                #print("vecteur",vecteur)
                antinode1 = (combinaison[1][0],combinaison[1][1])
                while is_in(antinode1,max_l=max_l,max_c=max_c) :
                    antinodes.add(str(antinode1[0])+"-"+str(antinode1[1]))
                    antinode1 = (antinode1[0]+vecteur[0],antinode1[1]+vecteur[1])
                antinode2 = (combinaison[0][0],combinaison[0][1])
                while is_in(antinode2,max_l=max_l,max_c=max_c) :
                    antinodes.add(str(antinode2[0])+"-"+str(antinode2[1]))
                    antinode2 = (antinode2[0]-vecteur[0],antinode2[1]-vecteur[1])
    return len(antinodes)


def test_enigme_day08():
    assert enigme_day08_first_part("input-08-test.txt")==14
    assert enigme_day08_second_part("input-08-test.txt")==34

if __name__ == "__main__" :
    #print(enigme_day08_first_part("input-08.txt"))
    print(enigme_day08_second_part("input-08.txt"))