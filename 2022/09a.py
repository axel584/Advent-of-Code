

position_head_x = 0
position_head_y = 0
position_tail_x = 0
position_tail_y = 0

increment_head_x = {'L':-1,'R':1,'U':0,'D':0}
increment_head_y = {'L':0,'R':0,'U':1,'D':-1}

liste_position_tail = []

def move_tail():
    global position_head_x,position_head_y,position_tail_x,position_tail_y
    if position_head_x==position_tail_x and position_head_y==position_tail_y :
        return
    if position_head_x==position_tail_x : # meme ligne 
        if abs(position_head_y-position_tail_y)==1 : # cas d'une seule separation
            return
        if position_head_y>position_tail_y : # cas de deux separations dans un sens
            position_tail_y += 1
        else :
            position_tail_y -= 1
        return    
    if position_head_y==position_tail_y : # meme colonne
        if abs(position_head_x-position_tail_x)==1 : # cas d'une seule separation
            return
        if position_head_x>position_tail_x : # cas de deux separations dans un sens
            position_tail_x += 1
        else :
            position_tail_x -= 1            
        return
    # cas diagonal
    # cas d'une case de separation en diagonal
    if abs(position_head_x-position_tail_x)==1 and abs(position_head_y-position_tail_y)==1 : 
        return 
    # cas de plus d'une case
    if position_head_x>position_tail_x :
        position_tail_x += 1
    else :
        position_tail_x -= 1
    if position_head_y>position_tail_y :
        position_tail_y += 1
    else :
        position_tail_y -= 1
    return


for line in open('input09.txt').readlines():
    line = line.strip()
    direction,nb_pas = line.split(' ')
    print(direction,nb_pas,increment_head_x[direction],increment_head_y[direction])
    for i in range(int(nb_pas)) :
        position_head_x += increment_head_x[direction]
        position_head_y += increment_head_y[direction]
        print(position_head_x,position_head_y)
        move_tail()
        liste_position_tail.append(str(position_tail_x)+"-"+str(position_tail_y))

print(len(set(liste_position_tail)))
