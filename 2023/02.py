import re
import pytest

NB_RED = 12
NB_GREEN = 13
NB_BLUE = 14

def is_game_possible(str):
    data = str[str.find(':')+2:]
    tirages = data.split(';')
    for tirage in tirages :
        couleurs = tirage.split(',')
        for couleur in couleurs :
            couleur=couleur.strip()
            nombre_de_cube = int(couleur[:couleur.find(' ')])
            if couleur.endswith('red'):
                if nombre_de_cube>NB_RED :
                    return False
            if couleur.endswith('blue'):
                if nombre_de_cube>NB_BLUE :
                    return False
            if couleur.endswith('green'):
                if nombre_de_cube>NB_GREEN :
                    return False                                
    return True

def puissance(str):
    max_blue = 0
    max_red = 0
    max_green = 0
    data = str[str.find(':')+2:]
    tirages = data.split(';')
    for tirage in tirages :
        couleurs = tirage.split(',')
        for couleur in couleurs :
            couleur=couleur.strip()
            nombre_de_cube = int(couleur[:couleur.find(' ')])
            if couleur.endswith('red'):
                if nombre_de_cube>max_red :
                    max_red = nombre_de_cube
            if couleur.endswith('blue'):
                if nombre_de_cube>max_blue :
                    max_blue = nombre_de_cube
            if couleur.endswith('green'):
                if nombre_de_cube>max_green :
                    max_green = nombre_de_cube                     
    return max_blue*max_green*max_red


def enigme_day2(chemin):
    fichier = open(chemin,'r')
    somme = 0
    for ligne in fichier.readlines():
        ligne = ligne.strip()
        num_game = int(ligne[ligne.find(' ')+1:ligne.find(':')])
        if is_game_possible(ligne):
            somme += num_game
    return somme

def enigme_day2_second_part(chemin):
    fichier = open(chemin,'r')
    somme = 0
    for ligne in fichier.readlines():
        ligne = ligne.strip()
        somme += puissance(ligne)
    return somme

def test_is_game_possible():
    assert is_game_possible("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert not is_game_possible("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    assert not is_game_possible("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")

def test_enigme_day2():
    assert enigme_day2("input-02a-test.txt") == 8

def test_puissance():
    assert puissance("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 48

def test_enigme_day2_second_part():
    assert enigme_day2_second_part("input-02a-test.txt") == 2286


if __name__ == "__main__" :
    print(enigme_day2_second_part("input-02.txt"))