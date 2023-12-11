
a_traiter = []
map = []

class Case:

    ligne : int
    colonne : int
    distance : int
    value : str

    def __init__(self,ligne,colonne,value,distance=None):
        self.ligne = ligne
        self.colonne = colonne
        self.value = value
        self.distance=-1
        if value == 'S':
            self.distance = 0
            a_traiter.append(self)

    def __repr__(self):
        return f'[{self.ligne}/{self.colonne}] {self.value} ({self.distance})'

def trouve_voisin(element):
    print(element.value,element.ligne,element.colonne,element,element.distance)
    # recherche en haut
    if element.ligne>0 and (element.value=="|" or element.value=="J" or element.value=="L" or element.value=="S")  :
        if map[element.ligne-1][element.colonne].value=="|" or map[element.ligne-1][element.colonne].value=="F" or map[element.ligne-1][element.colonne].value=="7":
            case_nord = map[element.ligne-1][element.colonne]
            print("case nord",case_nord)
            if case_nord.distance<0 :
                case_nord.distance = element.distance +1
                a_traiter.append(case_nord)
    # recherche en bas
    if element.ligne<len(map) and (element.value=="|" or element.value=="F" or element.value=="7" or element.value=="S")  :
        if map[element.ligne+1][element.colonne].value=="|" or map[element.ligne+1][element.colonne].value=="J" or map[element.ligne+1][element.colonne].value=="L":
            case_sud = map[element.ligne+1][element.colonne]
            print("case sud",case_sud)
            if case_sud.distance<0 :
                case_sud.distance = element.distance +1
                a_traiter.append(case_sud)
    # recherche ouest
    if element.colonne>0 and (element.value=="-" or element.value=="J" or element.value=="7" or element.value=="S")  :
        if map[element.ligne][element.colonne-1].value=="-" or map[element.ligne][element.colonne-1].value=="F" or map[element.ligne][element.colonne-1].value=="L":
            case_ouest = map[element.ligne][element.colonne-1]
            print("case ouest",case_ouest)
            if case_ouest.distance<0 :
                case_ouest.distance = element.distance +1
                a_traiter.append(case_ouest)
    # recherche est
    if element.colonne<len(map[0]) and (element.value=="-" or element.value=="F" or element.value=="L" or element.value=="S")  :
        if map[element.ligne][element.colonne+1].value=="-" or map[element.ligne][element.colonne+1].value=="J" or map[element.ligne][element.colonne+1].value=="7":
            case_est = map[element.ligne][element.colonne+1]
            #print("case est",case_est)
            if case_est.distance<0 :
                case_est.distance = element.distance +1
                a_traiter.append(case_est)            

def enigme_day10(chemin):
    somme = 0
    with open(chemin,'r') as fichier :
        for num_ligne,ligne in enumerate(fichier) :
            ligne_case = []
            for num_colonne,colonne in enumerate(ligne.strip()):
                print(num_ligne,num_colonne,colonne)
                ligne_case.append(Case(num_ligne,num_colonne,colonne))
            #print(ligne_case)
            map.append(ligne_case)
    #print(a_traiter)
    max = 0
    while len(a_traiter)>0 :
        element = a_traiter.pop(0)
        if element.distance>0:
            max=element.distance
        trouve_voisin(element)
        print("a traiter : ",a_traiter)
    # affiche map:
    for ligne in map:
        print(ligne)
    return max

def test_enigme_day10():
    assert enigme_day10("input-10a-test.txt") == 8


if __name__ == "__main__" :
    print(enigme_day10("input-10.txt"))