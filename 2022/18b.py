import sys

TAILLE_GRILLE = 21

sys.setrecursionlimit(20000)

grille={}

for line in open('input18.txt').readlines():
    line = line.strip()
    x,y,z = [int(i) for i in line.split(',')]
    grille[x,y,z]=1

def remplir(x,y,z,couleur): # trouve toutes les valeurs comprises entre 0 et TAILLE_GRILLE contigue qui ne sont pas dans la grille
    grille[x,y,z]=couleur
    if x-1>-1 and (x-1,y,z) not in grille :
        remplir(x-1,y,z,couleur)
    if x+1<TAILLE_GRILLE and (x+1,y,z) not in grille :
        remplir(x+1,y,z,couleur)
    if y-1>-1 and (x,y-1,z) not in grille :
        remplir(x,y-1,z,couleur)
    if y+1<TAILLE_GRILLE and (x,y+1,z) not in grille :
        remplir(x,y+1,z,couleur)
    if z-1>-1 and (x,y,z-1) not in grille :
        remplir(x,y,z-1,couleur)
    if z+1<TAILLE_GRILLE and (x,y,z+1) not in grille :
        remplir(x,y,z+1,couleur)        

def display():
    for z in range(TAILLE_GRILLE):
        for y in range(TAILLE_GRILLE):
            ligne = ""
            for x in range(TAILLE_GRILLE):
                if (x,y,z) in grille :
                    ligne += str(grille[x,y,z])
                else :
                    ligne += " "
            print(ligne)
        print("-"*TAILLE_GRILLE)


remplir(0,0,0,2) # exterieur en "2"
# display()
# exit()
# remplir(3,5,7,3) # premier trou trouve en "3"
# remplir(3,6,9,3) # premier trou trouve en "3"
# remplir(4,9,14,3) # premier trou trouve en "3"
# remplir(4,11,16,3) # premier trou trouve en "3"
# remplir(5,7,14,3) # premier trou trouve en "3"
# remplir(5,8,4,3) # premier trou trouve en "3"
remplir(10,10,10,3) # premier trou trouve en "3"

# display()
# exit()

print(len(grille))

totalCoteExterieur = 0
for x,y,z in grille:
    if grille[x,y,z]!=1 :
        continue
    if (x+1,y,z) in grille and grille[x+1,y,z]==2 : # on verifie qu'il est sur l'exterieur
        totalCoteExterieur += 1
    if (x-1,y,z) in grille and grille[x-1,y,z]==2:
        totalCoteExterieur += 1
    if (x,y+1,z) in grille and grille[x,y+1,z]==2:
        totalCoteExterieur += 1
    if (x,y-1,z) in grille and grille[x,y-1,z]==2:
        totalCoteExterieur += 1
    if (x,y,z+1) in grille and grille[x,y,z+1]==2:
        totalCoteExterieur += 1
    if (x,y,z-1) in grille and grille[x,y,z-1]==2:
        totalCoteExterieur += 1

print("cote exterieur",totalCoteExterieur)

totalCote = 0
for x,y,z in grille:
    if grille[x,y,z]!=1 :
        continue
    if (x+1,y,z) not in grille :
        totalCote += 1
    if (x-1,y,z) not in grille :
        totalCote += 1
    if (x,y+1,z) not in grille :
        totalCote += 1
    if (x,y-1,z) not in grille :
        totalCote += 1
    if (x,y,z+1) not in grille :
        totalCote += 1
    if (x,y,z-1) not in grille :
        totalCote += 1

print("cote interieur",totalCote)

for x in range(TAILLE_GRILLE):
    for y in range(TAILLE_GRILLE):
        for z in range(TAILLE_GRILLE):
            if (x,y,z) not in grille :
                print("premier element manquant :",x,y,z)
                exit()