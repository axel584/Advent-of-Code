from itertools import product
import pytest

def applique(pattern,combinaison):
    i = 0
    res = ''
    for c in pattern:
        if c=='?':
            res += combinaison[i]
            i += 1
        else :
            res += c
    return res

def verif(pattern,nombres):
    ressorts = [ressort for ressort in pattern.split('.') if len(ressort)>0]
    
    if len(ressorts)!=len(nombres):
        return False
    nombre_ressorts = [len(i) for i in ressorts]
    #print(pattern,nombres)
    #print("comparaison",nombre_ressorts,nombres)
    return nombre_ressorts==nombres


def nb_combinaison(ligne):
    pattern,nombres = ligne.split(' ')
    #print(pattern,nombres)
    nb_interrogation = pattern.count('?')
    somme = 0
    for combinaison in product('.#',repeat=nb_interrogation):
        #print(combinaison)
        pattern_combinaison = applique(pattern,combinaison)
        #print(pattern_combinaison)
        if verif(pattern_combinaison,[int(i) for i in nombres.split(',')]):
            somme += 1
    #print("somme",somme)
    return somme

    

def enigme_day12(chemin):
    somme = 0
    with open(chemin,'r') as fichier :
        for ligne in fichier :
            somme += nb_combinaison(ligne.strip())
    return somme


def test_nb_combinaison():
    assert nb_combinaison("???.### 1,1,3")==1
    assert nb_combinaison(".??..??...?##. 1,1,3")==4
    assert nb_combinaison("?###???????? 3,2,1")==10


def test_enigme_day12():
    assert enigme_day12("input-12a-test.txt") == 21


if __name__ == "__main__" :
    print(enigme_day12("input-12.txt"))