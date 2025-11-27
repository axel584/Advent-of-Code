import pytest

def is_safe(rapport):
    print(rapport)
    prec = rapport[0]
    signe = None
    for i in rapport[1:] :
        difference = i-prec
        if difference==0 or difference>3 or difference<-3 :
            return False
        if difference>0 and signe=='-':
            return False
        if difference<0 and signe=='+':
            return False    
        if signe is None :
            if difference>0 :
                signe = "+"
            if difference<0 :
                signe = '-'
        prec = i
    return True

def is_safe_with_dampener(rapport):
    dampener = 0
    print(rapport)
    prec = rapport[0]
    signe = None
    for i in rapport[1:] :
        difference = i-prec
        if difference==0 or difference>3 or difference<-3 :
            if dampener==0 :
                dampener += 1
                continue
            return False
        if difference>0 and signe=='-':
            if dampener==0 :
                dampener += 1
                continue            
            return False
        if difference<0 and signe=='+':
            if dampener==0 :
                dampener += 1
                continue            
            return False    
        if signe is None :
            if difference>0 :
                signe = "+"
            if difference<0 :
                signe = '-'
        prec = i
    return True

def enigme_day02_first_part(chemin):
    somme = 0
    with open(chemin,'r') as fichier :
        for ligne in fichier:
            rapport = [int(i) for i in ligne.strip().split(' ')]
            if is_safe(rapport):
                somme += 1
    return somme

# def enigme_day02_second_part(chemin):
#     somme = 0
#     with open(chemin,'r') as fichier :
#         for ligne in fichier:
#             rapport = [int(i) for i in ligne.strip().split(' ')]
#             print(rapport)
#             if is_safe_with_dampener(rapport):
#                 print("safe with dampener")
#                 somme += 1
#             elif is_safe(rapport[1:]): # essaye de supprimer le premier element
#                 print("safe sans premier")
#                 somme += 1
#     return somme

def enigme_day02_second_part(chemin):
    somme = 0
    with open(chemin,'r') as fichier :
        for ligne in fichier:
            rapport = [int(i) for i in ligne.strip().split(' ')]
            #print(rapport)
            safe = False
            for i in range(len(rapport)):
                if i==1 :
                    if is_safe(rapport[1:]):
                        safe = True
                        break
                if i==len(rapport):
                    if is_safe(rapport[:-1]):
                        safe = True
                        break
                if is_safe(rapport[:i]+rapport[i+1:]):
                    safe = True
                    break
            if safe :
                somme += 1
    return somme

def test_enigme_day01_first_part():
    assert enigme_day02_first_part("input-02-test.txt")==2

def test_enigme_day01_second_part():
    assert enigme_day02_second_part("input-02-test.txt")==4

if __name__ == "__main__" :
    #print(enigme_day02_first_part("input-02.txt"))
    print(enigme_day02_second_part("input-02.txt"))