

position_head_x = 0
position_head_y = 0

increment_head_x = {'L':-1,'R':1,'U':0,'D':0}
increment_head_y = {'L':0,'R':0,'U':1,'D':-1}

liste_position = []
for _ in range(10) :
    element = [0,0]
    liste_position.append(element)

historique_position_tail = []

def move_tail(position_head_x,position_head_y,position_tail_x,position_tail_y):
    if position_head_x==position_tail_x and position_head_y==position_tail_y :
        return position_tail_x,position_tail_y
    if position_head_x==position_tail_x : # meme ligne 
        if abs(position_head_y-position_tail_y)==1 : # cas d'une seule separation
            return position_tail_x,position_tail_y
        if position_head_y>position_tail_y : # cas de deux separations dans un sens
            position_tail_y += 1
        else :
            position_tail_y -= 1
        return position_tail_x,position_tail_y
    if position_head_y==position_tail_y : # meme colonne
        if abs(position_head_x-position_tail_x)==1 : # cas d'une seule separation
            return position_tail_x,position_tail_y
        if position_head_x>position_tail_x : # cas de deux separations dans un sens
            position_tail_x += 1
        else :
            position_tail_x -= 1            
        return position_tail_x,position_tail_y
    # cas diagonal
    # cas d'une case de separation en diagonal
    if abs(position_head_x-position_tail_x)==1 and abs(position_head_y-position_tail_y)==1 : 
        return position_tail_x,position_tail_y
    # cas de plus d'une case
    if position_head_x>position_tail_x :
        position_tail_x += 1
    else :
        position_tail_x -= 1
    if position_head_y>position_tail_y :
        position_tail_y += 1
    else :
        position_tail_y -= 1
    return position_tail_x,position_tail_y


for line in open('input09.txt').readlines():
    line = line.strip()
    direction,nb_pas = line.split(' ')
    print(direction,nb_pas,increment_head_x[direction],increment_head_y[direction])
    for i in range(int(nb_pas)) :
        liste_position[0][0] += increment_head_x[direction]
        liste_position[0][1] += increment_head_y[direction]
        print(position_head_x,position_head_y)
        # on deplace chaque element de la chaine :
        for i in range(1,10) :
            x,y = move_tail(liste_position[i-1][0],liste_position[i-1][1],liste_position[i][0],liste_position[i][1])
            liste_position[i][0]=x
            liste_position[i][1]=y
        historique_position_tail.append(str(liste_position[9][0])+"-"+str(liste_position[9][1]))

print(len(set(historique_position_tail)))
