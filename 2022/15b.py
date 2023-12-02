import re


TAILLE = 4000000
#TAILLE =20

p = re.compile(r'Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)')


class Balise():

    def __init__(self,sx,sy,bx,by):
        self.sx = sx
        self.sy = sy
        self.bx = bx
        self.by = by
        self.d = abs(sx-bx)+abs(sy-by)

    def isCloser(self,x,y):
        return self.distance(x,y)<=self.d

    def baliseIsOn(self,x,y):
        return self.bx==x and self.by==y

    def distance(self,x,y):
        return abs(self.sx-x)+abs(self.sy-y)

    def xFrontiereDroite(self,y): # coordonnee x du points le plus eloignes sur la ligne y
        dx = self.d - abs(self.sy-y)
        return self.sx+dx

    def __str__(self):
        return f"Capteur : {self.sx}/{self.sy} / Balise : {self.bx}/{self.by} / Distance : {self.d}"

listeBalises = []
for line in open('input15.txt').readlines():
    line = line.strip()
    #print(line)
    m = p.search(line)
    b = Balise(int(m.group(1)),int(m.group(2)),int(m.group(3)),int(m.group(4)))
    #print(b)
    listeBalises.append(b)

def capteurPlusProche(x,y):
    for b in listeBalises:
        if b.isCloser(x,y):
            return b
    print("trouve : ",x,y)
    print(x*4000000+y)
    exit()



nb_test = 0
y = 0
while y<TAILLE:
    x = 0
    while x<TAILLE:
        b = capteurPlusProche(x,y)
        nb_test += 1
        #print(x,y,b,"=>",b.xFrontiereDroite(y))
        x = b.xFrontiereDroite(y)
        x += 1
    y += 1

