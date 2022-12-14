registre = 1
cycle = 1

somme = 0

crt = []
for _ in range(6):
    crt.append(['.' for _ in range(40)])

ligne = 0
colonne = 0

def estCyclePertinent(cycle):
    return (cycle-20)%40==0

def affiche() :
    if abs(colonne-registre)<=1 :
        print(ligne,colonne)
        crt[ligne][colonne]="#"

def incremente():
    global ligne,colonne
    colonne += 1
    if colonne==40 :
        ligne += 1
        colonne =0

for line in open('input10.txt').readlines():
    line = line.strip()
    #print(line,cycle,registre)
    if line == "noop" :
        affiche()
        cycle += 1
        incremente()
        continue
    _,valeur=line.split(' ')
    affiche()
    cycle += 1
    incremente()
    affiche()
    cycle += 1
    incremente()
    registre += int(valeur)

for ligne in crt:
    print(''.join(ligne))