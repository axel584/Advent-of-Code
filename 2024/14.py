from collections import defaultdict
import pytest
import re
from itertools import combinations, product

# LARGEUR = 11
# HAUTEUR = 7
LARGEUR = 101
HAUTEUR = 103

def enigme_day14_first_part(chemin):
    somme = 0
    robots = []
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            robot = []
            p_data,v_data = ligne.strip().split(' ')
            robot.append(list(map(int,p_data[2:].split(','))))
            robot.append(list(map(int,v_data[2:].split(','))))
            robots.append(robot)
    print(robots)
    for i in range(100):
        for robot in robots :
            position,vitesse = robot
            position[0]=(position[0]+vitesse[0])%LARGEUR
            position[1]=(position[1]+vitesse[1])%HAUTEUR
            print("robot",robot)
        print("*"*50)
    a,b,c,d = 0,0,0,0    
    for robot in robots :
        print(robot[0])
        if robot[0][0]<LARGEUR//2 and robot[0][1]<HAUTEUR//2:
            a += 1
        if robot[0][0]<LARGEUR//2 and robot[0][1]>HAUTEUR//2:
            b += 1
        if robot[0][0]>LARGEUR//2 and robot[0][1]<HAUTEUR//2:
            c += 1
        if robot[0][0]>LARGEUR//2 and robot[0][1]>HAUTEUR//2:
            d += 1                        
    print(a,b,c,d)
    return a * b * c * d

def enigme_day14_second_part(chemin):
    somme = 0
    robots = []
    with open(chemin, "r") as fichier:
        for ligne in fichier:
            robot = []
            p_data,v_data = ligne.strip().split(' ')
            robot.append(list(map(int,p_data[2:].split(','))))
            robot.append(list(map(int,v_data[2:].split(','))))
            robots.append(robot)
    print(robots)
    i = 0
    while True:
        for robot in robots :
            position,vitesse = robot
            position[0]=(position[0]+vitesse[0])%LARGEUR
            position[1]=(position[1]+vitesse[1])%HAUTEUR
        # imprime
        tab=[["."]*LARGEUR for _ in range(HAUTEUR)]
        for robot in robots : 
            tab[robot[0][1]][robot[0][0]]="#"
        res = ""
        trouve = 0
        for line in tab :
            res += "".join(line)+"\n"
            for c in range(len(line)//5):
                if "".join(line[c*5:(c*5)+5])=="#####" :
                    trouve += 1
        if trouve>4 :
            print(i,res)
        i +=1 
    return 0

def test_enigme_day14():
    #assert enigme_day14_first_part("input-14-test2.txt") == 12
    assert enigme_day14_second_part("input-14-test2.txt") == 12


if __name__ == "__main__":
    #print(enigme_day14_first_part("input-14.txt"))
    print(enigme_day14_second_part("input-14.txt"))
