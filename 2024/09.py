from collections import defaultdict
import pytest
import re
from itertools import combinations, product


def enigme_day09_first_part(chemin):
    somme = 0
    disque = []
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            for num, element in enumerate(ligne.strip()):
                identifiant = num // 2
                is_file = num % 2 == 0
                if is_file:
                    disque.extend([identifiant for i in range(int(element))])
                else:
                    disque.extend(["." for _ in range(int(element))])
        gauche = 0
        droite = len(disque) - 1
        # print("gauche / droite", gauche, droite)
        print(disque)
        while gauche < droite:
            # print("element", disque[gauche], disque[droite], gauche, droite)
            if disque[gauche] == ".":
                disque[gauche] = disque[droite]
                disque[droite] = "."
                droite -= 1
                while disque[droite] == ".":
                    droite -= 1
            gauche += 1
        for num, element in enumerate(disque):
            # print(num, element, somme)
            if element == ".":
                break
            somme += int(element) * num
    return somme


def next_element_droite(droite, disque):
    while disque[droite][1] == ".":
        droite -= 1
    return droite


def find_place_libre(max, disque, taille):
    for i in range(len(disque)):
        if disque[i][1] == "." and disque[i][0] >= taille:
            return i
        if i > max:
            return None
    return None


def enigme_day09_second_part(chemin):
    disque = []
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            for num, element in enumerate(ligne.strip()):
                identifiant = num // 2
                is_file = num % 2 == 0
                if is_file:
                    disque.append((int(element), identifiant))
                else:
                    if element != "0":
                        disque.append((int(element), "."))
    droite = len(disque) - 1
    print("debut : ", disque[:50])
    print("fin : ", disque[-50:])
    # print("*" * 50)
    # print("".join([str(i[1]) * i[0] for i in disque]))
    while droite > 0:
        # print("element", disque[droite], droite)
        num_fichier_a_ranger = next_element_droite(droite, disque)
        droite = num_fichier_a_ranger
        taille_fichier_a_ranger = disque[num_fichier_a_ranger][0]
        nom_fichier_a_ranger = disque[num_fichier_a_ranger][1]
        # print("fichier a ranger : ", nom_fichier_a_ranger, taille_fichier_a_ranger)
        indice_libre = find_place_libre(
            max=droite, disque=disque, taille=taille_fichier_a_ranger
        )
        # print("indice libre", indice_libre)
        if indice_libre is not None:
            disque[num_fichier_a_ranger] = (taille_fichier_a_ranger, ".")
            taille_libre = disque[indice_libre][0]
            disque[indice_libre] = (taille_fichier_a_ranger, nom_fichier_a_ranger)
            if taille_fichier_a_ranger != taille_libre:
                disque.insert(
                    indice_libre + 1, (taille_libre - taille_fichier_a_ranger, ".")
                )
            else:
                droite -= 1
        else:
            droite -= 1
        # print("debut : ", disque[:50])
        # print("fin : ", disque[-50:])
    # supprime les trucs vides
    i = 0
    while i < len(disque):
        if disque[i][0] == 0:
            del disque[i]
        else:
            i += 1
    somme = 0

    i = 0
    # print(disque)

    # print("".join([str(i[1]) * i[0] for i in disque]))
    i = 0
    for element in disque:
        if element[1] == ".":
            i += element[0]
            continue
        for j in range(element[0]):
            somme += int(element[1]) * (i + j)
        i += element[0]
    return somme


def test_enigme_day09():
    # assert enigme_day09_first_part("input-09-test.txt") == 1928
    assert enigme_day09_second_part("input-09-test.txt") == 2858


if __name__ == "__main__":
    # print(enigme_day09_first_part("input-09.txt"))
    print(enigme_day09_second_part("input-09-pro.txt"))
