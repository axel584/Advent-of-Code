class Node:

    def __init__(self, valeur):
        self.old_next = None
        self.old_prev = None
        self.new_next = None
        self.new_prev = None
        self.valeur = valeur


debut = None
precedent = None
dernier = None
nb_element = 0
for line in open('input20.txt'):
    line = line.strip()
    element = Node(int(line))
    dernier = element
    nb_element += 1
    if debut is None:
        debut = element
        precedent = element
    else:
        precedent.new_next = element
        precedent.old_next = element
        element.old_prev = precedent
        element.new_prev = precedent
        precedent = element
dernier.new_next = debut
dernier.old_next = debut
debut.new_prev = dernier
debut.old_prev = dernier


def avance(noeud):
    global debut
    if noeud == debut: 
        debut = debut.new_next
    precedent = noeud.new_prev
    suivant = noeud.new_next
    suivant_suivant = suivant.new_next
    # on rattache le precedent et le suivant ensemble
    precedent.new_next = suivant
    suivant.new_prev = precedent
    # on positionne correctement le noeud
    noeud.new_next = suivant_suivant
    noeud.new_prev = suivant
    # on rattache les suivants et suivant du suivant au noeud
    suivant.new_next = noeud
    suivant_suivant.new_prev = noeud
    
 
def affiche():
    res = ""
    pointeur = debut 
    for _ in range(nb_element):
        res += str(pointeur.valeur) + " "
        pointeur = pointeur.new_next
    print(res)


affiche()
pointeur = debut 
for _ in range(nb_element):
    nb_iteration = pointeur.valeur%(nb_element-1)
    #print("on avance de ", nb_iteration)
    for _ in range(nb_iteration):
        avance(pointeur)
    #affiche()
    pointeur = pointeur.old_next


pointeur = debut 
# cherche 0
for _ in range(nb_element):
    if pointeur.valeur==0 :
        break
    pointeur = pointeur.new_next
print(pointeur.valeur)
somme = 0
for _ in range(1000):
    pointeur = pointeur.new_next
print(pointeur.valeur)
somme += pointeur.valeur
for _ in range(1000):
    pointeur = pointeur.new_next
print(pointeur.valeur)
somme += pointeur.valeur
for _ in range(1000):
    pointeur = pointeur.new_next
print(pointeur.valeur)
somme += pointeur.valeur

print(somme)
