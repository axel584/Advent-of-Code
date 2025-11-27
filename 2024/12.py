from collections import defaultdict
import pytest
import re
from itertools import combinations, product


def enigme_day12_first_part(chemin):
    tab = []
    regions = {}
    a_ranger = []
    with open(chemin, "r") as fichier:
        for num_ligne, ligne in enumerate(fichier):
            tab.append([])
            for num_colonne, colonne in enumerate(ligne.strip()):
                tab[num_ligne].append(colonne)
                regions[(num_ligne, num_colonne)] = [(num_ligne, num_colonne)]
                a_ranger.append((num_ligne, num_colonne))
    MAX_LIGNE = len(tab)
    MAX_COLONNE = len(tab[0])
    index = 0
    while len(a_ranger) > 0:
        source_region = a_ranger.pop(0)
        todo = [source_region]
        while len(todo) > 0:
            point = todo.pop()
            region_du_point = tab[point[0]][point[1]]
            nord = (point[0] - 1, point[1])
            if (
                nord[0] >= 0
                and nord[0] < MAX_LIGNE
                and nord[1] >= 0
                and nord[1] < MAX_COLONNE
            ):
                if tab[nord[0]][nord[1]] == region_du_point and nord in a_ranger:
                    regions[source_region].extend(regions[nord])
                    todo.append(nord)
                    a_ranger.remove(nord)
                    del regions[nord]
            sud = (point[0] + 1, point[1])
            if (
                sud[0] >= 0
                and sud[0] < MAX_LIGNE
                and sud[1] >= 0
                and sud[1] < MAX_COLONNE
            ):
                if tab[sud[0]][sud[1]] == region_du_point and sud in a_ranger:
                    regions[source_region].extend(regions[sud])
                    todo.append(sud)
                    a_ranger.remove(sud)
                    del regions[sud]
            est = (point[0], point[1] + 1)
            if (
                est[0] >= 0
                and est[0] < MAX_LIGNE
                and est[1] >= 0
                and est[1] < MAX_COLONNE
            ):
                if tab[est[0]][est[1]] == region_du_point and est in a_ranger:
                    regions[source_region].extend(regions[est])
                    todo.append(est)
                    a_ranger.remove(est)
                    del regions[est]
            ouest = (point[0], point[1] - 1)
            if (
                ouest[0] >= 0
                and ouest[0] < MAX_LIGNE
                and ouest[1] >= 0
                and ouest[1] < MAX_COLONNE
            ):
                if tab[ouest[0]][ouest[1]] == region_du_point and ouest in a_ranger:
                    regions[source_region].extend(regions[ouest])
                    todo.append(ouest)
                    a_ranger.remove(ouest)
                    del regions[ouest]
    index += 1
    somme = 0
    for region in regions.keys():
        surface = len(regions[region])
        # print("Region ", tab[region[0]][region[1]], "surface", surface)
        perimetre = 0
        for point in regions[region]:
            perimetre += 4
            if (point[0] - 1, point[1]) in regions[region]:
                perimetre -= 1
            if (point[0] + 1, point[1]) in regions[region]:
                perimetre -= 1
            if (point[0], point[1] - 1) in regions[region]:
                perimetre -= 1
            if (point[0], point[1] + 1) in regions[region]:
                perimetre -= 1
        # print("perimetre", perimetre)
        somme += surface * perimetre
    return somme


def enigme_day12_second_part(chemin):
    tab = []
    regions = {}
    a_ranger = []
    with open(chemin, "r") as fichier:
        for num_ligne, ligne in enumerate(fichier):
            tab.append([])
            for num_colonne, colonne in enumerate(ligne.strip()):
                tab[num_ligne].append(colonne)
                regions[(num_ligne, num_colonne)] = [(num_ligne, num_colonne)]
                a_ranger.append((num_ligne, num_colonne))
    MAX_LIGNE = len(tab)
    MAX_COLONNE = len(tab[0])
    index = 0
    while len(a_ranger) > 0:
        source_region = a_ranger.pop(0)
        todo = [source_region]
        while len(todo) > 0:
            point = todo.pop()
            region_du_point = tab[point[0]][point[1]]
            nord = (point[0] - 1, point[1])
            if (
                nord[0] >= 0
                and nord[0] < MAX_LIGNE
                and nord[1] >= 0
                and nord[1] < MAX_COLONNE
            ):
                if tab[nord[0]][nord[1]] == region_du_point and nord in a_ranger:
                    regions[source_region].extend(regions[nord])
                    todo.append(nord)
                    a_ranger.remove(nord)
                    del regions[nord]
            sud = (point[0] + 1, point[1])
            if (
                sud[0] >= 0
                and sud[0] < MAX_LIGNE
                and sud[1] >= 0
                and sud[1] < MAX_COLONNE
            ):
                if tab[sud[0]][sud[1]] == region_du_point and sud in a_ranger:
                    regions[source_region].extend(regions[sud])
                    todo.append(sud)
                    a_ranger.remove(sud)
                    del regions[sud]
            est = (point[0], point[1] + 1)
            if (
                est[0] >= 0
                and est[0] < MAX_LIGNE
                and est[1] >= 0
                and est[1] < MAX_COLONNE
            ):
                if tab[est[0]][est[1]] == region_du_point and est in a_ranger:
                    regions[source_region].extend(regions[est])
                    todo.append(est)
                    a_ranger.remove(est)
                    del regions[est]
            ouest = (point[0], point[1] - 1)
            if (
                ouest[0] >= 0
                and ouest[0] < MAX_LIGNE
                and ouest[1] >= 0
                and ouest[1] < MAX_COLONNE
            ):
                if tab[ouest[0]][ouest[1]] == region_du_point and ouest in a_ranger:
                    regions[source_region].extend(regions[ouest])
                    todo.append(ouest)
                    a_ranger.remove(ouest)
                    del regions[ouest]
    index += 1
    somme = 0
    for region in regions.keys():
        surface = len(regions[region])
        # print("Region ", tab[region[0]][region[1]], "surface", surface)
        angles = 0
        for point in regions[region]:
            # bas à gauche
            if (point[0] + 1, point[1]) not in regions[region] and (
                point[0],
                point[1] - 1,
            ) not in regions[region]:
                angles += 1
            if (
                (point[0] + 1, point[1]) in regions[region]
                and (point[0], point[1] - 1) in regions[region]
                and (point[0] + 1, point[1] - 1) not in regions[region]
            ):
                angles += 1
            # bas à droite
            if (point[0] + 1, point[1]) not in regions[region] and (
                point[0],
                point[1] + 1,
            ) not in regions[region]:
                angles += 1
            if (
                (point[0] + 1, point[1]) in regions[region]
                and (point[0], point[1] + 1) in regions[region]
                and (point[0] + 1, point[1] + 1) not in regions[region]
            ):
                angles += 1
            # haut à gauche
            if (point[0] - 1, point[1]) not in regions[region] and (
                point[0],
                point[1] - 1,
            ) not in regions[region]:
                angles += 1
            if (
                (point[0] - 1, point[1]) in regions[region]
                and (point[0], point[1] - 1) in regions[region]
                and (point[0] - 1, point[1] - 1) not in regions[region]
            ):
                angles += 1
            # haut à droite
            if (point[0] - 1, point[1]) not in regions[region] and (
                point[0],
                point[1] + 1,
            ) not in regions[region]:
                angles += 1
            if (
                (point[0] - 1, point[1]) in regions[region]
                and (point[0], point[1] + 1) in regions[region]
                and (point[0] - 1, point[1] + 1) not in regions[region]
            ):
                angles += 1
        # print("perimetre", perimetre)
        # print(
        #     "Region ",
        #     tab[region[0]][region[1]],
        #     "surface",
        #     surface,
        #     " angles ",
        #     angles,
        # )
        somme += surface * angles
    return somme


def test_enigme_day12():
    # assert enigme_day12_first_part("input-12-test.txt") == 1930
    assert enigme_day12_second_part("input-12-test.txt") == 1206


if __name__ == "__main__":
    # print(enigme_day12_first_part("input-12.txt"))
    print(enigme_day12_second_part("input-12.txt"))
