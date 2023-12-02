
monkeys = {}

for line in open('input21.txt').readlines():
    line = line.strip()
    nom,action = line.split(': ')
    print(nom,action)
    monkeys[nom] = action

while not isinstance(monkeys['root'],int):
    for k,v in monkeys.items():
        print(k,v)
        if isinstance(v,str) and v.isdigit() :
            monkeys[k]=int(v)
            print("conversion",k,int(v))
        elif isinstance(v,int):
            pass
        else :
            print("split ",v,type(v),v.isdigit())
            monkey1,operateur,monkey2 = v.split(' ')
            print("decomposition : ",monkey1,operateur,monkey2)
            if isinstance(monkeys[monkey1],int) and isinstance(monkeys[monkey2],int) :
                monkeys[k]=int(eval(str(monkeys[monkey1])+operateur+str(monkeys[monkey2])))
                print("eval : ",monkeys[k])

print("resultat : ",monkeys['root'])
