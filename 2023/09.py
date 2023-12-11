
def has_only_zero(ligne):
    for i in ligne : 
        if i!=0 :
            return False
    return True

def calcule_difference(ligne):
    difference = []
    for indice,element in enumerate(ligne[:-1]):
        difference.append(ligne[indice+1]-element)
    return difference


def calcule_valeur_suivante(ligne):
    liste_ligne = []
    liste_ligne.append(ligne)
    ligne_courante = ligne
    while not has_only_zero(ligne_courante):
        difference = calcule_difference(ligne_courante)
        liste_ligne.append(difference)
        ligne_courante = difference
    print(liste_ligne)
    somme_des_derniers = 0
    for ligne in liste_ligne[::-1]:
        print(ligne)
        somme_des_derniers += ligne[-1]
    print(somme_des_derniers)
    return somme_des_derniers

def calcule_valeur_precedente(ligne):
    liste_ligne = []
    liste_ligne.append(ligne)
    ligne_courante = ligne
    while not has_only_zero(ligne_courante):
        difference = calcule_difference(ligne_courante)
        liste_ligne.append(difference)
        ligne_courante = difference
    print(liste_ligne)
    precedent_premier=0
    for ligne in liste_ligne[::-1]:
        precedent_premier = ligne[0]-precedent_premier
    return precedent_premier

def enigme_day09(chemin):
    somme = 0
    with open(chemin,'r') as fichier :
        for ligne in [i.strip() for i in fichier] :
            ligne = [int(i) for i in ligne.split()]
            print(ligne)
            somme += calcule_valeur_suivante(ligne)
    return somme

def enigme_day09_second_part(chemin):
    somme = 0
    with open(chemin,'r') as fichier :
        for ligne in [i.strip() for i in fichier] :
            ligne = [int(i) for i in ligne.split()]
            print(ligne)
            somme += calcule_valeur_precedente(ligne)
    return somme

def test_calcule():
    assert calcule_valeur_suivante([10,13,16,21,30,45]) == 68
    assert calcule_valeur_precedente([10,13,16,21,30,45]) == 5


def test_enigme_day09():
    assert enigme_day09("input-09a-test.txt") == 114
    assert enigme_day09_second_part("input-09a-test.txt") == 2


if __name__ == "__main__" :
    print(enigme_day09_second_part("input-09.txt"))