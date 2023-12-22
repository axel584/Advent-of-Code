
def calcul_nb_differences_lignes(l1,l2):
    differences = 0
    for i,l in enumerate(l1):
        if l2[i]!=l :
            differences += 1
    return differences

def cherche_axe_horizontal(carte):
    for num_ligne in range(len(carte)-1):
        #print(f"verifie si {num_ligne} est l'axe de symetrie")
        nb_lignes_a_verifier = min(num_ligne+1,len(carte)-num_ligne-1)
        #print(f"{nb_lignes_a_verifier} lignes a verifier")
        total_differences = 0
        for i in range(nb_lignes_a_verifier):
            total_differences += calcul_nb_differences_lignes(carte[num_ligne-i],carte[num_ligne+i+1])
        if total_differences==1 :
            print("TROUVE axe horizontal ",num_ligne)    
            return num_ligne+1        
    return 0

def colonnes_are_differents(carte,c1,c2):
    differences = 0
    for l in carte:
        if l[c1]!=l[c2]:
            differences += 1
    return differences

def cherche_axe_vertical(carte):
    for num_colonnes in range(len(carte[0])-1):
        #print(f"verifie si {num_colonnes} est l'axe de symetrie")
        nb_lignes_a_verifier = min(num_colonnes+1,len(carte[0])-num_colonnes-1)
        #print(f"{nb_lignes_a_verifier} lignes a verifier")
        total_differences = 0
        for i in range(nb_lignes_a_verifier):
            #print(num_colonnes-i,num_colonnes+i+1)
            total_differences += colonnes_are_differents(carte,num_colonnes-i,num_colonnes+i+1)
        if total_differences==1 :
            print("TROUVE axe vertical ",num_colonnes)    
            return num_colonnes+1
    return 0

def print_carte(carte):
    for ligne in carte:
        print(''.join(ligne))

def enigme_day13(chemin):
    carte = []
    somme = 0
    with open(chemin,'r') as fichier :
        for ligne in fichier :
            if ligne.strip()=='' :
                #print("nouvelle carte")
                #print_carte(carte)
                somme += 100*cherche_axe_horizontal(carte)+cherche_axe_vertical(carte)
                carte = []
                continue
            carte.append([i for i in ligne.strip()])
        #print_carte(carte)
        somme += 100*cherche_axe_horizontal(carte)+cherche_axe_vertical(carte)
    return somme


# def test_nb_combinaison():
#     assert nb_combinaison("???.### 1,1,3")==1
#     assert nb_combinaison(".??..??...?##. 1,1,3")==4
#     assert nb_combinaison("?###???????? 3,2,1")==10


def test_enigme_day13():
    assert enigme_day13("input-13-test.txt") == 405


if __name__ == "__main__" :
    print(enigme_day13("input-13.txt"))