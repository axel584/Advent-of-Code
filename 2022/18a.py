grille=[]

for line in open('input18.txt').readlines():
    line = line.strip()
    x,y,z = [int(i) for i in line.split(',')]
    print(x,y,z)
    grille.append([x,y,z])

print(grille)

totalCote = 0
for x,y,z in grille:
    print(x,y,z)
    cote = 0
    if [x+1,y,z] not in grille :
        totalCote += 1
        cote += 1
    if [x-1,y,z] not in grille :
        totalCote += 1
        cote += 1
    if [x,y+1,z] not in grille :
        totalCote += 1
        cote += 1
    if [x,y-1,z] not in grille :
        totalCote += 1
        cote += 1
    if [x,y,z+1] not in grille :
        totalCote += 1
        cote += 1
    if [x,y,z-1] not in grille :
        totalCote += 1
        cote += 1
    print("cote",cote)

print(totalCote)                      
