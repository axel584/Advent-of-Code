
def compare(gauche,droite) :
    # print("gauche",type(gauche),gauche)
    # print("droite",type(droite),droite)
    if type(gauche)==list and type(droite)==list :
        if gauche==None or len(gauche)==0 :
            return True
        if droite==None or len(droite)==0 :
            return False
        if gauche[0] == droite[0]:
            return compare(gauche[1:],droite[1:])
        return compare(gauche[0],droite[0])
    if type(gauche)==list and type(droite)==int:
        return compare(gauche,[droite])
    if type(gauche)==int and type(droite)==list:
        return compare([gauche],droite)        
    if type(gauche)==int and type(droite)==int :
        return gauche<=droite
           
    
indice = 1
somme = 0
with open('input13.txt') as fichier :
    while True :
        ligneGauche = fichier.readline().strip()
        if ligneGauche=='':
            break
        gauche = eval(ligneGauche)
        ligneDroite = fichier.readline().strip()
        droite = eval(ligneDroite)
        espaceVide = fichier.readline()
        if compare(gauche,droite) :
            somme += indice
        indice += 1

print(somme)