elf = []
max_calorie = 0
somme_courante = 0
for line in open('input01.txt').readlines():
    line = line.strip()
    if line=='' :
        elf.append(somme_courante)
        somme_courante=0
        continue
    nb_calorie = int(line)
    somme_courante += nb_calorie
    if somme_courante>max_calorie:
        max_calorie = somme_courante
elf.sort()
print("max",elf[-1])
print("max des 3 ",elf[-1]+elf[-2]+elf[-3])

