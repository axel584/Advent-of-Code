


def cherche_axe_horizontal(carte):
    for num_ligne in range(len(carte)-1):
        #print(f"verifie si {num_ligne} est l'axe de symetrie")
        nb_lignes_a_verifier = min(num_ligne+1,len(carte)-num_ligne-1)
        #print(f"{nb_lignes_a_verifier} lignes a verifier")
        for i in range(nb_lignes_a_verifier):
            if carte[num_ligne-i]!=carte[num_ligne+i+1]:
                break
        else :
            return num_ligne+1
    return 0

def colonnes_are_differents(carte,c1,c2):
    for l in carte:
        if l[c1]!=l[c2]:
            return True
    return False

def cherche_axe_vertical(carte):
    for num_colonnes in range(len(carte[0])-1):
        #print(f"verifie si {num_colonnes} est l'axe de symetrie")
        nb_lignes_a_verifier = min(num_colonnes+1,len(carte[0])-num_colonnes-1)
        #print(f"{nb_lignes_a_verifier} lignes a verifier")
        for i in range(nb_lignes_a_verifier):
            #print(num_colonnes-i,num_colonnes+i+1)
            if colonnes_are_differents(carte,num_colonnes-i,num_colonnes+i+1):
                break
        else :
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