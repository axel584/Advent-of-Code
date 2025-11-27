from collections import defaultdict
import pytest
import re
from itertools import combinations, product, permutations

move1_dict = {
    'A0':'<',
    'A1':'<<^',
    'A2':'^<',
    'A3':'^',
    'A4':'^^<<',
    'A5':'^^<',
    'A6':'^^',
    'A7':'^^^<<',
    'A8':'<^^^',
    'A9':'^^^',
    '0A':'>',
    '01':'<^',
    '02':'^',
    '03':'^>',
    '04':'<^^',
    '05':'^^',
    '06':'^^>',
    '07':'<^^^',
    '08':'^^',
    '09':'^^>',
    '1A':'>>v',
    '10':'>v',
    '12':'>',
    '13':'>>',
    '14':'^',
    '15':'^>',
    '16':'^>>',
    '17':'^^',
    '18':'^^>',
    '19':'^^>>',
    '2A':'>v',
    '20':'v',
    '21':'<',
    '23':'>',
    '24':'^<',
    '25':'^',
    '26':'^>',
    '27':'^^<',
    '28':'^^',
    '29':'^^>',
    '3A':'v',
    '30':'v<',
    '31':'<<',
    '32':'<',
    '34':'^<<',
    '35':'^<',
    '36':'^',
    '37':'^^<<',
    '38':'^^<',
    '39':'^^',
    '40':'>>vv',
    '40':'>vv',
    '45':'>',
    '48':'>^',
    '5A':'>vv',
    '56':'>',
    '6A':'vv',
    '7A':'>>vvv',
    '76':'>>v',
    '78':'>',
    '79':'>>',
    '80':'vvv',
    '89':'>',
    '8A':'>vvv',
    '9A':'vvv',
    '90':'vvv<',
    '91':'vv<<',
    '92':'vv<',
    '93':'vv',
    '94':'v<<',
    '95':'v<',
    '96':'v',
    '97':'<<',
    '98':'<',

}

move2_dict = {
    'AA':'',
    'A^':'<',
    'A<':'v<<',
    'Av':'v<',
    'A>':'v',
    '^^':'',
    '^A':'>',
    '^<':'v<',
    '^v':'v',
    '^>':'>v',
    '<<':'',
    '<A':'>>^',
    '<^':'>^',
    '<v':'>',
    '<>':'>>',
    'vv':'',
    'vA':'>^',
    'v^':'^',
    'v<':'<',
    'v>':'>',
    '>>':'',
    '>A':'^',
    '>^':'^<',
    '><':'<<',
    '>v':'<'
}

def move1(src,dst):
    return move1_dict[src+dst]

def find(code,dict):
    res = ''
    element = 'A'
    for bouton in code :
        if element+bouton not in dict:
            print("MANQUE",element,bouton)
            continue
        res += dict[element+bouton]+'A'
        element = bouton
    return res

def find1(code):
    res = ''
    element = 'A'
    for bouton in code :
        if element+bouton not in move1_dict:
            print("MANQUE",element,bouton)
            continue
        res += move1_dict[element+bouton]+'A'
        element = bouton
    return res

def find2(code):
    res = ''
    element = 'A'
    for bouton in code :
        res += move2_dict[element+bouton]+'A'
        element = bouton
    return res

def findall(code):
    print("digicode : ",code)
    code1 = find1(code)
    #print("code 1",code1)
    code2 = find2(code1)
    #print("code 2",code2)
    res = find2(code2)
    print("combinaison ",res)
    print("longueur ",len(res))
    code_int = int(code.replace('A',''))
    print("produit : ",len(res)*code_int)
    return len(res)*code_int

def decode2(chaine):
    position = "A"
    res = ''
    for element in chaine.split('A')[:-1]:
        trouve = False
        for k,v in move2_dict.items():
            if k.startswith(position) :
                if sorted(list(v))==sorted(list(element)):
                    position=k[1]
                    trouve = True
                    res += position
                    break
        if not trouve :
            print("****************** n'a pas trouve pour decoder")
    return res

def decode1(chaine):
    position = "A"
    res = ''
    for element in chaine.split('A')[:-1]:
        trouve = False
        for k,v in move1_dict.items():
            if k.startswith(position) :
                if sorted(list(v))==sorted(list(element)):
                    position=k[1]
                    trouve = True
                    res += position
                    break
        if not trouve :
            print("****************** n'a pas trouve pour decoder")
    return res

def verify(dict):
    for k,v in dict.items():
        #print("verify : ",k,v)
        longueur_min = len(find(v,move2_dict))
        for perm in permutations(v,len(v)):
            essai = "".join(perm)
            if essai==v :
                continue
            if len(find(essai,move2_dict))<longueur_min:
                print("trouve mieux pour : ",k,v," => ",essai,len(find(essai,move2_dict)),longueur_min)
                longueur_min = len(find(essai,move2_dict))

def enigme_day21_first_part(chemin):
    somme = 0
    with open(chemin, "r") as fichier:
        i = 0
        for ligne in fichier:
            somme += findall(ligne.strip())
    return somme

def test_enigme_day21():
    #assert find1("029A") == "<A^A^^>AvvvA"
    #assert find2("<A^A>^^AvvvA")=="v<<A>>^A<A>AvA<^AA>A<vAAA>^A"
    #assert find2("v<<A>>^A<A>AvA<^AA>A<vAAA>^A")=="<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"
    #assert findall("029A") == 1972
    #assert findall("379A")==24256
    assert enigme_day21_first_part("input-21-test.txt") == 126384
    #assert enigme_day21_second_part("input-21-test2.txt") == 


if __name__ == "__main__":
    #{print(decode("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"))
    #print(decode(decode("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A")))
    #print(decode("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"),len(decode("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A")))
    #print(decode(decode("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A")),len(decode(decode("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"))))
    #print(decode2("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"))
    #print(decode2("<vA<AA>>^AvA^<A>AvA^A<vA<A>^>AAvA^A<A>A<vA<A>>^AA<Av>A^A<v<A>>^AAAvA^A"))
    #print(decode2("v<<A>^A>Av<AA>A^Av<AA^>A<AAA>A"))
    #print(decode1("<^Avv>AvvA^^^A"))
    #print(decode1("^A<<^^A>>AvvvA"))
    #print(findall("379A"))
    #print(enigme_day21_first_part("input-21-test.txt"))
    #print(enigme_day21_first_part("input-21.txt"))
    #print(enigme_day21_second_part("input-21.txt"))
    # print(find2("^<"))
    # print(len(find2("<<^^")))
    # print(len(find2("^^<<")))
    # print(find2("<^"))
    # print(len(find2("<^")))
    verify(move1_dict)
    # verify(move2_dict)