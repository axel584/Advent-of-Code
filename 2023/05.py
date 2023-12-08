
import pytest
from typing import List


class Plage():
    debut_source : int
    fin_source : int
    diff : int
    debut_destination : int
    fin_destination : int

    def is_in(self,value):
        return value>=self.debut_source and value<=self.fin_source
    
    def is_from(self,value):
        return value>=self.debut_destination and value<self.fin_destination

    def convert(self,value):
        #print("convert value diff",value,self.diff)
        return value+self.diff
    
    def anticonvert(self,value):
        #print("value / diff : ",value,self.diff)
        return value-self.diff    
    
    def __init__(self,destination,source,longueur):
        self.debut_source = source
        self.fin_source = source+longueur
        self.diff = destination-source
        self.debut_destination = destination
        self.fin_destination = destination+longueur
    
    def __str__(self):
        return f"debut source : {self.debut_source} / fin source : {self.fin_source} / diff : {self.diff} / debut destination : {self.debut_destination} / fin destination : {self.fin_destination} "

    def __repr__(self):
        return f"debut source : {self.debut_source} / fin source : {self.fin_source} / diff : {self.diff} / debut destination : {self.debut_destination} / fin destination : {self.fin_destination} "

class Convertisseur():

    def ajoute(self,plage):
        self.plages.append(plage)

    def __init__(self):
        self.plages = []

    def convert(self,value):
        for plage in self.plages:
            if plage.is_in(value):
                return plage.convert(value)
        return value
    
    def anticonvert(self,value):
        #print("anticonvert ",value)
        for plage in self.plages:
            #print("anticonvert, plage ",plage)
            if plage.is_from(value):
                #print("is from : ",plage.anticonvert(value))
                return plage.anticonvert(value)
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
all_seeds = []
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
                #print("p",p)
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


def search_from(id):
    id = convertisseurs["humidity-to-location"].anticonvert(id)
    id = convertisseurs["temperature-to-humidity"].anticonvert(id)
    id = convertisseurs["light-to-temperature"].anticonvert(id)
    id = convertisseurs["water-to-light"].anticonvert(id)
    id = convertisseurs["fertilizer-to-water"].anticonvert(id)
    id = convertisseurs["soil-to-fertilizer"].anticonvert(id)
    id = convertisseurs["seed-to-soil"].anticonvert(id)
    return id

def search_to(id):
    id = convertisseurs["seed-to-soil"].convert(id)
    id = convertisseurs["soil-to-fertilizer"].convert(id)
    id = convertisseurs["fertilizer-to-water"].convert(id)
    id = convertisseurs["water-to-light"].convert(id)
    id = convertisseurs["light-to-temperature"].convert(id)
    id = convertisseurs["temperature-to-humidity"].convert(id)
    id = convertisseurs["humidity-to-location"].convert(id)
    return id

def is_in_seeds(value,all_seeds):
    for i,debut_seed in enumerate(all_seeds[::2]) :
        fin_seed = debut_seed+all_seeds[(i*2)+1]
        if value>=debut_seed and value<=fin_seed :
            return True
    return False

def enigme_day05_second_part(chemin):
    nom_map = ""
    with open(chemin,'r') as fichier :
        for ligne in [i.strip() for i in fichier] :
            if ligne.startswith("seeds:"):
                all_seeds = [int(i) for i in ligne[ligne.find(':')+1:].split()]
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
    id = 0
    while True :
        id_from = search_from(id)
        if is_in_seeds(id_from,all_seeds):
            return id
        id += 1

@pytest.mark.skip()
def test_convert():
    convertisseur = Convertisseur()
    plage1=Plage(50,98,2)
    #print("plage1",plage1)
    convertisseur.ajoute(plage1)
    plage2=Plage(52,50,48)
    #print("plage2",plage2)
    convertisseur.ajoute(plage2)

    assert convertisseur.convert(49)==49
    assert convertisseur.convert(50)==52
    assert convertisseur.convert(97)==99
    assert convertisseur.convert(98)==50
    assert convertisseur.convert(99)==51

    assert convertisseur.anticonvert(49)==49
    assert convertisseur.anticonvert(52)==50
    assert convertisseur.anticonvert(99)==97
    assert convertisseur.anticonvert(50)==98
    assert convertisseur.anticonvert(51)==99

@pytest.mark.skip()
def test_enigme_day05():
    assert enigme_day05("input-05a-test.txt") == 35

def test_enigme_day05_second_part():
    assert enigme_day05_second_part("input-05a-test.txt") == 46

if __name__ == "__main__" :
    print(enigme_day05_second_part("input-05.txt"))