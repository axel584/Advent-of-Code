from collections import defaultdict
import pytest


def enigme_day11_first_part(chemin, nb_blink):
    tab = []
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            # print(ligne)
            tab = [int(i) for i in ligne.strip().split(" ")]
    print(tab)
    for _ in range(nb_blink):
        i = 0
        while i < len(tab):
            stone = tab[i]
            # print("i", i, "/ stone", stone)
            if stone == 0:
                tab[i] = 1
                i += 1
                continue
            longueur = len(str(stone))
            # print("longueur", longueur, "/ stone", stone)
            if longueur % 2 == 0:
                tab.pop(i)
                left_stone = str(stone)[: longueur // 2]
                right_stone = str(stone)[longueur // 2 :]
                # print("left_stone", left_stone, "/ right_stone", right_stone)
                tab.insert(i, int(right_stone))
                tab.insert(i, int(left_stone))
                i += 2
                continue
            tab[i] = stone * 2024
            i += 1
        # print(tab)
    return len(tab)


def enigme_day11_second_part(chemin, nb_blink):
    tab = defaultdict(int)
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            for stone in ligne.strip().split(" "):
                tab[int(stone)] += 1
    for _ in range(nb_blink):
        # print("blink : ", blink)
        tab_next = defaultdict(int)
        for stone, occurence in tab.items():
            # print("Stone", stone)
            if stone == 0:
                tab_next[1] += occurence
                continue
            longueur = len(str(stone))
            if longueur % 2 == 0:
                left_stone = str(stone)[: longueur // 2]
                right_stone = str(stone)[longueur // 2 :]
                tab_next[int(right_stone)] += occurence
                tab_next[int(left_stone)] += occurence
                continue
            tab_next[stone * 2024] += occurence
        tab = tab_next
    somme = 0
    for stone, occurence in tab.items():
        somme += occurence
    return somme


def test_enigme_day11():
    # assert enigme_day11_first_part("input-11-test2.txt", 6) == 22
    assert enigme_day11_second_part("input-11-test2.txt", 6) == 22
    # assert enigme_day11_second_part("input-11-test2.txt", 25) == 55312
    # assert enigme_day11_second_part("input-11-test.txt") == 81


if __name__ == "__main__":
    # print(enigme_day11_first_part("input-11-test.txt", 6))
    print(enigme_day11_second_part("input-11.txt", 25))
    print(enigme_day11_second_part("input-11.txt", 75))
