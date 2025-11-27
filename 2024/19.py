from collections import defaultdict
import functools
import pytest
import re
from itertools import combinations, product

serviettes = []

def find(pattern, serviettes):
    #print("find ",pattern,serviettes)
    if len(pattern)==0 :
        return True
    res = []
    for serviette in serviettes : 
        if pattern.startswith(serviette):
            nouveau_pattern = pattern[len(serviette):]
            res.append(find(nouveau_pattern,serviettes))
    return any(res)

@functools.cache
def find2(pattern):
    if len(pattern)==0 :
        return 1
    res = 0
    for serviette in serviettes : 
        if pattern.startswith(serviette):
            res += find2(pattern[len(serviette):])
    return res

def enigme_day19_first_part(chemin):
    serviettes = []
    somme = 0
    with open(chemin, "r") as fichier:
        premierePartie = True
        for ligne in fichier:
            if premierePartie :
                serviettes = list(ligne.strip().split(', '))
                #print(serviettes)
                premierePartie = False
            elif ligne.strip()=="" :
                serviettes.sort(key=lambda x:len(x),reverse=True)
                print(serviettes)
                i = 0
                while i<len(serviettes) :
                    #print("*"*50)
                    #print("i : ",i)
                    if i==0:
                        autres_serviettes = serviettes[i+1:]
                    elif i==len(serviettes):
                        autres_serviettes = serviettes[:i-1]
                    else :
                        autres_serviettes = serviettes[:i-1]+serviettes[i+1:]
                    #print("autre ",autres_serviettes)
                    if find(serviettes[i],autres_serviettes) :
                        print("on retire : ",serviettes[i])
                        serviettes.pop(i)
                    else :
                        i += 1
                print("serviette apres filtre ",serviettes)    
            else : 
                if find(ligne.strip(),serviettes) :
                    somme += 1
    return somme

def enigme_day19_second_part(chemin):
    global serviettes
    somme = 0
    with open(chemin, "r") as fichier:
        premierePartie = True
        nb_ligne = 0
        for ligne in fichier:
            if premierePartie :
                serviettes = list(ligne.strip().split(', '))
                premierePartie = False
            elif ligne.strip()!="" :
                nb_configuration = find2(ligne.strip())
                somme += nb_configuration
                print(nb_ligne,somme,nb_configuration, ligne.strip())
                nb_ligne += 1
    return somme

def test_enigme_day19():
    #assert enigme_day19_first_part("input-19-test.txt") == 6
    assert enigme_day19_second_part("input-19-test.txt") == 16
    #assert find2("gbbr",["r","wr","b","g","bwu","rb","gb","br"])==4


if __name__ == "__main__":
    #print(enigme_day19_first_part("input-19-test.txt"))
    #print(enigme_day19_first_part("input-19.txt"))
    print(enigme_day19_second_part("input-19.txt"))
