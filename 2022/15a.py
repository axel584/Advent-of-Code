import re

p = re.compile(r'Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)')


class Balise():

    def __init__(self,sx,sy,bx,by):
        self.sx = sx
        self.sy = sy
        self.bx = bx
        self.by = by
        self.d = abs(sx-bx)+abs(sy-by)

    def isCloser(self,x,y):
        d2 = abs(self.sx-x)+abs(self.sy-y)
        return d2<=self.d

    def baliseIsOn(self,x,y):
        return self.bx==x and self.by==y

    def __str__(self):
        return f"Capteur : {self.sx}/{self.sy} / Balise : {self.bx}/{self.by}"

listeBalises = []
for line in open('input15.txt').readlines():
    line = line.strip()
    print(line)
    m = p.search(line)
    b = Balise(int(m.group(1)),int(m.group(2)),int(m.group(3)),int(m.group(4)))
    print(b)
    listeBalises.append(b)

nb_element = 0
for i in range(-5000000,10000000):
    occupe = False
    for b in listeBalises:
        if b.isCloser(i,2000000) :
            occupe = True
        if b.baliseIsOn(i,2000000):
            occupe=False
            break
    if occupe:
        nb_element += 1

print(nb_element)

