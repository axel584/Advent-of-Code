import re

p = re.compile(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)')

piles = []
for i in range(9) :
    print(i)
    piles.append([])

print(piles)

def lecture_initial() :
    for line in fichier:
        line = line.strip()
        print(line,len(line))
        for i in range(9) :
            if len(line)<i*4 + 2 :
                continue
            lettre = line[i*4 + 1]
            if lettre==' ':
                continue
            print(i,lettre)
            piles[i].insert(0,lettre)
        if line=='' :
            return


def modification() :
    for line in fichier:
        line = line.strip()
        print(line)
        m = p.search(line)
        nbElements = int(m.group(1))
        source = int(m.group(2))-1
        destination = int(m.group(3))-1
        print(nbElements, source, destination)
        print("avant :", piles)
        groupe = []
        for _ in range(nbElements):
            print("plop")
            element = piles[source].pop()
            groupe.append(element)
        groupe.reverse()
        for element in groupe:
            piles[destination].append(element)
        print("apres :", piles)


fichier = open('input05.txt')
lecture_initial()
print(piles)
modification()

reponse = ''
for i in range(9):
    reponse += piles[i].pop()

print(reponse)