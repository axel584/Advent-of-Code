import pytest

boxes = [{} for _ in range(256)]

def hash_chaine(chaine):
    resultat = 0
    for c in chaine:
        resultat += ord(c) 
        resultat *= 17
        resultat %= 256
    return resultat



def enigme_day15(chemin):
    somme = 0
    with open(chemin,'r') as fichier :
        for ligne in fichier :
            for element in ligne.strip().split(','):
                somme += hash_chaine(element)
    return somme

def get_nom_box(element):
    res = ''
    for lettre in element:
        if lettre.isalpha() :
            res += lettre
    return res

def enigme_day15b(chemin):
    with open(chemin,'r') as fichier :
        for ligne in fichier :
            for element in ligne.strip().split(','):
                #print("element : ",element)
                nom_box = get_nom_box(element)
                num_box = hash_chaine(nom_box)
                #print("box ",num_box,nom_box)
                if element.find("-")>-1:
                    if nom_box in boxes[num_box]:
                        del boxes[num_box][nom_box]
                if element.find("=")>-1:
                    valeur_focal = int(element[element.find("=")+1:])
                    #print("valeur focal:",valeur_focal)
                    boxes[num_box][nom_box]=valeur_focal
                #print(boxes)
    somme = 0            
    for num_box,box in enumerate(boxes):   
        if box==None :
            continue
        for indice,(nom_box,valeur_focale) in enumerate(box.items()):
            pouvoir_focalisant = (num_box+1)*(indice+1)*valeur_focale
            #print(indice,nom_box,valeur_focale,somme,pouvoir_focalisant)
            somme += pouvoir_focalisant
    print(boxes)
    return somme



def test_hash_chaine():
    assert hash_chaine("HASH")==52

def test_enigme_day15():
    assert enigme_day15("input-15-test.txt") == 1320
    assert enigme_day15b("input-15-test.txt") == 145


if __name__ == "__main__" :
    print(enigme_day15b("input-15.txt"))