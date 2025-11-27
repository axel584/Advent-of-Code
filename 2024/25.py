from collections import defaultdict
import functools
import pytest
import re
from itertools import combinations, product

 

def enigme_day25_first_part(chemin):
    clefs = []
    serrures = []
    nouveau_schema=True
    type_schema = None
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            if nouveau_schema : 
                if ligne.strip()=="#####":
                    type_schema = "serrure"
                else :
                    type_schema = "clef"
                nouveau_schema = False
                schema = [-1,-1,-1,-1,-1]
            if ligne.strip()=="" :
                nouveau_schema = True
                if type_schema=="serrure":
                    serrures.append(schema)
                else :
                    clefs.append(schema)
            else :
                for indice,case in enumerate(ligne.strip()):
                    if case == "#":
                        schema[indice]+=1
        if type_schema=="serrure":
            serrures.append(schema)
        else :
            clefs.append(schema)
    somme = 0
    print("clefs",clefs)
    print("serrures",serrures)
    for clef in clefs:
        for serrure in serrures:
            serrure_ok = True
            for i in range(5):
                if clef[i]+serrure[i]>5 :
                    serrure_ok = False
            if serrure_ok:
                somme += 1
    return somme

def test_enigme_day25():
    assert enigme_day25_first_part("input-25-test.txt") == 3
    #assert enigme_day25_second_part("input-25-test.txt") == 7
    #print(calcule2(125,10))
    #assert enigme_day25_second_part("input-25-test2.txt") == 25

if __name__ == "__main__":
    print(enigme_day25_first_part("input-25.txt"))
    #print(enigme_day25_second_part("input-25-test2.txt"))
    #print(enigme_day25_second_part("input-25.txt"))
