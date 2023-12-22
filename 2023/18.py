import sys


carte = {}
min_ligne = 0
max_ligne = 0
min_colonne = 0
max_colonne = 0


HAUT = (-1,0)
BAS = (1,0)
GAUCHE = (0,-1)
DROITE = (0,1)

direction_map = {'R':DROITE,'U':HAUT,'L':GAUCHE,'D':BAS}


sys.setrecursionlimit(10000)

def imprime_carte():
    #print(min_ligne,max_ligne)
    for l in range(min_ligne-1,max_ligne+1):
        ligne = ''
        for c in range(min_colonne-1,max_colonne+1):
            #print(l,c)
            if (l,c) in carte:
                ligne += carte[(l,c)]
            else : 
                ligne += '.'
        print(ligne)

def rempli_exterieur():
    a_traiter = [(min_ligne-1,min_colonne-1)]
    traite = []
    while len(a_traiter)>0:
        coordonnee = a_traiter.pop(0)
        traite.append(coordonnee)
        if coordonnee in carte :
            continue
        carte[coordonnee]='O'
        if coordonnee[0]>min_ligne-1:
            if (coordonnee[0]-1,coordonnee[1]) not in a_traiter and (coordonnee[0]-1,coordonnee[1]) not in traite:
                #print("ajoute au dessus",coordonnee[0],min_ligne-1)
                a_traiter.append((coordonnee[0]-1,coordonnee[1]))
        if coordonnee[0]<max_ligne+1:
            if (coordonnee[0]+1,coordonnee[1]) not in a_traiter and (coordonnee[0]+1,coordonnee[1]) not in traite:
                #print("ajoute en dessous")
                a_traiter.append((coordonnee[0]+1,coordonnee[1]))
        if coordonnee[1]>min_colonne-1:
            if (coordonnee[0],coordonnee[1]-1) not in a_traiter and (coordonnee[0],coordonnee[1]-1) not in traite:
                #print("ajoute à gauche")
                a_traiter.append((coordonnee[0],coordonnee[1]-1))
        if coordonnee[1]<max_colonne+1:
            if (coordonnee[0],coordonnee[1]+1) not in a_traiter and (coordonnee[0],coordonnee[1]+1) not in traite:
                #print("ajoute à droite")
                a_traiter.append((coordonnee[0],coordonnee[1]+1))

def rempli_interieur():
    for l in range(min_ligne,max_ligne+1):
        for c in range(min_colonne,max_colonne+1):
            if (l,c) not in carte:
                carte[(l,c)]='I'

def compte():
    res = {}
    for l in range(min_ligne,max_ligne+1):
        for c in range(min_colonne,max_colonne+1):
            if (l,c) in carte :
                if carte[(l,c)] not in res:
                    res[carte[(l,c)]]=1
                else :
                    res[carte[(l,c)]] += 1
    return res

def enigme_day18(chemin):
    global min_ligne,max_ligne,min_colonne,max_colonne
    position = (0,0)
    carte[position]="#"
    with open(chemin,'r') as fichier :
        for ligne in fichier :
            direction,distance,couleur=ligne.strip().split()
            for _ in range(int(distance)):
                position = (position[0]+direction_map[direction][0],position[1]+direction_map[direction][1])
                carte[position]="#"
                if position[0]<min_ligne:
                    min_ligne=position[0]
                if position[0]>max_ligne:
                    max_ligne=position[0]
                if position[1]<min_colonne:
                    min_colonne=position[1]
                if position[1]>max_colonne:
                    max_colonne=position[1]
    imprime_carte()     
    print("------------------------------")           
    rempli_exterieur()                    
    imprime_carte()     
    print("------------------------------")           
    rempli_interieur()
    imprime_carte()
    comptage = compte()
    return comptage['#']+comptage['I']



def test_enigme_day18():
    assert enigme_day18("input-18-test.txt") == 62


if __name__ == "__main__" :
    print(enigme_day18("input-18.txt"))