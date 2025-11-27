from collections import defaultdict
import functools
import pytest
import re
from itertools import combinations, product

 

def enigme_day23_first_part(chemin):
    reseaux = defaultdict(list)
    somme = 0
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            ordi1,ordi2 = ligne.strip().split('-')
            #print(ordi1,ordi2)
            reseaux[ordi1].append(ordi2)
            reseaux[ordi2].append(ordi1)
    #print(reseaux)
    for ordi1,reseau1 in reseaux.items():
        for ordi2 in reseau1:
            for ordi3 in reseaux[ordi2]:
                if ordi3 in reseau1 :
                    if ordi1 < ordi2 and ordi2 < ordi3 :
                        if ordi1[0]=='t' or ordi2[0]=='t' or ordi3[0]=='t' :
                            somme += 1
                            #print(ordi1,ordi2,ordi3)
    return somme

def enigme_day23_second_part(chemin):
    reseaux = defaultdict(list)
    somme = 0
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            ordi1,ordi2 = ligne.strip().split('-')
            reseaux[ordi1].append(ordi2)
            reseaux[ordi2].append(ordi1)
    print("reseaux ",reseaux)
    for ordi,voisins in reseaux.items():
        lan_ok = True
        for ordi_voisin in voisins : 
            if len(reseaux[ordi_voisin])!=len(voisins) or set(reseaux[ordi_voisin])!=set(voisins):
                lan_ok = False
                break
        if lan_ok :
            print(ordi,voisins)
                
    return somme


def test_enigme_day23():
    #assert enigme_day23_first_part("input-23-test.txt") == 7
    assert enigme_day23_second_part("input-23-test.txt") == 7
    #print(calcule2(123,10))
    #assert enigme_day23_second_part("input-23-test2.txt") == 23

if __name__ == "__main__":
    print(enigme_day23_first_part("input-23.txt"))
    #print(enigme_day23_second_part("input-23-test2.txt"))
    #print(enigme_day23_second_part("input-23.txt"))
