carte = {}
max_x,max_y = (0,0)
chemins = []


HAUT = (-1,0)
BAS = (1,0)
GAUCHE = (0,-1)
DROITE = (0,1)

direction_map = {'R':DROITE,'U':HAUT,'L':GAUCHE,'D':BAS}

class Chemin:
    positions : list[(tuple)]

    def __init__(self):
        self.positions=[]

    def __str__(self):
        return f"{len(self.positions)} : {self.positions[-1]}"

    def __repr__(self):
        return f"{len(self.positions)} : {self.positions[-1]}"

    def avance(self):
        derniere_position = self.positions[-1]
        peut_continue = True
        while peut_continue:
            positions_possible = []
            for nom_direction,direction in direction_map.items():
                #print("direction",derniere_position,direction)
                nouvelle_position = (derniere_position[0]+direction[0],derniere_position[1]+direction[1])
                if nouvelle_position not in carte :
                    continue
                if carte[nouvelle_position]=="#":
                    continue
                if nouvelle_position in self.positions:
                    continue
                if nouvelle_position==(max_x,max_y-1):
                    solution = []
                    solution.append(nouvelle_position)
                    return solution
                #print("direction carte",nom_direction,direction,carte[nouvelle_position],nouvelle_position)
                if nom_direction=="D" and carte[nouvelle_position]!="v" and carte[nouvelle_position]!=".":
                    continue
                if nom_direction=="U" and carte[nouvelle_position]!="^" and carte[nouvelle_position]!=".":
                    continue
                if nom_direction=="R" and carte[nouvelle_position]!=">" and carte[nouvelle_position]!=".":
                    continue
                if nom_direction=="L" and carte[nouvelle_position]!="<" and carte[nouvelle_position]!=".":
                    continue
                positions_possible.append(nouvelle_position)
            if len(positions_possible)>1 :
                peut_continue = False
                return positions_possible
            elif len(positions_possible)==0: # cul de sac
                return None
            else :
                self.positions.append(positions_possible[0])
                derniere_position = positions_possible[0] 

    def imprime(self):
        for x in range(max_x+1):
            ligne = ''
            for y in range(max_y+1):
                if (x,y) in self.positions :
                    ligne += "O"
                else :
                    ligne += carte[(x,y)]
            print(ligne)
        print("*"*(max_y+1))

def imprime_carte():
    for x in range(max_x+1):
        ligne = ''
        for y in range(max_y+1):
            ligne += carte[(x,y)]
        print(ligne)

def enigme_day23(chemin_fichier):
    global max_x,max_y,max_z,carte
    with open(chemin_fichier,'r') as fichier :
        for num_ligne,ligne in enumerate(fichier) :
            for num_colonne,element in enumerate(ligne.strip()):
                carte[(num_ligne,num_colonne)]=element
                max_x,max_y = num_ligne,num_colonne
    #imprime_carte()
    a_traiter = []
    c = Chemin()
    c.positions.append((0,1))
    a_traiter.append(c)
    max = 0
    while len(a_traiter)>0:
        c = a_traiter.pop(0)
        #print("on va traiter ",c," et il restera ",len(a_traiter))
        chemins_possibles = c.avance()
        #print("chemins possibles: ",chemins_possibles)
        if chemins_possibles:
            if len(chemins_possibles)==1 :
                #print("trouve sortie",len(c.positions))
                nombre_de_pas = len(c.positions)
                if max<nombre_de_pas:
                    max=nombre_de_pas
                    #print("trouve un nouveau max :",max)
                #print("a traiter",a_traiter)
                continue
            for choix in chemins_possibles:
                #print("choix",choix)
                nouveau_choix = Chemin()
                nouveau_choix.positions = list(c.positions)
                nouveau_choix.positions.append(choix)
                #print("append ",nouveau_choix,nouveau_choix.positions)
                a_traiter.append(nouveau_choix)
        #c.imprime()
        #print("reste ",len(a_traiter)," choix à essayer : ",a_traiter)
    #print(max_x,max_y)
    return max


def test_enigme_day23():
    assert enigme_day23("input-23-test.txt") == 94


if __name__ == "__main__" :
    print(enigme_day23("input-23.txt"))