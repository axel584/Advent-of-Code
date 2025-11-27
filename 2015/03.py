

def enigme1_day3(chemin):
    row,col = 0,0
    map = {}
    map[(row,col)]=True
    data = open(chemin,'r').read()
    for car in data:
        print(car)
        if car=='v':
            row += 1
        if car=='^':
            row -= 1
        if car=='<':
            col -= 1
        if car=='>':
            col += 1
        map[(row,col)]=True
    print(len(map))

def enigme2_day3(chemin):
    row1,col1 = 0,0
    row2,col2 = 0,0
    map = {}
    map[(row1,col1)]=True
    map[(row2,col2)]=True
    data = open(chemin,'r').read()
    iteration = 0
    for car in data:
        iteration += 1
        if iteration%2==0 :
            if car=='v':
                row1 += 1
            if car=='^':
                row1 -= 1
            if car=='<':
                col1 -= 1
            if car=='>':
                col1 += 1
            map[(row1,col1)]=True
        else : 
            if car=='v':
                row2 += 1
            if car=='^':
                row2 -= 1
            if car=='<':
                col2 -= 1
            if car=='>':
                col2 += 1
            map[(row2,col2)]=True            
    print(len(map))



if __name__ == "__main__" :
    print(enigme2_day3("input-03.txt"))    