registre = 1
cycle = 1

somme = 0

def estCyclePertinent(cycle):
    return (cycle-20)%40==0

def observe():
    global somme
    if estCyclePertinent(cycle):
        somme += cycle*registre

for line in open('input10.txt').readlines():
    line = line.strip()
    #print(line,cycle,registre)
    if line == "noop" :
        observe()
        cycle += 1
        continue
    operation,valeur=line.split(' ')
    observe()
    cycle += 1
    observe()
    cycle += 1
    registre += int(valeur)

print(somme)    