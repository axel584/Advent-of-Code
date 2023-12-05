
import pytest
from typing import List


class Plage():
    debut : int
    fin : int
    diff : int

    def is_in(self,value):
        return value>=self.debut and value<=self.fin
    
    def convert(self,value):
        return value+self.diff
    
    def __init__(self,destination,source,longueur):
        self.debut = source
        self.fin = source+longueur
        self.diff = destination-source
    
    def __str__(self):
        return f"debut : {self.debut} / fin : {self.fin} / diff : {self.diff}"

    def __repr__(self):
        return f"debut : {self.debut} / fin : {self.fin} / diff : {self.diff}"

class Convertisseur():

    def ajoute(self,plage):
        self.plages.append(plage)

    def __init__(self):
        self.plages = []

    def convert(self,value):
        for plage in self.plages:
            if plage.is_in(value):
                return plage.diff+value
        return value

    def __str__(self):
        for plage in self.plages:
            print(plage)

    def __repr__(self):
        representation = ''
        for plage in self.plages:
            representation += str(plage)+"\n"
        return representation

convertisseurs = {}
seeds = []
locations = []
#order_des_convertisseurs # dictionnaire ?

def enigme_day05(chemin):
    nom_map = ""
    with open(chemin,'r') as fichier :
        for ligne in [i.strip() for i in fichier] :
            #print(ligne)
            #print("----------")
            if ligne.startswith("seeds:"):
                seeds = [int(i) for i in ligne[ligne.find(':')+1:].split()]
                print("seeds",seeds)
            elif ligne=="" :
                nom_map=""
            elif ligne.endswith("map:"):
                #print("map")
                nom_map=ligne[:ligne.find(' ')]
                #print(nom_map)
                convertisseurs[nom_map]=Convertisseur()
            else :
                destination,source,longueur = [int(i) for i in ligne.split()]
                #print(destination,source,longueur)
                p = Plage(destination,source,longueur)
                convertisseurs[nom_map].ajoute(p)
    for id in seeds :
        id = convertisseurs["seed-to-soil"].convert(id)
        #print(id)
        id = convertisseurs["soil-to-fertilizer"].convert(id)
        id = convertisseurs["fertilizer-to-water"].convert(id)
        id = convertisseurs["water-to-light"].convert(id)
        id = convertisseurs["light-to-temperature"].convert(id)
        id = convertisseurs["temperature-to-humidity"].convert(id)
        id = convertisseurs["humidity-to-location"].convert(id)
        #print(id)
        locations.append(id)
    #print(locations)    
    return min(locations)

def enigme_day05_second_part(chemin):
    nom_map = ""
    minimum = 9999999999999999999999
    with open(chemin,'r') as fichier :
        for ligne in [i.strip() for i in fichier] :
            #print(ligne)
            #print("----------")
            if ligne.startswith("seeds:"):
                seeds = [int(i) for i in ligne[ligne.find(':')+1:].split()]
                #print(seeds)
            elif ligne=="" :
                nom_map=""
            elif ligne.endswith("map:"):
                #print("map")
                nom_map=ligne[:ligne.find(' ')]
                #print(nom_map)
                convertisseurs[nom_map]=Convertisseur()
            else :
                destination,source,longueur = [int(i) for i in ligne.split()]
                #print(destination,source,longueur)
                p = Plage(destination,source,longueur)
                convertisseurs[nom_map].ajoute(p)
    #print("seeds",seeds,seeds[::2])            
    for i,id in enumerate(seeds[::2]) :
        #print("seed / 2 :",i,id)
        fin_seed = id+seeds[(i*2)+1]
        #print("intervale",fin_seed)
        for id in range(id,fin_seed):
            #print(id)
            id = convertisseurs["seed-to-soil"].convert(id)
            id = convertisseurs["soil-to-fertilizer"].convert(id)
            id = convertisseurs["fertilizer-to-water"].convert(id)
            id = convertisseurs["water-to-light"].convert(id)
            id = convertisseurs["light-to-temperature"].convert(id)
            id = convertisseurs["temperature-to-humidity"].convert(id)
            id = convertisseurs["humidity-to-location"].convert(id)
            #print(id)
            if id<minimum : 
                minimum = id
                print(minimum)
    return minimum

def test_convert():
    convertisseur = Convertisseur()
    plage1=Plage(50,98,2)
    convertisseur.ajoute(plage1)
    plage2=Plage(52,50,48)
    convertisseur.ajoute(plage2)

    assert convertisseur.convert(49)==49
    assert convertisseur.convert(50)==52
    assert convertisseur.convert(97)==99
    assert convertisseur.convert(98)==50
    assert convertisseur.convert(99)==51


def test_enigme_day05():
    assert enigme_day05("input-05a-test.txt") == 35

def test_enigme_day05_second_part():
    assert enigme_day05_second_part("input-05a-test.txt") == 46

if __name__ == "__main__" :
    print(enigme_day05_second_part("input-05.txt"))