
carte=[]
for i in range(200):
    carte.append(['.' for j in range(1000)])

ligneMax = 0
for line in open('input14.txt').readlines():
    line = line.strip()
    #print(line)
    slices = line.split(' -> ')
    #print(slices)
    colonneSrc, ligneSrc = [int(x) for x in slices[0].split(',')]
    for slice in slices[1:]:
        carte[ligneSrc][colonneSrc]="#"
        colonneDst, ligneDst = [int(x) for x in slice.split(',')]
        if max(ligneSrc,ligneDst)>ligneMax:
            ligneMax = max(ligneSrc,ligneDst)
        if colonneSrc==colonneDst : # meme colonne : on "dessine" un trait vertical
            i = min(ligneSrc,ligneDst)
            while i<=max(ligneSrc,ligneDst):
                carte[i][colonneSrc]="#"
                i += 1
        elif ligneSrc==ligneDst :         
            i = min(colonneSrc,colonneDst)
            while i<=max(colonneSrc,colonneDst):
                #print(ligneSrc,i)
                carte[ligneSrc][i]="#"
                i += 1
        else :
            print("ERROR : on ne peut pas aller de ",colonneSrc,ligneSrc,colonneDst,ligneDst)
        colonneSrc = colonneDst
        ligneSrc = ligneDst    

#print(ligneMax)
for i in range(1000):
    carte[ligneMax+2][i]="#"

# on affiche un zoom pour verifier le test :
# for ligne in carte[:12] :
#     print("".join(ligne[94:105]))

nbUniteSable = 0
while True : # boucle sur toutes les unites de sable, en sortant, on a le nombre d'unite recherche
    sableColonne = 500
    sableLigne = 0
    if carte[sableLigne][sableColonne]=="o":
        print("fini : ",nbUniteSable)
        exit()
    nbUniteSable += 1
    # print("------------------------------")
    # for ligne in carte[:10] :
    #     print("".join(ligne[94:105]))
    #input("?")
    while True : # boucle sur UNE unite de sable qui descend
        try :
            if carte[sableLigne+1][sableColonne]=="." : # cas avec du vide en dessous
                sableLigne += 1
                continue
            # cas avec du vide a gauche
            if (carte[sableLigne+1][sableColonne]=="#" or carte[sableLigne+1][sableColonne]=="o") and carte[sableLigne+1][sableColonne-1]==".":
                sableLigne +=1 
                sableColonne -=1
                continue
            # cas avec du vide a droite
            if (carte[sableLigne+1][sableColonne]=="#" or carte[sableLigne+1][sableColonne]=="o") and carte[sableLigne+1][sableColonne+1]==".":
                sableLigne +=1 
                sableColonne +=1
                continue      
            # cas sans vide : on est donc bloque
            carte[sableLigne][sableColonne]="o"
            break
        except IndexError :
            print("IndexError : ",sableLigne,sableColonne)
            exit()
      



