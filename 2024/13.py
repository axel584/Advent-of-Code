from collections import defaultdict
import pytest
import re
from itertools import combinations, product
import numpy as np

# def find(ax, ay, bx, by, px, py):
#     res = 0
#     print("ax", ax, "ay", ay, "bx", bx, "px", px, "py", py)
#     for jeton_a in range(100):
#         if jeton_a * ax > px or jeton_a * ay > py:
#             return res
#         reste = px - (ax * jeton_a)
#         if reste % bx == 0:
#             jeton_b = reste // bx
#             if jeton_a * ay + jeton_b * by == py:
#                 print("TROUVE ", jeton_a, jeton_b, jeton_a * 3 + jeton_b)
#                 if res != 0:
#                     print("*" * 50)
#                 res = jeton_a * 3 + jeton_b

#     return res

# def find(ax, ay, bx, by, px, py):
#     res = 0
#     print("ax", ax, "ay", ay, "bx", bx,"by", by, "px", px, "py", py)
#     ratio_a = ax/ay
#     coef_b = by * ratio_a
#     coef_res = py * ratio_a
#     diff_b = bx - coef_b
#     diff_res = px - coef_res
#     jeton_b = diff_res / diff_b
#     jeton_a = int((px - (bx * jeton_b))/ax)
#     jeton_b = int(jeton_b)
#     print("jeton a et b",jeton_a,jeton_b)
#     print(ax*jeton_a + bx * jeton_b)
#     print(ay*jeton_a + by * jeton_b)
#     if ax*jeton_a + bx * jeton_b == px and ay*jeton_a + by * jeton_b == py :
#         print("cout : ",int(jeton_a * 3 + jeton_b))
#         return int(jeton_a * 3 + jeton_b)
#     else : 
#         print("rien")
#         return 0

# def is_integer_close(value, tol=1e-6):
#     return abs(value - round(value)) < tol


def find(ax, ay, bx, by, px, py):
    res = 0
    print("ax", ax, "ay", ay, "bx", bx,"by", by, "px", px, "py", py)
    A = np.array([[ax,bx], [ay, by]])
    B = np.array([px,py])
    solution = np.linalg.solve(A, B)
    x, y = solution
    x = int(x)
    y = int(y)
    if ax*x + bx * y == px and ay*x + by * y == py :
        print("cout :",int(x)*3 + y)
        return int(x * 3 + y)
    else :
        print("rien")
        return 0
 

def enigme_day13_first_part(chemin):
    somme = 0
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            if ligne.startswith("Button A: "):
                bouton_a_data = ligne.strip().split(": ")[1].split(", ")
                # print("bouton_a_data", bouton_a_data)
            if ligne.startswith("Button B: "):
                bouton_b_data = ligne.strip().split(": ")[1].split(", ")
                # print("bouton_b_data", bouton_b_data)
            if ligne.startswith("Prize: "):
                prize_data = ligne.strip().split(": ")[1].split(", ")
                # print("prize_data", prize_data)
            if ligne.strip() == "":
                print("*"*50)
                # print(int(bouton_a_data[0][2:]))
                somme += find(
                    int(bouton_a_data[0][2:]),
                    int(bouton_a_data[1][2:]),
                    int(bouton_b_data[0][2:]),
                    int(bouton_b_data[1][2:]),
                    int(prize_data[0][2:]),
                    int(prize_data[1][2:]),
                )
    somme += find(
            int(bouton_a_data[0][2:]),
            int(bouton_a_data[1][2:]),
            int(bouton_b_data[0][2:]),
            int(bouton_b_data[1][2:]),
            int(prize_data[0][2:]),
            int(prize_data[1][2:]),
        )
    return somme

def enigme_day13_second_part(chemin):
    somme = 0
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            if ligne.startswith("Button A: "):
                bouton_a_data = ligne.strip().split(": ")[1].split(", ")
                # print("bouton_a_data", bouton_a_data)
            if ligne.startswith("Button B: "):
                bouton_b_data = ligne.strip().split(": ")[1].split(", ")
                # print("bouton_b_data", bouton_b_data)
            if ligne.startswith("Prize: "):
                prize_data = ligne.strip().split(": ")[1].split(", ")
                # print("prize_data", prize_data)
            if ligne.strip() == "":
                # print("ligne vide")
                print("*"*50)
                # print(int(bouton_a_data[0][2:]))
                somme += find(
                    int(bouton_a_data[0][2:]),
                    int(bouton_a_data[1][2:]),
                    int(bouton_b_data[0][2:]),
                    int(bouton_b_data[1][2:]),
                    int(prize_data[0][2:])+10000000000000,
                    int(prize_data[1][2:])+10000000000000,
                )
                print("somme", somme)
    somme += find(
                int(bouton_a_data[0][2:]),
                int(bouton_a_data[1][2:]),
                int(bouton_b_data[0][2:]),
                int(bouton_b_data[1][2:]),
                int(prize_data[0][2:])+10000000000000,
                int(prize_data[1][2:])+10000000000000,
            )
    print("somme", somme)
    return somme

def test_enigme_day13():
    #assert enigme_day13_first_part("input-13-test.txt") == 480
    assert enigme_day13_second_part("input-13-test.txt") == 480


if __name__ == "__main__":
    #print(enigme_day13_first_part("input-13.txt"))
    print(enigme_day13_second_part("input-13.txt"))
