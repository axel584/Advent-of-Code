map = {} # map de tuple !!!
nb_lignes = 0
nb_colonnes = 0


def imprime_map():
    for num_ligne in range(nb_lignes):
        ligne = ""
        for num_colonne in range(nb_colonnes):
            ligne += map[(num_ligne,num_colonne)]
        print(ligne)
    print("------------------")

def glisse_nord():
    for num_ligne in range(1,nb_lignes):
        for num_colonne in range(nb_colonnes):
            if map[(num_ligne,num_colonne)]=="O":
                dest_ligne = num_ligne
                while map[(dest_ligne-1,num_colonne)]=='.':
                    dest_ligne -= 1
                    if dest_ligne==0 :
                        break
                map[dest_ligne,num_colonne],map[num_ligne,num_colonne]=map[num_ligne,num_colonne],map[dest_ligne,num_colonne] # interverti

def glisse_ouest():
    for num_colonne in range(1,nb_colonnes):
        for num_ligne in range(nb_lignes):
            if map[(num_ligne,num_colonne)]=="O":
                dest_colonne = num_colonne
                while map[(num_ligne,dest_colonne-1)]=='.':
                    dest_colonne -= 1
                    if dest_colonne==0 :
                        break
                map[num_ligne,num_colonne],map[num_ligne,dest_colonne]=map[num_ligne,dest_colonne],map[num_ligne,num_colonne] # interverti

def glisse_sud():
    for num_ligne in range(nb_lignes-2,-1,-1):
        for num_colonne in range(nb_colonnes):
            if map[(num_ligne,num_colonne)]=="O":
                dest_ligne = num_ligne
                while map[(dest_ligne+1,num_colonne)]=='.':
                    dest_ligne += 1
                    if dest_ligne==nb_lignes-1 :
                        break
                map[dest_ligne,num_colonne],map[num_ligne,num_colonne]=map[num_ligne,num_colonne],map[dest_ligne,num_colonne] # interverti

def glisse_est():
    for num_colonne in range(nb_colonnes-2,-1,-1):
        for num_ligne in range(nb_lignes):
            if map[(num_ligne,num_colonne)]=="O":
                dest_colonne = num_colonne
                while map[(num_ligne,dest_colonne+1)]=='.':
                    dest_colonne += 1
                    if dest_colonne==nb_colonnes-1 :
                        break
                map[num_ligne,num_colonne],map[num_ligne,dest_colonne]=map[num_ligne,dest_colonne],map[num_ligne,num_colonne] # interverti

def calcule_poids():
    somme = 0
    for num_ligne in range(nb_lignes):
        for num_colonne in range(nb_colonnes):
            if map[(num_ligne,num_colonne)]=="O":
                somme += nb_lignes-num_ligne
    return somme

def enigme_day14(chemin):
    global nb_lignes,nb_colonnes
    with open(chemin,'r') as fichier :
        for num_ligne,ligne in enumerate(fichier) :
            for num_colonne,element in enumerate(ligne.strip()):
                map[(num_ligne,num_colonne)]=element
                nb_lignes,nb_colonnes=num_ligne+1,num_colonne+1
    for i in range(1_000_000):
        glisse_nord()
        #imprime_map()
        glisse_ouest()
        #imprime_map()
        glisse_sud()
        #imprime_map()
        glisse_est()
        if i>1000 and (i+1)%93==1000000000%93:
            return calcule_poids()
    


def test_enigme_day14():
    assert enigme_day14("input-14-test.txt") == 136


if __name__ == "__main__" :
    print(enigme_day14("input-14.txt"))