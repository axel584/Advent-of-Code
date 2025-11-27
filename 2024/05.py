from collections import defaultdict
import pytest
import re


ordres_src = defaultdict(list)
ordres_dst = defaultdict(list)

def enigme_day05_first_part(chemin):

    somme = 0
    premiere_partie = True
    with open(chemin,'r') as fichier :
        for ligne in fichier:
            if ligne.strip()=="" :
                premiere_partie = False
                print("SRC:",ordres_src)
                print("*"*50)
                print("DST:",ordres_dst)                
                continue
            if premiere_partie:
                src,dst=ligne.strip().split('|')
                ordres_src[src].append(dst)
                ordres_dst[dst].append(src)
            else :
                print("deuxieme partie",ligne.strip())
                pages = [page for page in ligne.strip().split(',')]
                correct = True
                for i in range(len(pages)):
                    page = pages[i]
                    avant = pages[:i]
                    apres = pages[i+1:]
                    print(page,avant,apres)
                    erreur_avant = [element for element in avant if element in ordres_src[page]]
                    erreur_apres = [element for element in apres if element in ordres_dst[page]]
                    if len(erreur_avant)>0 or len(erreur_apres)>0:
                        correct = False
                        break
                if correct:
                    print(ligne," est correct")
                    print("on ajoute ",pages[len(pages)//2])
                    somme += int(pages[len(pages)//2])
    return somme


def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        # Parcours de la liste jusqu'à la dernière position non triée
        for j in range(0, n - i - 1):
            # Si l'élément courant est plus grand que le suivant, on les échange
            if liste[j] in ordres_src[liste[j + 1]]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste
        


def enigme_day05_second_part(chemin):
    

    somme = 0
    premiere_partie = True
    with open(chemin,'r') as fichier :
        for ligne in fichier:
            if ligne.strip()=="" :
                premiere_partie = False
                print("SRC:",ordres_src)
                print("*"*50)
                print("DST:",ordres_dst)                
                continue
            if premiere_partie:
                src,dst=ligne.strip().split('|')
                ordres_src[src].append(dst)
                ordres_dst[dst].append(src)
            else :
                print("deuxieme partie",ligne.strip())
                pages = [page for page in ligne.strip().split(',')]
                correct = True
                for i in range(len(pages)):
                    page = pages[i]
                    avant = pages[:i]
                    apres = pages[i+1:]
                    #print(page,avant,apres)
                    erreur_avant = [element for element in avant if element in ordres_src[page]]
                    erreur_apres = [element for element in apres if element in ordres_dst[page]]
                    if len(erreur_avant)>0 or len(erreur_apres)>0:
                        correct = False
                        break
                if not correct:
                    #print("a ordonner : ",pages)
                    pages_trie = bubble_sort(pages)
                    #print(pages_trie)
                    somme += int(pages[len(pages_trie)//2])

    return somme


# def test_enigme_day05_first_part():
#     assert enigme_day05_first_part("input-05-test.txt")==143

def test_enigme_day05_second_part():
    assert enigme_day05_second_part("input-05-test.txt")==123

if __name__ == "__main__" :
    #print(enigme_day05_first_part("input-05.txt"))
    print(enigme_day05_second_part("input-05.txt"))