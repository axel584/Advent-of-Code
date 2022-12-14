data = open('input06.txt').read()
debut = 14
while True:
    lettres = set(data[debut-14:debut])
    print(debut,len(lettres))
    if len(lettres) == 14 or len(lettres) == 0 :
        print(debut)
        exit()
    debut += 1    
    