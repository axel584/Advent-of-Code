import pytest
import re

MUL_PATTERN = r"mul\(([0-9]+),([0-9]+)\)"
MUL_AND_DO_PATTERN = r"mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\)"

def enigme_day03_first_part(chemin):
    somme = 0
    with open(chemin,'r') as fichier :
        contenu = fichier.read()
        occurences = re.findall(MUL_PATTERN,contenu)
        for x,y in occurences :
            somme += int(x)*int(y)
    return somme

def enigme_day03_second_part(chemin):
    somme = 0
    with open(chemin,'r') as fichier :
        contenu = fichier.read()
        occurences = re.finditer(MUL_AND_DO_PATTERN,contenu)
        enable = True
        for occurence in occurences:
            print(occurence)
            print(occurence.group(0))
            if occurence.group(0)=="don't()":
                print("disable")
                enable = False
            elif occurence.group(0)=="do()":
                print("enable")
                enable = True
            else :
                if enable :
                    somme += int(occurence.group(1))*int(occurence.group(2))
    return somme

def test_enigme_day03_first_part():
    assert enigme_day03_first_part("input-03-test.txt")==161

def test_enigme_day03_second_part():
    assert enigme_day03_second_part("input-03-test.txt")==48

if __name__ == "__main__" :
    #print(enigme_day03_first_part("input-03.txt"))
    print(enigme_day03_second_part("input-03.txt"))