from collections import defaultdict
import pytest
import re
from itertools import combinations, product


def run(registre_a,registre_b,registre_c,operations):
    #print(registre_a,registre_b,registre_c,operations)
    i = 0
    out = []
    while i<len(operations) :
        operation = operations[i]
        operande = operations[i+1]
        #print("operation ",operation,operande)
        #print("registre ",registre_a,registre_b,registre_c)
        if operande<=3:
            combo = operande
        if operande==4 :
            combo = registre_a
        if operande==5 :
            combo = registre_b    
        if operande==6 :
            combo = registre_c
        if operation==0:
            res = registre_a / 2**combo
            res = int(str(res)[:str(res).find('.')])
            registre_a = int(res)
        elif operation==1:
            registre_b = registre_b ^ operande
        elif operation==2:
            registre_b = combo % 8   
        elif operation==3:
            if registre_a!=0:
                i = combo
                continue
        elif operation==4:
            registre_b = registre_b ^registre_c
        elif operation==5:
            out.append(combo%8)
        elif operation==6:
            res = registre_a / 2**combo
            res = int(str(res)[:str(res).find('.')])
            registre_b = int(res)
        elif operation==7:
            res = registre_a / 2**combo
            res = int(str(res)[:str(res).find('.')])
            registre_c = int(res)
        else :
            print("operateur inconnu")
        i += 2

    return ",".join(list(map(str,out)))

def enigme_day17_first_part(chemin):
    registre_a,registre_b,registre_c = 0,0,0
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            if ligne.strip().startswith("Register A:") :
                print(int(ligne.strip()[11:]))
                registre_a=int(ligne.strip()[11:])
            if ligne.strip().startswith("Register B:") :
                print(int(ligne.strip()[11:]))
                registre_b=int(ligne.strip()[11:])    
            if ligne.strip().startswith("Register C:") :
                print(int(ligne.strip()[11:]))
                registre_c=int(ligne.strip()[11:])        
            if ligne.strip().startswith("Program:"):
                operations = list(map(int,ligne.strip()[8:].split(',')))
                print(operations)
    return run(registre_a,registre_b,registre_c,operations)




def enigme_day17_second_part(chemin):
    registre_a,registre_b,registre_c = 0,0,0
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            if ligne.strip().startswith("Register A:") :
                print(int(ligne.strip()[11:]))
                registre_a=int(ligne.strip()[11:])
            if ligne.strip().startswith("Register B:") :
                print(int(ligne.strip()[11:]))
                registre_b=int(ligne.strip()[11:])    
            if ligne.strip().startswith("Register C:") :
                print(int(ligne.strip()[11:]))
                registre_c=int(ligne.strip()[11:])        
            if ligne.strip().startswith("Program:"):
                operations = list(map(int,ligne.strip()[8:].split(',')))
                print(operations)
    print(registre_a,registre_b,registre_c,operations)
    registre_a = 1
    res = run(registre_a,registre_b,registre_c,operations)
    print("res / operations : ",res,operations)
    while res!=",".join(list(map(str,operations))):
        res = run(registre_a,registre_b,registre_c,operations)
        registre_a +=1
        if registre_a%1000 == 0:
            print("registre_a : ",registre_a)
    return registre_a-1



def test_enigme_day17():
    #assert enigme_day17_first_part("input-17-test.txt") == "4,6,3,5,6,3,5,2,1,0"
    assert enigme_day17_second_part("input-17-test2.txt") == 117440


if __name__ == "__main__":
    #print(enigme_day17_first_part("input-17-test.txt"))
    #print(enigme_day17_first_part("input-17.txt"))
    #enigme_day17_second_part("input-17-test2.txt")
    print(enigme_day17_second_part("input-17.txt"))
