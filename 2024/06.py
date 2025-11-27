from collections import defaultdict
import pytest
import re


MAX_LIGNE,MAX_COLONNE = 0,0

def imprime(tab):
    for ligne in tab:
        print("".join(ligne))


ordre_avancement=['^','>','v','<'] 

avancement = {
    '^' : [-1,0],
    '>' : [0,1],
    'v' : [1,0],
    '<' : [0,-1],
}

def is_boucle(tab,garde,direction):
    tab[garde[0]][garde[1]]='X'
    while garde[0]>=0 and garde[0]<=MAX_LIGNE and garde[1]>=1 and garde[1]<=MAX_LIGNE:
        #print(garde)
        next_step_ligne = garde[0] + avancement[direction][0]
        next_step_colonne = garde[1] + avancement[direction][1]
        if next_step_ligne<0 or next_step_ligne>=MAX_LIGNE or next_step_colonne<0 or next_step_colonne>=MAX_COLONNE :
            tab[garde[0]][garde[1]]=direction
            return False
        #print("next",next_step_ligne,next_step_colonne)
        if tab[next_step_ligne][next_step_colonne]=="#":
            # tourne de 90
            direction=ordre_avancement[(ordre_avancement.index(direction)+1)%4]
            #print("tourne, direction apres ",direction)
            #imprime(tab)
        elif tab[next_step_ligne][next_step_colonne]==direction: # on retombe sur la même direction que ce qu'on a, c'est qu'on boucle
            return True
        else :
            if tab[garde[0]][garde[1]]=='.':
                tab[garde[0]][garde[1]]=direction
            garde = [next_step_ligne,next_step_colonne]
    return False

def convert(tab,elements,dst):
    for num_ligne,ligne in enumerate(tab):
        for num_colonne,colonne in enumerate(ligne):
            if colonne in elements : 
                tab[num_ligne][num_colonne]=dst

def enigme_day06_first_part(chemin):
    global MAX_LIGNE,MAX_COLONNE
    somme = 0
    garde = [0,0]
    source_garde = [0,0]
    direction = ''
    tab=[]
    with open(chemin,'r') as fichier :
        for num_ligne,ligne in enumerate(fichier):
            tab.append(list(ligne.strip()))
            for num_colonne,colonne in enumerate(ligne.strip()):
                if colonne!='.' and colonne!="#":
                    direction = colonne
                    garde = [num_ligne,num_colonne]
        source_garde=garde
        MAX_COLONNE = len(tab[0])
        MAX_LIGNE = len(tab)
        #imprime(tab)
        #print("*"*50)
        #print("8,60",tab[8][60])
        #tab[8][60]='X'
        is_boucle(tab,garde,direction)
        #imprime(tab)
        #print("8,60",tab[8][60])
        convert(tab,['v','<','>','^'],'X')
        #imprime(tab)
        for ligne in tab: # compte les elements
            for colonne in ligne:
                if colonne=='X':
                    somme += 1
        garde=source_garde
    return somme

def enigme_day06_second_part(chemin):
    global MAX_LIGNE,MAX_COLONNE
    somme = 0
    garde = [0,0]
    source_garde = [0,0]
    direction = ''
    tab=[]
    with open(chemin,'r') as fichier :
        for num_ligne,ligne in enumerate(fichier):
            tab.append(list(ligne.strip()))
            for num_colonne,colonne in enumerate(ligne.strip()):
                if colonne!='.' and colonne!="#":
                    direction = colonne
                    garde = [num_ligne,num_colonne]
        source_garde=garde                    
        MAX_COLONNE = len(tab[0])
        MAX_LIGNE = len(tab)
        imprime(tab)
        is_boucle(tab,garde,direction)
        convert(tab,['v','<','>','^'],'X')
        positions = []
        for num_ligne,ligne in enumerate(tab): # compte les elements
            for num_colonne,colonne in enumerate(ligne):
                if colonne=='X':
                    positions.append([num_ligne,num_colonne])
        print("nombre de positions differentes ",len(positions))
        for position in positions:
            #print("test la position ",position)
            convert(tab,['X','v','<','>','^'],'.')
            garde = source_garde
            if position[0]==source_garde[0] and position[1]==source_garde[1]:
                print("continue")
                continue
            tab[position[0]][position[1]]='#'
            tab[garde[0]][garde[1]]='^'
            if is_boucle(tab,garde,'^'):
                print("on boucle si on ajoute un element sur ",position," somme : ",somme)
                #imprime(tab)
                somme += 1
            tab[position[0]][position[1]]='.'
    return somme
     


def test_enigme_day06():
    assert enigme_day06_first_part("input-06-test.txt")==41
    assert enigme_day06_second_part("input-06-test.txt")==6

if __name__ == "__main__" :
    #print(enigme_day06_first_part("input-06-test.txt"))
    #print(enigme_day06_first_part("input-06.txt"))
    print(enigme_day06_second_part("input-06.txt"))