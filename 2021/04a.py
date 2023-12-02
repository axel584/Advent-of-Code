TAILLE_GRILLE = 5

lines = open('input04.txt').readlines()

liste_nombres = [int(x) for x in lines[0].split(',')]
#print(liste_nombres)

liste_grilles = []

grille = []
for line in [x.strip() for x in lines[2:]]:
    if line=='' :
        liste_grilles.append(grille)
        grille = []
        continue
    grille.append([int(x) for x in line.split( )])
liste_grilles.append(grille)

def coche(nombre):
    num_grille = 0
    for grille in liste_grilles:
        num_ligne = 0
        for ligne in grille:
            num_colonne = 0
            for colonne in ligne:
                if colonne==nombre :
                    #print("trouve",colonne,num_grille,num_ligne,num_colonne)
                    liste_grilles[num_grille][num_ligne][num_colonne] = '*'
                num_colonne += 1        
            num_ligne += 1
        num_grille += 1

def verifieGrille() :
    num_grille = 0
    for grille in liste_grilles:
        # verifie les lignes
        for ligne in grille:
            gagnant = True
            for colonne in ligne:
                if colonne!='*' :
                    gagnant = False
                    break
            if gagnant :
                return num_grille
        # on verifie les colonnes
        for c in range(TAILLE_GRILLE) :
            gagnant = True
            for l in range(TAILLE_GRILLE):
                if grille[l][c] != '*':
                    gagnant = False
                    break
            if gagnant :
                return num_grille        
        num_grille += 1
    return None

def imprimeGrille(num):
    for ligne in liste_grilles[num]:
        print(" ".join([str(i) for i in ligne]))

def calculePoint(num):
    somme = 0
    for ligne in liste_grilles[num]:
        #print(ligne)
        #print(sum([i for i in ligne if i!='*']))
        somme += sum([i for i in ligne if i!='*'])
    return somme

for nombre in liste_nombres:
    #print("coche ",nombre)
    coche(nombre)
    grilleGagnante = verifieGrille()
    if grilleGagnante!=None :
        #print("gagnant :",grilleGagnante+1)
        #imprimeGrille(grilleGagnante)
        print(nombre * calculePoint(grilleGagnante))
        exit()

# imprimeGrille(2)
# grilleGagnante = verifieGrille()
