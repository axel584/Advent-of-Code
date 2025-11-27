from collections import defaultdict
import functools
import pytest
import re
from itertools import combinations, product

serviettes = []

def next(nombre):
    # 1er etape
    res = 64 * nombre
    nombre = res ^ nombre
    nombre = nombre % 16777216
    # 2eme etape
    res = int(nombre / 32)
    nombre = res ^ nombre
    nombre = nombre % 16777216
    # 3eme etape
    res = nombre  * 2048
    nombre = res ^ nombre # ou le changer avant
    return nombre % 16777216


def calcule(nombre,occurence):
    for _ in range(occurence):
        nombre = next(nombre)
    return nombre

def calcule2(nombre,occurence):
    res = [nombre%10]
    for _ in range(occurence):
        nombre = next(nombre)
        res.append(nombre%10)
    return res

def find_max(secrets,differences):
    maximum = 0
    combinaisons = defaultdict(int)
    for acheteur,d in enumerate(differences):
        combinaisons_acheteur = defaultdict(list)
        for i in range(1996):
            combinaisons_acheteur[tuple(d[i:i+4])].append(secrets[acheteur][i+4])
        for k,v in combinaisons_acheteur.items():
            #print(acheteur,k,v)
            combinaisons[k] += v[0] 
    return max(combinaisons.values())        

def enigme_day22_first_part(chemin):
    somme = 0
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            somme +=calcule(int(ligne.strip()),2000)
    return somme

def enigme_day22_second_part(chemin):
    secrets = []
    difference = []
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            secrets_pour_acheteur = calcule2(int(ligne.strip()),2000)
            secrets.append(secrets_pour_acheteur)
            difference.append([b - a for a, b in zip(secrets_pour_acheteur[:-1], secrets_pour_acheteur[1:])])
    #print(len(difference))
    return find_max(secrets,difference)


def test_enigme_day22():
    #assert next(123)==15887950
    #assert next(15887950)==16495136
    #assert enigme_day22_first_part("input-22-test.txt") == 37327623
    #print(calcule2(123,10))
    assert enigme_day22_second_part("input-22-test2.txt") == 23

if __name__ == "__main__":
    #print(enigme_day22_first_part("input-22-test.txt"))
    #print(enigme_day22_first_part("input-22.txt"))
    #print(enigme_day22_second_part("input-22-test2.txt"))
    print(enigme_day22_second_part("input-22.txt"))
