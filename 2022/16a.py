import re
from enum import Enum
from typing import TypeVar, Optional, Generic


NB_MINUTES = 30
class Valve():

    nom:str = ''
    taux:int = 0


    def __init__(self,nom,taux,chemins) :
        self.nom = nom
        self.taux = taux
        self.chemins = chemins

    def __str__(self):
        return f'{self.nom} taux {self.taux} vers {self.chemins}'

    def __repr__(self):
        return f'{self.nom} taux {self.taux} vers {self.chemins}'        

class Action(Enum):
    MOVE = 1
    OPEN = 2
    STAY = 1 
    
class Etat(Enum):
    CLOSE =1
    OPEN = 2

class Step():

    def __init__(self,action:Action=None,minutes:int=0,current_valve:str=None):
        self.action = action
        self.minutes = minutes
        self.currentValve = current_valve
        self.liste_valves_ouvertes : list[str] = []
        self.minutes:int=minutes
        self.pression_cumul:int=0
        self.pression_vannes_ouvertes:int=0
        self.chemin='' 

    def __str__(self):
        return f'{self.action} / {self.minutes} min / valve : {self.currentValve} / pression {self.pression_vannes_ouvertes}:{self.pression_cumul} / chemin {self.chemin} / vanne ouverte {self.liste_valves_ouvertes}'

    def __repr__(self):
        return self.__str__()

p = re.compile(r'Valve ([A-Z]+) has flow rate=([-0-9]+); tunnels? leads? to valves? (.+)')

liste_valves : dict[str,Valve] = {}
liste_step : list[Step] = []
somme_total_valve = 0
maximum = 0

for line in open('input16.txt').readlines():
    line = line.strip()
    #print(line)
    m = p.search(line)
    #print(m)
    taux = int(m.group(2))
    somme_total_valve += taux
    v = Valve(m.group(1),taux,[x for x in m.group(3).split(', ')])
    #print(v)
    liste_valves[v.nom]=v

print("total des vales : ",somme_total_valve)
#print(liste_valves)

def calculePression(valves_ouvertes : list[Valve]):
    somme = 0
    for valve in valves_ouvertes:
        somme += liste_valves[valve].taux
    #print("total pression :",somme)    
    return somme


def listePossibilite(s:Step)->list[Step]:
    # if s.chemin.startswith('AA>DD+>CC>BB'):
    #     log = True
    # else :
    #     log = False
    log = False
    if log :    
        print("TRAITE",s)
    
    if s.minutes>=NB_MINUTES :
        return
    nb_minutes_restantes = NB_MINUTES - s.minutes
    # Cas ou on n'arriverait pas a faire mieux, meme en ouvrant toutes les valves instantanements
    # print("minutes restantes * sommes total : ",nb_minutes_restantes*somme_total_valve)
    # print("maximum",maximum)
    if ((nb_minutes_restantes*somme_total_valve) + s.pression_cumul) < maximum :
        return
    v = liste_valves[s.currentValve]
    if v.nom not in s.liste_valves_ouvertes and v.taux!=0:
        # on choisi d'ouvir la valve
        nouveau_step_open = Step()
        nouveau_step_open.minutes = s.minutes + 1
        nouveau_step_open.action=Action.OPEN
        nouveau_step_open.chemin = s.chemin + "+" 
        nouveau_step_open.currentValve = v.nom if v!=None else 'AA'
        #print("OPEN avant liste valve ouverte ",s)
        nouveau_step_open.liste_valves_ouvertes = s.liste_valves_ouvertes.copy()
        nouveau_step_open.liste_valves_ouvertes.append(v.nom)
        #print("OPEN apres liste valve ouverte ",nouveau_step_open)
        #print(v.taux)
        nouveau_step_open.pression_vannes_ouvertes = s.pression_vannes_ouvertes + v.taux
        nouveau_step_open.pression_cumul = s.pression_cumul + s.pression_vannes_ouvertes
        #print("nouveauStep pressionCumule : ",nouveauStep.pression_cumul)
        if log:
            print("ajoute ",nouveau_step_open)
        liste_step.insert(0,nouveau_step_open) # pour les "OPEN", on les ajoute en début
    for chemin in v.chemins :
        #print("chemin : ",chemin)
        # if s!=None and s.last_step!=None and s.last_step.action==Action.MOVE and s.last_step.currentValve==chemin :
        #     continue
        if s.chemin.endswith(chemin+">"+s.currentValve) :
            #print("chemin qui fait demi tour",s.chemin,chemin,s.currentValve)
            continue
        nouveau_step_move = Step(Action.MOVE,s.minutes+1,chemin)
        #print("minute precedente : ",s.minutes)
        # if liste_valves[chemin].taux==0 :
        #     print("on ajoute dans liste valve ouverte : ",chemin,liste_valves[chemin])
        #     nouveauStep.liste_valves_ouvertes.append(chemin) # si la valve de destination est nulle, on dit qu'elle est ouverte
        nouveau_step_move.pression_vannes_ouvertes = s.pression_vannes_ouvertes
        nouveau_step_move.pression_cumul = s.pression_cumul + s.pression_vannes_ouvertes # on se deplace, on n'augmente pas 
        nouveau_step_move.liste_valves_ouvertes = s.liste_valves_ouvertes.copy()
        nouveau_step_move.chemin = s.chemin + ">" + chemin
        #print("MOVE avant liste valve ouverte ",s)
        #print("MOVE apres liste valve ouverte ",nouveau_step_move)
        if log:
            print("ajoute ",nouveau_step_move)
        liste_step.append(nouveau_step_move)


s = Step()
s.currentValve='AA'
s.chemin='AA'
listePossibilite(s)
i = 0
actuel_minute = 0

while len(liste_step)>0 :
    step_courant = liste_step.pop(0)
    #print("traite Step : ",step_courant," reste : ",len(liste_step))
    listePossibilite(step_courant)
    # il faudrait retrier ici
    #if actuel_minute!=step_courant.minutes:
        #liste_step.sort(key=lambda x:(-x.pression_cumul))
        #print("+ une minuste :",liste_step[0])
        #actuel_minute = step_courant.minutes
    # if step_courant.minutes==30 :
    #     liste_step.sort(key=lambda x:(-x.pression_cumul))
    #     print("final Step:",liste_step[0])
    #     exit()        
    #print("liste apres trie :",listeStep)
    # on trie a chaque fois ?
    #if i%100 == 0 :
        #liste_step.sort(key=lambda x:(-len(x.liste_valves_ouvertes),-x.pression_cumul))
    # if i%10000 == 0 :
    #     print("avant trie ")
    #     print(liste_step)
    liste_step.sort(key=lambda x:(-len(x.liste_valves_ouvertes),-x.pression_vannes_ouvertes))
    # if i%10000 == 0 :
    #     print("apres trie ")
    #     print(liste_step)
    if step_courant.pression_cumul>maximum and step_courant.minutes==30 :
        maximum = step_courant.pression_cumul
        print("Nouveau reccord : ",step_courant)
    i += 1     


#[print(listeValves[k]) for k in listeValves]