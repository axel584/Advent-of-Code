foret = []
NB_ARBRE = 99

for line in open('input08.txt').readlines():
    line = line.strip()
    foret.append([int(x) for x in line])
#print(foret)


def estVisible(x,y):
    valeur = foret[x][y]
    #print("est visible a calculer : ",x,y,valeur)
    if x==0 or x==NB_ARBRE or y==0 or y==NB_ARBRE:
        return True
    trouvePlusGrand = False    
    for i in range(x): # verifie les arbres sur la meme ligne avant l'arbre en question
        if foret[i][y]>=valeur :
            #print("arbre plus grand a gauche :",i,y,foret[i][y])
            trouvePlusGrand = True
    if not trouvePlusGrand:
        #print("visible de la gauche : ",trouvePlusGrand)      
        return True
    trouvePlusGrand = False    
    for i in range(x+1,NB_ARBRE): # verifie les arbres sur la meme ligne apres l'arbre
        if foret[i][y]>=valeur :
            #print("arbre plus grand a droite:",i,y,foret[i][y])
            trouvePlusGrand = True
    if not trouvePlusGrand:
        #print("visible de la droite",trouvePlusGrand)      
        return True
    trouvePlusGrand = False    
    for i in range(y): # verifie les arbres sur la meme colonne avant l'arbre en question
        if foret[x][i]>=valeur :
            #print("arbre plus grand en haut :",i,y,foret[x][i])
            trouvePlusGrand = True
    if not trouvePlusGrand:
        #print("visible du haut")
        return True  
    trouvePlusGrand = False      
    for i in range(y+1,NB_ARBRE): # verifie les arbres sur la meme colonne apres l'arbre
        if foret[x][i]>=valeur :
            trouvePlusGrand = True
            #print("arbre plus grand en bas :",i,y,foret[x][i],trouvePlusGrand)
    if not trouvePlusGrand:
        #print("visible du bas. trouvePlusGrand :",trouvePlusGrand)
        return True    
    return False


nb_arbre_visible = 0
for x in range(NB_ARBRE):
    for y in range(NB_ARBRE):
        if estVisible(x,y) :
            nb_arbre_visible += 1
            #print(nb_arbre_visible, x, y, foret[x][y])
print("nombre d'arbres visibles :",nb_arbre_visible)            