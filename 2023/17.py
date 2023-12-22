from copy import copy

map = {} # map de tuple !!!
nb_lignes = 0
nb_colonnes = 0

a_traiter = []


HAUT = (-1,0)
BAS = (1,0)
GAUCHE = (0,-1)
DROITE = (0,1)

minimum = 999999999

class Choix:

    somme :int=0
    direction=None
    meme_direction:int=0
    position:tuple=(0,0)
    chemin=[]
    distance_de_fin:int

    def __init__(self,position:tuple,direction:tuple,somme:int,meme_direction:int,precedent):
        self.somme=somme
        self.position=position
        self.direction=direction
        self.meme_direction=meme_direction
        self.distance_de_fin = abs(nb_lignes-position[0])+abs(nb_colonnes-position[1])
        self.precedent=precedent
        

    def traite(self):
        global a_traiter
        #print("traite ",self,len(a_traiter))
        #print("distance de la fin ",self.distance_de_fin)
        #print("nombre de solution restante a tester : ",len(a_traiter))
        if self.position[0]==nb_lignes-1 and self.position[1]==nb_colonnes-1:
            #print("derniere case : ",self.somme + map[self.position])
            return self.somme + map[self.position]
        if self.position[0]<0 or self.position[1]<0 or self.position[0]>=nb_lignes or self.position[1]>=nb_colonnes:
            #print("hors zone")
            return        
        if self.meme_direction>=3:
            #print("trois fois dans la meme direction ",self.chemin)
            return
        self.somme += map[self.position]
        # meme direction : 
        
        if self.meme_direction<3 :
            position = (self.position[0]+self.direction[0],self.position[1]+self.direction[1])
            if position[0]>=0 and position[1]>=0 and position[0]<nb_lignes and position[1]<nb_colonnes:
                if position[0]==nb_lignes-1 and position[1]==nb_colonnes-1:
                    return self.somme                
                if self.pas_deja_test(position) :
                    if map[position]+self.somme<minimum :
                        #print("tout droit ajoute ",map[position])
                        tout_droit = Choix((self.position[0]+self.direction[0],self.position[1]+self.direction[1]),self.direction,self.somme,self.meme_direction+1,self)
                        a_traiter.append(tout_droit)
        # tourne à gauche (sens antihoraire)
        direction = self.tourne_antihoraire()
        position = (self.position[0]+direction[0],self.position[1]+direction[1])
        if self.pas_deja_test(position) :
            if position[0]>=0 and position[1]>=0 and position[0]<nb_lignes and position[1]<nb_colonnes:
                if position[0]==nb_lignes-1 and position[1]==nb_colonnes-1:
                    return self.somme
                if map[position]+self.somme<minimum :
                    #print("gauche ajoute : ",map[position])
                    gauche = Choix(position,direction,self.somme,0,self)
                    a_traiter.append(gauche)
        # tourne à droite (sens horaire)
        direction = self.tourne_horaire()
        position = (self.position[0]+direction[0],self.position[1]+direction[1])
        if self.pas_deja_test(position) :
            if position[0]>=0 and position[1]>=0 and position[0]<nb_lignes and position[1]<nb_colonnes:
                if position[0]==nb_lignes-1 and position[1]==nb_colonnes-1:
                    return self.somme                
                if map[position]+self.somme<minimum :
                    #print("droite ajoute : ",map[position])
                    droite = Choix(position,direction,self.somme,0,self)
                    a_traiter.append(droite)
        return None

    def __str__(self):
        chemin_chaine = ''
        precedent = self.precedent
        while precedent:
            chemin_chaine = str(map[precedent.position])+chemin_chaine
            precedent = precedent.precedent
        return f"{self.position} : {map[self.position]} (s:{self.somme}/r:{self.distance_de_fin}) - {chemin_chaine}"
    
    def __repr__(self):
        chemin_chaine = ''
        precedent = self.precedent
        while precedent:
            chemin_chaine = str(map[precedent.position])+chemin_chaine
            precedent = precedent.precedent
        return f"{self.position} : {map[self.position]} (s:{self.somme}/r:{self.distance_de_fin}) - {chemin_chaine}"
    
    def tourne_horaire(self):
        if self.direction==HAUT :
            return DROITE
        if self.direction==DROITE :
            return BAS
        if self.direction==BAS :
            return GAUCHE
        if self.direction==GAUCHE:
            return HAUT        

    def tourne_antihoraire(self):
        if self.direction==HAUT :
            return GAUCHE
        if self.direction==GAUCHE :
            return BAS
        if self.direction==BAS :
            return DROITE
        if self.direction==DROITE:
            return HAUT

    def pas_deja_test(self,position):
        chemin = []
        precedent = self
        while precedent :
            chemin.append(precedent.position)
            precedent = precedent.precedent        
        return position not in chemin



def imprime_map(element=None):
    chemin = []
    precedent = element
    while precedent :
        chemin.append(precedent.position)
        precedent = precedent.precedent
    #print("chemin dans imprime map",chemin)
    for num_ligne in range(nb_lignes):
        ligne = ''
        for num_colonne in range(nb_colonnes):
            if (num_ligne,num_colonne) in chemin :
                ligne += "\033[0;31m"+str(map[(num_ligne,num_colonne)])+"\033[0;m"
            else :
                ligne += str(map[(num_ligne,num_colonne)])
        print(ligne)

def meilleure_choix():
    global a_traiter
    meilleur = a_traiter[0]
    indice_meilleur = 0
    for indice,element in enumerate(a_traiter):
        if (element.distance_de_fin*5)+element.somme<(meilleur.distance_de_fin*5)+meilleur.somme : 
            meilleur=element
            indice_meilleur=indice
    return a_traiter.pop(indice_meilleur)


def enigme_day17(chemin):
    global nb_lignes,nb_colonnes,a_traiter,minimum
    with open(chemin,'r') as fichier :
        for num_ligne,ligne in enumerate(fichier) :
            for num_colonne,element in enumerate(ligne.strip()):
                map[(num_ligne,num_colonne)]=int(element)
                nb_lignes,nb_colonnes=num_ligne+1,num_colonne+1
    imprime_map()
    droite = Choix((0,1),DROITE,0,0,None)
    a_traiter.append(droite)
    bas = Choix((1,0),BAS,0,0,None)
    a_traiter.append(bas)
    i = 0
    minimum = 999999
    while len(a_traiter)>0:
        i += 1
        possibilite = meilleure_choix()
        solution = possibilite.traite()
        if solution :
            if minimum>solution :
                minimum = solution
                print("minimum trouve : ",minimum,possibilite,len(a_traiter))
                a_traiter = [choix for choix in a_traiter if choix.somme<minimum]
                imprime_map(possibilite)
    return minimum
        


def test_enigme_day17():
    assert enigme_day17("input-17-test.txt") == 102


if __name__ == "__main__" :
    print(enigme_day17("input-17-test.txt"))