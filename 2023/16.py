map = {} # map de tuple !!!
nb_lignes = 0
nb_colonnes = 0

a_traiter = []

class Case:

    num_ligne:int
    num_colonne:int
    element:str
    energized:bool=False
    direction_deja_eu:list[tuple]

    def __init__(self,element,num_ligne,num_colonne):
        self.element = element
        self.num_colonne=num_colonne
        self.num_ligne=num_ligne
        self.direction_deja_eu=[]

    def __str__(self):
        if self.energized :
            return "#"
        else :
            return f"{self.element}"    
        
    def __repr__(self):
        if self.energized :
            return f"\033[0;31m{self.element}\033[0;m"
        else :
            return f"{self.element}"            

class Rayon:
    position = (0,0)
    direction = (0,0)

    def __init__(self,position,direction):
        self.position=position
        self.direction=direction

    def __str__(self):
        return f"{self.position} : {self.direction}"

    def __repr__(self):
        return f"{self.position} : {self.direction}"

    def traite(self):
        if self.position[0]<0 or self.position[1]<0 or self.position[0]>=nb_lignes or self.position[1]>=nb_colonnes:
            return
        case = map[self.position]
        if case.energized and self.direction in case.direction_deja_eu :
            return
        case.energized = True
        case.direction_deja_eu.append(self.direction)
        
        if case.element=='.':
            a_traiter.append(Rayon((self.position[0]+self.direction[0],self.position[1]+self.direction[1]),self.direction))
        if case.element=="-" :
            if self.direction[1]==1 or self.direction[1]==-1:
                a_traiter.append(Rayon((self.position[0]+self.direction[0],self.position[1]+self.direction[1]),self.direction))
            if self.direction[0]==1 or self.direction[0]==-1:
                a_traiter.append(Rayon((self.position[0],self.position[1]+1),(0,1)))
                a_traiter.append(Rayon((self.position[0],self.position[1]-1),(0,-1)))    
        if case.element=="|" :
            if self.direction[1]==1 or self.direction[1]==-1:
                a_traiter.append(Rayon((self.position[0]+1,self.position[1]),(1,0)))
                a_traiter.append(Rayon((self.position[0]-1,self.position[1]),(-1,0)))
            if self.direction[0]==1 or self.direction[0]==-1:
                a_traiter.append(Rayon((self.position[0]+self.direction[0],self.position[1]+self.direction[1]),self.direction))
        if  case.element=="\\":
            if self.direction[1]==1:
                a_traiter.append(Rayon((self.position[0]+1,self.position[1]),(1,0)))
            if self.direction[1]==-1:
                a_traiter.append(Rayon((self.position[0]-1,self.position[1]),(-1,0)))            
            if self.direction[0]==-1:
                a_traiter.append(Rayon((self.position[0],self.position[1]-1),(0,-1)))
            if self.direction[0]==1:
                a_traiter.append(Rayon((self.position[0],self.position[1]+1),(0,1)))                
        if  case.element=="/":
            if self.direction[1]==1:
                a_traiter.append(Rayon((self.position[0]-1,self.position[1]),(-1,0)))
            if self.direction[1]==-1:
                a_traiter.append(Rayon((self.position[0]+1,self.position[1]),(1,0)))    
            if self.direction[0]==-1:
                a_traiter.append(Rayon((self.position[0],self.position[1]+1),(0,1)))
            if self.direction[0]==1:
                a_traiter.append(Rayon((self.position[0],self.position[1]-1),(0,-1)))    

def compte():
    somme = 0
    for num_ligne in range(nb_lignes):
        for num_colonne in range(nb_colonnes):
            if map[(num_ligne,num_colonne)].energized:
                somme += 1
    return somme

def imprime_map():
    for num_ligne in range(nb_lignes):
        ligne = []
        for num_colonne in range(nb_colonnes):
            ligne.append(map[(num_ligne,num_colonne)])
        print(ligne)

def reinitialise_map():
    for num_ligne in range(nb_lignes):
        for num_colonne in range(nb_colonnes):
            map[(num_ligne,num_colonne)].energized=False
            map[(num_ligne,num_colonne)].direction_deja_eu=[]

def enigme_day16(chemin):
    global nb_lignes,nb_colonnes
    with open(chemin,'r') as fichier :
        for num_ligne,ligne in enumerate(fichier) :
            for num_colonne,element in enumerate(ligne.strip()):
                map[(num_ligne,num_colonne)]=Case(element,num_ligne,num_colonne)
                nb_lignes,nb_colonnes=num_ligne+1,num_colonne+1
    max = 0
    for i in range(nb_lignes):                
        a_traiter.append(Rayon((i,0),(0,1)))
        while len(a_traiter)>0 :
            rayon = a_traiter.pop(0)
            rayon.traite()
        if max<compte():
            max=compte()
        reinitialise_map()
    for i in range(nb_lignes):                
        a_traiter.append(Rayon((i,nb_colonnes),(0,-1)))
        while len(a_traiter)>0 :
            rayon = a_traiter.pop(0)
            rayon.traite()
        if max<compte():
            max=compte()
        reinitialise_map()    
    for i in range(nb_colonnes):                
        a_traiter.append(Rayon((0,i),(1,0)))
        while len(a_traiter)>0 :
            rayon = a_traiter.pop(0)
            rayon.traite()
        if max<compte():
            max=compte()
        reinitialise_map()    
    for i in range(nb_colonnes):                
        a_traiter.append(Rayon((nb_lignes,i),(-1,0)))
        while len(a_traiter)>0 :
            rayon = a_traiter.pop(0)
            rayon.traite()
        if max<compte():
            max=compte()  
        reinitialise_map()              
    return max




def test_enigme_day16():
    assert enigme_day16("input-16-test.txt") == 46


if __name__ == "__main__" :
    print(enigme_day16("input-16.txt"))