from collections import defaultdict
import pytest
import re
from itertools import product

def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def concat(a,b):
    return int(str(a)+str(b))

def verif(resultat,nombres):
    #print("verif",resultat,nombres,len(nombres))
    combinaisons = product([add,mul],repeat=len(nombres)-1)
    for combinaison in combinaisons:
        i = 0
        res = nombres[0]
        for nombre in nombres[1:]:
            operateur = combinaison[i]
            res = operateur(res,nombre)
            i += 1
            
        if res == resultat :
            return True
    return False

def verif2(resultat,nombres):
    #print("verif",resultat,nombres,len(nombres))
    combinaisons = product([add,mul,concat],repeat=len(nombres)-1)
    for combinaison in combinaisons:
        i = 0
        res = nombres[0]
        for nombre in nombres[1:]:
            operateur = combinaison[i]
            res = operateur(res,nombre)
            i += 1
            
        if res == resultat :
            return True
    return False

def enigme_day07_first_part(chemin):
    somme = 0
    with open(chemin,'r') as fichier :
        for ligne in fichier:
            resultat,nombres = ligne.strip().split(':')
            if verif(int(resultat),[int(x) for x in nombres.strip().split(' ')]):
                somme += int(resultat)

    return somme

def enigme_day07_second_part(chemin):
    somme = 0
    with open(chemin,'r') as fichier :
        for ligne in fichier:
            resultat,nombres = ligne.strip().split(':')
            if verif2(int(resultat),[int(x) for x in nombres.strip().split(' ')]):
                somme += int(resultat)

    return somme    


def test_enigme_day07():
    #assert enigme_day07_first_part("input-07-test.txt")==3749
    assert enigme_day07_second_part("input-07-test.txt")==11387

if __name__ == "__main__" :
    #print(enigme_day07_first_part("input-07-test.txt"))
    #print(enigme_day07_first_part("input-07.txt"))
    print(enigme_day07_second_part("input-07.txt"))