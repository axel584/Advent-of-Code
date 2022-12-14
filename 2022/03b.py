def priorite(lettre):
    if lettre.isupper():
        return ord(lettre)-ord('A')+27
    else:
        return ord(lettre)-ord('a')+1


somme = 0
i = 0
groupe = []
for line in open('input03.txt'):
    line = line.strip()
    groupe.append(line)
    i += 1
    if i == 3 :
        element_commun = list(set(groupe[0]) & set(groupe[1]) & set(groupe[2]))
        somme += priorite(element_commun[0])
        i=0
        groupe=[]

print("somme :",somme)
        