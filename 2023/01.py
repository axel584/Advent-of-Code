import re
import pytest

word2digit = {  "zero": "0","one": "1","two": "2","three": "3","four": "4","five": "5","six": "6","seven": "7","eight": "8","nine": "9","0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}


def traite_ligne(str,with_word=False):
    if with_word : 
        first_word_position = len(str)
        last_word_position=0
        first_word = None
        last_word = None
        for key, _ in word2digit.items():
            if str.find(key)!=-1 and str.find(key)<first_word_position:
                first_word_position = str.find(key)
                first_word = key
            if str.rfind(key)!=-1 and str.rfind(key)>last_word_position:
                last_word_position = str.rfind(key)
                last_word = key
        if first_word :
            str = str.replace(first_word, word2digit[first_word],1)
        if last_word :
            str = word2digit[last_word].join(str.rsplit(last_word,1))
    sans_lettre = re.sub("[^0-9]", "", str)
    if len(sans_lettre)==0 :
        return 0
    return sans_lettre[0]+sans_lettre[-1]

def enigme_day1(chemin,with_word=False):
    fichier = open(chemin,'r')
    somme = 0
    for ligne in fichier.readlines():
        ligne = ligne.strip()
        somme += int(traite_ligne(ligne.strip(),with_word))
    return somme


def test_traite_ligne():
    assert traite_ligne("pqr3stu8vwx")=="38"
    assert traite_ligne("1abc2")=="12"
    assert traite_ligne("a1b2c3d4e5f")=="15"
    assert traite_ligne("treb7uchet")=="77"
    assert traite_ligne("two1nine",True)=="29"
    assert traite_ligne("zoneight234",True)=="14"
    assert traite_ligne("345696958584eightwo",True)=="32"
    assert traite_ligne("twone5",True)=="25"
    assert traite_ligne("7pqrstsixteen",True)=="76"
    assert traite_ligne("twone5",True)=="25"
    assert traite_ligne("eight2onethree6eight",True)=="88"
    

def test_enigme_day1():
    assert enigme_day1("input-01a-test.txt") == 142
    assert enigme_day1("input-01b-test.txt",True) == 281 


if __name__ == "__main__" :
    print(enigme_day1("input-01.txt",True))