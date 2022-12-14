
carte=[]
for i in range(200):
    carte.append(['.' for j in range(200)])

for line in open('input14.txt').readlines():
    line = line.strip()
    #print(line)
    slices = line.split(' -> ')
    #print(slices)
    colonneSrc, ligneSrc = [int(x) for x in slices[0].split(',')]
    for slice in slices[1:]:
        carte[ligneSrc][colonneSrc-400]="#"
        colonneDst, ligneDst = [int(x) for x in slice.split(',')]
        if colonneSrc==colonneDst : # meme colonne : on "dessine" un trait vertical
            i = min(ligneSrc,ligneDst)
            while i<=max(ligneSrc,ligneDst):
                carte[i][colonneSrc-400]="#"
                i += 1
        elif ligneSrc==ligneDst :         
            i = min(colonneSrc,colonneDst)
            while i<=max(colonneSrc,colonneDst):
                #print(ligneSrc,i)
                carte[ligneSrc][i-400]="#"
                i += 1
        else :
            print("ERROR : on ne peut pas aller de ",colonneSrc,ligneSrc,colonneDst,ligneDst)
        colonneSrc = colonneDst
        ligneSrc = ligneDst    

# on affiche un zoom pour verifier le test :
# for ligne in carte[:10] :
#     print("".join(ligne[94:105]))

nbUniteSable = 0
while True : # boucle sur toutes les unites de sable, en sortant, on a le nombre d'unite recherche
    sableColonne = 100
    sableLigne = 0
    nbUniteSable += 1
    while True : # boucle sur UNE unite de sable qui descend
        #carte[sableLigne][sableColonne]='+'
        # print("------------------------------")
        # for ligne in carte[:10] :
        #     print("".join(ligne[94:105]))
        #carte[sableLigne][sableColonne]='.'
        if sableLigne>=199 : # abysse : on arrete
            print("fin : ",nbUniteSable-1)
            exit()
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
      



