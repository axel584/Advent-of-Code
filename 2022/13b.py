import functools

def compare(gauche,droite) :
    # print("gauche",type(gauche),gauche)
    # print("droite",type(droite),droite)
    if type(gauche)==list and type(droite)==list :
        if gauche==None or len(gauche)==0 :
            return True
        if droite==None or len(droite)==0 :
            return False
        if gauche[0] == droite[0]:
            return compare(gauche[1:],droite[1:])
        return compare(gauche[0],droite[0])
    if type(gauche)==list and type(droite)==int:
        return compare(gauche,[droite])
    if type(gauche)==int and type(droite)==list:
        return compare([gauche],droite)        
    if type(gauche)==int and type(droite)==int :
        return gauche<=droite

def fonctionCompare(gauche,droite):
    res = compare(gauche,droite)
    if res :
        return -1
    else :
        return 1      
    
tableau = []
for line in open('input13.txt'):
    line = line.strip()
    if line=='' :
        continue
    tableau.append(eval(line))
tableau.append([[2]])
tableau.append([[6]])
tableauTrie = sorted(tableau,key=functools.cmp_to_key(fonctionCompare))
i =1
for element in tableauTrie:
    if element==[[2]]:
        premierIndice = i
    if element==[[6]]:
        deuxiemeIndice = i 
    i += 1
print(premierIndice*deuxiemeIndice)