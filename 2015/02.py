
def calcul_papier_paquet(dimension):
    print(dimension)
    dimension = sorted(dimension)
    extra = dimension[0]*dimension[1]
    taille_paquet = 2*dimension[0]*dimension[1]+2*dimension[0]*dimension[2]+2*dimension[1]*dimension[2]
    return extra + taille_paquet

def enigme1_day2(chemin):
    fichier = open(chemin,'r')
    somme = 0
    for ligne in fichier.readlines():
        print(ligne.strip())
        dimension = [int(i) for i in ligne.strip().split('x')]
        somme += calcul_papier_paquet(dimension)
        
    print(somme)

def calcul_ruban_paquet(dimension):
    print(dimension)
    dimension = sorted(dimension)
    extra = dimension[0]*dimension[1]*dimension[2]
    taille = 2*dimension[0]+2*dimension[1]
    print(extra,taille)
    return extra + taille

def enigme2_day2(chemin):
    fichier = open(chemin,'r')
    somme = 0
    for ligne in fichier.readlines():
        print(ligne.strip())
        dimension = [int(i) for i in ligne.strip().split('x')]
        somme += calcul_ruban_paquet(dimension)
        
    print(somme)    

if __name__ == "__main__" :
    # print(enigme1_day2("input-02.txt"))
    print(enigme2_day2("input-02.txt"))
    # print(calcul_papier_paquet([2,3,4]))
    # print(calcul_papier_paquet([1,1,10]))
    # print(calcul_ruban_paquet([2,3,4]))
    # print(calcul_ruban_paquet([1,1,10]))