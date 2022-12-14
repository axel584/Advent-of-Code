class Fichier():
    taille : int  
    nom: str

    def __init__(self, nom,taille) :
        self.nom = nom
        self.taille = int(taille)

class Repertoire():
    taille: int
    fichiers : list
    repertoires : list
    chemin : str
    nom: str
    parent = None

    def __init__(self,parent,nom):
        self.parent = parent
        self.nom = nom
        self.fichiers = []
        self.repertoires = []

    def calculeTaille(self):
        somme =0 
        for repertoire in self.repertoires :
            somme += repertoire.calculeTaille()
        for fichier in self.fichiers :
            somme += fichier.taille
        self.taille = somme       
        return somme 

pwd = '/'
arborescence = Repertoire(None, "")
repertoireCourant = arborescence
for line in open('input07.txt').readlines():
    line = line.strip()
    if line == "$ cd /" : # 1ere ligne
        pass
    elif line == "$ ls" : # on va lire les lignes mais on s'en fout
        pass
    elif line[0].isdigit() :
        taille,nom = line.split(' ')
        fichier = Fichier(taille=taille, nom=nom)
        repertoireCourant.fichiers.append(fichier)
    elif line[0:4] == "dir " :
        nom = line.split(' ')[1]
        repertoire = Repertoire(parent=repertoireCourant,nom=nom)
        repertoireCourant.repertoires.append(repertoire)
    elif line == "$ cd .." :
        repertoireCourant = repertoireCourant.parent
    elif line[0:5] == "$ cd " :
        chemin = line.split(' ')[2]
        for repertoire in repertoireCourant.repertoires : # on balaye les repertoires pour aller dans celui passé en paramètre
            if repertoire.nom == chemin :
                repertoireCourant = repertoire
                break
    else : 
        print("ERROR !!!")
        exit()

arborescence.calculeTaille()
print("somme : ",arborescence.taille)
print("recherche ceux qui ont plus de 100 000 octets")
sommeTotale = 0
# parcourir les differents repertoires et verifier leur taille
liste = []
liste.append(arborescence)
while len(liste)>0 :
    repertoire = liste.pop()
    if repertoire.taille<100000 :
        sommeTotale += repertoire.taille
    for r in repertoire.repertoires:
        liste.append(r)

print(sommeTotale)