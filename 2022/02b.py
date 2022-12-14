
points = {'X': 1, 'Y': 2, 'Z': 3}

choix_coup = {'AX': 'Z','AY': 'X','AZ': 'Y','BX': 'X','BY': 'Y','BZ': 'Z','CX': 'Y','CY': 'Z','CZ': 'X'}


def victoire(a, b):
    if (a == 'A' and b == 'X') or (a == 'B' and b == 'Y') or (a == 'C' and b == 'Z') :
        return 3
    if (a == 'A' and b == 'Z') or (a == 'B' and b == 'X') or (a == 'C' and b == 'Y') : 
        return 0
    return 6


def calcul_point(coup_adversaire, coup_moi):
    return victoire(coup_adversaire, coup_moi) + points.get(coup_moi)


somme = 0
for line in open('input02.txt'):
    line = line.strip()
    coup_adversaire, resultat = line.split(' ')
    coup_moi = choix_coup.get(coup_adversaire+resultat)
    somme += calcul_point(coup_adversaire, coup_moi)
print("total :", somme)