data = open('input06.txt').read()
debut = 4
while True:
    print(data[debut-4:debut])
    lettres = set(data[debut-4:debut])
    print(len(lettres))
    if len(lettres) == 4 :
        print(debut)
        exit()
    debut += 1
    
    