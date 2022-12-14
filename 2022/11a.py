import math

monkeys = []

class Monkey():

    fileObjets = []
    condition = 0
    monkeySiVrai = 0
    monkeySiFaux = 0
    numero = 0
    operation = None
    compteur = 0

    def run(self):
        for old in self.fileObjets :
            self.compteur += 1
            objetCourant = self.operation(old)
            objetCourant = math.floor(objetCourant / 3)
            if (objetCourant%self.condition)==0 :
                monkeys[self.monkeySiVrai].fileObjets.append(objetCourant)
            else :    
                monkeys[self.monkeySiFaux].fileObjets.append(objetCourant)
        self.fileObjets = [] # on a tout traite les objets
                

    def __str__(self):
        return f'monkey {self.numero} / objets : {self.fileObjets} / compteur : {self.compteur}'        


def parseOperation(chaine):
    if chaine=="old * old" :
        return lambda x : x * x 
    if chaine.startswith('old *') :
        return lambda x : x * int(chaine[6:])
    if chaine.startswith('old +') :
        return lambda x : x + int(chaine[6:])

monkeyEnCours = None
for line in open('input11.txt').readlines():
    line = line.strip()
    if line.startswith('Monkey'):
        monkeyEnCours = Monkey()
        monkeyEnCours.numero = int(line[7:8])
        continue
    if line.startswith('Starting items:'):
        monkeyEnCours.fileObjets = [int(x.strip()) for x in line[16:].split(',')]
        continue
    if line.startswith('Operation:'):
        monkeyEnCours.operation = parseOperation(line[17:])
        continue
    if line.startswith('Test:'):
        monkeyEnCours.condition = int(line[19:])
        continue
    if line.startswith('If true:'):
        monkeyEnCours.monkeySiVrai = int(line[25:])
        continue
    if line.startswith('If false:'):
        monkeyEnCours.monkeySiFaux = int(line[26:])
        continue
    if line=="" :
        monkeys.append(monkeyEnCours)
monkeys.append(monkeyEnCours) # on ajoute le dernier        

for _ in range(20):
    for monkey in monkeys :
        monkey.run()

listeCompteurs = []
for monkey in monkeys:
    listeCompteurs.append(monkey.compteur)

listeCompteurs.sort()
print(listeCompteurs[-1]*listeCompteurs[-2])