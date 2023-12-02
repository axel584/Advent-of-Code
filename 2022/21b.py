
monkeys = {}

for line in open('input21.txt').readlines():
    line = line.strip()
    nom,action = line.split(': ')
    #print(nom,action)
    monkeys[nom] = action

fils_de_root1,operateur,fils_de_root2 = monkeys['root'].split(' ')

def calcule(humain) :
    dictionnaire = monkeys.copy()
    dictionnaire['humn']=humain
    while not isinstance(dictionnaire[fils_de_root1],int) or not isinstance(dictionnaire[fils_de_root2],int):
        for k,v in dictionnaire.items():
            #print(k,v)
            if k=="root":
                continue
            if isinstance(v,str) and v.isdigit() :
                dictionnaire[k]=int(v)
                #print("conversion",k,int(v))
            elif isinstance(v,int):
                pass
            else :
                #print("split ",v,type(v),v.isdigit())
                monkey1,operateur,monkey2 = v.split(' ')
                #print("decomposition : ",monkey1,operateur,monkey2)
                if isinstance(dictionnaire[monkey1],int) and isinstance(dictionnaire[monkey2],int) :
                    dictionnaire[k]=int(eval(str(dictionnaire[monkey1])+operateur+str(dictionnaire[monkey2])))
    return abs(dictionnaire[fils_de_root1]-dictionnaire[fils_de_root2])


# au final, ce qui marche mieux, c'est d'essayer chaque décile et d'affiner pour chaque chiffre du nombre à trouver
# h = 3_848_301_405_750
# a,b = calcule(h)
# print(abs(a-b),h)    
# h = 3_848_301_405_760
# a,b = calcule(h)
# print(abs(a-b),h)    
# h = 3_848_301_405_770
# a,b = calcule(h)
# print(abs(a-b),h)      
# h = 3_848_301_405_780
# a,b = calcule(h)
# print(abs(a-b),h) 
# h = 3_848_301_405_790
# a,b = calcule(h)
# print(abs(a-b),h)    
# h = 3_848_301_405_800
# a,b = calcule(h)
# print(abs(a-b),h)    
# h = 3_848_301_405_810
# a,b = calcule(h)
# print(abs(a-b),h)      
# h = 3_848_301_405_820
# a,b = calcule(h)
# print(abs(a-b),h)
# h = 3_848_301_405_830
# a,b = calcule(h)
# print(abs(a-b),h)      
# h = 3_848_301_405_840
# a,b = calcule(h)
# print(abs(a-b),h)     


# j'ai essayé une recherche par dichotomie mais sans success
min_h = 0
max_h = 1_000_000_000_000_000
while True :
    milieu = int((max_h + min_h)/2)
    f_min_h =  calcule(min_h)
    f_max_h =  calcule(max_h)
    f_milieu = calcule(milieu)
    if f_milieu == 0 :
        print(milieu)
        exit()
    if f_milieu<f_max_h:
        max_h = milieu
    else :
        max_h = max_h + milieu    
    if f_milieu<f_min_h :
        min_h = milieu
    else :
        min_h = min_h - milieu
    print(min_h,max_h)

