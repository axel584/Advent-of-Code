from collections import defaultdict
import pytest
import re
from itertools import combinations, product


def imprime(tab):
    for ligne in tab:
        print("".join([str(i) for i in ligne]))


# MAX = 7
MAX = 41


def search_next(point, tab):
    valeur = tab[point[0]][point[1]]
    # print("valeur", valeur)
    res = []

    if point[0] != 0 and int(tab[point[0] - 1][point[1]]) == int(valeur) + 1:
        res.append((point[0] - 1, point[1]))

    if point[1] != 0 and int(tab[point[0]][point[1] - 1]) == int(valeur) + 1:
        res.append((point[0], point[1] - 1))

    if point[0] != MAX and int(tab[point[0] + 1][point[1]]) == int(valeur) + 1:
        res.append((point[0] + 1, point[1]))

    if point[1] != MAX and int(tab[point[0]][point[1] + 1]) == int(valeur) + 1:
        res.append((point[0], point[1] + 1))

    return res


def enigme_day10_first_part(chemin):
    somme = 0
    tab = []
    trailheads = {}
    with open(chemin, "r") as fichier:
        for num_ligne, ligne in enumerate(fichier):
            tab.append([int(i) for i in ligne.strip()])
            for num_colonne, colonne in enumerate(ligne.strip()):
                if colonne == "0":
                    trailheads[(num_ligne, num_colonne)] = []
        print(tab)
        imprime(tab)
        # print(trailheads)
        for trailhead in trailheads.keys():
            todo = [trailhead]
            while len(todo) > 0:
                # print("todo", todo)
                point = todo.pop()
                nexts = search_next(point, tab)
                # print("nexts", nexts)
                for next in nexts:
                    # print("next", next)
                    if tab[next[0]][next[1]] == 9:
                        # print("=====> trouve 9", point)
                        trailheads[trailhead].append(next)
                    else:
                        # print("continuer", next)
                        todo.append(next)
    # print(trailheads)
    for trail in trailheads.values():
        somme += len(set(trail))
    return somme


def enigme_day10_second_part(chemin):
    somme = 0
    tab = []
    trailheads = {}
    with open(chemin, "r") as fichier:
        for num_ligne, ligne in enumerate(fichier):
            tab.append([int(i) for i in ligne.strip()])
            for num_colonne, colonne in enumerate(ligne.strip()):
                if colonne == "0":
                    trailheads[(num_ligne, num_colonne)] = []
        print(tab)
        imprime(tab)
        # print(trailheads)
        for trailhead in trailheads.keys():
            todo = [trailhead]
            while len(todo) > 0:
                # print("todo", todo)
                point = todo.pop()
                nexts = search_next(point, tab)
                # print("nexts", nexts)
                for next in nexts:
                    # print("next", next)
                    if tab[next[0]][next[1]] == 9:
                        # print("=====> trouve 9", point)
                        trailheads[trailhead].append(next)
                    else:
                        # print("continuer", next)
                        todo.append(next)
    # print(trailheads)
    for trail in trailheads.values():
        somme += len(trail)
    return somme


def test_enigme_day10():
    assert enigme_day10_first_part("input-10-test.txt") == 36
    assert enigme_day10_second_part("input-10-test.txt") == 81


if __name__ == "__main__":
    # print(enigme_day10_first_part("input-10.txt"))
    print(enigme_day10_second_part("input-10.txt"))
