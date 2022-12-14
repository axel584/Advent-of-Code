foret = []
NB_ARBRE = 99
#NB_ARBRE = 5

for line in open('input08.txt').readlines():
    line = line.strip()
    foret.append([int(x) for x in line])
#print(foret)


def score(x,y):
    valeur = foret[x][y]
    #print("score de : ",x,y,valeur)
    if x==0 or x==NB_ARBRE or y==0 or y==NB_ARBRE:
        return 0
    scoreGauche = 0  
    #for i in range(y-1,-1,-1):
        #print("i, y :",i, y)
        #print("element vers la gauche :",i,y,foret[x][i])    
    for i in range(y-1,-1,-1):
        #print("Gauche i",i,scoreGauche,foret[x][i])
        if foret[x][i]>=valeur :
            #print("trouve plus grand a gauche")
            scoreGauche += 1
            break
        scoreGauche += 1
    #print("scoreGauche :",scoreGauche)    
    scoreBas = 0     
    for i in range(x+1,NB_ARBRE): 
        #print("Bas i",i,scoreBas,foret[i][y])
        if foret[i][y]>=valeur :
            #print("trouve plus grand")
            scoreBas += 1
            break
        scoreBas += 1
    #print("scoreBas :",scoreBas)        
    scoreHaut = 0   
    #for i in range(x-1,-1,-1):
        #print("i, x :",i, x)
        #print("element vers le haut :",i,y,foret[i][y])
    for i in range(x-1,-1,-1):
        #print("Haut i",x,i,scoreHaut,foret[i][y])
        if foret[i][y]>=valeur :
            scoreHaut += 1
            break
        scoreHaut += 1
    #print("scoreHaut :",scoreHaut) 
    # DROITE
    scoreDroite = 0  
    #for i in range(y+1,NB_ARBRE):
        #print("i, y :",i, y)
        #print("element vers la droite :",i,y,foret[x][i])
    for i in range(y+1,NB_ARBRE): # verifie les arbres sur la meme colonne apres l'arbre
        #print("Droite i",i,scoreDroite,foret[x][i])
        if foret[x][i]>=valeur :
            scoreDroite += 1
            break
        scoreDroite += 1
    #print("scoreDroite :",scoreDroite) 
    return scoreHaut*scoreBas*scoreGauche*scoreDroite


#print(score(1,2)) # doit trouver 4
#print(score(3,2)) # doit trouver 8

#nb_arbre_visible = 0
score_max = 0
for x in range(NB_ARBRE):
    for y in range(NB_ARBRE):
        score_courant = score(x,y)
        if score_max<score_courant :
            score_max = score_courant
print("score :",score_max)            