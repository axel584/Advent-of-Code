def priorite(lettre):
    if lettre.isupper():
        return ord(lettre)-ord('A')+27
    else:
        return ord(lettre)-ord('a')+1


somme = 0
for line in open('input03.txt'):
    line = line.strip()
    premier = line[:int(len(line)/2)]
    deuxieme = line[int(len(line)/2):]
    commun = list(set(premier) & set(deuxieme))
    print(commun[0],priorite(commun[0]))
    somme += priorite(commun[0])

print("somme : ",somme)    