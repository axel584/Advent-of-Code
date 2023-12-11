



def enigme_day08(chemin):
    ordre_des_directions = []
    map = {}
    avant_espace=True
    with open(chemin,'r') as fichier :
        for ligne in [i.strip() for i in fichier] :
            print(ligne)
            if ligne=="" :
                print("espace")
                avant_espace=False    
                continue
            if avant_espace :
                ordre_des_directions = [i for i in ligne]
            else :
                element,direction = ligne.split(" = ")
                #print(element,direction)
                direction = direction.strip('()')
                #print(direction)
                gauche,droite = direction.split(', ')
                #print(gauche,droite)   
                map[element]=(gauche,droite)
    i = 0
    element_courant = "AAA"
    while element_courant!="ZZZ":
        direction = ordre_des_directions[i%len(ordre_des_directions)] 
        if direction=="L":
            element_courant = map[element_courant][0]
        else : 
            element_courant = map[element_courant][1]        
        i += 1
    return i


def endswithz(liste):
    for element in liste :
        if not element.endswith("Z"):
            return False
    return True

def enigme_day08_second_part(chemin):
    ordre_des_directions = []
    map = {}
    avant_espace=True
    with open(chemin,'r') as fichier :
        for ligne in [i.strip() for i in fichier] :
            print(ligne)
            if ligne=="" :
                print("espace")
                avant_espace=False    
                continue
            if avant_espace :
                ordre_des_directions = [i for i in ligne]
            else :
                element,direction = ligne.split(" = ")
                #print(element,direction)
                direction = direction.strip('()')
                #print(direction)
                gauche,droite = direction.split(', ')
                #print(gauche,droite)   
                map[element]=(gauche,droite)
    elements_source = []
    for element in map.keys():
        if element.endswith("A"):
            elements_source.append(element) # une copie aurait été plus propre garçon !
    # print(len(ordre_des_directions)) # 271
    nb_steps = ({"AAA":[],"RLA":[],"QLA":[],"QFA":[],"RXA":[],"JSA":[]})
    print(nb_steps,type(nb_steps))
    for element in elements_source :
        i = 0
        element_courant = element
        print("element",element)
        while (not element_courant.endswith("Z")) and i%271!=0: # a corriger ici, je pense que c'est là que se trouve le problème
            direction = ordre_des_directions[i%len(ordre_des_directions)] 
            if direction=="L":
                element_courant = map[element_courant][0]
            else : 
                element_courant = map[element_courant][1]        
            i += 1
            if element_courant.endswith("Z"):
                nb_steps[element].append(i)
        print(nb_steps)

    return i



def test_enigme_day08():
    assert enigme_day08("input-08a-test.txt") == 2
    assert enigme_day08("input-08b-test.txt") == 6
    assert enigme_day08_second_part("input-08c-test.txt") == 6


if __name__ == "__main__" :
    print(enigme_day08_second_part("input-08.txt"))