
a_traiter = []
map = []

class Case:

    ligne : int
    colonne : int
    distance : int
    value : str
    angle_haut_gauche = 'U' # Unknow / Inside / Outside
    angle_haut_droite = 'U'
    angle_bas_gauche = 'U'
    angle_bas_droite = 'U'

    def __init__(self,ligne,colonne,value,distance=None):
        self.ligne = ligne
        self.colonne = colonne
        self.value = value
        self.distance=-1
        if value == 'S':
            self.distance = 0
            a_traiter.append(self)

    def __str__(self):
        if self.value == '7' :
            return u'\u2510'
        return f'[{self.ligne}/{self.colonne}] {self.value} ({self.distance}) #{self.angle_haut_gauche}{self.angle_haut_droite}{self.angle_bas_gauche}{self.angle_bas_droite}#'

    def __repr__(self):
        return f'{self.value}'

def trouve_voisin(element):
    #print(element.value,element.ligne,element.colonne,element,element.distance)
    # recherche en haut
    if element.ligne>0 and (element.value=="|" or element.value=="J" or element.value=="L" or element.value=="S")  :
        if map[element.ligne-1][element.colonne].value=="|" or map[element.ligne-1][element.colonne].value=="F" or map[element.ligne-1][element.colonne].value=="7":
            case_nord = map[element.ligne-1][element.colonne]
            if case_nord.distance<0 :
                case_nord.distance = element.distance +1
                a_traiter.append(case_nord)
    # recherche en bas
    if element.ligne<len(map) and (element.value=="|" or element.value=="F" or element.value=="7" or element.value=="S")  :
        if map[element.ligne+1][element.colonne].value=="|" or map[element.ligne+1][element.colonne].value=="J" or map[element.ligne+1][element.colonne].value=="L":
            case_sud = map[element.ligne+1][element.colonne]
            if case_sud.distance<0 :
                case_sud.distance = element.distance +1
                a_traiter.append(case_sud)
    # recherche ouest
    if element.colonne>0 and (element.value=="-" or element.value=="J" or element.value=="7" or element.value=="S")  :
        if map[element.ligne][element.colonne-1].value=="-" or map[element.ligne][element.colonne-1].value=="F" or map[element.ligne][element.colonne-1].value=="L":
            case_ouest = map[element.ligne][element.colonne-1]
            if case_ouest.distance<0 :
                case_ouest.distance = element.distance +1
                a_traiter.append(case_ouest)
    # recherche est
    if element.colonne<len(map[0]) and (element.value=="-" or element.value=="F" or element.value=="L" or element.value=="S")  :
        if map[element.ligne][element.colonne+1].value=="-" or map[element.ligne][element.colonne+1].value=="J" or map[element.ligne][element.colonne+1].value=="7":
            case_est = map[element.ligne][element.colonne+1]
            if case_est.distance<0 :
                case_est.distance = element.distance +1
                a_traiter.append(case_est)            


def inverse(inout):
    if inout=='O':
        return 'I'
    else : 
        return 'O'

def trouve_inout(element):
    voisin_gauche = map[element.ligne-1][element.colonne].angle_bas_gauche
    voisin_droite = map[element.ligne-1][element.colonne].angle_bas_droite
    if element.value == '.' :
        element.angle_haut_gauche = voisin_gauche
        element.angle_haut_droite = voisin_gauche
        element.angle_bas_gauche = voisin_gauche
        element.angle_bas_droite = voisin_gauche        
    if element.value == '-':
        element.angle_haut_gauche = voisin_gauche
        element.angle_haut_droite = voisin_droite
        element.angle_bas_gauche = inverse(voisin_gauche)
        element.angle_bas_droite = inverse(voisin_gauche)
    if element.value == '|' or element.value == 'S': # dans mon jeu d'entree, le S relie la case du haut et du bas
        element.angle_haut_gauche = voisin_gauche
        element.angle_haut_droite = voisin_droite
        element.angle_bas_gauche = voisin_gauche
        element.angle_bas_droite = voisin_droite
    if element.value == 'F':
        element.angle_haut_gauche = voisin_gauche
        element.angle_haut_droite = voisin_droite
        element.angle_bas_gauche = voisin_gauche
        element.angle_bas_droite = inverse(voisin_droite)
    if element.value == 'J':
        element.angle_haut_gauche = voisin_gauche
        element.angle_haut_droite = voisin_droite
        element.angle_bas_gauche = inverse(voisin_gauche)
        element.angle_bas_droite = voisin_droite
    if element.value == '7':
        element.angle_haut_gauche = voisin_gauche
        element.angle_haut_droite = voisin_droite
        element.angle_bas_gauche = inverse(voisin_gauche)
        element.angle_bas_droite = voisin_droite
    if element.value == 'L':
        element.angle_haut_gauche = voisin_gauche
        element.angle_haut_droite = voisin_droite
        element.angle_bas_gauche = voisin_gauche
        element.angle_bas_droite = inverse(voisin_droite)
    if element.colonne==6 :    
        print("trouve inout : ",element)

def enigme_day10(chemin):
    with open(chemin,'r') as fichier :
        for num_ligne,ligne in enumerate(fichier) :
            ligne_case = []
            for num_colonne,colonne in enumerate(ligne.strip()):
                #print(num_ligne,num_colonne,colonne)
                ligne_case.append(Case(num_ligne,num_colonne,colonne))
            map.append(ligne_case)
    #print(a_traiter)
    maximum = 0
    while len(a_traiter)>0 :
        element = a_traiter.pop(0)
        if element.distance>0:
            maximum=element.distance
        trouve_voisin(element)
    print("solution premiere partie :",maximum)
    # retire les élements qui ne sont pas dans la boucle
    for ligne in map:
        for case in ligne :
            if case.distance==-1:
                case.value='.'  
    # calcule les angles  
    for element in map[0]:
        element.angle_haut_gauche,element.angle_haut_droite,element.angle_bas_gauche,element.angle_bas_droite = ('O','O','O','O')
    for ligne in map[1:]:
        for element in ligne :
            trouve_inout(element)
    # compte les intérieurs
    nb_interieur = 0
    for ligne in map:
        for case in ligne :
            if case.value=='.' and case.angle_haut_gauche == 'I':
                nb_interieur += 1
                case.value='I'
            if case.value=='.' and case.angle_haut_gauche == 'O':
                case.value='O'                
    # affiche map:
    for ligne in map:
        print(''.join([case.value for case in ligne]))
    print(nb_interieur)
    

def test_enigme_day10():
    assert enigme_day10("input-10a-test.txt") == 8


if __name__ == "__main__" :
    print(enigme_day10("input-10.txt"))