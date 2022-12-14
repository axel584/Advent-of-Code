compteur = 0

for line in open('input04.txt'):
    line = line.strip()
    elf1,elf2=line.split(',')
    section1 =  [x for x in range(int(elf1.split('-')[0]), int(elf1.split('-')[1])+1)]
    section2 = [x for x in range(int(elf2.split('-')[0]), int(elf2.split('-')[1])+1)]
    intersection = list(set(section1) & set(section2))
    if len(intersection)==len(section1) or len(intersection)==len(section2):
        compteur += 1

print("nombre d'intersection inclue dans l'une des sections : ",compteur)
