import pytest



def traite_ligne(str):
    all_card_value = str[str.find(':')+1:]
    winning_draw,my_numbers = all_card_value.split('|')
    print(winning_draw)
    print(my_numbers)
    winning_value = [i for i in winning_draw.split(' ') if i!=""]
    my_value = [i for i in my_numbers.split(' ') if i!=""]
    common_value = list(set(winning_value) & set(my_value))
    print(common_value)
    print(2**(len(common_value)-1))
    if len(common_value)==0 :
        return 0
    return 2**(len(common_value)-1)

def traite_ligne_second_part(str):
    all_card_value = str[str.find(':')+1:]
    winning_draw,my_numbers = all_card_value.split('|')
    winning_value = [i for i in winning_draw.split(' ') if i!=""]
    my_value = [i for i in my_numbers.split(' ') if i!=""]
    common_value = list(set(winning_value) & set(my_value))
    return len(common_value)

def enigme_day04(chemin):
    fichier = open(chemin,'r')
    somme = 0
    for ligne in fichier.readlines():
        ligne = ligne.strip()
        somme += int(traite_ligne(ligne.strip()))
    return somme

def enigme_day04_second_part(chemin):
    fichier = open(chemin,'r')
    compteur = 0
    lignes = fichier.readlines()
    max_cards = len(lignes)
    instance_cards = [1 for _ in range(max_cards)]
    print(instance_cards)
    for ligne in lignes:
        gain_line = int(traite_ligne_second_part(ligne.strip()))
        # calculate_won_cards(instance_cards,gain_line)->instance_cards
        gain_line_total = gain_line * instance_cards[compteur]
        print(compteur+1,gain_line,gain_line_total)
        for winning_card in range(compteur,compteur+gain_line):
            instance_cards[winning_card+1]+=instance_cards[compteur]
        compteur +=1
        print(instance_cards)
    return sum(instance_cards)

@pytest.mark.skip()
def test_traite_ligne():
    assert traite_ligne("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")==8
    assert traite_ligne("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19")==2
    assert traite_ligne("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36")==0

def test_traite_ligne_second_part():
    assert traite_ligne_second_part("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")==4
    assert traite_ligne_second_part("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19")==2
    assert traite_ligne_second_part("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1")==2
    assert traite_ligne_second_part("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83")==1
    assert traite_ligne_second_part("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36")==0
    assert traite_ligne_second_part("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")==0

@pytest.mark.skip()
def test_enigme_day04():
    assert enigme_day04("input-04a-test.txt") == 13

def test_enigme_day04_second_part():
    assert enigme_day04_second_part("input-04b-test.txt") == 30

if __name__ == "__main__" :
    print(enigme_day04_second_part("input-04-theo.txt"))