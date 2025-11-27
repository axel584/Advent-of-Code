import pytest

liste1 = []
liste2= []

def enigme_day01_first_part(chemin):
    with open(chemin,'r') as fichier :
        for ligne in fichier:
            element1,element2=ligne.split()
            liste1.append(int(element1))
            liste2.append(int(element2))
    liste1.sort()
    liste2.sort()
    #print(liste1)
    #print(liste2)    
    somme = 0
    for rang,element in enumerate(liste1):
        #print(element,liste2[rang])
        somme += abs((element-liste2[rang]))
    return somme

def enigme_day01_second_part(chemin):
    with open(chemin,'r') as fichier :
        for ligne in fichier:
            element1,element2=ligne.split()
            liste1.append(int(element1))
            liste2.append(int(element2))
    print(liste1)
    print(liste2)    
    somme = 0
    for element in liste1:
        print(element)
        print(liste2.count(element))
        somme += (element*liste2.count(element))
    return somme

def test_enigme_day01_first_part():
    assert enigme_day01_first_part("input-01-test.txt")==11

def test_enigme_day01_second_part():
    assert enigme_day01_first_part("input-01-test.txt")==31

if __name__ == "__main__" :
    #print(enigme_day01_first_part("input-01.txt"))
    print(enigme_day01_second_part("input-01.txt"))