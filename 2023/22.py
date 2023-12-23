carte = {}

briques = []

max_x,max_y,max_z = (0,0,0)

class Brique:

    nom : str
    blocs : list[(tuple)]
    hauteur_base:int

    def __init__(self,nom):
        self.nom=nom
        self.blocs = []

    def __str__(self):
        return f"{self.nom}:{self.blocs}({self.hauteur_base})"
    
    def __repr__(self):
        return f"{self.nom}:{self.blocs}({self.hauteur_base})"


    def calcule_hauteur_base(self):
        self.hauteur_base = min([bloc[2] for bloc in self.blocs])

    def a_vide_dessous(self):
        # recherche tous les blocs qui sont en bas de la figure
        for bloc in [bloc for bloc in self.blocs if bloc[2]==self.hauteur_base] :
            dessous = (bloc[0],bloc[1],bloc[2]-1)
            if dessous in carte or dessous[2]==0:
                return False
        return True

    def brique_dessus(self):
        hauteur_sommet = max([bloc[2] for bloc in self.blocs])
        briques_dessus = []
        for bloc in [bloc for bloc in self.blocs if bloc[2]==hauteur_sommet] :
            dessus = (bloc[0],bloc[1],bloc[2]+1)
            if dessus in carte:
                briques_dessus.append(carte[dessus])
        return list(set(briques_dessus))
    
    def brique_dessous(self):
        hauteur_base = min([bloc[2] for bloc in self.blocs])
        briques_dessous = []
        for bloc in [bloc for bloc in self.blocs if bloc[2]==hauteur_base] :
            dessous = (bloc[0],bloc[1],bloc[2]-1)
            if dessous in carte:
                briques_dessous.append(carte[dessous])
        return list(set(briques_dessous))
    
    def est_supprimable(self,verbose=False):
        briques_dessus = self.brique_dessus()
        if len(briques_dessus)==0 : 
            if verbose:
                print("0 brique dessus")
            return True
        for brique in briques_dessus:
            if verbose:
                print("dessus : ",brique," possede ",len(brique.brique_dessous())," briques dessous")
            if len(brique.brique_dessous())==1 :
                return False
        return True


    def descendre(self):
        while self.a_vide_dessous() :
            for bloc in self.blocs :
                del carte[bloc]
            nouvelles_positions = []
            for bloc in self.blocs :
                bloc = (bloc[0],bloc[1],bloc[2]-1)
                nouvelles_positions.append(bloc)
            self.blocs=nouvelles_positions
            self.hauteur_base -= 1
            for bloc in self.blocs :
                carte[bloc]=self


def imprime_carte(niveaux):
    i = 65 # A
    correspondance = {}
    for z in niveaux :
        for x in range(max_x+1):
            ligne = ''
            for y in range(max_y+1):
                if (x,y,z) in carte :
                    if carte[(x,y,z)].nom not in correspondance.keys() :
                        correspondance[carte[(x,y,z)].nom]=chr(i)
                        i += 1
                    if carte[(x,y,z)].est_supprimable() :
                        ligne += "\033[0;31m"+correspondance[carte[(x,y,z)].nom]+"\033[0;m"
                    else :
                        ligne += correspondance[carte[(x,y,z)].nom]
                else : 
                    ligne += '.'
            print(ligne)
        print()
    print(correspondance)
            

def enigme_day22(chemin):
    global max_x,max_y,max_z,carte
    with open(chemin,'r') as fichier :
        num_brique = 1
        for ligne in fichier :
            debut,fin=ligne.strip().split('~')
            b = Brique(str(num_brique))
            coord_debut = [int(x) for x in debut.split(',')]
            coord_fin = [int(x) for x in fin.split(',')]
            for x in range(coord_debut[0],coord_fin[0]+1):
                for y in range(coord_debut[1],coord_fin[1]+1):
                    for z in range(coord_debut[2],coord_fin[2]+1):
                        b.blocs.append((x,y,z))
                        carte[(x,y,z)]=b
                        if x>max_x:
                            max_x=x
                        if y>max_y:
                            max_y=y
                        if z>max_z:
                            max_z=z
            b.calcule_hauteur_base()                
            briques.append(b)   
            num_brique += 1
    briques.sort(key=lambda b:b.hauteur_base)
    for brique in briques :
        brique.descendre()
    briques.sort(key=lambda b:b.hauteur_base)
    # imprime_carte([100,101,102])  
    # for brique in briques : 
    #     if brique.nom=="1341":
    #         print(brique)
    #         brique.est_supprimable(verbose=True)
    res = 0
    for brique in briques :
        if brique.est_supprimable():
            res += 1
            print(brique)
    return res

def test_enigme_day22():
    assert enigme_day22("input-22-test.txt") == 5


if __name__ == "__main__" :
    print(enigme_day22("input-22.txt"))


