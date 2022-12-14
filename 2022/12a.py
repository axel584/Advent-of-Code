carte = []


class Etape :
    distanceFromOrigine = 0
    parent = None
    ligne = 0
    colonne = 0
    valeur = None

    def __str__(self) :
        return f'{self.ligne}/{self.colonne} : {self.valeur} ({self.distanceFromOrigine} etapes)'

    def __repr__(self) :
        return f'{self.ligne}/{self.colonne} : {self.valeur} ({self.distanceFromOrigine} etapes)'        

 
# lit les inputs
for line in open('input12.txt'):
    line = line.strip()
    carte.append([x for x in line])

ligne_max = len(carte)
colonne_max = len(carte[0])
etapeATraiter = []
dejaExplore = []

print(ligne_max,colonne_max)
carteCheminMax = []
for _ in range(ligne_max) :
    carteCheminMax.append(['.' for _ in range(colonne_max)])

#trouve le 'S'
for ligne in range(len(carte)):
    for colonne in range(len(carte[ligne])):
        if carte[ligne][colonne] == 'S':
            depart = Etape()
            depart.ligne = ligne
            depart.colonne = colonne
            depart.valeur='a'
            etapeATraiter.append(depart)


def explore(ligne, colonne, etapePrecedente):
    sommet = False
    if str(ligne)+"-"+str(colonne) in dejaExplore:
        return   
    nouvelleValeur = carte[ligne][colonne]
    if nouvelleValeur == "E" :
        nouvelleValeur = "z"
        sommet = True
        print("sommet trouve")
    #if abs(ord(etapePrecedente.valeur)-ord(nouvelleValeur)) <= 1 :
    if ord(nouvelleValeur) - ord(etapePrecedente.valeur) <= 1 :
        nouvelleEtape = Etape()
        nouvelleEtape.valeur = carte[ligne][colonne]
        nouvelleEtape.distanceFromOrigine = etapePrecedente.distanceFromOrigine + 1
        nouvelleEtape.parent = etapePrecedente
        nouvelleEtape.colonne = colonne
        nouvelleEtape.ligne = ligne
        etapeATraiter.append(nouvelleEtape)
        carteCheminMax[ligne][colonne]=nouvelleEtape.valeur
        dejaExplore.append(str(nouvelleEtape.ligne)+"-"+str(nouvelleEtape.colonne))
        if sommet:
            print("trouve en :",nouvelleEtape.distanceFromOrigine," etapes") 
            exit()

i = 0
while len(etapeATraiter)>0 :
    i += 1
    if i%100==0 :
        print(i)
    etape = etapeATraiter.pop(0)
    if etape.ligne > 0 :
        explore(etape.ligne-1,etape.colonne,etape)
    if etape.ligne+1<ligne_max :
        explore(etape.ligne+1,etape.colonne,etape)  
    if etape.colonne > 0 :
        explore(etape.ligne,etape.colonne-1,etape)
    if etape.colonne+1 < colonne_max:
        explore(etape.ligne,etape.colonne+1,etape)
    #sorted(etapeATraiter,key=lambda e:e.distanceFromOrigine)

#print(dejaExplore)

for ligne in carteCheminMax :
    print("".join([x for x in ligne]))

            

