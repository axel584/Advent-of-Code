import pytest 


workflows = {}
pieces = []


class Piece:
    x:int
    m:int
    a:int
    s:int

    etat:str="in"

    def __init__(self,x:int,m:int,a:int,s:int):
        self.x=int(x)
        self.m=int(m)
        self.a=int(a)
        self.s=int(s)

    def __str__(self):
        return f"x={self.x},m={self.m},a={self.a},s={self.s}"

    def somme(self):
        return self.x+self.m+self.a+self.s


class Rules:

    parametre:str
    operateur:str
    valeur:int
    sortie:str

    def __init__(self,parametre=None,operateur=None,valeur=0,sortie=None):
        self.parametre=parametre
        self.operateur=operateur
        self.valeur=int(valeur)
        self.sortie=sortie

    def __str__(self):
        if self.parametre:
            return f"{self.parametre}{self.operateur}{self.valeur}:{self.sortie}"
        else :
            return f"{self.sortie}"

    def apply(self,piece):
        if self.parametre:
            parametre_valeur = piece.__getattribute__(self.parametre)
            if self.operateur==">" and parametre_valeur>self.valeur :
                return self.sortie
            if self.operateur=="<" and parametre_valeur<self.valeur :
                return self.sortie                
        else :
            return self.sortie

class Workflow:
    name:str
    rules:list

    def __init__(self,name:str):
        self.name=name
        self.rules=[]

    def apply(self,p:Piece):
        for r in self.rules :
            sortie = r.apply(p)
            if sortie : 
                return sortie
        

def split(rule):
    parametre = ''
    operateur = ''
    valeur = ''
    sortie = ''
    i = 0
    while rule[i].isalpha():
        parametre += rule[i]
        i += 1
    operateur = rule[i]
    i += 1
    while rule[i].isdigit():
        valeur += rule[i]
        i += 1
    sortie = rule[i+1:]
    return parametre,operateur,valeur,sortie


def enigme_day19(chemin):
    global workflows
    has_blank_line = False
    with open(chemin,'r') as fichier :
        for ligne in fichier :
            ligne=ligne.strip()
            if ligne=="":
                has_blank_line=True
                continue
            if has_blank_line==False: # workflow
                nom_workflow = ligne[:ligne.find("{")]
                rules_workflow = ligne[ligne.find("{")+1:ligne.find("}")]
                w = Workflow(nom_workflow)
                for rule in rules_workflow.split(','):
                    if rule.find(":")>-1 :
                        parametre,operateur,valeur,sortie = split(rule)
                        r = Rules(parametre,operateur,valeur,sortie)
                    else : 
                        r = Rules(sortie=rule)
                    w.rules.append(r)
                workflows[nom_workflow]=w
            if has_blank_line==True : # piece
                ligne = ligne[1:-1]
                x,m,a,s = [e[e.find("=")+1:]for e in ligne.split(',')]
                p = Piece(x,m,a,s)
                pieces.append(p)
    somme = 0
    for p in pieces:
        etat = "in"
        while etat!="A" and etat!="R":
            etat = workflows[etat].apply(p)
        if etat=="A":
            somme += p.somme()
    return somme        








def test_enigme_day19():
    assert enigme_day19("input-19-test.txt") == 19114


if __name__ == "__main__" :
    print(enigme_day19("input-19.txt"))