def enigme1_day1(chemin):
    data = open(chemin,'r').read()
    plus = data.count('(')
    moins = data.count(')')
    print(plus-moins)


def enigme2_day1(chemin):
    data = open(chemin,'r').read()
    etage = 0
    step = 0
    for i in data :
        step += 1
        if i == '(' :
            etage += 1
        else :
            etage -= 1
        if etage == -1 :
            print(step)
            exit()



if __name__ == "__main__" :
    print(enigme1_day1("input-01.txt"))